# App para agendar citas

Este proyecto contiene una configuración con Docker Compose para levantar un entorno de base de datos con MariaDB y una interfaz web de gestión mediante phpMyAdmin.

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

## Acceder a phpMyAdmin

Una vez corriendo, se puede acceder desde el navegador usando:

```txt
http://localhost:8080
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
