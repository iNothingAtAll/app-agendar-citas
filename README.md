# App para agendar citas

Este es un proyecto para una clase de aplicaciones web en dones se espera conectar dos bases de datos mediante apis, implementación de jwt y el uso de algún framework para desarrollo front-end

---

## Requisitos

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

---

## Cómo levantar los servicios

Ejecutar en una terminal dentro del proyecto:

```bash
docker-compose up --build
```

## Cómo detener y limpiar todo

Para detener los servicios y eliminar los contenedores:

```bash
docker-compose down 
```

Si también deseas eliminar **los volúmenes y todos los datos**:

```bash
docker-compose down -v
```
