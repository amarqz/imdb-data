from DataLoader import DataLoader
from FileManager import FileManager
from config import path_base, files

if __name__ == '__main__':
    file_manager = FileManager(
        path_base=path_base,
        files=files
    )
    data_loader = DataLoader()
    data_loader.update_data_control('ON')
    
    file_manager.fetch()

    end_status = 'OK'
    for file in files:
        if not data_loader.load('downloads/' + file):
            end_status = 'KO'
            break
        file_manager.remove('downloads/' + file)
    if end_status == 'OK':
        data_loader.staging_to_production()
    data_loader.update_data_control(end_status)
