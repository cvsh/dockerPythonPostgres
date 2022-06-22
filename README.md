
# dockerPythonPostgres

/// Script gets data from google spreadsheets and writes it to PostgresSQL ///

# Command to start
* docker-compose up --build

# Enter database container to check if data ammended in spreadsheet becomes ammended in database as well
* docker exec -it <container_id with database> /bin/bash 
* psql -U postgres 
* \c googledata
* SELECT * FROM orders;
