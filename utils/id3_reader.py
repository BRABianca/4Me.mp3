from mutagen.mp3 import MP3
from mutagen.mp4 import MP4
from mutagen.wave import WAVE
from mutagen.easyid3 import EasyID3

def get_genre_from_file(file_path):
    try:
        if file_path.lower().endswith(".mp3"):
            audio = MP3(file_path, ID3=EasyID3)
            genre = audio.get("genre", ["Desconhecido"])[0]
        elif file_path.lower().endswith(".mp4"):
            audio = MP4(file_path)
            genre = audio.tags.get("\xa9gen", ["Desconhecido"])[0]
        elif file_path.lower().endswith(".wav"):
            audio = WAVE(file_path)
            genre = audio.get("INAM", "Desconhecido")  # WAVE pode não ter gênero específico
        else:
            genre = "Desconhecido"
        return genre
    except Exception as e:
        print(f"Erro ao ler o arquivo {file_path}: {e}")
        return "Desconhecido"
