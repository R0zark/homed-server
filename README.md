# Homed Server

### [EN]
The purpose of this project is to set up a server for handling requests from [HomeD](https://github.com/R0zark/homed-app) app. It is a REST API written in Django, a famous Python framework. It is used to obtain data from files stored in an embedded database.

All the files are storaged in the media directory, if media directory doesn't exist you must to create it.

### [ES]

El proposito de este proyecto es establecer un servidor que se encargue de controlar las peticiones de la aplicación [HomeD](https://github.com/R0zark/homed-app). Es una API REST hecha en Django, un famoso framework de Python. Se encarga de obtener los datos de los ficheros almacenados en una base de datos embebida.

Todos los ficheros se almacenan en el directorio media, si no existe debes de crearlo.
### Routes

Route | HTTP Method | Description 
------------ | ------------- |-----------
/ | GET | Welcome message.
/files | GET | List all the files.
/upload| POST| Upload a file sended from the frontend.
/[integer] parameter | GET | Get the information of a file.
/file/[integer] parameter | GET | Download the specified file 
/delete/[integer] parameter | GET | Delete the specified file.
