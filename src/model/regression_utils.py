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

    # Print coverage BEFORE feature cleaning
    print(f"    Complete coverage: {n_valid:,}/{n_total_timestamps:,} hours ({coverage_pct:.1f}%) → {n_samples_after_overlap:,} samples before features")
    
    # Check if we have any data after filtering
    if len(df_station) == 0:
        print(f"    No overlapping data with other stations - skipping")
        return None, None, None
    
    # Add station features
    df_model = add_station_features(df_station, station_name, df_city)
    
    # Select features (temporal only, no is_weekend since we have day_of_week)
    temporal_features = ['hour', 'day_of_week', 'month']
    weather_features = ['site_temperature', 'site_rain_accumulation'] 
    
    # Get station features
    station_features = [col for col in df_model.columns if col.startswith('station_')]
    
    # Combine all features
    features = temporal_features + weather_features + station_features
    
    # IMPORTANT: Sort by timestamp to ensure temporal train/test split
    # This ensures first 80% of time period is training, last 20% is testing
    df_model = df_model.sort_values('iso_timestamp').reset_index(drop=True)
    
    # Drop rows with missing features BEFORE splitting
    # This ensures we only work with complete data
    n_before_drop = len(df_model)
    df_complete = df_model.dropna(subset=features)
    n_dropped = n_before_drop - len(df_complete)
    
    # Print coverage AFTER feature cleaning
    if n_dropped > 0:
        print(f"    After feature cleaning: {len(df_complete):,} samples ({n_dropped:,} dropped due to missing features, {n_dropped/n_before_drop*100:.1f}%)")
    else:
        print(f"    After feature cleaning: {len(df_complete):,} samples (no rows dropped)")
    
    if len(df_complete) < 100:
        print(f"    Insufficient data after cleaning: {len(df_complete)} hours")
        return None, None, None
    
    # NOW split train/test (80/20) on the clean data - TEMPORAL SPLIT
    split_idx = int(len(df_complete) * 0.8)
    train_data = df_complete.iloc[:split_idx]
    test_data = df_complete.iloc[split_idx:]
    n_train_samples = len(train_data)
    n_test_samples = len(test_data)
    
    # Sanity check: verify temporal ordering
    train_end = train_data['iso_timestamp'].iloc[-1]
    test_start = test_data['iso_timestamp'].iloc[0]
    print(f"    Train period: {train_data['iso_timestamp'].iloc[0]} to {train_end} ({n_train_samples:,} hours)")
    print(f"    Test period:  {test_start} to {test_data['iso_timestamp'].iloc[-1]} ({n_test_samples:,} hours)")
    
    if train_end >= test_start:
        print(f"    WARNING: Train/test periods overlap! Check data sorting.")
    
    # Prepare X and y
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
        'n_train_samples': n_train_samples,
        'n_test_samples': n_test_samples,
    }
    
    return results, model, features