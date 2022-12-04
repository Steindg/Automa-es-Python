import pandas as pd
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


#obs se der erro continuo tente aumentar os tempos dos sleep
csv=pd.read_csv(r'lista de emails.csv')
df=pd.DataFrame(csv)
options=webdriver.ChromeOptions()
nami=uc.Chrome(options=options)

email=" digite seu email"
senha="sua senha"
assunto="não faço ideia"
mensagem="""
        Eu estou cansado de não fazer nada, 
        mas eu sou muito preguiçoso pra fazer alguma coisa.
        """
def entrar_email(email,senha):
    nami.get('https://accounts.google.com/v3/signin/identifier?dsh=S889727721%3A1669300418002496&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=ARgdvAshwnNirYWiZCahc3SjlGmZZhMmvsWsqTlyRjMvXh93rCwsF5aV2B2pG5cUun0t83tz6D_l')
    sleep(3)
    nami.find_element(By.CSS_SELECTOR,'[type="email"]').send_keys(email)
    sleep(0.5)
    nami.find_element(By.CSS_SELECTOR,'.VfPpkd-dgl2Hf-ppHlrf-sM5MNb button[class="VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b"]').click()
    sleep(2)
    nami.find_element(By.CSS_SELECTOR,'[type="password"]').send_keys(senha)
    sleep(0.5)
    nami.find_element(By.CSS_SELECTOR,'.VfPpkd-dgl2Hf-ppHlrf-sM5MNb button[class="VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b"]').click()
    sleep(3)
def enviar_mensagem(Assunto,Mensagem):
    emails=df['Emails'].tolist()
    for i in range(len(df)):
        nami.find_element(By.CSS_SELECTOR,'.z0').click()
        sleep(3)
        nami.find_element(By.CSS_SELECTOR,'.aH9 input[class="agP aFw"]').send_keys(f'{emails[i]} ')
        sleep(0.5)
        nami.find_element(By.CSS_SELECTOR,'[name="subjectbox"]').send_keys(Assunto)
        sleep(0.5)
        nami.find_element(By.CSS_SELECTOR,'[class="Am Al editable LW-avf tS-tW"]').send_keys(Mensagem)
        sleep(0.5)
        nami.find_element(By.CSS_SELECTOR,'[class="T-I J-J5-Ji aoO v7 T-I-atl L3"]').click()
        sleep(3)

try:
    entrar_email(email,senha)
except:
    entrar_email(email,senha)    
    
enviar_mensagem(assunto,mensagem)
