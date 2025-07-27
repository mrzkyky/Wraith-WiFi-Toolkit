from core.deauth import deauth_attack
from core.reporter import generate_report
from core.utils import show_banner, list_monitor_interfaces, auto_enable_monitor_mode
from core.scanner import scan_wifi   
from core.handshake import capture_handshake
from core.cracker import crack_password

monitor_iface = None

def show_menu():
    print("\n[1] Scan Jaringan")
    print("[2] Tangkap Handshake")
    print("[3] Jalankan Deauth Attack")
    print("[4] Crack Password")
    print("[5] Generate Report")
    print("[6] Keluar\n")

def main():
    show_banner()
    global monitor_iface

    monitor_iface = auto_enable_monitor_mode()  # ✅ Panggil fungsi dengan ()

    while True:
        interfaces = list_monitor_interfaces()
        show_menu()
        choice = input("Pilih menu: ")
        
        if choice == "1":
            if not interfaces:
                print("[!] Tidak ada interface monitor mode. Silakan aktifkan terlebih dahulu.")
                continue

            iface = input("Masukkan interface monitor mode (misalnya: wlx98038e9e524e): ").strip()
            if iface not in interfaces:
                print("[!] Interface tidak valid atau bukan mode monitor.")
                continue

            scan_wifi(iface)

        elif choice == "2":
            if not interfaces:
                print("[!] Tidak ada interface monitor mode. Silakan aktifkan terlebih dahulu.")
                continue

            iface = input("Masukkan interface monitor mode: ").strip()
            if iface not in interfaces:
                print("[!] Interface tidak valid atau bukan mode monitor.")
                continue

            bssid = input("Masukkan BSSID target (Contoh: 50:5B:1D:F4:BC:C0): ").strip()
            channel = input("Masukkan channel target (Contoh: 6): ").strip()

            if not bssid or not channel.isdigit():
                print("[!] BSSID dan channel harus diisi dengan benar.")
                continue

            capture_handshake(iface, bssid, channel)

        elif choice == "3":
            iface = input("Masukkan interface monitor mode: ").strip()
            bssid = input("Masukkan BSSID target (contoh: AA:BB:CC:DD:EE:FF): ").strip()
            client_mac = input("Masukkan MAC client (atau kosong untuk broadcast): ").strip()
            try:
                count = int(input("Jumlah paket deauth (default 10): ") or 10)
            except ValueError:
                count = 10
            deauth_attack(iface, bssid, client_mac, count)

        elif choice == "4":
            cap_file = input("Masukan path ke file handshake (.cap): ").strip()
            wordlist = input("Masukan path ke wordlist (misalnya /usr/share/wordlist/rockyou.txt): ").strip()
            crack_password(cap_file, wordlist)

        elif choice == "5":
            bssid = input("Masukkan BSSID target: ").strip()
            essid = input("Masukkan nama SSID: ").strip()
            channel = input("Masukkan channel: ").strip()
            crack_result = input("Masukkan hasil crack (jika ada, kosongkan jika tidak): ").strip()
            generate_report(bssid, essid, channel, crack_result)

        elif choice == "6":
            print("Keluar...")
            break
        else:
            print("[!] Pilihan tidak valid.")

# ✅ Tangani Ctrl+C dan error global
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Program dihentikan oleh pengguna (Ctrl + C).")
    except Exception as e:
        print(f"[!] Terjadi error tak terduga: {e}")
