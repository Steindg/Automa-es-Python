from selenium import webdriver
from selenium.webdriver.common.by import By
from pytube import YouTube
from moviepy.editor import * 
from time import sleep
import os

#obs se der erro continuo tente aumentar os tempos dos sleep

options=webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-logging'])
nami=webdriver.Chrome(options=options)
nami.get('https://web.whatsapp.com')
sleep(10)

def botlink():  #envia o LINK de um video dgbot/nome do video
    for i in nami.find_elements(By.CSS_SELECTOR,'span [dir="ltr"]'):  #veja as mensagens recentes do zap
        try:
            if i.text.split("/")[0] == 'dgbot': #se dgbot foi chamado
                i.click()    
                video=i.text.split("/")[1:][0].replace(' ','+') #pega o nome do video
                url=(f"https://www.youtube.com/results?search_query={video}") #adiciona o nome ao link de busca
                nami.execute_script("window.open('');") 
                nami.switch_to.window(nami.window_handles[1]) #abre uma nova aba
                nami.get(url)  #vai pro link de busca
                links=[]
                sleep(0.2)
                for i in nami.find_elements(By.CSS_SELECTOR,'#video-title'): #pega todos os links de video 
                    if i.get_attribute("href")==None:
                        continue
                    links.append(i.get_attribute("href"))
                nami.close()  #fecha a aba do youtube
                nami.switch_to.window(nami.window_handles[0]) 
                sleep(0.5)
                nami.find_element(By.CSS_SELECTOR,'span [class="selectable-text copyable-text"]').send_keys(links[0]) #cola o link do video 
                sleep(0.5)
                nami.find_element(By.CSS_SELECTOR,'span [data-icon="send"]').click()  #envia a mensagem  
                links.clear()
                del i
        except:
            if nami.window_handles==nami.window_handles[1]:#Se a aba do youtube tiver aberta
                nami.close() #feche
                nami.switch_to.window(nami.window_handles[0]) #volte pro zap 
            break

def botmp3():   #envia o AUDIO de um video dgbotmp3/nome do video
    for i in nami.find_elements(By.CSS_SELECTOR,'span [dir="ltr"]'):
        try:       
            if i.text.split("/")[0] == 'dgbotmp3':
                i.click()    
                video=i.text.split("/")[1:][0].replace(' ','+')
                url=(f"https://www.youtube.com/results?search_query={video}")
                nami.execute_script("window.open('');") 
                nami.switch_to.window(nami.window_handles[1]) 
                nami.get(url)                
                links=[]
                sleep(0.2)
                for i in nami.find_elements(By.CSS_SELECTOR,'#video-title'):
                    if i.get_attribute("href")==None:
                        continue
                    links.append(i.get_attribute("href"))
                nami.close() 
                nami.switch_to.window(nami.window_handles[0])
                sleep(0.5)             
                yt=YouTube(links[0]) #pega o link
                video=yt.streams.filter(only_audio=True).first()
                download_video=video.download()#baixa o video
                base, ext=os.path.splitext(download_video)
                mp3=base + ".mp3"
                mp4_without_frames = AudioFileClip(download_video)     
                mp4_without_frames.write_audiofile(mp3) #converte pra mp3    
                mp4_without_frames.close()
                print("cabou")
                sleep(0.5)
                nami.find_element(By.CSS_SELECTOR,"span[data-icon='clip']").click()
                nami.find_element(By.CSS_SELECTOR,"input[type='file']").send_keys(mp3) #envia o video
                sleep(5)
                nami.find_element(By.CSS_SELECTOR,"span[data-icon='send']").click()    
                links.clear()
                del i
                sleep(3)
                if os.path.exists(mp3): # exclui o video e o audio do pc
                    os.remove(mp3)
                    os.remove(download_video)

        except:
            if nami.window_handles==nami.window_handles[1]:
                    nami.close()
                    nami.switch_to.window(nami.window_handles[0]) 
            break
while True: #faz o codigo ficar sempre aberto
    try:
        sleep(0.5)
        botlink()
        botmp3()
    except:
        continue
