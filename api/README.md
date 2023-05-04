# API Moodle

La siguiente API creada con Flask se utiliza como intermediario entre contenedores Docker de MariaDB y Moodle.
Se utiliza Localtunnel para redireccionar nuestro host local a internet y que se pueda acceder desde cualquier computadora.

Para realizar peticiones la url por defecto es:
```
https://tnmapi.loca.lt
```
Si quisiera cambiarse la misma, modificar el archivo api.py en la linea 9:
```
run_with_lt(app, subdomain="tnmapi")
```
Donde se deberia el subdominio "tnmapi" por lo que quisieramos.
Con este cambio, las peticiones las realizaremos a la url:
```
https://example.loca.lt
```
Siendo "example" el subdominio que elegimos. En caso de que este en uso nos dara un subdominio aleatorio, por lo tanto, deberia cambiarse por uno que sepamos que no se utilizara.