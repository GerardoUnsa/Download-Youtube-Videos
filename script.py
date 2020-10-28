from pytube import YouTube

link = 'https://www.youtube.com/watch?v=oygrmJFKYZY' # Dua Lipa Song
yt = YouTube(link)
print("Title: ",yt.title) # Title video

yt.streams.filter('mp4')
yt.streams.first().download()