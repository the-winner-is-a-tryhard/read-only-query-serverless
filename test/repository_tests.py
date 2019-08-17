import unittest
import sys
sys.path.append('../repository')
from repository.postgres_repository import execute_sql


class RepositoryTests(unittest.TestCase):
	def test_execute_sql(self):
		raised = False
		try:
			sql = 'select * from public.player'
			execute_sql(sql)
		except:
			raised = True
		self.assertEqual(raised, False)


if __name__ == '__main__':
	unittest.main()