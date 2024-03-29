import unittest
import sys
sys.path.append('../')
sys.path.append('../repository')
from repository.postgres_repository import execute_sql


class RepositoryTests(unittest.TestCase):
	def test_execute_valid_input_sql_select(self):
		sql = 'select * from public.player where first_name = \'Lamar\';'
		output = execute_sql(sql)
		self.assertEqual(output.get('was_exception_thrown'), False)
		self.assertIsNone(output.get('exception_message'))
		self.assertIsNotNone(output.get('column_names'))

	def test_execute_invalid_input_sql_insert(self):
		sql = 'insert into twiath."LEAGUE" values (2, \'Test\');'
		output = execute_sql(sql)
		self.assertEqual(output.get('was_exception_thrown'), True)
		self.assertIsNotNone(output.get('exception_message'))

	def test_execute_invalid_input_sql_drop(self):
		sql = 'drop table twiath."LEAGUE";'
		output = execute_sql(sql)
		self.assertEqual(output.get('was_exception_thrown'), True)
		self.assertIsNotNone(output.get('exception_message'))


if __name__ == '__main__':
	unittest.main()