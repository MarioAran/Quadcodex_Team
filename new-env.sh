deactivate 
rm -rf .env
mkdir data
python3.10 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
source .env/bin/activate

#dowload gym recomendatio dataset
URL="https://data.mendeley.com/public-files/datasets/zw8mtbm5b9/files/427f3c4b-58d5-42d1-8de1-163408184f6b/file_downloaded"
# Archivo de salida (puedes cambiarle el nombre si quieres)
OUTPUT="data/gym_recomendation.xlsx"
# Descargar archivo
curl -L "$URL" -o "$OUTPUT"
echo "Descarga completa. Archivo guardado en $OUTPUT"

URL=https://www.kaggle.com/api/v1/datasets/download/ambarishdeb/gym-exercises-dataset
OUTPUT="data/gym_exercises.zip"
curl -L "$URL" -o "$OUTPUT"
unzip data/gym_exercises.zip -d data/
echo "Descarga completa. Archivo guardado en $OUTPUT"
rm -rf "$OUTPUT"


URL=https://www.kaggle.com/api/v1/datasets/download/peshimaammuzammil/the-ultimate-gym-exercises-dataset-for-all-levels
OUTPUT="data/the-ultimate-gym-exercises-dataset-for-all-levels.zip"
curl -L "$URL" -o "$OUTPUT"
unzip data/the-ultimate-gym-exercises-dataset-for-all-levels.zip -d data/
echo "Descarga completa. Archivo guardado en $OUTPUT"
rm -rf "$OUTPUT"
