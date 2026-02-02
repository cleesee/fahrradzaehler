# 0. Preparation

``notebooks/0_preparation.ipynb``


# 1. Data Quality Assessment

``notebooks/1_sanity_checks.ipynb``

- Aggregates hourly bike count data to daily totals and filters for complete days per city
- Visualizes station availability, daily distributions, weekly/monthly/seasonal patterns, and city-wise time series
- Examines station growth & activation timeline
- Analyzes weather impact on bike counts (temperature, rain, seasonal effects)
- Summarizes data quality, outliers, and basic statistical metrics per station and city


# 2. Distance & Correlation

``notebooks/distcorr_updated.ipynb``

- Computes Euclidean and bike-network distances between bicycle counting stations
- Calculates pairwise Spearman correlations of hourly bike counts
- Visualizes distance–correlation relationships for multiple cities
- Excludes stations without network connectivity or sufficient temporal overlap
- City can be selected via a single configuration cell


# 3. Regression Model

``notebooks/all_cities_regression.ipynb``

- Exploratory linear regression (OLS) to explain bike counts using temporal and weather features
- Models trained city-wise (no parameter sharing across cities)
- Performance evaluated mainly via coefficient of determination ($R^2$)
- Comparison of models with vs. without statistical outlier removal
- Aggregate performance statistics across all cities
- Analysis of how weather features affect data availability
- Visualization of $R^2$ distributions to assess sensitivity to preprocessing choices


# 4. Gaussian Process (GP)

``notebooks/GP UPDATED.ipynb``

- Compares Euclidean Gaussian Process (GP) and Graph-based GP on single-hour snapshot
- Euclidean GP: Matérn kernel on projected 2D coordinates
- Graph GP: Diffusion kernel constructed from the symmetric normalized graph Laplacian
- Road and bike network built using ``OSMnx``, counters mapped to nearest graph nodes
- Graph kernel approximated using the lowest 5% of Laplacian eigenpairs
- Hyperparameters optimized via GP marginal likelihood (with fixed process variance for Graph GP)
- Evaluated using leave-two-out cross-validation (MAE, MAPE, TLPD)

