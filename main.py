from pytube import YouTube

url = input('Enter video url: ')

video = YouTube(url)

#for youtube title
print(video.title)

#for video download
video.streams.filer(resolution='720p').first().download()