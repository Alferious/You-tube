from pytube import YouTube

link = input("The video link: ")

yt = YouTube(link)

yt.streams.get_highest_resolution().download()


