import pytube
url = input("Enter Video Url: ")
path = " "
pytube.YouTube(url).streams.get_audio_only().download(path)