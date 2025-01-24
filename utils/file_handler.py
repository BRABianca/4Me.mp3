import os
import shutil
from utils.id3_reader import get_genre_or_artist_from_file, identify_artist_or_genre_with_musicbrainz

def organize_files_by_artist_or_genre(folder_path):
    """Organiza arquivos por artista principal ou gênero, com fallback para 'Desconhecido'."""
    supported_formats = (".mp3", ".mp4", ".wav")  # Formatos suportados
    
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(supported_formats):
                file_path = os.path.join(root, file)
                
                # Obtém metadados básicos
                genre, artist = get_genre_or_artist_from_file(file_path)
                
                # Consulta MusicBrainz se necessário
                if artist == "Desconhecido" or genre == "Desconhecido":
                    artist, genre = identify_artist_or_genre_with_musicbrainz(artist, os.path.splitext(file)[0])
                
                # Usa o artista como prioridade
                folder_name = artist if artist != "Desconhecido" else "Desconhecido"
                
                # Cria a pasta de destino
                folder_name_path = os.path.join(folder_path, folder_name)
                os.makedirs(folder_name_path, exist_ok=True)
                
                # Move o arquivo
                shutil.move(file_path, os.path.join(folder_name_path, file))
                print(f"Movido: {file} -> {folder_name_path}")
