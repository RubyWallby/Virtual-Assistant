from gtts import gTTS
from playsound import playsound
import os
import sys
from random import choice


class Komut():
    def __init__(self,gelenSes):
        self.ses = gelenSes.upper()
        self.sesBloklari = self.ses.split()
        print(self.sesBloklari)
        self.komutlar = ("NABER","NASILSIN","KAPAT")

# KOMUT VE İŞLEMLERİ

    def seslendirme(self,yazi):
        tts = gTTS(text=yazi, lang='tr')
        tts.save("ses.mp3")
        playsound("ses.mp3")
        os.remove("ses.mp3")
        print(yazi)
    def kapat(self):
        self.seslendirme("Allaha emanet yiğidim")
        sys.exit()

    def sohbet(self):
        sozler = ("Hayat hain kardeşim",
              "Dert etme sıkıntı yok",
              "İyi iyi idare eder")
        secim = choice(sozler)
        self.seslendirme(secim)

# KOMUT VE İŞLEMLERİ KAPANIŞ
    def komutBul(self):
        for komut in self.komutlar:
            if komut in self.sesBloklari:
                self.komutCalistir(komut)

    def komutCalistir(self,komut):
        if komut == "NABER" or komut == "NASILSIN":
            self.sohbet()
        if komut == "KAPAT":
            self.kapat()

