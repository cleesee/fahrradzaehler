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
