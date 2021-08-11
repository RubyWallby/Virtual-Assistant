from nltk.chat.util import Chat,reflections

ciftler = [

    ["Selamun Aleyküm",["Ve Aleyküm Selam Kardeş"]],
    ["Benim adım (.*)",["Eyvallah %1"]],
    ['(merhaba|Selam|Hey|Naber)',['merhaba ben iyiyim ya sen ?','Nasıl gidiyor',
                                  'İyi değilsin sanırım']],
    ['(.*) hava (.*)',['%1 hava %2,bence keyfini çıkarmaya bak']]
]

yansimalar = {
'merhaba': 'Merhaba,nasılsın',
'Selamun Aleyküm': 'Aleyküm selam'
}
chat=Chat(ciftler,yansimalar)
chat.converse(quit='Allaha emanet')