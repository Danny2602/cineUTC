set -o errexit
pip install -r requirements.txt

py -m collectstatic --noinput
py -m manage migrate