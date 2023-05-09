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

## Especificar url de Moodle

Para especificar el subdominio de la url de Moodle se debe crear un archivo .env replicando el archivo .env.example.
El archivo debe quedar de la siguiente forma:
```
MOODLE_SUBDOMAIN = example
```
Al determinar el subdominio, la url sera la siguiente: 
```
https://example.loca.lt
```
Siendo "example" el subdominio que elegimos. En caso de que este en uso nos dara un subdominio aleatorio, por lo tanto, deberia cambiarse por uno que sepamos que no se utilizara.

## Comprobacion

* Para comprobar que funciona debes ingresar a la siguiente direccion:
```
https://example.loca.lt
```
* Si aparece un login de Moodle es porque ya esta en funcionamiento
* Las consultas se devuelven en formato JSON