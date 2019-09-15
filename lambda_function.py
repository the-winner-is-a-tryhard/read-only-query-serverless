import json

from repository.postgres_repository import execute_sql


def lambda_handler(event, context):
	sql = event['sql']
	output = execute_sql(sql)
	print(output)
	return {
		'statusCode': 200,
		'body': json.dumps(output)
	}