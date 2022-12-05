from pytube import YouTube
from moviepy.editor import *


yt=YouTube('https://www.youtube.com/watch?v=30wGWLdidDY') #pega o link
print("aguarde um pouco")
video=yt.streams.filter(res="720p").first()
video.download()#baixa o video
print('prontinho')