import requests

from bs4 import BeautifulSoup

file= open("zararli.txt","w",encoding="utf-8") # dosya açmak

 




for j in range(1,1055):
    url="https://www.usom.gov.tr/zararli-baglantilar/"+str(j)+".html"# url aldık

    respon=requests.get(url)# urlyi respona atadık
    htmli=respon.content# responun tuttugu sitenin contentlerini htmli ye atadık
    soup=BeautifulSoup(htmli,"html.parser")# düzgünleştirdik ve soupa atadık
    tdler=soup.find_all("td")# tüm tdler tdler adlı listeye atııyor

    
    for i in range(1,500,5):# burda linklerin liste sırarı
        x=tdler[i].get_text()# 1 6 11 16 21 diye 1+5k şeklinde
        file.write(x+"\n")# dosya yazdırma
    print("sayfa "+str(j)+" yazdırma işlemi bitti \n")
    




file.close()#dosya kapama

   
   

