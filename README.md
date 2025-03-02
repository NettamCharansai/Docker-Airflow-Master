# Dockerized Apache Airflow

## Overview
This repository provides a **Dockerized Apache Airflow** setup, enabling easy deployment and management of workflows. The project uses:
- **Python 3.7-slim-buster**
- **PostgreSQL** as the backend database
- **Redis** as the task queue

## Prerequisites
Ensure you have the following installed:
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Installation
Pull the latest Docker image:
```sh
docker pull puckel/docker-airflow
```

## Build from Source
To customize the image, you can build it with additional dependencies:
```sh
docker build --rm --build-arg AIRFLOW_DEPS="datadog,dask" -t my-airflow .
```

## Usage
By default, Airflow runs with **SequentialExecutor**:
```sh
docker run -d -p 8080:8080 puckel/docker-airflow webserver
```
For other executors, use Docker Compose:
```sh
docker-compose -f docker-compose-LocalExecutor.yml up -d
```

## Environment Variables
Airflow configurations can be set via environment variables:
```sh
AIRFLOW__CORE__SQL_ALCHEMY_CONN=postgresql+psycopg2://user:password@localhost:5432/airflow
```

## Scaling Workers (Celery Executor)
```sh
docker-compose -f docker-compose-CeleryExecutor.yml scale worker=5
```

## UI Access
- **Airflow Web UI**: [http://localhost:8080](http://localhost:8080/)
- **Flower Monitoring**: [http://localhost:5555](http://localhost:5555/)

## Contributing
Fork, improve, and submit a PR to help enhance the project!
