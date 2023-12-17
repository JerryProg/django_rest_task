# Django rest task
Aplicación del tipo RESTful con los recursos de Python. Está basado en la funciones CRUD.

### Requerimientos:

El archivo requirements.txt contiene los recursos necesarios para crear el proyecto.

Django 4.2.7

Django Rest Framework 3.14.0

PosgreSQL psycopg2 2.9.9

Python decouple 3.8

### PROCEDIMIENTO PARA REALIZAR LAS PRUEBAS:
Creación de usuario: Debemos crear un usuario con el comando

`python manage.py createsuperuser`

Ingresamos los datos que nos pide e ingresamos al panel de administración de django. Se pueden crear los usuarios también en el panel.

![Crear user en django](/readme_img/django_create_user.png)

Utilizamos la API de pruebas llamada *Postman* para realizar las pruebas para cada uno de los principales métodos (GET, POST, PUT, DELETE).
Debemos escoger en la ventana de la api el *método* y escribir la *url*.

### CREATE.

Utiliza el método POST para crear el elemento. Tenemos que agregar en la pestaña de *body* todos los campos que vamos a enviar teniendo en cuenta que 
los nombres deben **coincidir** con los que asignamos en el modelo creado en django.


URL: http://localhost:8000/api/marketplace/create/

Resultado.

![Crear user en django](/readme_img/postman_create.png)

### READ.

Utiliza el método GET para crear el elemento. Tenemos dos opciones; ver una lista con todos los elementos creados y solo ver un elemento (a través del id del elemento).

URL: http://localhost:8000/api/marketplace/

![Crear user en django](/readme_img/postman_list.png)

URL: http://localhost:8000/api/marketplace/pk/

![Crear user en django](/readme_img/postman_retrieve.png)

#### Tenemos que sustituir por el valor del pk de las urls por el valor llamado id.

### UPDATE.

Utiliza el método PUT para actualizar el elemento. Tenemos que agregar en la pestaña de *body* todos los campos que queremos actualizar teniendo en cuenta que 
los nombres deben **coincidir** con los que asignamos en el modelo creado en django.

URL: http://localhost:8000/api/marketplace/pk/update/

![Crear user en django](/readme_img/postman_update.png)

#### Tenemos que sustituir por el valor del pk de las urls por el valor llamado id.

### DELETE

Utiliza el método DELETE para borrar el elemento. Solo debemos agregar el id del elemento que querenmos borrar

![Crear user en django](/readme_img/django_admin_before_delete.png)

URL: http://localhost:8000/api/marketplace/pk/delete/

![Crear user en django](/readme_img/postman_delete.png)

Panel de admin de django sin el elemento borrado.

![Crear user en django](/readme_img/django_admin_after_delete.png)

#### Tenemos que sustituir por el valor del pk de las urls por el valor llamado id.

