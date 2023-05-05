hosts = "C:\Windows\System32\drivers\etc\hosts"

engellenecekSiteler =["www.facebook.com","facebook.com","www.twitter.com","twitter.com"]
  
with open(hosts,'r+') as dosya:
    satır = dosya.read()
    for site in engellenecekSiteler:
        if site in satır:
            print(f"{site} zaten engellendi ...")
        else:
            dosya.write("127.0.0.1" + " " + site + "\n")
            print(f"{site} başarıyla engellendi...")
            
            
            
            