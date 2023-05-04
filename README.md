# Como utilizar el docker compose

* Tener instalado Docker en tu computadora
* Desde la carpeta donde tengas el proyecto, correr con bash el siguiente comando:
```
docker compose up -d
```
* Para dejar de correr el docker:
```
docker compose down
```

## Comprobacion

* Para comprobar que funciona debes ingresar a la siguiente direccion:
```
https://tnmmoodle.loca.lt
```
* Si aparece un login de Moodle es porque ya esta en funcionamiento
* Las consultas se devuelven en formato JSON

## Cambiar url de Moodle

Para cambiar la url de Moodle se debe cambiar la linea 20 del Dockerfile.moodle:
```
RUN echo "* * * * * root /bin/bash -c 'lt -p 8080 -s tnmmoodle'" >> /etc/crontab
```
En este caso modificar "tnmmoodle" por el subdominio que quieras. La url de Moodle quedaria:
```
https://example.loca.lt
```
Donde "example" es el subdominio elegido. En caso de que este en uso nos dara un subdominio aleatorio, por lo tanto, deberia cambiarse por uno que sepamos que no se utilizara.