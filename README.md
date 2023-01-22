# NaNLab

## Ejecución
El projecto está armado para ser ejecutado con Docker, tanto para probarlo como para continuar su desarollo (el Dockerfile.dev que adjunto no está pensado para producción).
Por otro lado utilizo un esquema modular en el projecto Django propiamente dicho, con requerimientos en cascada según dónde se vaya a utilizar (producción, testing o desarrollo local).

Se requiere tener instalado Docker y make, detallo los pasos a continuación:

`make docker-build-dev`: Crea la imagen de Docker con Python, las dependencias del proyecto y lo monta. Esto permite editar el projecto sin tener que rehacer la imagen.

`make docker-shell`: Instancia un contenedor y nos sitúa en el raíz del repo.

`make docker-start`: Ejecuta las migraciones de Django y luego runserver, dejando la API online.

`make docker-pytest`: Ejecuta los tests.

## SetUp de Trello
Para utilizar el webservice hay que obtener la APIKey y el Token de trello y guardarlos en `nanlab/settings/.env`. (Utilizar la plantilla [env.example](nanlab/settings/env.example)

Por último hay que crear un board llamado "NaNLab", una list llamada "To Do" y las labels "Bug", "Research", "Maintenance" y "Test".

## Uso de la API
El endpoint es `/api/v1/trello_cards`, allí se debe postear para crear las cards deseadas.
Se puede consultar el archivo [test_endpoints.py](tests/api_v1/test_endpoints.py) para ejemplos ;)
