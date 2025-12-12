## Regression

Features: hour, day_of_week, month, + hourly counts from other stations  
Selection: Only use datapoints where data from all stations is available  
Oultier threshhold: 1000  


**SUMMARY - Stadt Freiburg**

![alt text](<../plots/data_availability_Stadt Freiburg.png>)



| Station | R² (with) | RMSE (with) | MAE (with) | R² (no outl) | RMSE (no outl) | MAE (no outl) | ΔR² | Features | n_train | n_train_no_outl |
|---------|-----------|-------------|------------|--------------|----------------|---------------|-----|----------|---------|-----------------|
| Wiwilibrücke                   |    0.9733 |       53.05 |      38.02 |       0.9712 |          50.37 |         36.16 | -0.0021 |       12 |    4853 |            4576 |
| FR2 Güterbahn / Ferd.-Weiß-Str |    0.9682 |       25.60 |      16.49 |       0.9598 |          25.36 |         16.17 | -0.0083 |       12 |    4853 |            4576 |
| FR1 Dreisam / Otto-Wels-Str.   |    0.7984 |      109.33 |      69.04 |       0.7507 |         108.87 |         69.24 | -0.0478 |       12 |    4853 |            4576 |
| FR3 Eschholzstr. / Egonstr. ei |    0.9531 |       21.28 |      15.63 |       0.9443 |          21.01 |         15.33 | -0.0087 |       12 |    4853 |            4576 |
| Mundenhof 2 - Mundenhofer Str. |    0.6693 |       16.40 |      10.82 |       0.6109 |          16.27 |         10.74 | -0.0583 |       12 |    4853 |            4576 |
| H.-v.-Stephan-Str. 9 / JobRad  |    0.9217 |       14.54 |      10.78 |       0.9084 |          13.92 |         10.28 | -0.0133 |       12 |    4853 |            4576 |
| H.-v.-Stephan-Str. 9 / JobRad  |    0.8966 |       16.14 |      11.71 |       0.8890 |          15.45 |         10.89 | -0.0076 |       12 |    4853 |            4576 |
| FR6 Rotteckring / H Theater -  |    0.9537 |       64.32 |      47.32 |       0.9492 |          61.77 |         45.77 | -0.0045 |       12 |    4853 |            4576 |
| FR2 Elsässer Str. / Uniklinik  |    0.9171 |       34.71 |      19.57 |       0.8989 |          33.59 |         17.89 | -0.0182 |       12 |    4853 |            4576 |
| FR8 Schützenallee / Stadthalle |    0.9415 |       27.76 |      19.20 |       0.9359 |          26.53 |         18.26 | -0.0056 |       12 |    4853 |            4576 |

Summary Statistics:
  Outlier threshold:         >1000 hourly counts
  Avg R² (with outliers):    0.8993 ± 0.0953
  Avg R² (no outliers):      0.8818 ± 0.1141
  Avg ΔR²:                   -0.0174 ± 0.0195
  Avg RMSE (with outliers):  38.31 ± 29.91
  Avg RMSE (no outliers):    37.32 ± 29.62


**SUMMARY - Stadt Heidelberg**

![alt text](<../plots/data_availability_Stadt Heidelberg.png>)


| Station | R² (with) | RMSE (with) | MAE (with) | R² (no outl) | RMSE (no outl) | MAE (no outl) | ΔR² | Features | n_train | n_train_no_outl |
|---------|-----------|-------------|------------|--------------|----------------|---------------|-----|----------|---------|-----------------|
| Plöck                          |    0.8339 |       51.94 |      29.92 |       0.8244 |          51.86 |         29.80 | -0.0095 |       16 |    9244 |            9189 |
| Gaisbergstraße                 |    0.9611 |       29.49 |      19.15 |       0.9595 |          28.99 |         18.81 | -0.0016 |       16 |    9244 |            9189 |
| Mannheimer Straße              |    0.9533 |       16.29 |      10.69 |       0.9533 |          15.66 |         10.34 | +0.0001 |       16 |    9244 |            9189 |
| Ernst-Walz-Brücke Querschnitt  |    0.9322 |       66.47 |      47.05 |       0.9274 |          64.75 |         46.00 | -0.0048 |       16 |    9244 |            9189 |
| Thedor-Heuss-Brücke Querschnit |    0.9697 |       45.98 |      29.96 |       0.9674 |          46.11 |         30.03 | -0.0023 |       16 |    9244 |            9189 |
| Rohrbacher Straße Querschnitt  |    0.9647 |       18.47 |      12.69 |       0.9626 |          18.26 |         12.52 | -0.0021 |       16 |    9244 |            9189 |
| Liebermannstraße               |    0.9798 |       20.77 |      13.83 |       0.9791 |          20.46 |         13.60 | -0.0008 |       16 |    9244 |            9189 |
| Schlierbacher Landstraße       |    0.8762 |       11.60 |       6.80 |       0.8759 |          11.16 |          6.59 | -0.0003 |       16 |    9244 |            9189 |
| Ziegelhäuser Landstraße        |    0.8399 |       13.49 |       8.33 |       0.8525 |          12.60 |          8.03 | +0.0126 |       16 |    9244 |            9189 |
| Kurfürstenanlage Querschnitt   |    0.8824 |       15.00 |      10.04 |       0.8765 |          14.92 |          9.98 | -0.0059 |       16 |    9244 |            9189 |
| Hardtstraße                    |    0.9561 |       13.10 |       8.72 |       0.9551 |          12.83 |          8.58 | -0.0011 |       16 |    9244 |            9189 |
| Berliner Straße Querschnitt    |    0.8423 |        9.63 |       7.13 |       0.8322 |           9.40 |          6.97 | -0.0101 |       16 |    9244 |            9189 |
| Eppelheimer Str. Querschnitt   |    0.8980 |        9.16 |       6.30 |       0.8952 |           8.89 |          6.12 | -0.0028 |       16 |    9244 |            9189 |
| Bahnstadtpromenade             |    0.9527 |       24.64 |      16.61 |       0.9508 |          24.15 |         16.36 | -0.0018 |       16 |    9244 |            9189 |

Summary Statistics:
  Excluded station:          Ernst-Walz-Brücke West - alt
  Outlier threshold:         >1000 hourly counts
  Avg R² (with outliers):    0.9173 ± 0.0533
  Avg R² (no outliers):      0.9151 ± 0.0541
  Avg ΔR²:                   -0.0022 ± 0.0053
  Avg RMSE (with outliers):  24.72 ± 17.72
  Avg RMSE (no outliers):    24.29 ± 17.56

**SUMMARY - Stadt Konstanz**
![alt text](<../plots/data_availability_Stadt Konstanz.png>)

| Station | R² (with) | RMSE (with) | MAE (with) | R² (no outl) | RMSE (no outl) | MAE (no outl) | ΔR² | Features | n_train | n_train_no_outl |
|---------|-----------|-------------|------------|--------------|----------------|---------------|-----|----------|---------|-----------------|
| Herosepark                     |    0.9636 |       61.52 |      41.46 |       0.9658 |          55.11 |         37.71 | +0.0022 |        8 |    6540 |            6223 |
| Bahnhaltepunkt Fürstenberg     |    0.9434 |       31.74 |      19.84 |       0.9407 |          30.39 |         19.05 | -0.0026 |        8 |    6540 |            6223 |
| Bahnhaltepunkt Petershausen    |    0.9717 |       23.61 |      15.30 |       0.9707 |          22.42 |         14.58 | -0.0010 |        8 |    6540 |            6223 |
| Alte Rheinbrücke               |    0.9289 |       62.24 |      41.08 |       0.9440 |          52.83 |         34.98 | +0.0151 |        8 |    6540 |            6223 |
| Friedrichstraße                |    0.8442 |       33.19 |      23.99 |       0.8455 |          30.66 |         22.23 | +0.0013 |        8 |    6540 |            6223 |
| Beethovenstraße                |    0.9135 |       12.81 |       8.89 |       0.9198 |          11.65 |          7.95 | +0.0063 |        8 |    6540 |            6223 |

Summary Statistics:
  Outlier threshold:         >1000 hourly counts
  Avg R² (with outliers):    0.9275 ± 0.0462
  Avg R² (no outliers):      0.9311 ± 0.0458
  Avg ΔR²:                   +0.0035 ± 0.0064
  Avg RMSE (with outliers):  37.52 ± 20.22
  Avg RMSE (no outliers):    33.84 ± 17.07

**SUMMARY - Stadt Ludwigsburg**
![alt text](<../plots/data_availability_Stadt Ludwigsburg.png>)

| Station | R² (with) | RMSE (with) | MAE (with) | R² (no outl) | RMSE (no outl) | MAE (no outl) | ΔR² | Features | n_train | n_train_no_outl |
|---------|-----------|-------------|------------|--------------|----------------|---------------|-----|----------|---------|-----------------|
| Alleenstraße                   |    0.9382 |       31.82 |      19.80 |       0.9383 |          31.79 |         19.76 | +0.0001 |       17 |   31515 |           31508 |
| Marbacher Straße - Favoritepar |    0.9813 |        7.70 |       4.97 |       0.9814 |           7.70 |          4.96 | +0.0000 |       17 |   31515 |           31508 |
| Schlieffenstraße               |    0.8992 |        6.34 |       4.20 |       0.8992 |           6.34 |          4.20 | +0.0001 |       17 |   31515 |           31508 |
| Fuchshof                       |    0.9492 |        8.36 |       5.55 |       0.9492 |           8.36 |          5.55 | -0.0000 |       17 |   31515 |           31508 |
| Seestraße                      |    0.9015 |        7.43 |       4.86 |       0.9023 |           7.40 |          4.84 | +0.0008 |       17 |   31515 |           31508 |
| Schlossstraße                  |    0.9724 |        9.34 |       5.99 |       0.9724 |           9.33 |          5.99 | +0.0000 |       17 |   31515 |           31508 |
| Kesseläcker (Verl. Nussackerwe |    0.7996 |        4.33 |       2.93 |       0.7995 |           4.34 |          2.93 | -0.0001 |       17 |   31515 |           31508 |
| Zugwiesen                      |    0.7606 |       27.27 |      17.82 |       0.7606 |          27.28 |         17.82 | -0.0000 |       17 |   31515 |           31508 |
| Bismarckstraße                 |    0.8134 |       11.14 |       7.64 |       0.8138 |          11.13 |          7.63 | +0.0004 |       17 |   31515 |           31508 |
| Solitudeallee                  |    0.9132 |        7.01 |       4.50 |       0.9133 |           7.01 |          4.49 | +0.0000 |       17 |   31515 |           31508 |
| Aldinger Straße                |    0.8762 |        5.31 |       3.44 |       0.8761 |           5.31 |          3.44 | -0.0000 |       17 |   31515 |           31508 |
| Bottwartalstraße               |    0.9666 |        7.17 |       4.29 |       0.9666 |           7.17 |          4.29 | -0.0000 |       17 |   31515 |           31508 |
| Marbacher Straße - Neckarbrück |    0.8837 |        6.21 |       4.22 |       0.8836 |           6.21 |          4.22 | -0.0000 |       17 |   31515 |           31508 |
| Königinallee                   |    0.5281 |       10.23 |       6.93 |       0.5282 |          10.23 |          6.93 | +0.0001 |       17 |   31515 |           31508 |
| Friedrich-Ebert-Straße         |    0.9591 |       18.03 |      10.37 |       0.9591 |          18.03 |         10.37 | -0.0000 |       17 |   31515 |           31508 |

Summary Statistics:
  Outlier threshold:         >1000 hourly counts
  Avg R² (with outliers):    0.8762 ± 0.1169
  Avg R² (no outliers):      0.8763 ± 0.1169
  Avg ΔR²:                   +0.0001 ± 0.0002
  Avg RMSE (with outliers):  11.18 ± 8.16
  Avg RMSE (no outliers):    11.17 ± 8.16


**SUMMARY - Stadt Mannheim**
![alt text](<../plots/data_availability_Stadt Mannheim.png>)

| Station | R² (with) | RMSE (with) | MAE (with) | R² (no outl) | RMSE (no outl) | MAE (no outl) | ΔR² | Features | n_train | n_train_no_outl |
|---------|-----------|-------------|------------|--------------|----------------|---------------|-----|----------|---------|-----------------|
| Renzstraße                     |    0.9650 |       24.98 |      18.63 |       0.9652 |          24.93 |         18.62 | +0.0002 |       16 |   15768 |           15767 |
| Kurpfalzbrücke                 |    0.5677 |       93.48 |      56.89 |       0.5690 |          93.35 |         56.72 | +0.0013 |       16 |   15768 |           15767 |
| Jungbuschbrücke                |    0.8304 |       16.97 |      12.28 |       0.8272 |          17.13 |         12.38 | -0.0032 |       16 |   15768 |           15767 |
| Konrad-Adenauer-Brücke         |    0.9565 |       18.48 |      12.07 |       0.9565 |          18.48 |         12.07 | +0.0000 |       16 |   15768 |           15767 |
| Lindenhofüberführung           |    0.2558 |       46.90 |      27.49 |       0.2624 |          46.69 |         27.47 | +0.0066 |       16 |   15768 |           15767 |
| Neckarauer Übergang -Schwetzin |    0.9123 |       10.97 |       7.64 |       0.9124 |          10.96 |          7.63 | +0.0001 |       16 |   15768 |           15767 |
| Schlosspark Lindenhof (Richtun |    0.9535 |       12.53 |       7.91 |       0.9537 |          12.51 |          7.91 | +0.0002 |       16 |   15768 |           15767 |
| Feudenheimstr. stadtauswärts   |    0.7334 |       12.09 |       7.44 |       0.7334 |          12.09 |          7.43 | -0.0000 |       16 |   15768 |           15767 |
| Feudenheimerstr. stadteinwärts |    0.7868 |        8.23 |       5.69 |       0.7868 |           8.23 |          5.69 | +0.0000 |       16 |   15768 |           15767 |
| Luzenbergstr.                  |    0.8495 |        9.84 |       7.16 |       0.8661 |           9.28 |          6.83 | +0.0167 |       16 |   15768 |           15767 |
| B38. RI. AUS                   |   -0.2331 |       35.09 |      20.37 |      -0.2263 |          34.99 |         20.52 | +0.0068 |       16 |   15768 |           15767 |
| Theodor-Heuss-Anlage. RI. IN.  |    0.8611 |        7.36 |       4.89 |       0.8619 |           7.34 |          4.87 | +0.0009 |       16 |   15768 |           15767 |
| Theodor-Heuss-Anlage. RI. AUS  |    0.7570 |        5.87 |       3.89 |       0.7573 |           5.86 |          3.89 | +0.0003 |       16 |   15768 |           15767 |
| Fernmeldeturm.                 |    0.9237 |       22.31 |      15.71 |       0.9239 |          22.29 |         15.71 | +0.0002 |       16 |   15768 |           15767 |

Summary Statistics:
  Outlier threshold:         >1000 hourly counts
  Avg R² (with outliers):    0.7228 ± 0.3341
  Avg R² (no outliers):      0.7250 ± 0.3323
  Avg ΔR²:                   +0.0021 ± 0.0049
  Avg RMSE (with outliers):  23.22 ± 23.28
  Avg RMSE (no outliers):    23.15 ± 23.26

**SUMMARY - Ravensburg Tws Gmbh & Co. Kg**

![
](<../plots/data_availability_Ravensburg Tws Gmbh & Co. Kg.png>)


| Station | R² (with) | RMSE (with) | MAE (with) | R² (no outl) | RMSE (no outl) | MAE (no outl) | ΔR² | Features | n_train | n_train_no_outl |
|---------|-----------|-------------|------------|--------------|----------------|---------------|-----|----------|---------|-----------------|
| 03 WGT Krankenhaus Ost         |    0.8018 |        7.44 |       5.11 |       0.8018 |           7.44 |          5.11 | +0.0000 |        9 |   23169 |           23169 |
| 04 WGT Krankenhaus West        |    0.8522 |       10.61 |       7.38 |       0.8522 |          10.61 |          7.38 | +0.0000 |        9 |   23169 |           23169 |
| 05 RV Eissporthalle            |    0.8499 |        5.81 |       4.06 |       0.8499 |           5.81 |          4.06 | +0.0000 |        9 |   23169 |           23169 |
| 06 Meersburger Brücke abwärts  |    0.7478 |       11.45 |       7.08 |       0.7478 |          11.45 |          7.08 | +0.0000 |        9 |   23169 |           23169 |
| 07 Meersburger Brücke aufwärts |    0.8212 |       11.68 |       7.30 |       0.8212 |          11.68 |          7.30 | +0.0000 |        9 |   23169 |           23169 |
| 08 RV Bahnhofstr.              |    0.8746 |       10.57 |       7.18 |       0.8746 |          10.57 |          7.18 | +0.0000 |        9 |   23169 |           23169 |
| 01 / 02 WGT Doggenriedstraße   |    0.7970 |        4.86 |       3.30 |       0.7970 |           4.86 |          3.30 | +0.0000 |        9 |   23169 |           23169 |

Summary Statistics:
  Outlier threshold:         >1000 hourly counts
  Avg R² (with outliers):    0.8206 ± 0.0428
  Avg R² (no outliers):      0.8206 ± 0.0428
  Avg ΔR²:                   +0.0000 ± 0.0000
  Avg RMSE (with outliers):  8.92 ± 2.83
  Avg RMSE (no outliers):    8.92 ± 2.83

**SUMMARY - Reutlingen**
![alt text](<../plots/data_availability_Stadt Reutlingen.png>)


| Station | R² (with) | RMSE (with) | MAE (with) | R² (no outl) | RMSE (no outl) | MAE (no outl) | ΔR² | Features | n_train | n_train_no_outl |
|---------|-----------|-------------|------------|--------------|----------------|---------------|-----|----------|---------|-----------------|
| Tübinger Tor                   |    0.7325 |       32.01 |      14.15 |       0.8879 |          20.63 |         11.93 | +0.1555 |       10 |   31284 |           31204 |
| Charlottenstraße               |    0.5401 |       19.93 |       9.18 |       0.7698 |          14.04 |          7.81 | +0.2297 |       10 |   31284 |           31204 |
| Konrad-Adenauer-Straße         |    0.8865 |        6.13 |       4.18 |       0.8874 |           6.08 |          4.15 | +0.0009 |       10 |   31284 |           31204 |
| Metzgerstraße                  |   -0.7899 |       30.87 |       9.64 |       0.5541 |          15.36 |          6.82 | +1.3440 |       10 |   31284 |           31204 |
| Bellinostraße                  |    0.2603 |       35.69 |      11.38 |       0.8053 |          18.26 |          7.94 | +0.5450 |       10 |   31284 |           31204 |
| Hindenburgstraße               |   -0.0006 |      306.00 |      40.06 |       0.4906 |          34.02 |          8.18 | +0.4912 |       10 |   31284 |           31204 |
| Moltkestraße                   |    0.6947 |        7.06 |       3.81 |       0.8022 |           5.66 |          3.47 | +0.1075 |       10 |   31284 |           31204 |
| Unter den Linden               |    0.8670 |       11.32 |       7.49 |       0.9024 |           9.65 |          6.95 | +0.0354 |       10 |   31284 |           31204 |

Summary Statistics:
  Outlier threshold:         >1000 hourly counts
  Avg R² (with outliers):    0.3988 ± 0.5692
  Avg R² (no outliers):      0.7625 ± 0.1566
  Avg ΔR²:                   +0.3636 ± 0.4434
  Avg RMSE (with outliers):  56.13 ± 101.63
  Avg RMSE (no outliers):    15.46 ± 9.25

**SUMMARY - Stuttgart**
![alt text](<../plots/data_availability_Landeshauptstadt Stuttgart.png>)

| Station | R² (with) | RMSE (with) | MAE (with) | R² (no outl) | RMSE (no outl) | MAE (no outl) | ΔR² | Features | n_train | n_train_no_outl |
|---------|-----------|-------------|------------|--------------|----------------|---------------|-----|----------|---------|-----------------|
| König-Karls-Brücke Barometer   |    0.8407 |       41.07 |      25.81 |       0.8400 |          41.16 |         25.88 | -0.0007 |       17 |   36125 |           36123 |
| Böblinger Straße               |    0.8460 |       21.10 |      12.08 |       0.8460 |          21.10 |         12.08 | -0.0000 |       17 |   36125 |           36123 |
| Taubenheimstraße               |    0.5070 |        7.74 |       5.33 |       0.5323 |           7.54 |          5.19 | +0.0253 |       17 |   36125 |           36123 |
| Waiblinger Straße              |    0.8532 |        4.69 |       3.26 |       0.8533 |           4.68 |          3.26 | +0.0001 |       17 |   36125 |           36123 |
| Samaraweg                      |    0.8604 |       25.80 |      14.79 |       0.8613 |          25.72 |         14.73 | +0.0010 |       17 |   36125 |           36123 |
| Waldburgstraße                 |    0.8347 |       10.42 |       5.24 |       0.8357 |          10.39 |          5.23 | +0.0011 |       17 |   36125 |           36123 |
| Kremmlerstraße                 |    0.8883 |       13.06 |       8.17 |       0.8887 |          13.04 |          8.16 | +0.0005 |       17 |   36125 |           36123 |
| Kirchheimer Straße             |    0.9119 |        7.86 |       5.12 |       0.9124 |           7.84 |          5.11 | +0.0005 |       17 |   36125 |           36123 |
| Stuttgarter Straße             |    0.7707 |        8.89 |       5.33 |       0.7706 |           8.89 |          5.33 | -0.0001 |       17 |   36125 |           36123 |
| Solitudestraße                 |    0.8214 |        8.30 |       5.03 |       0.8216 |           8.30 |          5.03 | +0.0001 |       17 |   36125 |           36123 |
| Am Kräherwald                  |    0.8670 |        6.75 |       4.37 |       0.8669 |           6.75 |          4.37 | -0.0002 |       17 |   36125 |           36123 |
| Inselstraße                    |    0.9057 |       13.20 |       7.79 |       0.9058 |          13.20 |          7.77 | +0.0001 |       17 |   36125 |           36123 |
| Neckartalstraße                |    0.3869 |       13.25 |       8.63 |       0.3803 |          13.32 |          8.66 | -0.0066 |       17 |   36125 |           36123 |
| Lautenschlager Straße          |    0.8215 |       20.90 |      14.12 |       0.8215 |          20.90 |         14.12 | -0.0000 |       17 |   36125 |           36123 |
| Tübinger Straße                |    0.9190 |       29.42 |      20.97 |       0.9190 |          29.40 |         20.96 | +0.0001 |       17 |   36125 |           36123 |

Summary Statistics:
  Outlier threshold:         >1000 hourly counts
  Avg R² (with outliers):    0.8023 ± 0.1511
  Avg R² (no outliers):      0.8037 ± 0.1491
  Avg ΔR²:                   +0.0014 ± 0.0068
  Avg RMSE (with outliers):  15.50 ± 10.23
  Avg RMSE (no outliers):    15.48 ± 10.25
**SUMMARY - Tübingen**

![alt text](<../plots/data_availability_Stadt Tübingen.png>)
| Station | R² (with) | RMSE (with) | MAE (with) | R² (no outl) | RMSE (no outl) | MAE (no outl) | ΔR² | Features | n_train | n_train_no_outl |
|---------|-----------|-------------|------------|--------------|----------------|---------------|-----|----------|---------|-----------------|
| Fuß- & Radtunnel Südportal - D |    0.9137 |       56.91 |      40.21 |       0.9147 |          56.60 |         39.80 | +0.0010 |        7 |    9941 |            9929 |
| Unterführung Steinlach/Karlstr |    0.6965 |      133.94 |      79.33 |       0.6964 |         133.99 |         79.69 | -0.0001 |        7 |    9941 |            9929 |
| Neckartalradweg Hirschau - par |    0.2425 |       36.92 |      26.73 |       0.2239 |          37.38 |         26.46 | -0.0186 |        7 |    9941 |            9929 |
| Radbrücke Mitte - Wöhrdstraße  |    0.5465 |       61.16 |      43.34 |       0.5254 |          62.57 |         43.10 | -0.0210 |        7 |    9941 |            9929 |
| Radbrücke Ost                  |    0.7902 |       20.58 |      13.35 |       0.7867 |          20.75 |         13.06 | -0.0034 |        7 |    9941 |            9929 |

Summary Statistics:
  Outlier threshold:         >1000 hourly counts
  Avg R² (with outliers):    0.6379 ± 0.2585
  Avg R² (no outliers):      0.6294 ± 0.2673
  Avg ΔR²:                   -0.0084 ± 0.0106
  Avg RMSE (with outliers):  61.90 ± 43.43
  Avg RMSE (no outliers):    62.26 ± 43.36