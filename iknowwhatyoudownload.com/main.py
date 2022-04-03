import requests 
from bs4 import BeautifulSoup 
dosya1=input("dosya adı giriniz:")
file = open("torrent.txt", "w", encoding="utf-8")
file.close()
with open(dosya1, "r") as file:
    for ipaddress in file:
        file = open("torrent.txt", "a", encoding="utf-8")
        file.write("\ngirilen ip adres\n:"+ipaddress)
        headers_param = { 
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 OPR/78.0.4093.153"}
        iknow = requests.get("https://iknowwhatyoudownload.com/en/peer/?ip=" + ipaddress, headers=headers_param)
        content = iknow.content 
        soup = BeautifulSoup(content, "html.parser")
        table = soup.find_all("href", {"class": "danger"})
        link = soup.find_all("div", {"class": "torrent_files"})
        boyut=soup.find_all("td",{"class": "size-column"})
        tarih=soup.find_all("td",{"class": "date-column"})
        for data in link:
            data = data.text
            file.write("\ngirilen zararlı siteler"+data)
        for size in boyut:
            size=size.text
            file.write("dosyanın boyutu"+size)
        for tarihler in tarih:
            tarihler=tarihler.text
            file.write("\n"+tarihler)
        file.write("\n\n----------------")