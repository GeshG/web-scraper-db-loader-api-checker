import sqlite3
import json
import shutil
from pathlib import Path
import os

class Loader:

    source_dir = Path('/Users/gginchev/Downloads/Desktop - 21-10-2022/downloaded_news') 
    destination_dir = Path('/Users/gginchev/Downloads/Desktop - 21-10-2022/uploaded_news')

    def __init__(self):
        self.connection = sqlite3.connect('/Users/gginchev/Desktop/news.db')

    def read_files(self, file_name):
            data = {}
            with open(file_name, 'r') as json_file:
                data = json.load(json_file)
                return(data)
    
    def dir_path(self): 
        found_files = []
        files_only = (entry for entry in self.source_dir.iterdir() if entry.is_file()) 
        for entry in files_only: 
            found_files.append(entry)
        return found_files 
    
    
    def load(self, data):
        try:
            cur = self.connection.cursor() 
            for d in data:
                placeholders = ', '.join(['?'] * len(d))  
                columns = ', '.join(d.keys()) 
                query = f"INSERT INTO news ({columns}) VALUES ({placeholders})" 
                cur.execute(query, list(d.values())) 
            self.connection.commit()
            print('Load Completed')
        except Exception:
            self.connection.rollback() 
            raise 
        finally:
            cur.close()

    def move_files(self):
        moving_files_only = (entry for entry in self.source_dir.iterdir() if entry.is_file()) 
        print(moving_files_only) 
        files_list = [] 
        try: 
            for file in moving_files_only:
                files_list.append(file) 
            print(f'File that will be moved {file.name}') 
            shutil.move(os.path.join(self.source_dir, file), self.destination_dir)
        except: 
            print('There are no files left to move') 

    def close(self):    
        self.connection.close()
        

def main():
    loader = Loader()
    show = loader.dir_path()
    for item in show:
        data = loader.read_files(item)
        loader.load(data)
    loader.close()
    loader.move_files()
main()

