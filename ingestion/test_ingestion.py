import unittest
from DataLoader import DataLoader
from FileManager import FileManager
from config import path_base, files
import os

class TestIngestion(unittest.TestCase):
    def test_dataloader_init(self):
        loader = DataLoader()
        self.assertIsNotNone(loader)

    def test_filemanager_init(self):
        manager = FileManager(path_base=path_base, files=files)
        self.assertIsNotNone(manager)

    def test_dataloader_update_data_control(self):
        loader = DataLoader()
        loader.update_data_control('ON')
        loader.update_data_control('KO')

    def test_filemanager_fetch_invalid(self):
        manager = FileManager(path_base='http://invalid-url/', files=['nonexistent.tsv'])
        result = manager.fetch()
        self.assertFalse(result)

    def test_filemanager_unpackage_invalid(self):
        manager = FileManager(path_base=path_base, files=files)
        result = manager.unpackage('downloads/nonexistent.tsv')
        self.assertFalse(result)

    def test_filemanager_remove_invalid(self):
        manager = FileManager(path_base=path_base, files=files)
        result = manager.remove('downloads/nonexistent.tsv')
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main() 