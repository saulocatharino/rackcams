import requests, re, time


lista = []
cidades = []
arq = open("cameras.txt","w")
arq.write("cidade,url\n")
arq.close()
try:

    while True:

        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}       
            for page in range (0,100):

                url = ("https://www.insecam.org/en/bycountry/BR/?page="+str(page))

                res = requests.get(url, headers=headers)

                local = res.text.split("title=")[-3].split(">")[0].split(",")[1].replace('"',"")[1:]
                if local not in cidades:
                    cidades.append(local)
                print(cidades)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+\S+', res.text)

                for ID,_ in enumerate(findip):
                    url = findip[ID].replace('"',"")
                    if url not in lista:
                        print("#### Total de câmeras: " , len(lista))
                        lista.append(url)
                        arq = open("cameras.txt","a")
                        arq.write("{},{}\n".format(local,url.replace('"',"")))
                        arq.close()
                        print (url)

        except:
            time.sleep(1)


except KeyboardInterrupt:
    print("")


                

