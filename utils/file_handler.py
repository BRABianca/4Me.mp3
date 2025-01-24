import os
import shutil
from utils.id3_reader import get_genre_from_file

def organize_files_by_genre(folder_path):
    supported_formats = (".mp3", ".mp4", ".wav")  # Formatos suportados
    
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(supported_formats):  # Verifica os formatos suportados
                file_path = os.path.join(root, file)
                
                # Obtém o gênero do arquivo
                genre = get_genre_from_file(file_path)
                
                # Cria a subpasta do gênero, se não existir
                genre_folder = os.path.join(folder_path, genre)
                os.makedirs(genre_folder, exist_ok=True)
                
                # Move o arquivo para a pasta do gênero
                shutil.move(file_path, os.path.join(genre_folder, file))
                print(f"Movido: {file} -> {genre_folder}")
