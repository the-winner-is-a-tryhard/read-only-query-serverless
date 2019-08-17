import os
import psycopg2


def execute_sql(sql):
	database_name = os.environ['POSTGRES_DATABASE_NAME']
	port = os.environ['POSTGRES_DATABASE_PORT']
	user = os.environ['POSTGRES_DATABASE_USER']
	password = os.environ['POSTGRES_DATABASE_PASSWORD']
	host = os.environ['POSTGRES_DATABASE_HOST']
	connection_string = "dbname='{database_name}' port='{port}' user='{username}' password='{password}' host='{endpoint}'"
	connection = psycopg2.connect(connection_string)
	cursor = connection.cursor()
	cursor.execute(sql)
	connection.commit()
	cursor.close()
