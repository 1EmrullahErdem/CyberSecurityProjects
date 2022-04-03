

dosya1=input("deneme.txt")

dosyaz="zararli.txt"



with open(dosya1,"r") as file:
    for i in file:
        with open(dosyaz,"r") as file:
            for j in file:
                if(i==j):
                    file= open("ortak.txt","a",encoding="utf-8")
                    file.write(i)
                    file.close()
                    
            
            
    
        