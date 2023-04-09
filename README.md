# Como utilizar el docker-compose

* Tener instalado Docker en tu computadora
* Desde la carpeta donde tengas el proyecto, correr con bash el siguiente comando:
````
docker-compose up -d
````
* Si ya ejecutaste el anterior comando, la proxima vez que quieras correr el docker solamente ejecuta el siguiente comando:
````
docker-compose up
````
* Para dejar de correr el docker:
````
docker-compose down
````

## Comprobacion

* Para comprobar que funciona debes ingresar a la siguiente direccion:
````
https://localhost:8080
````
* Si aparece un login de Moodle es porque ya esta en funcionamiento
* Las consultas se devuelven en formato JSON