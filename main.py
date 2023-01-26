from pytube import YouTube

url = "https://www.youtube.com/watch?v=iYP9L_77WGM"
yt = YouTube(url)
audio = yt.streams.filter(only_audio=True).first()

path = "C:\\Videos" # Especifica la ruta de descarga
audio.download(output_path=path)
