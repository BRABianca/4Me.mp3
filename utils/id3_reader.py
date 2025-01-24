from mutagen.mp3 import MP3
from mutagen.mp4 import MP4
from mutagen.wave import WAVE
from mutagen.easyid3 import EasyID3

def get_genre_or_artist_from_file(file_path):
    try:
        if file_path.lower().endswith(".mp3"):
            audio = MP3(file_path, ID3=EasyID3)
            genre = audio.get("genre", [None])[0]
            artist = audio.get("artist", ["Desconhecido"])[0]
        elif file_path.lower().endswith(".mp4"):
            audio = MP4(file_path)
            genre = audio.tags.get("\xa9gen", [None])[0]
            artist = audio.tags.get("\xa9ART", ["Desconhecido"])[0]
        elif file_path.lower().endswith(".wav"):
            audio = WAVE(file_path)
            genre = None
            artist = audio.get("IART", "Desconhecido")  # Para arquivos WAV
        else:
            return "Desconhecido", "Desconhecido"

        # Se gênero não for encontrado, retorna o artista
        return genre if genre else artist, artist
    except Exception as e:
        print(f"Erro ao ler o arquivo {file_path}: {e}")
        return "Desconhecido", "Desconhecido"
