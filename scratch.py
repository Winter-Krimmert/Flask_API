from faker import Faker

import faker_commerce
from random import randint

fake = Faker()
fake.add_provider(faker_commerce.Provider)

for _ in range(10):
    print(fake.ecommerce_name() + ' costs $' + str(randint(1, 100)))




# Set up virtual environment
# python3 -m venv venv
# source venv/bin/activate
# Install the following:
# pip install Flask-Limiter && pip freeze > requirements.txt
# pip install Faker
# pip install flask-caching && pip freeze > requirements.txt
# pip install flask-swagger-ui && pip freeze > requirements.txt
# pip install Flask-Migrate
# pip install faker-commerce
# pip install flask_marshmallow
# pip install PyJWT
# pip install flask_httpauth
# pip install mysql
# pip install mysql-connector-python
# pip install python-dotenv
# pip instlal marshmallow-sqlalchemy
# pip install marshmallow

# Create a .env file in the root directory and add the following:
# DATABASE_URL=mysql+mysqlconnector://root:sqlpass#4@localhost/Advanced Ecommerce DB
# SECRET_KEY=a20476a941f034911ec85b1c933b896f73be6fbe8ca8f0e4f551f26a904e2fb4