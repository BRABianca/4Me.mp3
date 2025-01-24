import os
import shutil
from utils.id3_reader import get_genre_or_artist_from_file

def organize_files_by_genre_or_artist(folder_path):
    supported_formats = (".mp3", ".mp4", ".wav")  # Formatos suportados
    
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(supported_formats):  # Verifica os formatos suportados
                file_path = os.path.join(root, file)
                
                # Obtém o gênero ou artista do arquivo
                genre, artist = get_genre_or_artist_from_file(file_path)
                
                # Decide a pasta com base no gênero ou artista
                folder_name = genre if genre != "Desconhecido" else artist
                
                # Cria a subpasta, se não existir
                folder_path = os.path.join(folder_path, folder_name)
                os.makedirs(folder_path, exist_ok=True)
                
                # Move o arquivo para a pasta correspondente
                shutil.move(file_path, os.path.join(folder_path, file))
                print(f"Movido: {file} -> {folder_path}")
