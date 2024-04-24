import os
from pytube import YouTube

def download_video():
    # Solicitar que o usuário insira a URL do vídeo
    url = input("Insira a URL do vídeo do YouTube: ")

    # Criar uma instância da classe YouTube com a URL do vídeo
    video = YouTube(url)

    # Criar a pasta 'videos' se ainda não existir
    if not os.path.exists('videos'):
        os.makedirs('videos')

    # Obter todas as streams disponíveis para download
    streams = video.streams

    # Listar todas as opções disponíveis de stream para o usuário escolher
    print("Escolha uma opção de stream para baixar o vídeo:")
    for i, stream in enumerate(streams):
        print(f"{i+1}. {stream}")

    # Solicitar ao usuário que insira o número correspondente à opção desejada
    opcao = int(input("Digite o número da opção desejada: "))

    # Baixar o vídeo na opção escolhida
    video_path = os.path.join('videos', video.title + '.mp4')
    streams[opcao - 1].download(output_path='videos', filename=video.title)
    print(f"Vídeo baixado com sucesso! O vídeo foi salvo em: {video_path}")

def main():
    download_video()

if __name__ == "__main__":
    main()
