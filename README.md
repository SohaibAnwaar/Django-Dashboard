# Dependencies
1. conda (https://docs.conda.io/en/latest/miniconda.html)
2. conda environment (environment.yml)
3. Python 3.9


# Setup
1. install conda (https://docs.conda.io/en/latest/miniconda.html)
2. create conda environment
    conda env create -f environment.yml
3. activate conda environment
    conda activate dashboard
4. Install requirements
    pip install -r requirements.txt

# Run
1. activate conda environment
    conda activate dashboard
2. run dashboard

# Make Migration
1. python manage.py makemigrations
2. python manage.py migrate

# RunServer
1. python manage.py runserver
2. http://127.0.0.1:8000/api/schema/docs/#/

# Make Secret key Django
Make Django secret key and add to settings.py
```
SECRET_KEY = ''
```
1. ```python manage.py shell -c 'from django.core.management import utils; print(utils.get_random_secret_key())'```
