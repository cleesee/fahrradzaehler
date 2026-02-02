# 1. Data Quality Assessment

``notebooks/1_sanity_checks.ipynb``

## 1.1. Sanity checks

- Distribution of counts: Shows whether the data is realistic - (normal distribution)
- Hourly pattern: Rush hour peaks (7-9 a.m., 4-7 p.m.)
- Weekly pattern: Differences between weekdays and weekends
- Outlier detection: Box plots for the top 5 stations

## 1.2. Station growth & predictability

- Activation timeline: When were the stations installed?
- Correlation matrix: How strongly do different stations correlate?
- Regression model: Can one station be predicted from another?
- Growth trend: Overall development over time

## 1.3. Weather analysis

- Temperature vs. bicycles: Scatter plot with rain color-coded
- Rain impact: How much does rain reduce bicycle use?
- Seasonal temperature: Box plots per season
- Seasonal usage: Average bicycle usage per season

## 1.4. Statistical summary

- Data quality (missing values, outliers)
- Bike count statistics
- Weather correlations
- Station insights

# 2. Distance & Correlation

``notebooks/distcorr_updated.ipynb``

- Computes Euclidean and bike-network distances between bicycle counting stations
- Calculates pairwise Spearman correlations of hourly bike counts
- Compares correlations using aligned vs. partially overlapping time series
- Visualizes distance–correlation relationships for multiple cities
- Excludes stations without network connectivity or sufficient temporal overlap
- City can be selected via a single configuration cell

# 3. Regression Model

``notebooks/all_cities_regression.ipynb``

- Exploratory linear regression (OLS) to explain bike counts using temporal and weather features
- Models trained city-wise (no parameter sharing across cities)
- Performance evaluated mainly via coefficient of determination ($R^2$)
- Comparison of models with vs. without statistical outlier removal
- Detailed inspection for Heidelberg (with one station excluded for data overlap)
- Aggregate performance statistics computed across all cities
- Analysis of how weather features affect data availability, not just prediction accuracy
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


