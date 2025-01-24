import requests

def get_genre_or_artist_from_file(file_path):
    """Retorna o gênero ou artista com base nos metadados básicos do arquivo."""
    from mutagen.mp3 import MP3
    from mutagen.mp4 import MP4
    from mutagen.wave import WAVE
    from mutagen.easyid3 import EasyID3

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
            artist = audio.get("IART", "Desconhecido")  # WAVE pode não ter gênero específico
        else:
            return "Desconhecido", "Desconhecido"

        return genre if genre else "Desconhecido", artist
    except Exception as e:
        print(f"Erro ao ler os metadados do arquivo {file_path}: {e}")
        return "Desconhecido", "Desconhecido"


def identify_artist_or_genre_with_musicbrainz(artist, track):
    """Consulta a API MusicBrainz para buscar o artista e o gênero."""
    url = "https://musicbrainz.org/ws/2/recording/"
    params = {
        "query": f"artist:{artist} AND recording:{track}",
        "fmt": "json"
    }
    try:
        response = requests.get(url, params=params)
        data = response.json()

        if "recordings" in data and len(data["recordings"]) > 0:
            recording = data["recordings"][0]
            main_artist = recording.get("artist-credit", [{}])[0].get("name", "Desconhecido")
            tags = recording.get("tags", [])
            genre = tags[0]["name"] if tags else "Desconhecido"
            return main_artist, genre
        return "Desconhecido", "Desconhecido"
    except Exception as e:
        print(f"Erro ao acessar MusicBrainz para {artist} - {track}: {e}")
        return "Desconhecido", "Desconhecido"
