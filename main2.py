import requests
while True:
    kime = input("kim:")
    mesaj = input("mesaj:")
    if " " in kime or mesaj == "":
        break
    resp = requests.post('https://textbelt.com/text', {
      'phone': '{}'.format(kime),
      'message': '{}'.format(mesaj),
      'key': '3ee96a89c64821c63f7db553c1394b50d1fa0e4bUNkGM657MtBbNWCimBDhO6jrW',
    })
    print("Işlem: {} kalan hakkiniz: {}".format('Basarili'if resp.json()['success'] == 'True'
                                                else 'basarisiz!!!',resp.json()['quotaRemaining']))
    c = input("'exit()' or 'ENTER'")
    if c=="exit()":
        break
    else:
        pass