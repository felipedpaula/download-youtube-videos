import os
import tkinter as tk
from pytube import YouTube

def pesquisar_video():
    url = entry_url.get()
    video = YouTube(url)

    global streams
    streams = video.streams

    options = [f"{i+1}. {stream}" for i, stream in enumerate(streams)]

    label_feedback.config(text="Escolha uma opção de stream para baixar o vídeo:")
    label_options.config(text='\n'.join(options))

def download_video():
    try:
        option = int(entry_option.get()) - 1
        video_path = os.path.join('videos', streams[option].title + '.mp4')
        streams[option].download(output_path='videos', filename=streams[option].title)
        label_feedback.config(text=f"Vídeo baixado com sucesso! O vídeo foi salvo em: {video_path}")
    except Exception as e:
        label_feedback.config(text="Ocorreu um erro ao baixar o vídeo. Verifique a URL e a opção escolhida.")
        print("Erro:", e)

def criar_interface():
    # Criar a janela principal
    root = tk.Tk()
    root.title("Baixar Vídeo do YouTube")

    # Criar um rótulo para instruir o usuário a inserir a URL
    label_url = tk.Label(root, text="Insira a URL do vídeo do YouTube:")
    label_url.pack()

    # Criar um campo de entrada para a URL
    global entry_url
    entry_url = tk.Entry(root, width=50)
    entry_url.pack()

    # Criar um botão para pesquisar o vídeo
    button_pesquisar = tk.Button(root, text="Pesquisar", command=pesquisar_video)
    button_pesquisar.pack()

    # Criar um rótulo para exibir as opções de stream
    global label_options
    label_options = tk.Label(root, text="")
    label_options.pack()

    # Criar um rótulo para instruir o usuário a escolher uma opção
    label_option = tk.Label(root, text="Digite o número da opção de stream desejada:")
    label_option.pack()

    # Criar um campo de entrada para a opção
    global entry_option
    entry_option = tk.Entry(root, width=5)
    entry_option.pack()

    # Criar um botão para iniciar o download
    button_download = tk.Button(root, text="Baixar Vídeo", command=download_video)
    button_download.pack()

    # Criar um rótulo para exibir feedback
    global label_feedback
    label_feedback = tk.Label(root, text="")
    label_feedback.pack()

    # Executar o loop principal
    root.mainloop()

def main():
    criar_interface()

if __name__ == "__main__":
    main()
