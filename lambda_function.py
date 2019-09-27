import json

from repository.postgres_repository import execute_sql


def lambda_handler(event, context):
	sql = event['body']
	output = execute_sql(sql)
	return {
		'isBase64Encoded': False,
		'headers': {
			'Content-Type': 'application/json',
			'Access-Control-Allow-Origin': '*'
		},
		'statusCode': 200,
		'body': json.dumps(output)
	}
