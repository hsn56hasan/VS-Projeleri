import random
import time

class Uygulamalar():


    def __init__(self,tahta_durum = "Kapalı",tahta_ses = 0,kanal_listesi = ["HDMI"],kanal = "HDMI"):

        self.tahta_durum = tahta_durum
        self.tahta_ses = tahta_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal

    def tahta_ac(self):

        if (self.tahta_durum == "Açık"):
            print("Zaten açık")
        else:
            print("Tahta açılıyor")
            self.tahta_durum = "Açık"

    def tahta_kapat(self):

        if (self.tahta_durum == "Kapalı"):
            print("Zaten kapalı")
        else:
            print("Televizyon kapatılıyor")
            self.tahta_durum = "Kapalı"

    def ses_ayarları(self):

        while True:
            cevap = input("Sesi azalt: '<' \nSesi Artır: '>' \nÇıkış : Çıkış")

            if (cevap == "<"):
                if (self.tahta_ses != 0):

                    self.tv_ses -= 1
                    print("Ses:",self.tahta_ses)
            elif (cevap == ">"):
                if (self.tahta_ses != 30):

                    self.tahta_ses += 1

                    print("Ses:",self.tahta_ses)
            else:
                print("Ses güncellendi",self.tahta_ses)
                break
    def kanal_ekle(self,kanal_ismi):

        print("Kanal ekleniyor")
        time.sleep(1)

        self.kanal_listesi.append(kanal_ismi)

        print("kanal eklendi")
    def rastgele_kanal(self):

        rastgele = random.randint(0,len(self.kanal_listesi)-1)

        self.kanal = self.kanal_listesi[rastgele]

        print("Şu anki kanal:",self.kanal)
    def __len__(self):

        return len (self.kanal_listesi)
    
    def __str__(self):

        return "TV durumu: {}\nTV ses: {}\nKanal listesi: {}\nŞu anki kanal: {}\n".format(self.tahta_durum,self.tahta_ses,self.kanal_listesi,self.kanal)
    
uygulamalar = Uygulamalar()

print("""

Akıllı Tahta 

1.Akıllı Tahtayı Aç

2.Akıllı Tahtayı Kapat

3.Ses ayarları

4.Kanal Ekle 

5.Kanal Sayısı Öğrenme

6.Rastgele Kanala geçme

7.Akıllı Tahta Bilgileri

Çıkmak için "q"ya basınız




""")

while True:
    işlem = input("İşlemi Seçiniz:")

    if (işlem == "q"):
        print("Program sonlandırılıyor")
        break

    elif (işlem == "1"):
        uygulamalar.tahta_ac()
    elif (işlem == "2"):
        uygulamalar.tahta_kapat
    elif (işlem == "3"):
        uygulamalar.ses_ayarları
    elif (işlem == "4"):
        kanal_isimleri = input("Kanal isimleri ',' ayırarak giriniz:")

        kanal_listesi = kanal_isimleri.split(",")

        for eklenecekler in kanal_listesi:
            uygulamalar.kanal_ekle(eklenecekler)
    elif (işlem == "5"):
        print("Kanal sayısı:",len(uygulamalar))

    elif (işlem == "6"):
        uygulamalar.rastgele_kanal()
    elif (işlem == "7"):
        print(uygulamalar)

    else:
        print("Geçersiz İşlem...")

















