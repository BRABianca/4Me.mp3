from utils.file_handler import organize_files_by_artist_or_genre
import os

def main():
    print("Bem-vindo ao 4Me.mp3 - Organizador de músicas!")
    
    # Solicita ao usuário o diretório com músicas
    music_folder = input("Digite o caminho da pasta com suas músicas: ").strip('"')
    
    if not os.path.isdir(music_folder):
        print("Caminho inválido. Tente novamente.")
        return
    
    # Organiza os arquivos por artista ou gênero
    organize_files_by_artist_or_genre(music_folder)
    print("Organização concluída! Confira suas pastas.")

if __name__ == "__main__":
    main()
