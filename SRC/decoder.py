
# BLM101 - Bilgisayar Mühendisliğine Giriş Projesi
# Brookshear Makine Dili Yorumlayıcısı (Instruction Decoder)
# Hazırlayan: Ahsen Akyol


def brookshear_decoder():
    print("--- Brookshear Komut Yorumlayıcı Programı ---")
    
    # input() fonksiyonu ile kullanıcıdan 4 haneli kodu alıp küçük harf girerse diye .upper metodu ile büyütüyoruz
    # her kod girildiğinde programı yeniden başlatmak zorunda kalmayalım diye döngü kullandım
    while True:
        
        komut = input("Lütfen 4 haneli HEX kodu giriniz (Örn: 14A3): ").upper()
        
        #Kullanıcı 4 haneden az veya fazla girdi mi kontrol ediyoruz
        if len(komut) != 4:
            print(f"HATA: Komut tam olarak 4 karakter olmalıdır! (Siz {len(komut)} hane girdiniz)")
            return

        # Burada da G,H gibi saçma harfler girilmesin diye kontrol yapıyoruz.Girilen karakterin hex karakteri olması lazım
        hex_karakterler = "0123456789ABCDEF"
        for karakter in komut:
            if karakter not in hex_karakterler:
               print(f"HATA: '{karakter}' geçerli bir HEX karakteri değildir!")
               return

        # Komutu bölümlere ayırıyoruz
    
        opcode = komut[0]      # Birinci hane: İşlem Kodu (Opcode)
        register = komut[1]    # İkinci hane: Yazmaç (Register)
        adres = komut[2:]      # Son iki hane: Bellek Adresi (Memory Address)

        # parçalama çıktısını ekrana yazdırıyoruz
        print(f"Opcode={opcode}, Register={register}, Adres={adres}")
        print("-" * 60)

    
        # if-elif yapısı ile her bir Opcode'un ne yapacağını belirliyoruz
        # burda her şey Appendix C tablosuna göre çalışıyor
    
        # Opcode 1 ise: LOAD from Memory (Bellekten Yazmaca Yükleme)
        if opcode == '1':
            print(f" {adres} adresindeki bellek hücresinin içeriğini, "
             f"{register} numaralı yazmaca (Register) yükle.")
    
        # Opcode 2 ise: LOAD Immediate (Doğrudan Değer Yükleme)
        elif opcode == '2':
            print(f" {adres} değerini doğrudan {register} numaralı yazmaca (Register) yükle.")
              
        # Opcode 3 ise: STORE (Yazmaçtan Belleğe Kaydetme)
        elif opcode == '3':
            print(f" {register} numaralı yazmaçtaki veriyi, "
             f"{adres} adresindeki bellek hücresine kaydet.")
              
        # Opcode 4 ise: MOVE (Yazmaçlar arası taşıma)
        elif opcode == '4':
            print(f" {adres[1]} numaralı yazmaçtaki veriyi, "
             f"{register} numaralı yazmaca kopyala.")
              
        # Opcode 5 ise: ADD (İki yazmacı "ikinin tümleyeni" yöntemiyle toplama)
        elif opcode == '5':
            print(f" {adres[0]} ve {adres[1]} numaralı yazmaçları 'ikinin tümleyeni' yöntemine göre topla, "
             f"sonucu {register} numaralı yazmaca yaz.")
        
        # Opcode 6 ise: ADD (İki yazmacı "kayan noktalı" yöntemine göre toplama)    
        elif opcode == '6': 
           print(f" {adres[0]} ve {adres[1]} numaralı yazmaçları 'Kayan Noktalı' yöntemine göre topla, sonucu {register} numaralı yazmaca yaz.")
    
        # Opcode 7 ise: iki yazmaca mantıksal "OR" işlemi uygulama
        elif opcode == '7': 
            print(f" {adres[0]} ve {adres[1]} numaralı yazmaçlara mantıksal OR (VEYA) işlemi uygula, sonucu {register} numaralı yazmaca yaz.")
        
        # Opcode 8 ise: iki yazmaca mantıksal "AND" işlemi uygulama
        elif opcode == '8': 
            print(f" {adres[0]} ve {adres[1]} numaralı yazmaçlara mantıksal AND (VE) işlemi uygula, sonucu {register} numaralı yazmaca yaz.")
        
        # Opcode 9 ise: iki yazmaca mantıksal "XOR" işlemi uygulama
        elif opcode == '9': 
            print(f" {adres[0]} ve {adres[1]} numaralı yazmaçlara mantıksal XOR işlemi uygula, sonucu {register} numaralı yazmaca yaz.")
        
        # Opcode A (10) ise: yazmaçtaki bitleri sağa doğru döndürme
        elif opcode == 'A': 
            print(f" {register} numaralı yazmaçtaki bitleri sağa doğru {adres[1]} defa dairesel döndürür.")
              
        # Opcode B ise: JUMP (Koşullu Atlama)
        elif opcode == 'B':
            print(f" Eğer {register} numaralı yazmaç 0 numaralı yazmaç ile aynıysa, "
              f"programın akışını {adres} adresine atlat.")
              
        # Opcode C ise: HALT (Programı durdurma)
        # en başta döngü oluşturmuştum burda kullanıcı "C" girdiğinde döngüden çıkmış olacak, program sonlanacak
        elif opcode == 'C':
            print(" Programın çalışmasını tamamen sonlandır (HALT).")
            break
        
        # Eğer tabloda olmayan bir kod girilmişse kullanıcıyı uyarıyoruz
        else:
            print(f"UYARI: {opcode} numaralı işlem kodu için bir açıklama tanımlanmadı.")

# burada da programı başlatmak için fonksiyonu çağırıyoruz
brookshear_decoder()