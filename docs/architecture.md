# System architecture

## Service topology

The system follows a microservices architecture, that uses a Docker Compose file to orchestrate all services. They all work under a dedicated `imdb` network that allows communication between them and isolates them from any other interactions.

The **imdb_db** service mounts a volume named `imdb_db` for data persistence, while the **imdb_api** service mounts the Docker socket to enable the **imdb_ingestion** module invocation.

All the modules, except for `imdb_db` are built using a `Dockerfile` with arguments as specified in the `docker-compose.yml` file. The `imdb_api` module has its own `Dockerfile.api` to specify a different entrypoint to the container.

<img width="594" height="782" alt="imagen" src="https://github.com/user-attachments/assets/11f6fb82-14fe-4188-aba6-9208d3050053" />

## API service structure

`imdb_api` serves as the primary interface layer, implementing eight RESTful endpoints that provide access to IMDb data. The `/updatedata` endpoint uniquely demonstrates the system's container orchestration capability by dynamically spawning imdb_ingestion containers.

You may check the [API's definition](swagger.json) using a Swagger JSON viewer.

## Data flow architecture

The system implements a dual-layer flow pattern with staging and production schemas. With it, minimal downtime can be achieved when launching the ingestion module to update the data. Meanwhile newer data is loaded to the staging tables, the older data is still ready to be served from the production tables. Once the staging table load process finishes with success, a `staging_to_production()` migration is called.

*Note that, the ingestion ETL is a rather heavy process that could take hours depending on the system resources.*

Everything is governed by a control table named `DataControl`. It stores the `uploadDate` and the process status.

The `imdb_ingestion` module can be summoned in two different ways:
- During the CLI first time usage, it automatically checks the `DataControl` table. If the schema tables do not exist, the API creates them and automatically summons the `imdb_ingestion` module.
- If while checking the `DataControl` table it is detected that the last successful update was not done within the last 24 hours, it will prompt the user to update the data through the CLI. Furthermore, if the user tries to update the data while there is an ongoing ingestion process or the data was updated the same day, it will not be summoned.

