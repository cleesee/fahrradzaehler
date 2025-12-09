"""
Utility functions for bike counter regression analysis
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error


def add_station_features(df_station, station_name, df_city):
    """
    Add other station counts as features for predicting target station
    
    Returns DataFrame with new columns: station_A, station_B, etc.
    """
    # Get all other stations
    all_stations = df_city['counter_site'].unique()
    other_stations = [s for s in all_stations if s != station_name]
    
    # Create pivot table with other stations as columns
    df_pivot = df_city[df_city['counter_site'].isin(other_stations)].pivot_table(
        index='iso_timestamp', 
        columns='counter_site', 
        values='channels_all'
    )
    
    # Clean column names and add prefix
    df_pivot.columns = ['station_' + col.replace(' ', '_').replace('/', '_') for col in df_pivot.columns]
    
    # Merge with target station data
    return df_station.merge(df_pivot, left_on='iso_timestamp', right_index=True, how='left')


def train_model(df_station, station_name, df_city):
    """
    Train regression model to predict station traffic using temporal features + other station counts
    
    Returns: (results_dict, model, feature_list)
    """
    # Add station features
    df_model = add_station_features(df_station, station_name, df_city)
    
    # Select features (temporal only, no is_weekend since we have day_of_week)
    temporal_features = ['hour', 'day_of_week', 'month']
    weather_features = []
    
    # Include weather if available (>10% coverage)
    for weather_col in ['site_temperature', 'site_rain_accumulation']:
        if weather_col in df_model.columns and df_model[weather_col].notna().mean() > 0.1:
            weather_features.append(weather_col)
    
    # Get station features
    station_features = [col for col in df_model.columns if col.startswith('station_')]
    
    # Combine all features
    features = temporal_features + weather_features + station_features
    
    # Split train/test (80/20)
    split_idx = int(len(df_model) * 0.8)
    train_data = df_model.iloc[:split_idx]
    test_data = df_model.iloc[split_idx:]
    
    # Prepare X and y
    X_train = train_data[features].fillna(0)
    X_test = test_data[features].fillna(0)
    y_train = train_data['channels_all']
    y_test = test_data['channels_all']
    
    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Evaluate
    y_pred_test = model.predict(X_test)
    
    results = {
        'station': station_name,
        'test_r2': r2_score(y_test, y_pred_test),
        'test_rmse': np.sqrt(mean_squared_error(y_test, y_pred_test)),
        'test_mae': mean_absolute_error(y_test, y_pred_test),
        'n_features': len(features),
        'temporal_features': temporal_features,
        'weather_features': weather_features,
        'n_stations': len(station_features)
    }
    
    return results, model, features