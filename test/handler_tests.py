import unittest
import sys
sys.path.append('../')
from lambda_function import lambda_handler


class HandlerTests(unittest.TestCase):
	def test_event(self):
		event = {
			'input': 'test'
		}
		expected_output = {
			'statusCode': 200,
			'body': '{"input": "test"}'
		}
		actual_output = lambda_handler(event, None)
		self.assertEqual(expected_output, actual_output)


if __name__ == '__main__':
	unittest.main()
