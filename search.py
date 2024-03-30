import webbrowser
import time as t
import json
import os

def pre():
    def kelime_ara_google():
        kelime = input("Aratmak istediğin kelime: ")
        url = "https://www.google.com/search?q=" + kelime
        webbrowser.open_new_tab(url)

    def kelime_ara_youtube():
        kelimey = input("Aratmak istediğin kelime: ")
        url = "https://www.youtube.com/results?search_query=" + kelimey
        webbrowser.open_new_tab(url)

    while True:
        print('''
        1 - Google araması
        2 - Youtube araması
        0 - Ana Menüye Dön
        99 - Çıkış
        ''')
        a = int(input(""))

        if a == 1:
            kelime_ara_google()
        elif a == 2:
            kelime_ara_youtube()
        elif a == 0:
            main()
        else:
            print("Uygulama kapatılıyor...")
            t.sleep(2)
            exit()

def main():
    # Kullanıcı bilgilerini JSON dosyasından al
    if not os.path.exists("users.json"):
        with open("users.json", "w") as user_file:
            json.dump({}, user_file)

    with open("users.json", "r") as user_file:
        users = json.load(user_file)

    while True:
        print('''
        _______________________________________
        |              Hoşgeldiniz              |
        |_______________________________________|
        ''')
        print("1 - Giriş yap")
        print("2 - Yeni kullanıcı kaydı oluştur")
        print("0 - Çıkış")
        choice = input("Seçiminizi yapın: ")

        if choice == "1":
            username = input("Kullanıcı adını girin: ")
            password = input("Şifreyi girin: ")
        
            if username in users:
                if users[username]["password"] == password:
                    print("Giriş başarılı!")
                    if users[username]["has_extras"]:
                        pre()
                    else:
                        print("Bu kullanıcı için gerekli ek özellik bulunamadı.")
                        while True:
                            print("Ek özellik almak için 1'e, çıkış yapmak için 0'a basınız.")
                            option = input("Seçiminizi yapın: ")
                            if option == "1":
                                webbrowser.open_new_tab("https://eascript.free.nf/")
                            elif option == "0":
                                main()  # Ana menüye geri dön
                            else:
                                print("Geçersiz seçim!")

                else:
                    print("Şifre yanlış")
            else:
                print("Kullanıcı adı bulunamadı")

        elif choice == "2":
            new_username = input("Yeni kullanıcı adı: ")
            new_password = input("Yeni şifre: ")
            extras = input("Ek özellikler var mı? (Evet için 'e', Hayır için 'h'): ")
            if extras.lower() == 'e':
                has_extras = True
            else:
                has_extras = False
                
            users[new_username] = {"password": new_password, "has_extras": has_extras}

            # JSON dosyasına kullanıcıları yeniden yazma
            with open("users.json", "w") as user_file:
                json.dump(users, user_file, indent=4)
            print("Yeni kullanıcı kaydı oluşturuldu.")

        elif choice == "0":
            print("Çıkış yapılıyor...")
            t.sleep(2)
            exit()
        else:
            print("Geçersiz seçim!")

if __name__ == '__main__':
    main()
