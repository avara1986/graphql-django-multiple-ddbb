
# Graphql + Python + Django

Implementación de Python de [Paradigma: Graphql + Spring Boot](https://github.com/paradigmadigital/graphql-spring-boot) 

## Frameworks utilizados:

- [Django](https://github.com/django/django)
- [Graphene-django](https://github.com/graphql-python/graphene-django) 


## Requisitos

Python 3.x

Django

graphene-django

Ver requirements.txt

## Configuración


```
virtualenv --python=python3.6 venv
source venv/bin/activate
pip install -r requirements.txt
cd factory
python manage.py migrate
python manage.py loaddata cars/fixtures/01_initial_data.json 

```

## Ejecución

```
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





