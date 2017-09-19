
# Graphql + Python + Django

Implementación de Python de [Paradigma: Graphql + Spring Boot](https://github.com/paradigmadigital/graphql-spring-boot) 

## Librerías utilizadas:

- [Django](https://github.com/django/django)
- [Graphene-django](https://github.com/graphql-python/graphene-django) 
- [Django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar) 

## Configuración

```bash
virtualenv --python=python3.6 venv
source venv/bin/activate
pip install -r requirements.txt
cd factory
python manage.py migrate
python manage.py migrate --database=brands_ddbb
```

```bash
sqlite3 db.sqlite3_brands
```

```sql
insert into cars_brand (name) values("Seat");
insert into cars_brand (name) values("Ford");
```

```cmd
sqlite3 db.sqlite3
```

```sql
insert into cars_model (name, year, brand_id) values("Ibiza", 2015, 1);
insert into cars_model (name, year, brand_id) values("Arona", 2014, 1);
insert into cars_model (name, year, brand_id) values("León", 2013, 1);
insert into cars_model (name, year, brand_id) values("Alhambra", 2012, 1);
insert into cars_model (name, year, brand_id) values("Ateca", 2011, 1);
insert into cars_model (name, year, brand_id) values("Toledo", 2017, 1);
insert into cars_model (name, year, brand_id) values("Tourneo", 2001, 2);
insert into cars_model (name, year, brand_id) values("GT", 2017, 2);
```

```bash
python manage.py loaddata cars/fixtures/01_initial_data.json 
```
```python
client = MongoClient('127.0.0.1', 28000)

db = client.factory

brands = db.brands
brands.insert_one({"name": "seat"})
brands.insert_one({"name": "Ford"})
```

## Ejecución

```bash
python manage.py runserver
```

## Esquema

Accede tu mismo al [editor de consultas](http://localhost:8000/graphql) del proyecto una vez arrancado

Ejemplos de consultas y mutaciones:

```graphql

{
  cars {
    id
  }
}

```

```graphql

mutation {
    createCar(model: 1,color:"brown"){
    car{
      id
      color
    }
    ok
  }
}

```



```graphql

 {
  cars {
    id
    color
    model {
      id
      name
    }
  }
 
  models{
    id
  }

  car(id: "_id_que_corresponda_"){
    id
  }
}

```





