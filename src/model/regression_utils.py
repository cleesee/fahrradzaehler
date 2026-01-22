"""
Utility functions for bike counter regression analysis
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error, mean_absolute_percentage_error


def add_station_features(df_station, station_name, df_city):
    """
    Add other station counts as features for predicting target station
    
    Returns DataFrame with new columns: station_A, station_B, etc.
    """
    # Get all other stations
    all_stations = df_city['counter_site'].unique()
    # exclude the target station
    other_stations = [s for s in all_stations if s != station_name]
    
    # print message if there are duplicates, pivot will average them
    dup_mask = df_city.duplicated(subset=['iso_timestamp', 'counter_site'])
    if dup_mask.any():
        n_dups = dup_mask.sum()
        print(f"    ⚠ WARNING: {n_dups} duplicate (timestamp, station) rows found before pivoting")


    # Create pivot table with other stations as columns
    df_pivot = df_city[df_city['counter_site'].isin(other_stations)].pivot_table(
        index='iso_timestamp', 
        columns='counter_site', 
        values='channels_all'
    )
    
    
    # Clean column names and add prefix
    df_pivot.columns = ['station_' + col.replace(' ', '_').replace('/', '_') for col in df_pivot.columns]
    
    
    # Merge with target station data (left is fine since NaNs are already dropped before)
    return df_station.merge(df_pivot, left_on='iso_timestamp', right_index=True, how='left')


def train_model(df_station, station_name, df_city):
    """
    Train regression model to predict station traffic using temporal features + other station counts
    Only uses time frames where ALL stations have data available
    
    Returns: (results_dict, model, feature_list)
    """
    # First, find timestamps where ALL stations have data
    df_pivot_all = df_city.pivot_table(
        index='iso_timestamp',
        columns='counter_site',
        values='channels_all'
    )
    
    n_total_timestamps = len(df_pivot_all)
    
    # Keep only timestamps with complete data across all stations
    valid_timestamps = df_pivot_all.dropna().index
    n_valid = len(valid_timestamps)
    coverage_pct = (n_valid / n_total_timestamps * 100) if n_total_timestamps > 0 else 0
    
    # Filter target station to valid timestamps only
    df_station = df_station[df_station['iso_timestamp'].isin(valid_timestamps)].copy()
    n_samples_after_overlap = len(df_station)  # rows left after keeping only timestamps with full city coverage

    
    print(f"    Complete coverage: {n_valid:,}/{n_total_timestamps:,} hours ({coverage_pct:.1f}%)")
    
    # Check if we have any data after filtering
    if len(df_station) == 0:
        print(f"    No overlapping data with other stations - skipping")
        return None, None, None
    
    # Add station features
    df_model = add_station_features(df_station, station_name, df_city)
    n_samples_after_features = len(df_model)  # rows left after feature construction (may drop more rows)

    
    # Select features (temporal only, no is_weekend since we have day_of_week)
    temporal_features = ['hour', 'day_of_week', 'month']
    weather_features = []  # Excluding weather features, no good coverage and data
    
    # Get station features
    station_features = [col for col in df_model.columns if col.startswith('station_')]
    
    # Combine all features
    features = temporal_features + weather_features + station_features
    
    # Check if we have enough data for train/test split
    if len(df_model) < 100:
        print(f"    Insufficient overlapping data ({len(df_model)} hours)")
        return None, None, None
    
    # IMPORTANT: Sort by timestamp to ensure temporal train/test split
    # This ensures first 80% of time period is training, last 20% is testing
    df_model = df_model.sort_values('iso_timestamp').reset_index(drop=True)
    
    # Print time frame info
    start_date = df_model['iso_timestamp'].iloc[0]
    end_date = df_model['iso_timestamp'].iloc[-1]
    date_range = (pd.to_datetime(end_date) - pd.to_datetime(start_date)).days
    print(f"    Time frame: {start_date} to {end_date} ({date_range} days, {len(df_model):,} hours)")
    
    # Split train/test (80/20) - TEMPORAL SPLIT
    split_idx = int(len(df_model) * 0.8)
    train_data = df_model.iloc[:split_idx]
    test_data = df_model.iloc[split_idx:]
    n_train_samples = split_idx
    n_test_samples = len(df_model) - split_idx

    
    # Sanity check: verify temporal ordering
    train_end = train_data['iso_timestamp'].iloc[-1]
    test_start = test_data['iso_timestamp'].iloc[0]
    print(f"    Train period: {train_data['iso_timestamp'].iloc[0]} to {train_end}")
    print(f"    Test period:  {test_start} to {test_data['iso_timestamp'].iloc[-1]}")
    
    if train_end >= test_start:
        print(f"    WARNING: Train/test periods overlap! Check data sorting.")
    
    # Prepare X and y (no fillna needed since we dropped missing values)
    X_train = train_data[features]
    X_test = test_data[features]
    y_train = train_data['channels_all']
    y_test = test_data['channels_all']
    
    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Evaluate
    y_pred_test = model.predict(X_test)
    
    # MAPE explodes when actual values are near zero
    MIN_COUNT_FOR_MAPE = 10  # Only calculate MAPE on hours with at least 10 bikes
    mask_nonzero = y_test >= MIN_COUNT_FOR_MAPE
    
    if mask_nonzero.sum() > 0:
        mape = mean_absolute_percentage_error(y_test[mask_nonzero], y_pred_test[mask_nonzero]) * 100
    else:
        mape = np.nan  # Not enough data to calculate meaningful MAPE
    
    results = {
        'station': station_name,
        'test_r2': r2_score(y_test, y_pred_test),
        'test_rmse': np.sqrt(mean_squared_error(y_test, y_pred_test)),
        'test_mae': mean_absolute_error(y_test, y_pred_test),
        'test_mape': mape,
        'n_features': len(features),
        'temporal_features': temporal_features,
        'weather_features': weather_features,
        'n_stations': len(station_features),
        'n_samples_after_overlap': n_samples_after_overlap,
        'n_samples_after_features': n_samples_after_features,
        'n_train_samples': n_train_samples,
        'n_test_samples': n_test_samples,
    }
    
    return results, model, features