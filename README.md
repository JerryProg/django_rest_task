# Django rest task
Aplicación del tipo RESTful con los recursos de Python. Está basado en la funciones CRUD.

### Requerimientos:

El archivo requirements.txt contiene los recursos necesarios para crear el proyecto.

Django 4.2.7

Django Rest Framework 3.14.0

PosgreSQL psycopg2 2.9.9

Python decouple 3.8

Django oauth toolkit 2.3.0

### PROCEDIMIENTO PARA REALIZAR LAS PRUEBAS:
Creación de usuario: Debemos crear un usuario con el comando

`python manage.py createsuperuser`

Ingresamos los datos que nos pide e ingresamos al panel de administración de django. Se pueden crear los usuarios también en el panel.

![Crear user en django](/readme_img/django_create_user.png)

### CREAR LA APLICACION EN OAUTH2:
Para implementar la autenticación y la generación de un token debemos agregar los siguientes datos:

(Debemos ingresar nuestras credenciales en el panel de admin para poder crear la app)

Name: Nombre de la aplicación.

Client Id y Client Secret: Id y password de nuestra app que genera automaticamente cuando creamos la aplicación. Se pueden cambiar.

Client type: Vamos a seleccionar *Public*.

Authorization grant type: Selccionamos *Authorization grant type*

Guardamos para crear la aplicación

![Crear app oauth2](/readme_img/oauth_create_application.png)

### GENERAR EL TOKEN CON POSTMAN:
Utilizamos la API de pruebas llamada *Postman* para generar el token:

En la pestaña de *Authorization* debemos ingresar las credenciales de username y password con client Id y Client secret *respectivamente*. También seleccionamos Type: *Basic Auth*

![Crear app oauth2](/readme_img/postman_oauth_create_token_1.png)

También en la otra pestaña *Body* agregamos nuestras credenciales para generar el token; seleccionamos la opción *form-data*.

Usamos username y password de nuestro usuario que creamos y agregamos el campo *grant_type* con el valor password.

![Crear app oauth2](/readme_img/postman_oauth_create_token_2.png)

### PRUEBAS CRUD CON POSTMAN:
Vamos a realizar las pruebas para cada uno de los principales métodos (GET, POST, PUT, DELETE).
Debemos escoger en la ventana de la api el *método* y escribir la *url*.

Como habilitamos la autenticación con token debemos utilizar el token que generamos y agregarlo en la pestaña *Authorization -> Type* en Postman para poder realizar las pruebas.

![Crear app oauth2](/readme_img/oauth_token_generated.png)

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

