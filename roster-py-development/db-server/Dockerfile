FROM postgres:latest 

# TODO: initialize the database server with authorization credentials from a .env file
ENV POSTGRES_PASSWORD=postgres
ENV POSTGRES_USER=postgres

# Initializes our database with preset commands from initdb.sql
COPY initdb.sql /docker-entrypoint-initdb.d/