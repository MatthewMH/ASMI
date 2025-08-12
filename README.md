# ASMI (Artificial Intelligence System for Medical Images)

It is a computer-aided diagnosis of from medical images. Current features are COVID-19 diagnosis and Acid Fast Bacillus bacteria counting from sputum. 

## Step to INSTALL 

1. ```git clone https://github.com/MatthewMH/ASMI.git```

2. create local env with ```python=3.10```

3. run command ```pip install -r requirements.txt```

4. rename ```.env.example``` to ```.env```

5. on .env file you need to set your config

``SECRET_KEY=YOUR_KEY``

``DB_NAME=YOUR_DB_NAME`` 

``DB_USER=YOUR_DB_USER``

``DB_PASS=YOUR_DB_PASS``

 	5.1 for your SECRET_KEY run this command 

	python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())”

	5.3 paste the generated key to your .env file

6. run command ```python manage.py makemigrations```

7. run command ```python manage.py migrate```

8. Login to http://127.0.0.1:8000/

9. you need to create admin account by run this command

	```python manage.py createsuperuser```

# Acknowledgment
This project is an upgrade version of InDRI (Intelligent Diagnosis of Radiology Images). 
InDRI link: https://github.com/mahmudisnan/indri/tree/main
InDRI paper: 
``` Isnan, Mahmud, et al. "InDRI: Intelligent Diagnosis Radiology Images." 2024 6th International Conference on Cybernetics and Intelligent System (ICORIS). IEEE, 2024.```
