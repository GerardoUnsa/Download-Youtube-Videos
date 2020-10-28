from pytube import YouTube

link = 'https://www.youtube.com/watch?v=oygrmJFKYZY' # Dua Lipa Song
yt = YouTube(link)
print("Title: ",yt.title) # Title video
print("Descripcion: ",yt.description) # Title description
print("Duracion: ",yt.length) # Title description

yt.streams.filter('mp4')
yt.streams.first().download()