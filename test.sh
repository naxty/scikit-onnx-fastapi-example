curl -X POST \
  http://localhost/predict \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: 9a75cc9b-f940-40a0-9cb0-f02986e1e16d' \
  -H 'cache-control: no-cache' \
  -H 'token: 1337' \
  -d '{
  "CRIM": 300,
  "ZN": 0,
  "INDUS": 0,
  "CHAS": 0,
  "NOX": 0,
  "RM": 0,
  "AGE": 0,
  "DIS": 0,
  "RAD": 0,
  "TAX": 0,
  "PTRATIO": 0,
  "B": 0,
  "LSTAT": 0
}'