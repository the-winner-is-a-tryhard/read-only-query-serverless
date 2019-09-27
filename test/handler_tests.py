import unittest
import sys
sys.path.append('../')
from lambda_function import lambda_handler


class HandlerTests(unittest.TestCase):
	def test_event(self):
		serialized_expected_sql_response = '{"was_exception_thrown": true, "exception_message": "table \\"LEAGUE\\" does not exist\\n"}'
		event = {
			'body': 'drop table twiath."LEAGUE";'
		}
		expected_output = {
			'isBase64Encoded': False,
			'headers': {
				'Content-Type': 'application/json',
				'Access-Control-Allow-Origin': '*'
			},
			'statusCode': 200,
			'body': serialized_expected_sql_response,
		}
		actual_output = lambda_handler(event, None)
		self.assertEqual(expected_output, actual_output)


if __name__ == '__main__':
	unittest.main()
