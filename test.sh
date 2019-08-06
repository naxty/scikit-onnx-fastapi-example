curl -X POST \
  http://localhost/predict \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: 9a75cc9b-f940-40a0-9cb0-f02986e1e16d' \
  -H 'cache-control: no-cache' \
  -H 'token: 1337' \
  -d '{
  "CRIM": 0.06724,
  "ZN": 0.0,
  "INDUS": 3.24,
  "CHAS": 0.0,
  "NOX": 0.46,
  "RM": 6.333,
  "AGE": 17.2,
  "DIS": 5.2146,
  "RAD": 4.0,
  "TAX": 430.0,
  "PTRATIO": 16.9,
  "B": 375.21,
  "LSTAT": 7.34
}'