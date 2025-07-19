import unittest
from typer.testing import CliRunner
from application import app

class TestCLI(unittest.TestCase):
    def setUp(self):
        self.runner = CliRunner()

    def test_help(self):
        result = self.runner.invoke(app, ['help'])
        self.assertEqual(result.exit_code, 0)

    def test_check(self):
        result = self.runner.invoke(app, ['check'])
        self.assertEqual(result.exit_code, 0)

    def test_person_missing_args(self):
        result = self.runner.invoke(app, ['person'])
        self.assertNotEqual(result.exit_code, 0)

    def test_person_dummy(self):
        result = self.runner.invoke(app, ['person', 'actor', 'Nonexistent'])
        self.assertEqual(result.exit_code, 0)

    def test_title_missing_args(self):
        result = self.runner.invoke(app, ['title'])
        self.assertNotEqual(result.exit_code, 0)

    def test_title_dummy(self):
        result = self.runner.invoke(app, ['title', 'movie', 'Nonexistent'])
        self.assertEqual(result.exit_code, 0)

if __name__ == '__main__':
    unittest.main() 