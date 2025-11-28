deactivate 
rm -rf .env

python3.10 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
source .env/bin/activate
