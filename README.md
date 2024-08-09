# ToDo-List Challenge

- El Challenge consiste en crear una aplicación web sencilla que permita a los usuarios crear y mantener una lista de tareas.

## Objetivos:

El usuario de la aplicación tiene que ser capaz de:

- Autenticarse
- Crear una tarea
- Eliminar una tarea
- Marcar tareas como completadas
- Poder ver una lista de todas las tareas existentes
- Filtrar/buscar tareas por fecha de creación y/o por el contenido de la misma

## Ejecutar el proyecto
- Tener docker y docker-compose instalados
- Ubicarse en la raiz del proyecto
- Ejecutar:

```
docker-compose build
```

- Luego:
```
docker-compose up
```
- El proyecto deberia ejecutarse y en la terminal saldria que
se esta listo para acceder a los endpoints del proyecto

### Para endpoints disponibles
```
localhost:8002/swagger/
```

### Para ejecutar tests
```
docker-compose run --rm django pytest .
```


### Para ver las urls con su notacion para los pytest
```
docker-compose run --rm django python manage.py show_urls
```
