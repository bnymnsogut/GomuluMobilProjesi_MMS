# Raspberry Pi ile Kapı Güvenlik Sistemi </br>(SIM800L modülü ile MMS, EMAIL yoluyla resim gönderme)
<img align="right" src="https://github.com/bnymnsogut/GomuluMobilProjesi_MMS/blob/master/Resimler/genel-bakis.jpg">
ARM mimarisine sahip bir mikrodenetleyici olan Raspberry Pi kartı ile HC-SR04 Ultrasonik Mesafe Sensörü kullanılarak kapının açılıp açılmadığı kontrol edilip, kapı izinsiz açıldığında kameradan fotoğraf çekilip anlık olarak kullanıcıya e-posta ayrıca SiM800L Modülü kullanılarak sms ve mms gönderilecektir.

Projenin adım adım yapılışını [Youtube Video Link](https://youtu.be/WtqSSz-gh94) 'inde, 
sadece uygulama videosunu [Uygulama Video Link](https://drive.google.com/file/d/1Wm_SVOjfLgWVH2La9AvjPL-C57stzxIH/view) 'inde bulabilirsiniz.
Projenin sunum videosu 	[ZOOM Video Link](https://drive.google.com/file/d/18m6E6M5MvYTtqVnQzP9NNjvRkygyTHRK/view) 'inde yer alan videodan izleyebilirsiniz.



## Proje Gereksinimleri
  ### Donanım
     1-Raspberry Pi 2
     2-HC-SR04 Ultrasonik Mesafe Sensörü 
     3-SiM800L GSM GPRS Modülü
     4-Micro SD Kart 16 GB
     5-HP Pro Webcam (AU165AA)
     6-Adaptör 5V-3A  USB-C
     7-Bağlantı için gerekli kablolar
  ### İşletim Sistemi
     Raspbian İşletim Sistemi
## İşletim Sisteminin Kurulumu
SD Card Formatter programı ile SD Kart formatlanabilir. Daha sonra "Win32 Disk Imager" programı ile SD Kart'a önceden indirilen Rasbian işletim sistemi yüklenebilir. Ayrıca proje anlatım videosunun ilk dakikasında işletim sisteminin kurulumunu bulabilirsiniz.</br> [Proje Youtube Video Linki](https://youtu.be/WtqSSz-gh94)</br>
[Rasbian işletim sistemi indirme linki](https://www.raspberrypi.org/downloads/raspbian/) </br>
[SD Card Formatter programı indirme linki](https://www.sdcard.org/downloads/formatter/) </br>
[Win32 Disk Imager programı indirme linki](https://sourceforge.net/projects/win32diskimager/) </br>
##  HC-SR04 Ultrasonik Mesafe Sensörü  
İnsan kulağı doğadaki 20 Hz ile 20 kHz arasındaki sesleri algılayabilir. Ultrasonik ses dalgaları ise insan kulağının duyamayacağı 20 kHz – 500 kHz frekans aralığına sahiptir. Ultrasonik ses dalgalarını kullanan sensörler ile nesnelerle herhangi bir temas halinde olmadan mesafe ölçümleri yapılabilmektedir. Ultrasonik sensörlerin yaydıkları ses dalgaları cisimlere çarpıp geri gelir. Geri dönüş süreleri ve yayılan sesin hızı bilindiğine göre cisimle sensör arasındaki mesafe kolayca bulunabilir. Önerilen sistemde kontrol noktalarına konulan bu sensörlerin görevi, referans aldıkları yerle kendi arasında bir cisim geçtiğinde mikrodenetleyiciye haber vererek kamerayı aktif etmesidir.

Sensör Pinleri : </br>
    VCC = 5 Volt beslemeye pini => Raspberry Pi 5 Volt Çıkış pinine bağlanacak </br>
    GND = Toprak bağlantı pini => Raspberry Pi ground pinine bağlanacak </br>
    TRIG= Darbe üreten pin => Raspberry Pi GPIO 23 pinine bağlanacak </br>
    ECHO= Ses dalgasının geliş süresini hesaplamamızı sağlayan pin => Raspberry Pi GPIO 24 pinine bağlanacak </br>
<p align="center">
  <img src="https://github.com/bnymnsogut/GomuluMobilProjesi_MMS/blob/master/Resimler/hc-sr04.jpg">
</p>

##  Sim800L GSM/GPRS Modülü
Arama yapma ve arama cevaplama (Kulaklık ya da harici hoparlör ve mikrofon ile), SMS mesajları gönderme ve SMS alma, MMS mesajları gönderme ve MMS alma, GPRS gönderme ve alma (TCP/IP, HTTP, vb.), Bluetooth iletişimi, FM radyo yayınları tarama ve alma gibi özellikleri olan bir modül kullanılmıştır.</br>
    Sensör Pinleri : </br>
    VCC = 3.4V-4.2V harici bir güç kaynağı veya batarya kullanmanız gereklidir. </br>
    GND = Toprak bağlantı pini => Harici kullanılan güç kaynağına takılır ayrıca Raspberry Pi ground pini ile kısa devre yapılması gerekmektedir. Aynı gng hattına sahip olmaları lazım </br>
    RxD = UART portumuzun mesaj alan (receive) pinidir. Raspberry Pi GPIO 14 pinine bağlanacaktır </br>
    TxD = UART portumuzun mesaj gönderen (transmit) pinidir. Raspberry Pi GPIO 15 pinine bağlanacaktır </br>
    **Not: Komut dosyasındaki GPIO numaralandırılması BCM numaralandırmaya göre ayarlanmıştır.**</br>

<p align="center">
  <img src="https://github.com/bnymnsogut/GomuluMobilProjesi_MMS/blob/master/Resimler/sim800l.jpg">
</p> 
    
    
## HP Pro Web Kamera (AU165AA)
<img align="right" width="230" height="270" src="https://github.com/bnymnsogut/GomuluMobilProjesi_MMS/blob/master/Resimler/kamera.jpg">
    Ev içine izinsiz girişlerin fotoğraflanıp ilgili kişiye gönderilmesi için kamera kullanılmıştır. Mesafe sensörü beklenmedik bir durum algıladığında mikrodenetleyice haber vermektedir. Ardından mikrodenetleyiciye kameraya fotoğraf çekmesi komutunu verir. Daha sonra çekilen fotoğraf kullanıcının e-postasına atılır.
</br>Sistemde kullanılan kamera : HP Pro Webcam (AU165AA) . Kullanılan kameranın çözünürlüğü saniyede 30 kareye kadar 640 x 480 değerindedir. USB 2.0 ile diğer cihazlara bağlantısı yapılabilir.
</br> Siz elinizde bulunan herhangi bir web kamera ile aynı işlemi yapabilirsiniz. Benim kameram standart raspberry pi usb kütüphanesi ile uyumlu olduğu için driver yüklemedim. Kameranıza uygun driverı yüklemeniz gerekebilir.</br>    

## Donanım Yapısı
Yazılım aşamasına başlamadan önce donanımları uygun bir şekilde birleştirmek önemlidir.</br>
*Sim moduülü 3.4v ile 4.2v ile beslendiği için ona uygun batarya seçimi yapılmalıdır. 
Burada önemli nokta ise kullanılan batarya ile raspberry pi ground'u aynı seviyede olmalıdır. 
Bunun için bataryanın ground'u ile raspberry pi groundunu birleştirmeliyiz.</br>
*Mesafe sensörü 5V ile beslendiği için pin çıkışları da 5v tur. Fakat Raspberry PI pin girişleri maksimum 3.3V önerilmektedir. 
Bu yüzden bu modülden aldığımız sinyalleri 2 tane direnç yardımı ile gerilim bölücü yaparak raspberry pi pinlerine giriyoruz.</br>
<img  width="810" height="800" src="https://github.com/bnymnsogut/GomuluMobilProjesi_MMS/blob/master/Resimler/Donanim_semasi.jpg">

## Yazılım Yapısı

Yazılımımızı çalıştırmak için kodlarımızı raspberry pi'a kopyalıyoruz.</br>
<img align="right" width="350" height="478" src="https://github.com/bnymnsogut/GomuluMobilProjesi_MMS/blob/master/Resimler/Yazilim_Akis_Semasi.jpg">
Ana kodumuz `main.py` bu kodu komut satırında çalıştırdığımızda tüm projemiz çalışmış oluyor.</br></br>
Kodumuzu çalıştırmadan önce komut satırına `sudo su` yazarak root moduna alıyoruz. Sim modülünde seri haberleşme kullanacağımız için bunu yapmamız gerekiyor.</br>
Daha sonra `camera.py` dosyasını komut satırına `python camera.py` yazarak bir kere çağırıyoruz. İlk fotoğrafı kameradan manuel alıyoruz.
`main.py` dosyası içinde kamera ve MMS fonksiyonlarımızı sisteme tanıtmak için başlangıç kodlarını çağırıyoruz.</br></br>
Mesafe sensöründen alınan değerlerin hesabını sensörün [datasheet (HC-SR04)](https://cdn.sparkfun.com/datasheets/Sensors/Proximity/HCSR04.pdf) 'ine bakarak hesaplıyoruz.</br>
Mesafe sensörü kapının açıldığını algılarsa fotoğraf çekiyoruz. Kodların olduğu klasöre bu fotoğrafı kaydediyoruz. Ardından MMS gönderme fonksiyonunu çağırıyoruz.</br></br>
MMS gönderme fonksiyonları için AT komutları kullanmamız gerekiyor. [SIMM800L'nin datasheet](https://cdn-shop.adafruit.com/datasheets/sim800_series_at_command_manual_v1.01.pdf)'den AT komutlarını incelemeliyiz.</br>
Ayrıca MMS göndermek için özel bir [doküman](https://cdn-shop.adafruit.com/datasheets/sim800_series_mms_application_note_v1.00.pdf) hazırlanmış oradaki işlemleri sırasıyla uygulamamız yeterli olacaktır.</br></br>
MMS gönderme fonksiyonu içinde ilk önce modülü MMS moduna alma ayarlarını UART protokolü üzerinden sim modülümüze bildiriyoruz.</br>
Sonrasında UART üzerinden çektiğimiz resimleri byte larına ayırarak gönderiyoruz.</br>
Aşağıda UART protokolü üzerinden resim göndermek için yapılmış bir hesaplama mevcuttur.</br>
`1 Mb lık bir resim 9600 baud VE 115200 baud haberleşmede aşağıdaki formül ile süresi hesaplanır.
<p align="center">
  <img src="https://github.com/bnymnsogut/GomuluMobilProjesi_MMS/blob/master/Resimler/uart_hesap.jpg">
</p> 
Yukarıdaki resimde de görüldüğü gibi daha önceden bu baud ne işe yarıyor diyorsanız 9600 ve 115200 baud arasındaki resim gönderme hızı çok farklıdır.</br>
Resim uart datası üzerinden modüle başarılı bir şekilde aktarıldıktan sonra modüle uart üzerinden MMS gönder mesajı yolluyoruz.</br>

## Ugulama Aşaması   

*`main.py` komutu komutsatırı üzerinden çalıştırıyoruz.
*Kodumuz çalışmaya başladıktan sonra sürekli mesafe ölçümü yapacaktır.</br>
*Mesafe sensörürünün önüne bir engel geldiğinde onu algılayacak ve sırasıyla aşağıdaki gibi fotoğraf çekme komutu ardından çekilen fotoğrafı MMS ile göndermek için bytelarına ayıracaktır.</br></br>
<p align="center">
  <img width="700" height="700" src="https://github.com/bnymnsogut/GomuluMobilProjesi_MMS/blob/master/Resimler/kapi_ac.jpg">
</p> 
*Byte byte uart üzerinden yazılan datalar modül tarafından toplanmaktadır. Ardından Mesaj başlığı ve içerikte ekleyebiliyoruz.</br>
*Yükleme işlemleri tamamlandıktan sonra modül bize CONNECT yazısı gönderecektir. bu işlemlerden sonra telefon numarasını modüle bildiriyoruz</br>

*Başarılı bir şekilde ulaştıktan sonra MMS send komutunu modüle gönderiyoruz ve aşağıdaki gibi resmimiz telefonumuza gönderiliyor.</br>
<p><strong>Not: MMS mesajını telefonda görüntüleyebilmek için telefonun wifi'ı kapalı mobil verisinin açık olması gerekmektedir.</strong></p></br>
 
<p align="center">
  <img width="700" height="700" src="https://github.com/bnymnsogut/GomuluMobilProjesi_MMS/blob/master/Resimler/mms_geldi.jpg">
</p> 

*Ayrıca SMS ve MMS kodlarını sizler ile paylaşıyorum. [Proje Youtube Video Linki](https://youtu.be/WtqSSz-gh94) 'de nasıl kullanılacağına dair bilgi verdim.</br>
