import os
import psycopg2
import json


def execute_sql(sql):
	try:
		database_name = os.environ['POSTGRES_DATABASE_NAME']
		port = int(os.environ['POSTGRES_DATABASE_PORT'])
		user = os.environ['POSTGRES_DATABASE_USER']
		password = os.environ['POSTGRES_DATABASE_PASSWORD']
		host = os.environ['POSTGRES_DATABASE_HOST']
		connection_string = f"dbname='{database_name}' port='{port}' user='{user}' password='{password}' host='{host}'"
		connection = psycopg2.connect(connection_string)
		cursor = connection.cursor()
		cursor.execute(sql)
		result_set = cursor.fetchall()
		column_names = [description.name for description in cursor.description]
		connection.commit()
		cursor.close()
		return {
			'was_exception_thrown': False,
			'exception_message': None,
			'result_set': json.dumps(result_set),
			'column_names': json.dumps(column_names)
		}
	except Exception as exception:
		return {
			'was_exception_thrown': True,
			'exception_message': str(exception)
		}
