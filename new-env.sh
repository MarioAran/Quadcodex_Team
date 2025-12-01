deactivate 
rm -rf .env
mkdir Data
python3.10 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
source .env/bin/activate


#dowload gym recomendatio dataset
#!/bin/bash

URL="https://www.kaggle.com/api/v1/datasets/download/niharika41298/gym-exercise-data"
# Archivo de salida (puedes cambiarle el nombre si quieres)
OUTPUT="data/gym_recomendation.xlsx"
# Descargar archivo
curl -L "$URL" -o "$OUTPUT"
echo "Descarga completa. Archivo guardado en $OUTPUT"

