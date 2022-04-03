import pandas as pd
import time
import json
import pandas
from bs4 import BeautifulSoup
import requests

def karsilastir ():
    try:
        dosya1 = input("dosya adı giriniz:")
        dosyaz = "zararli.txt"

        with open(dosya1, "r", encoding="utf-8") as file:
            for i in file:
                with open(dosyaz, "r", encoding="utf-8") as file:
                    for j in file:
                        if (i == j):
                            file = open("ortak.txt", "a", encoding="utf-8")
                            file.write(i)
                            file.close()
        print("Uygulanıyor...")
        time.sleep(0.01)
        print("Başarılı yeni işlem seçiniz...")

    except NameError:
        print(NameError)

def zararlicek():
    file = open("zararli.txt", "w", encoding="utf-8")  # dosya açmak

    start = time.time()  # zamanlayıcı

    for j in range(1,1068):
        url = "https://www.usom.gov.tr/zararli-baglantilar/" + str(j) + ".html"  # url aldık

        respon = requests.get(url)  # urlyi respona atadık
        htmli = respon.content  # responun tuttugu sitenin contentlerini htmli ye atadık
        soup = BeautifulSoup(htmli, "html.parser")  # düzgünleştirdik ve soupa atadık
        tdler = soup.find_all("td")  # tüm tdler tdler adlı listeye atıyor

        for i in range(1, 500, 5):  # burada linklerin liste sırası
            x = tdler[i].get_text()  # 1 6 11 16 21 diye 1+5k şeklinde
            file.write(x + "\n")  # dosya yazdırma
        print("sayfa " + str(j) + " yazdırma işlemi bitti \n")

    file.close()  # dosya kapama
    print("%s second:" % (time.time() - start))

def virustotal():
    read_file = pd.read_csv(r'ortak.txt')
    read_file.to_csv(r'data.csv', index=None)
    file_path = str(input('please Enter The File Path: '))
    domain_CSV = pandas.read_csv((file_path))
    Urls = domain_CSV['Domain'].tolist()
    API_key = '5d1f61f0e9b08fa236c7383186769afd9fa64bfc160c863b59297f4a7f92a518'
    url = 'https://www.virustotal.com/vtapi/v2/u rl/report'

    parameters = {'apikey': API_key, 'resource': Urls}
    response = requests.get(url=url, params=parameters)
    json_response = json.loads(response.text)
    for i in Urls:
        parameters = {'apikey': API_key, 'resource': i}
        response = requests.get(url=url, params=parameters)
        json_response = json.loads(response.text)

        if json_response['response_code'] <=0:
                 if json_response['positives'] <= 0:
                     with open('virustotal_temizsiteler.txt', 'a') as clean:
                         clean.write(i) and clean.write("\t NOT malicious \n")
        else:
                     with open('virustotal_zararlisiteler.txt', 'a') as malicious:
                         malicious.write(i) and malicious.write("\t Malicious") and malicious.write(
                            "\t this Domains Detectd by   " + str(json_response['positives']) + "  Solutions\n")

        print("Uygulanıyor...")
        time.sleep(0.01)
        print("Başarılı yeni işlem seçiniz...")

while True:
    secenek = int(input("secenek giriniz: karsilastir:1 zararlicek:2 vırustotal:3"))
    if secenek == 1:
        karsilastir()
    elif secenek == 2:
        zararlicek()
    elif secenek == 3:
        virustotal()
    elif secenek == 0:
        break
    else:
        print("hata seçenek girin")

