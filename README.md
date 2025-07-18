# imdb-data

## Overview

**imdb-data** is a system that provides users a way to get information from IMDb in a friendly manner. It is a containerised microservices system capable of ingesting, processing and serving the IMDb dataset information through the usage of REST APIs and a CLI application.

The system consists of three main parts:
- **imdb_db**: a PostgreSQL database that provides data persistence. PostgreSQL is an open-source DBMS popular choice for reliable data storage and scalability.
- **imdb_ingestion** (namely system_module_1): a Docker container that performs the ETL pipeline for ingesting the database with the most up-to-date IMDb data from the [IMDb](https://datasets.imdbws.com) webpage. Developed in Python.
- **imdb_client-server** (namely system_module_2):
  - **imdb_api**: HTTP interface for the system's database, implemented using Python as a FastAPI application. This service exposes a set of RESTful endpoints for querying the data and managing the ingestion processes.
  - **imdb_cli**: user-friendly command line application developed in Python using the `Typer` library for command parsing and `rich` for enhanced console output. The CLI has been developed as a REPL CLI application.

## Quickstart
To quickly set up and run this project, make sure the following are installed on your system:
1. Docker
2. Git

### Clone the repository

Clone the repository and enter the folder:
```
git clone https://github.com/amarqz/imdb-data
cd imdb-data
```

Rename the `.env.example` file to `.env`. *You may change its contents but the example file is ready-for-production.*
```
mv .env.example .env
```

### Build the docker containers

With the help of the `docker-compose.yml` file, you may build the containers by running:

```
docker compose build
```

### Start the back-end containers

```
docker compose up -d imdb_db imdb_api
```

### Run the CLI container

Once the back-end containers are up and ready, you may run the CLI container by executing the following command:

```
docker compose run --rm imdb_cli
```

The `--rm` flag will remove the container once the user exits the application, and the back-end (and ingestion if applicable) will remain running.

**Note:** during the system's first run, the CLI will detect the schema tables are not created and will trigger their creation and the ingestion process.

**Note:** the user may type `help` in the CLI to display all the available commands. For more information on the CLI usage, click [here](TBD).

## Stopping the system

To stop all the services, you may head to the `imdb_data` folder and run:

```
docker compose down
```

In case you also want to remove the database data, you may also remove the volumes with the following:

```
docker compose down -v
```