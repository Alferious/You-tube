from pytube import YouTube

def download_video(url, resolution='720p'):
    yt = YouTube(url)
    stream = yt.streams.filter(res=resolution, progressive=True).first()
    stream.download()
    print(f'Downloaded: {yt.title}')


link = input('Enter link: ')
download_video(link)