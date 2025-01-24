import os
from utils.id3_reader import get_genre_from_file
from utils.file_handler import organize_file_by_genre

def main():
    print("Bem-vindo ao 4Me.mp3 - Organizador de músicas!")

    #diretório
    music_folder = input(("Digite o caminho da pasta com suas músicas."))

    if not os.path.isdir(music_folder):
        print("Caminho inválido. Tente novamente.")
        return
    
    #organizar os arquivos por gênero
    organize_files_by_genre(music_folder)
    print("Organização concluída! Confira suas pastas.")

    if __name__ == "__main__":
        main()