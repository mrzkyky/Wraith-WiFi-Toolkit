# WRAITH - WiFi Recon & Attack Intelligence Terminal Hub

WRAITH adalah toolkit terminal interaktif untuk auditing dan penetration testing jaringan WiFi. Tools ini dirancang agar ringan, powerful, dan mudah digunakan oleh para pentester, CTF player, atau pembelajar cybersecurity yang ingin mempelajari teknik pengujian keamanan WiFi secara praktis.

![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)

---

## ✨ Fitur Utama

| No | Fitur             | Deskripsi                                                  |
| -- | ----------------- | ---------------------------------------------------------- |
| 1  | Scan Jaringan     | Mendeteksi jaringan WiFi di sekitar melalui `airodump-ng`. |
| 2  | Tangkap Handshake | Menyimpan file .cap dari target jaringan WPA/WPA2.         |
| 3  | Deauth Attack     | Mengirim paket deauth ke client/target AP.                 |
| 4  | Crack Password    | Memecahkan password WiFi dari file handshake + wordlist.   |
| 5  | Generate Report   | Membuat laporan hasil audit: scan, deauth, crack.          |

---

## 🛠️ Dependencies

* Python 3.8+
* `aircrack-ng`
* `iw`, `ip`, `airodump-ng`, `aireplay-ng`
* `termcolor`

### Install Dependency (Linux/Ubuntu)

```bash
sudo apt update
sudo apt install aircrack-ng python3-pip -y
pip install termcolor
```

---

## 📂 Struktur Folder

```
WRAITH/
├── core/                  # Semua fungsi utama modular
│   ├── scanner.py         # Fitur scan dan handshake
│   ├── deauth.py          # Fitur deauth attack
│   ├── cracker.py         # Fitur crack handshake
│   ├── report.py          # Fitur generate laporan
│   ├── utils.py           # Fungsi bantu: banner, interface, logging
│   └── target.py          # Objek target
├── output/                # Folder hasil
│   ├── capture/           # File .csv dan .cap
│   ├── logs/              # File log .log
│   └── report/            # Laporan akhir .txt
├── wordlists/             # Wordlist lokal (opsional, TIDAK TERMASUK repo)
├── main.py                # Entry point
├── LICENSE                # Lisensi proyek MIT
└── README.md
```

---

## 🚀 Cara Menggunakan

```bash
git clone https://github.com/mrzkyky/WRAITH.git
cd WRAITH
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
sudo python3 main.py
```

### ⚠️ Note:

* Gunakan interface WiFi eksternal (misalnya TP-Link TL-WN722N). Noted : Cari yang V1 karena support mode monitor. pakai yang V2 bisa cuman butuh sedikit Polesan sedikit dan agak Lambat.
* Beberapa fitur membutuhkan mode monitor dan akses `sudo`.

---

## 🔑 Tentang Wordlist

File wordlist **tidak disertakan** dalam repo karena keterbatasan ukuran GitHub dan lisensi. Namun kamu bisa:

1. Mengunduh wordlist `rockyou.txt` dari sistem Linux:

```bash
sudo apt install wordlists
sudo gzip -d /usr/share/wordlists/rockyou.txt.gz
```

2. Atau buat wordlist sendiri:

```bash
echo -e "password123\nadmin123\n12345678" > wordlists/custom.txt
```

3. Jalankan WRAITH dengan wordlist tersebut:

```bash
> Pilih menu: 4
> Wordlist: wordlists/custom.txt
```

---

## 💻 Tampilan CLI

```
[1] Scan Jaringan
[2] Tangkap Handshake
[3] Jalankan Deauth Attack
[4] Crack Password
[5] Generate Report
[6] Keluar
```

---

## 📘 Contoh Penggunaan

### 1. Scan Jaringan

```bash
> Pilih menu: 1
> Interface: wlx98038e9e524e
```

### 2. Tangkap Handshake

```bash
> Pilih menu: 2
> BSSID: 08:40:F3:58:81:29
> Channel: 6
```

### 3. Deauth

```bash
> Pilih menu: 3
> BSSID: 08:40:F3:58:81:29
> Client MAC: (atau kosongkan untuk broadcast)
> Count: 10
```

### 4. Crack Password

```bash
> Pilih menu: 4
> File handshake: output/handshake/xxx.cap
> Wordlist: wordlists/custom.txt
```

### 5. Generate Report

```bash
> Pilih menu: 5
> Simpan sebagai: output/report/audit_220725.txt
```

---

## ✅ Platform Support

* Ubuntu/Debian Linux (100% tested)
* Kali Linux (100% supported)
* Parrot OS

> Windows/macOS: Tidak didukung secara penuh karena tools seperti `airodump-ng` dan `aireplay-ng` spesifik untuk Linux.

---

## ⚠️ Disclaimer

WRAITH hanya digunakan untuk **tujuan edukasi dan pengujian di lingkungan milik sendiri** atau yang mendapat izin. Penulis tidak bertanggung jawab atas penyalahgunaan tools ini.

---

## 👨‍💻 Kontribusi

Pull request, fitur tambahan, dan perbaikan bug sangat diterima.

---

## 📫 Kontak

**Developer:** \[ZkyR]
**Email:** [harvey01850@gmail.com](mailto:harvey01850@gmail.com)
**GitHub:** [github.com/mrzkyky](https://github.com/mrzkyky)

---

## 🧠 Next Feature Ideas (Opsional)

* Validasi handshake sebelum crack
* Mode otomatis: scan > capture > deauth > crack
* Ekspor SQLite/JSON
* Web GUI berbasis Flask/Streamlit

---

## 🔐 "Mengamankan butuh niat, membobol butuh ilmu."

---

**WRAITH** — WiFi Recon & Attack Intelligence Terminal Hub

---

## 📄 Lisensi

Project ini dilisensikan di bawah **MIT License**. Kamu bebas menggunakan, memodifikasi, dan mendistribusikan kode ini dengan mencantumkan atribusi yang sesuai.

---

