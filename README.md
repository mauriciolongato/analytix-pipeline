# analytix-pipeline

### Setup do ambiente de desenvolvimento

Clone o repositório

Rode o docker-compose
    
    docker-compose -f docker-compose.yml build
    docker-compose -f docker-compose.yml up -d

   
Setup do django - makemigrations, migrate and admin
    
    docker-compose -f docker-compose.yml exec web python manage.py makemigrations
    docker-compose -f docker-compose.yml exec web python manage.py migrate
    docker-compose -f docker-compose.yml exec web python manage.py createsuperuser