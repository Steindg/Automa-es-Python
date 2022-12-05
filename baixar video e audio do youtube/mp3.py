from pytube import YouTube
from moviepy.editor import * 
import os

yt=YouTube('https://www.youtube.com/watch?v=30wGWLdidDY') #pega o link
print("aguarde um pouco")
video=yt.streams.filter(res="144p").first()
download_video=video.download()#baixa o video
base, ext=os.path.splitext(download_video)
mp3=base + ".mp3"
mp4_without_frames = AudioFileClip(download_video)     
mp4_without_frames.write_audiofile(mp3) #converte pra mp3    
mp4_without_frames.close()
if os.path.exists(download_video):
    os.remove(download_video)
print('prontinho')