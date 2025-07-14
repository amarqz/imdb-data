import gzip
import os
import shutil
from urllib.request import urlretrieve
from pydantic import BaseModel, conlist

class FileManager(BaseModel):
    path_base: str
    files: conlist(str)

    def fetch(self) -> bool:
        if not os.path.exists('downloads/'):
            os.mkdir('downloads/')
        try:
            for file in self.files:
                print(f'Downloading file: {file}.gz')
                urlretrieve(self.path_base + file + '.gz', 'downloads/' + file + '.gz')
                self.unpackage('downloads/' + file)
        except Exception as e:
            print(e)
            return False
        return True

    def unpackage(self, file_path: str) -> bool:
        try:
            print(f'Decompressing file: {file_path}.gz')
            with gzip.open(file_path + '.gz', 'rb') as f_in:
                with open(file_path, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
            self.remove(file_path + '.gz')
        except Exception as e:
            print(e)
            return False
        return True

    def remove(self, path: str) -> bool:
        try:
            if os.path.isdir(path):
                shutil.rmtree(path, ignore_errors=True)
            if os.path.exists(path):
                os.remove(path)
                return True
        except Exception as e:
            print(e)
        return False