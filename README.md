# BLM101_25360859073_AhsenAkyol
### Öğrenci Bilgileri
- **Ad Soyad:** Ahsen Akyol
- **Öğrenci No:** 25360859073
### Proje Konusu
- Makine Dili ve Brookshear Mimarisi
### Youtube Linki
- https://youtu.be/EhnS2VlZVrc
- **Not:** Hocam hem teorik konuyu hem de kodun tüm işlevlerini eksiksiz sunabilmek adına süreyi 2 dakika aşmak durumunda kaldım,anlayışınız için teşekkür ederim.
### Proje Sunumu
Eğer sunum dosyası GitHub üzerinde görüntülenemiyorsa, lütfen aşağıdaki bağlantıya tıklayarak dosyayı bilgisayarınıza indiriniz:
📥 [Sunumu İndirmek İçin Tıklayın](Sunum.pdf?raw=true)

### Proje Açıklaması
Bu proje, Brookshear makine dilindeki 4 haneli onaltılık (hexadecimal) kodları analiz eden ve bunların işlemci seviyesinde ne anlama geldiğini açıklayan bir **Instruction Decoder** simülasyonudur.

#### 1. Kod Ne Yapıyor?:
Program, kullanıcının girdiği her bir komutu şu üç parçaya ayırarak analiz eder:
- **Op-code (İşlem Kodu):** Komutun hangi işlemi (Toplama, Yükleme, Döndürme vb.) yapacağını belirler.
- **Register (Yazmaç):** İşlemin hangi kaydedici üzerinde gerçekleşeceğini belirtir.
- **Adres:** İşlemin yapılacağı bellek adresini veya doğrudan kullanılacak değeri gösterir.

#### 2. Nasıl Çalıştırılır? (Kurulum):
- Bilgisayarınızda **Python 3.x** yüklü olmalıdır.
- Eğer Thonny kullanıyorsanız programın içindeki yerleşik Python sayesinde doğrudan çalıştırabilirsiniz.
- Diğer editörlerde (VS Code,IDLE vb.) çalıştırmak için bilgisayarda standart Python 3'ün yüklü olması gerekir.
- Kodun çalışması için dışarıdan bir kütüphane yüklenmesine gerek yoktur.
- "Run" (Çalıştır) butonuna bastığınızda program çalışacaktır.

#### 3. Çalışma Mantığının Detayı (Algoritma):
- Program bir `while True` döngüsü içinde sürekli olarak kullanıcıdan girdi bekler.
- Girilen kodun 4 haneli olup olmadığını ve geçerli HEX karakterleri içerip içermediğini kontrol eder.
- Eğer komut `C` (HALT) ile başlıyorsa, program gerçek bir işlemci durdurma komutu almış gibi kendini sonlandırır.
- Diğer tüm durumlar için (ADD, OR, JUMP, LOAD vb.) Appendix C tablosundaki kurallara göre yorumlama yapar.
  
