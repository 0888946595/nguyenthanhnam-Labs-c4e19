from youtube_dl import YoutubeDL
# 1: Download a Video
dl = YoutubeDL()
dl.download(["https://www.youtube.com/watch?v=fxeSvAsqzlo"])


# 2: Download a Audio
option = {
    'format': 'bestaudio/audio'

}

dl = YoutubeDL(option)
dl.download(["https://www.youtube.com/watch?v=NCr3gMoeiiE"])

# 3 Search and download a video

option = {
    'default_search': 'ytsearch',
    'max download': 1
}

dl = YoutubeDL(option)
dl.download (['sai nguoi sai thoi diem'])

# 4: Search and download a Audio

option = {
    'default_search': 'ytsearch',
    'max download': 1,
    'format': 'bestaudio/audio'
}

dl = YoutubeDL(option)
dl.download (['Bùa yêu'])