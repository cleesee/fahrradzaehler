## Regression

Features: hour, day_of_week, month, + hourly counts from other stations
Selection: Only use datapoints where data from all stations is available


**SUMMARY - Stadt Freiburg**


Average Test R²:   0.8993 ± 0.0953
Average Test RMSE: 38.31 ± 29.91
Average Test MAE:  25.86 ± 19.45

## Results Table

| Station | Test R² | RMSE | MAE | Features |
|---------|---------|------|-----|----------|
| FR1 Dreisam / Otto-Wels-Str. | 0.7984 | 109.33 | 69.04 | 12 |
| FR2 Elsässer Str. / Uniklinik  | 0.9171 | 34.71 | 19.57 | 12 |
| FR2 Güterbahn / Ferd.-Weiß-Str | 0.9682 | 25.60 | 16.49 | 12 |
| FR3 Eschholzstr. / Egonstr. ei | 0.9531 | 21.28 | 15.63 | 12 |
| FR6 Rotteckring / H Theater -  | 0.9537 | 64.32 | 47.32 | 12 |
| FR8 Schützenallee / Stadthalle | 0.9415 | 27.76 | 19.20 | 12 |
| H.-v.-Stephan-Str. 9 / JobRad  | 0.8966 | 16.14 | 11.71 | 12 |
| H.-v.-Stephan-Str. 9 / JobRad  | 0.9217 | 14.54 | 10.78 | 12 |
| Mundenhof 2 - Mundenhofer Str. | 0.6693 | 16.40 | 10.82 | 12 |
| Wiwilibrücke | 0.9733 | 53.05 | 38.02 | 12 |


**SUMMARY - Stadt Heidelberg**

![alt text](<../plots/data_availability_Stadt Heidelberg.png>)

**SUMMARY - Stadt Konstanz**
![alt text](<../plots/data_availability_Stadt Konstanz.png>)

Average Test R²:   0.9275 ± 0.0462
Average Test RMSE: 37.52 ± 20.22
Average Test MAE:  25.09 ± 13.50

## Results Table

| Station | Test R² | RMSE | MAE | Features |
|---------|---------|------|-----|----------|
| Alte Rheinbrücke | 0.9289 | 62.24 | 41.08 | 8 |
| Bahnhaltepunkt Fürstenberg | 0.9434 | 31.74 | 19.84 | 8 |
| Bahnhaltepunkt Petershausen | 0.9717 | 23.61 | 15.30 | 8 |
| Beethovenstraße | 0.9135 | 12.81 | 8.89 | 8 |
| Friedrichstraße | 0.8442 | 33.19 | 23.99 | 8 |
| Herosepark | 0.9636 | 61.52 | 41.46 | 8 |

**SUMMARY - Stadt Ludwigsburg**
![alt text](<../plots/data_availability_Stadt Ludwigsburg.png>)

Average Test R²:   0.8762 ± 0.1169
Average Test RMSE: 11.18 ± 8.16
Average Test MAE:  7.17 ± 5.09

## Results Table

| Station | Test R² | RMSE | MAE | Features |
|---------|---------|------|-----|----------|
| Aldinger Straße | 0.8762 | 5.31 | 3.44 | 17 |
| Alleenstraße | 0.9382 | 31.82 | 19.80 | 17 |
| Bismarckstraße | 0.8134 | 11.14 | 7.64 | 17 |
| Bottwartalstraße | 0.9666 | 7.17 | 4.29 | 17 |
| Friedrich-Ebert-Straße | 0.9591 | 18.03 | 10.37 | 17 |
| Fuchshof | 0.9492 | 8.36 | 5.55 | 17 |
| Kesseläcker (Verl. Nussackerwe | 0.7996 | 4.33 | 2.93 | 17 |
| Königinallee | 0.5281 | 10.23 | 6.93 | 17 |
| Marbacher Straße - Favoritepar | 0.9813 | 7.70 | 4.97 | 17 |
| Marbacher Straße - Neckarbrück | 0.8837 | 6.21 | 4.22 | 17 |
| Schlieffenstraße | 0.8992 | 6.34 | 4.20 | 17 |
| Schlossstraße | 0.9724 | 9.34 | 5.99 | 17 |
| Seestraße | 0.9015 | 7.43 | 4.86 | 17 |
| Solitudeallee | 0.9132 | 7.01 | 4.50 | 17 |
| Zugwiesen | 0.7606 | 27.27 | 17.82 | 17 |

**SUMMARY - Stadt Mannheim**
![alt text](<../plots/data_availability_Stadt Mannheim.png>)

Average Test R²:   0.7440 ± 0.3464
Average Test RMSE: 22.85 ± 25.04
Average Test MAE:  14.65 ± 15.09

 Results Table

| Station | Test R² | RMSE | MAE | Features |
|---------|---------|------|-----|----------|
| B38. RI. AUS | -0.2331 | 35.09 | 20.37 | 16 |
| Fernmeldeturm. | 0.9237 | 22.31 | 15.71 | 16 |
| Feudenheimerstr. stadteinwärts | 0.7868 | 8.23 | 5.69 | 16 |
| Feudenheimstr. stadtauswärts | 0.7334 | 12.09 | 7.44 | 16 |
| Konrad-Adenauer-Brücke | 0.9565 | 18.48 | 12.07 | 16 |
| Kurpfalzbrücke | 0.5677 | 93.48 | 56.89 | 16 |
| Neckarauer Übergang -Schwetzin | 0.9123 | 10.97 | 7.64 | 16 |
| Renzstraße | 0.9650 | 24.98 | 18.63 | 16 |
| Schlosspark Lindenhof (Richtun | 0.9535 | 12.53 | 7.91 | 16 |
| Theodor-Heuss-Anlage. RI. AUS | 0.7570 | 5.87 | 3.89 | 16 |
| Theodor-Heuss-Anlage. RI. IN. | 0.8611 | 7.36 | 4.89 | 16 |

**SUMMARY - Ravensburg Tws Gmbh & Co. Kg**

![
](<../plots/data_availability_Ravensburg Tws Gmbh & Co. Kg.png>)
Average Test R²:   0.8206 ± 0.0428
Average Test RMSE: 8.92 ± 2.83
Average Test MAE:  5.92 ± 1.73

Results Table

| Station | Test R² | RMSE | MAE | Features |
|---------|---------|------|-----|----------|
| 01 / 02 WGT Doggenriedstraße | 0.7970 | 4.86 | 3.30 | 9 |
| 03 WGT Krankenhaus Ost | 0.8018 | 7.44 | 5.11 | 9 |
| 04 WGT Krankenhaus West | 0.8522 | 10.61 | 7.38 | 9 |
| 05 RV Eissporthalle | 0.8499 | 5.81 | 4.06 | 9 |
| 06 Meersburger Brücke abwärts | 0.7478 | 11.45 | 7.08 | 9 |
| 07 Meersburger Brücke aufwärts | 0.8212 | 11.68 | 7.30 | 9 |
| 08 RV Bahnhofstr. | 0.8746 | 10.57 | 7.18 | 9 |

