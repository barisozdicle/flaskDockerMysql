# Flask Docker MySQL Projesi

Bu proje, Docker konteynerlerinde çalışan bir Flask web uygulaması ve MySQL veritabanından oluşmaktadır. Proje, mobilya verilerini JSON formatında sunan basit bir API içerir.

## 🚀 Teknolojiler

- Python 3.x
- Flask
- MySQL
- Docker & Docker Compose

## 📋 Gereksinimler

- Docker
- Docker Compose

## 🔧 Kurulum

1. Projeyi klonlayın:
```bash
git clone https://github.com/barisozdicle/flaskDockerMysql.git
cd flaskDockerMysql
```

2. `.env` dosyasını oluşturun:
```bash
# Flask Ayarları
FLASK_APP=app.py
FLASK_ENV=development
FLASK_DEBUG=1
FLASK_PORT=5001
CONTAINER_FLASK_PORT=5000

# MySQL Ayarları
MYSQL_HOST=mysql
MYSQL_PORT=3306
MYSQL_ROOT_PASSWORD=123
MYSQL_DATABASE=SuadiyeDB
MYSQL_USER=baris
MYSQL_PASSWORD=1

# Uygulama Ayarları
APP_SECRET_KEY=secret_key
```

3. Docker konteynerlerini başlatın:
```bash
docker-compose up
```

## 🌐 Kullanım

Uygulama başlatıldıktan sonra:

- API'ye http://localhost:5001 adresinden erişebilirsiniz
- Varsayılan endpoint (/) mobilya verilerini JSON formatında döndürür

Örnek yanıt:
```json
{
  "FurnitureName": "Televizyon",
  "FurnitureImage": "TV Resmi"
}
```

## 📁 Proje Yapısı

```
flaskDockerMysql/
├── app/
│   ├── app.py           # Flask uygulaması
│   └── requirements.txt # Python bağımlılıkları
├── db/
│   └── mysql/
│       └── schema.sql   # Veritabanı şeması
├── docker-compose.yaml  # Docker yapılandırması
├── .env                 # Çevre değişkenleri
└── README.md           # Bu dosya
```

## 🛠️ Geliştirme

1. Yeni bir özellik eklemek için:
   - Feature branch oluşturun
   - Değişikliklerinizi yapın
   - Pull request açın

2. Veritabanı şemasını güncellemek için:
   - `db/mysql/schema.sql` dosyasını düzenleyin
   - Konteynerleri yeniden başlatın

## 📝 Notlar

- `.env` dosyası git'e eklenmemiştir. Kendi `.env` dosyanızı oluşturmanız gerekmektedir.
- Üretim ortamında kullanmadan önce güvenlik ayarlarını gözden geçirin.
- MySQL bağlantısı için yeniden deneme mekanizması eklenmiştir.

## 🔒 Güvenlik

- Hassas bilgileri `.env` dosyasında saklayın
- `.env` dosyasını asla git'e eklemeyin
- Üretim ortamında güçlü şifreler kullanın

## 👥 Katkıda Bulunma

1. Bu depoyu fork edin
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Değişikliklerinizi commit edin (`git commit -m 'feat: Add some amazing feature'`)
4. Branch'inizi push edin (`git push origin feature/amazing-feature`)
5. Pull Request açın 