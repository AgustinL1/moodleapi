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
MOODLE_SUBDOMAIN = moodlesubdomain
API_SUBDOMAIN =
```
Al determinar el subdominio, la url sera la siguiente: 
```
https://moodlesubdomain.loca.lt
```
Siendo "moodlesubdomain" el subdominio que elegimos. En caso de que este en uso nos dara un subdominio aleatorio, por lo tanto, deberia cambiarse por uno que sepamos que no se utilizara.

## Especificar url de la API

De la misma forma que el subdominio de Moodle, debe especificarse en el archivo .env, debe quedar de la siguiente forma: 
```
MOODLE_SUBDOMAIN =
API_SUBDOMAIN = apisubdomain
```
Al determinar el subdominio, la url sera la siguiente: 
```
https://apisubdomain.loca.lt
```

## Comprobacion

* Para comprobar que funciona debes ingresar a la siguiente direccion:
```
https://moodlesubdomain.loca.lt
```
* Si aparece un login de Moodle es porque ya esta en funcionamiento
* Las consultas se devuelven en formato JSON
* Proceder de la misma forma para verificar si anda la API