## Regression

Features: hour, day_of_week, month, + hourly counts from other stations
Selection: Only use datapoints where data from all stations is available


**SUMMARY - Stadt Freiburg**


| Station | R² (with) | RMSE (with) | MAE (with) | R² (no outl) | RMSE (no outl) | MAE (no outl) | ΔR² | Features | n_train |
|---------|-----------|-------------|------------|--------------|----------------|---------------|-----|----------|---------|
| Wiwilibrücke                   |    0.9733 |       53.05 |      38.02 |       0.9435 |          32.16 |         23.10 | -0.0299 |       12 |    4853 |
| FR2 Güterbahn / Ferd.-Weiß-Str |    0.9682 |       25.60 |      16.49 |       0.9266 |          14.08 |          9.71 | -0.0415 |       12 |    4853 |
| FR1 Dreisam / Otto-Wels-Str.   |    0.7984 |      109.33 |      69.04 |       0.3209 |          87.81 |         55.17 | -0.4775 |       12 |    4853 |
| FR3 Eschholzstr. / Egonstr. ei |    0.9531 |       21.28 |      15.63 |       0.8902 |          16.42 |         11.49 | -0.0628 |       12 |    4853 |
| Mundenhof 2 - Mundenhofer Str. |    0.6693 |       16.40 |      10.82 |       0.4193 |          10.09 |          6.91 | -0.2499 |       12 |    4853 |
| H.-v.-Stephan-Str. 9 / JobRad  |    0.9217 |       14.54 |      10.78 |       0.8476 |           8.59 |          6.33 | -0.0741 |       12 |    4853 |
| H.-v.-Stephan-Str. 9 / JobRad  |    0.8966 |       16.14 |      11.71 |       0.7586 |          10.86 |          7.18 | -0.1380 |       12 |    4853 |
| FR6 Rotteckring / H Theater -  |    0.9537 |       64.32 |      47.32 |       0.8902 |          32.53 |         22.10 | -0.0635 |       12 |    4853 |
| FR2 Elsässer Str. / Uniklinik  |    0.9171 |       34.71 |      19.57 |       0.8404 |          14.96 |          8.06 | -0.0766 |       12 |    4853 |
| FR8 Schützenallee / Stadthalle |    0.9415 |       27.76 |      19.20 |       0.8264 |          19.33 |         12.35 | -0.1151 |       12 |    4853 |

Summary Statistics:
  Avg R² (with outliers):    0.8993 ± 0.0953
  Avg R² (no outliers):      0.7664 ± 0.2166
  Avg ΔR²:                   -0.1329 ± 0.1367
  Avg RMSE (with outliers):  38.31 ± 29.91
  Avg RMSE (no outliers):    24.68 ± 23.73


**SUMMARY - Stadt Heidelberg**

![alt text](<../plots/data_availability_Stadt Heidelberg.png>)

**SUMMARY - Stadt Konstanz**
![alt text](<../plots/data_availability_Stadt Konstanz.png>)

| Station | R² (with) | RMSE (with) | MAE (with) | R² (no outl) | RMSE (no outl) | MAE (no outl) | ΔR² | Features | n_train |
|---------|-----------|-------------|------------|--------------|----------------|---------------|-----|----------|---------|
| Herosepark                     |    0.9636 |       61.52 |      41.46 |       0.9411 |          36.61 |         23.56 | -0.0225 |        8 |    6540 |
| Bahnhaltepunkt Fürstenberg     |    0.9434 |       31.74 |      19.84 |       0.9100 |          19.13 |         11.36 | -0.0333 |        8 |    6540 |
| Bahnhaltepunkt Petershausen    |    0.9717 |       23.61 |      15.30 |       0.9573 |          13.17 |          8.56 | -0.0144 |        8 |    6540 |
| Alte Rheinbrücke               |    0.9289 |       62.24 |      41.08 |       0.9488 |          23.80 |         15.11 | +0.0199 |        8 |    6540 |
| Friedrichstraße                |    0.8442 |       33.19 |      23.99 |       0.8693 |          14.95 |          9.84 | +0.0252 |        8 |    6540 |
| Beethovenstraße                |    0.9135 |       12.81 |       8.89 |       0.8757 |           6.56 |          4.29 | -0.0377 |        8 |    6540 |

Summary Statistics:
  Avg R² (with outliers):    0.9275 ± 0.0462
  Avg R² (no outliers):      0.9171 ± 0.0381
  Avg ΔR²:                   -0.0105 ± 0.0269
  Avg RMSE (with outliers):  37.52 ± 20.22
  Avg RMSE (no outliers):    19.03 ± 10.38

**SUMMARY - Stadt Ludwigsburg**
![alt text](<../plots/data_availability_Stadt Ludwigsburg.png>)

| Station | R² (with) | RMSE (with) | MAE (with) | R² (no outl) | RMSE (no outl) | MAE (no outl) | ΔR² | Features | n_train |
|---------|-----------|-------------|------------|--------------|----------------|---------------|-----|----------|---------|
| Alleenstraße                   |    0.9382 |       31.82 |      19.80 |       0.9292 |          25.87 |         15.95 | -0.0090 |       17 |   31515 |
| Marbacher Straße - Favoritepar |    0.9813 |        7.70 |       4.97 |       0.9787 |           7.57 |          4.88 | -0.0026 |       17 |   31515 |
| Schlieffenstraße               |    0.8992 |        6.34 |       4.20 |       0.8852 |           6.21 |          4.11 | -0.0140 |       17 |   31515 |
| Fuchshof                       |    0.9492 |        8.36 |       5.55 |       0.9383 |           8.21 |          5.43 | -0.0109 |       17 |   31515 |
| Seestraße                      |    0.9015 |        7.43 |       4.86 |       0.9027 |           6.61 |          4.40 | +0.0012 |       17 |   31515 |
| Schlossstraße                  |    0.9724 |        9.34 |       5.99 |       0.9674 |           9.15 |          5.86 | -0.0050 |       17 |   31515 |
| Kesseläcker (Verl. Nussackerwe |    0.7996 |        4.33 |       2.93 |       0.7632 |           4.30 |          2.89 | -0.0364 |       17 |   31515 |
| Zugwiesen                      |    0.7606 |       27.27 |      17.82 |       0.7688 |          27.02 |         17.58 | +0.0082 |       17 |   31515 |
| Bismarckstraße                 |    0.8134 |       11.14 |       7.64 |       0.8081 |          10.48 |          7.14 | -0.0054 |       17 |   31515 |
| Solitudeallee                  |    0.9132 |        7.01 |       4.50 |       0.8983 |           6.62 |          4.29 | -0.0149 |       17 |   31515 |
| Aldinger Straße                |    0.8762 |        5.31 |       3.44 |       0.8619 |           5.19 |          3.35 | -0.0143 |       17 |   31515 |
| Bottwartalstraße               |    0.9666 |        7.17 |       4.29 |       0.9604 |           6.77 |          4.06 | -0.0063 |       17 |   31515 |
| Marbacher Straße - Neckarbrück |    0.8837 |        6.21 |       4.22 |       0.8887 |           6.06 |          4.07 | +0.0050 |       17 |   31515 |
| Königinallee                   |    0.5281 |       10.23 |       6.93 |       0.5011 |           9.90 |          6.61 | -0.0270 |       17 |   31515 |
| Friedrich-Ebert-Straße         |    0.9591 |       18.03 |      10.37 |       0.9591 |          15.74 |          9.44 | -0.0000 |       17 |   31515 |

Summary Statistics:
  Avg R² (with outliers):    0.8762 ± 0.1169
  Avg R² (no outliers):      0.8674 ± 0.1223
  Avg ΔR²:                   -0.0088 ± 0.0117
  Avg RMSE (with outliers):  11.18 ± 8.16
  Avg RMSE (no outliers):    10.38 ± 7.08


**SUMMARY - Stadt Mannheim**
![alt text](<../plots/data_availability_Stadt Mannheim.png>)

| Station | R² (with) | RMSE (with) | MAE (with) | R² (no outl) | RMSE (no outl) | MAE (no outl) | ΔR² | Features | n_train |
|---------|-----------|-------------|------------|--------------|----------------|---------------|-----|----------|---------|
| Renzstraße                     |    0.9650 |       24.98 |      18.63 |       0.9606 |          24.90 |         18.46 | -0.0044 |       16 |   15768 |
| Kurpfalzbrücke                 |    0.5677 |       93.48 |      56.89 |       0.5143 |          93.23 |         56.40 | -0.0534 |       16 |   15768 |
| Jungbuschbrücke                |    0.8304 |       16.97 |      12.28 |       0.8087 |          16.66 |         12.10 | -0.0218 |       16 |   15768 |
| Konrad-Adenauer-Brücke         |    0.9565 |       18.48 |      12.07 |       0.9509 |          18.05 |         11.85 | -0.0055 |       16 |   15768 |
| Lindenhofüberführung           |    0.2558 |       46.90 |      27.49 |       0.2414 |          44.95 |         26.82 | -0.0144 |       16 |   15768 |
| Neckarauer Übergang -Schwetzin |    0.9123 |       10.97 |       7.64 |       0.9082 |          10.66 |          7.41 | -0.0041 |       16 |   15768 |
| Schlosspark Lindenhof (Richtun |    0.9535 |       12.53 |       7.91 |       0.9458 |          12.54 |          8.02 | -0.0077 |       16 |   15768 |
| Feudenheimstr. stadtauswärts   |    0.7334 |       12.09 |       7.44 |       0.7078 |          12.14 |          7.44 | -0.0256 |       16 |   15768 |
| Feudenheimerstr. stadteinwärts |    0.7868 |        8.23 |       5.69 |       0.7820 |           7.92 |          5.41 | -0.0047 |       16 |   15768 |
| Luzenbergstr.                  |    0.8495 |        9.84 |       7.16 |       0.8596 |           8.98 |          6.62 | +0.0102 |       16 |   15768 |
| B38. RI. AUS                   |   -0.2331 |       35.09 |      20.37 |      -0.2044 |          35.40 |         20.22 | +0.0287 |       16 |   15768 |
| Theodor-Heuss-Anlage. RI. IN.  |    0.8611 |        7.36 |       4.89 |       0.8504 |           7.23 |          4.81 | -0.0107 |       16 |   15768 |
| Theodor-Heuss-Anlage. RI. AUS  |    0.7570 |        5.87 |       3.89 |       0.7496 |           5.57 |          3.72 | -0.0074 |       16 |   15768 |
| Fernmeldeturm.                 |    0.9237 |       22.31 |      15.71 |       0.9122 |          22.10 |         15.50 | -0.0115 |       16 |   15768 |

Summary Statistics:
  Avg R² (with outliers):    0.7228 ± 0.3341
  Avg R² (no outliers):      0.7134 ± 0.3292
  Avg ΔR²:                   -0.0095 ± 0.0182
  Avg RMSE (with outliers):  23.22 ± 23.28
  Avg RMSE (no outliers):    22.88 ± 23.19

**SUMMARY - Ravensburg Tws Gmbh & Co. Kg**

![
](<../plots/data_availability_Ravensburg Tws Gmbh & Co. Kg.png>)

| Station | R² (with) | RMSE (with) | MAE (with) | R² (no outl) | RMSE (no outl) | MAE (no outl) | ΔR² | Features | n_train |
|---------|-----------|-------------|------------|--------------|----------------|---------------|-----|----------|---------|
| 03 WGT Krankenhaus Ost         |    0.8018 |        7.44 |       5.11 |       0.8018 |           7.44 |          5.11 | +0.0000 |        9 |   23169 |
| 04 WGT Krankenhaus West        |    0.8522 |       10.61 |       7.38 |       0.8522 |          10.61 |          7.38 | +0.0000 |        9 |   23169 |
| 05 RV Eissporthalle            |    0.8499 |        5.81 |       4.06 |       0.8499 |           5.81 |          4.06 | +0.0000 |        9 |   23169 |
| 06 Meersburger Brücke abwärts  |    0.7478 |       11.45 |       7.08 |       0.7478 |          11.45 |          7.08 | +0.0000 |        9 |   23169 |
| 07 Meersburger Brücke aufwärts |    0.8212 |       11.68 |       7.30 |       0.8212 |          11.68 |          7.30 | +0.0000 |        9 |   23169 |
| 08 RV Bahnhofstr.              |    0.8746 |       10.57 |       7.18 |       0.8746 |          10.57 |          7.18 | +0.0000 |        9 |   23169 |
| 01 / 02 WGT Doggenriedstraße   |    0.7970 |        4.86 |       3.30 |       0.7970 |           4.86 |          3.30 | +0.0000 |        9 |   23169 |

Summary Statistics:
  Avg R² (with outliers):    0.8206 ± 0.0428
  Avg R² (no outliers):      0.8206 ± 0.0428
  Avg ΔR²:                   +0.0000 ± 0.0000
  Avg RMSE (with outliers):  8.92 ± 2.83
  Avg RMSE (no outliers):    8.92 ± 2.83

**SUMMARY - Reutlingen**
![alt text](<../plots/data_availability_Stadt Reutlingen.png>)

| Station | R² (with) | RMSE (with) | MAE (with) | R² (no outl) | RMSE (no outl) | MAE (no outl) | ΔR² | Features | n_train |
|---------|-----------|-------------|------------|--------------|----------------|---------------|-----|----------|---------|
| Tübinger Tor                   |    0.7325 |       32.01 |      14.15 |       0.9139 |          18.06 |         11.49 | +0.1815 |       10 |   31284 |
| Charlottenstraße               |    0.5401 |       19.93 |       9.18 |       0.8145 |          12.58 |          7.55 | +0.2744 |       10 |   31284 |
| Konrad-Adenauer-Straße         |    0.8865 |        6.13 |       4.18 |       0.8883 |           6.05 |          4.15 | +0.0018 |       10 |   31284 |
| Metzgerstraße                  |   -0.7899 |       30.87 |       9.64 |       0.7978 |          10.34 |          6.37 | +1.5877 |       10 |   31284 |
| Bellinostraße                  |    0.2603 |       35.69 |      11.38 |       0.9000 |          13.06 |          7.46 | +0.6397 |       10 |   31284 |
| Hindenburgstraße               |   -0.0006 |      306.00 |      40.06 |       0.7842 |          16.88 |          7.02 | +0.7848 |       10 |   31284 |
| Moltkestraße                   |    0.6947 |        7.06 |       3.81 |       0.8304 |           5.22 |          3.39 | +0.1357 |       10 |   31284 |
| Unter den Linden               |    0.8670 |       11.32 |       7.49 |       0.9062 |           9.45 |          6.86 | +0.0392 |       10 |   31284 |

Summary Statistics:
  Avg R² (with outliers):    0.3988 ± 0.5692
  Avg R² (no outliers):      0.8544 ± 0.0531
  Avg ΔR²:                   +0.4556 ± 0.5363
  Avg RMSE (with outliers):  56.13 ± 101.63
  Avg RMSE (no outliers):    11.46 ± 4.63

**SUMMARY - Stuttgart**
![alt text](<../plots/data_availability_Landeshauptstadt Stuttgart.png>)

| Station | R² (with) | RMSE (with) | MAE (with) | R² (no outl) | RMSE (no outl) | MAE (no outl) | ΔR² | Features | n_train |
|---------|-----------|-------------|------------|--------------|----------------|---------------|-----|----------|---------|
| König-Karls-Brücke Barometer   |    0.8407 |       41.07 |      25.81 |       0.8693 |          36.21 |         23.61 | +0.0286 |       17 |   36125 |
| Böblinger Straße               |    0.8460 |       21.10 |      12.08 |       0.8345 |          21.11 |         11.93 | -0.0115 |       17 |   36125 |
| Taubenheimstraße               |    0.5070 |        7.74 |       5.33 |       0.6694 |           6.26 |          4.32 | +0.1624 |       17 |   36125 |
| Waiblinger Straße              |    0.8532 |        4.69 |       3.26 |       0.8535 |           4.57 |          3.20 | +0.0004 |       17 |   36125 |
| Samaraweg                      |    0.8604 |       25.80 |      14.79 |       0.8559 |          25.53 |         14.54 | -0.0045 |       17 |   36125 |
| Waldburgstraße                 |    0.8347 |       10.42 |       5.24 |       0.8283 |          10.43 |          5.22 | -0.0063 |       17 |   36125 |
| Kremmlerstraße                 |    0.8883 |       13.06 |       8.17 |       0.8888 |          12.75 |          7.99 | +0.0006 |       17 |   36125 |
| Kirchheimer Straße             |    0.9119 |        7.86 |       5.12 |       0.9139 |           7.68 |          5.02 | +0.0020 |       17 |   36125 |
| Stuttgarter Straße             |    0.7707 |        8.89 |       5.33 |       0.7740 |           8.70 |          5.26 | +0.0034 |       17 |   36125 |
| Solitudestraße                 |    0.8214 |        8.30 |       5.03 |       0.8183 |           8.23 |          4.99 | -0.0032 |       17 |   36125 |
| Am Kräherwald                  |    0.8670 |        6.75 |       4.37 |       0.8651 |           6.66 |          4.34 | -0.0019 |       17 |   36125 |
| Inselstraße                    |    0.9057 |       13.20 |       7.79 |       0.9064 |          12.92 |          7.53 | +0.0007 |       17 |   36125 |
| Neckartalstraße                |    0.3869 |       13.25 |       8.63 |       0.3299 |          13.74 |          8.69 | -0.0569 |       17 |   36125 |
| Lautenschlager Straße          |    0.8215 |       20.90 |      14.12 |       0.8180 |          20.82 |         14.02 | -0.0036 |       17 |   36125 |
| Tübinger Straße                |    0.9190 |       29.42 |      20.97 |       0.9209 |          28.41 |         20.08 | +0.0019 |       17 |   36125 |

Summary Statistics:
  Avg R² (with outliers):    0.8023 ± 0.1511
  Avg R² (no outliers):      0.8098 ± 0.1468
  Avg ΔR²:                   +0.0075 ± 0.0462
  Avg RMSE (with outliers):  15.50 ± 10.23
  Avg RMSE (no outliers):    14.94 ± 9.40
**SUMMARY - Tübingen**

![alt text](<../plots/data_availability_Stadt Tübingen.png>)
| Station | R² (with) | RMSE (with) | MAE (with) | R² (no outl) | RMSE (no outl) | MAE (no outl) | ΔR² | Features | n_train |
|---------|-----------|-------------|------------|--------------|----------------|---------------|-----|----------|---------|
| Fuß- & Radtunnel Südportal - D |    0.9137 |       56.91 |      40.21 |       0.8514 |          52.37 |         34.43 | -0.0623 |        7 |    9941 |
| Unterführung Steinlach/Karlstr |    0.6965 |      133.94 |      79.33 |       0.5311 |         112.32 |         63.40 | -0.1654 |        7 |    9941 |
| Neckartalradweg Hirschau - par |    0.2425 |       36.92 |      26.73 |       0.3593 |          26.62 |         18.11 | +0.1167 |        7 |    9941 |
| Radbrücke Mitte - Wöhrdstraße  |    0.5465 |       61.16 |      43.34 |       0.6143 |          41.31 |         28.86 | +0.0679 |        7 |    9941 |
| Radbrücke Ost                  |    0.7902 |       20.58 |      13.35 |       0.7629 |          15.53 |         10.42 | -0.0273 |        7 |    9941 |

Summary Statistics:
  Avg R² (with outliers):    0.6379 ± 0.2585
  Avg R² (no outliers):      0.6238 ± 0.1935
  Avg ΔR²:                   -0.0141 ± 0.1109
  Avg RMSE (with outliers):  61.90 ± 43.43
  Avg RMSE (no outliers):    49.63 ± 37.75