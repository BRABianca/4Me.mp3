import os
from utils.file_handler import organize_files_by_genre

def main():
    print("Bem-vindo ao 4Me.mp3 - Organizador de músicas!")
    
    # Solicita ao usuário o diretório com músicas
    music_folder = input("Digite o caminho da pasta com suas músicas: ")
    
    if not os.path.isdir(music_folder):
        print("Caminho inválido. Tente novamente.")
        return
    
    # Organiza os arquivos por gênero
    organize_files_by_genre(music_folder)
    print("Organização concluída! Confira suas pastas.")

if __name__ == "__main__":
    main()
