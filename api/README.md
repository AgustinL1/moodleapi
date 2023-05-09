# API Moodle

La siguiente API creada con Flask se utiliza como intermediario entre contenedores Docker de MariaDB y Moodle.
Se utiliza Localtunnel para redireccionar nuestro host local a internet y que se pueda acceder desde cualquier computadora.

Para especificar un subdominio para la url crear un archivo .env replicando el archivo .env.example.
El archivo debe quedar de la siguiente forma:
```
API_SUBDOMAIN = example
```
Al determinar el subdominio, la url sera la siguiente: 
```
https://example.loca.lt
```
Siendo "example" el subdominio que elegimos. En caso de que este en uso nos dara un subdominio aleatorio, por lo tanto, deberia cambiarse por uno que sepamos que no se utilizara.