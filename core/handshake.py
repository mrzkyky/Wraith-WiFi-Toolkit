import os 
import subprocess
import datetime

CAPTURE_DIR = "output/handshake"

def capture_handshake(interface, bssid, channel):
    print(f"[*] Memulai tangkap handshake pada BSSID: {bssid} di channel: {channel} menggunakan interface: {interface}")

    os.makedirs(CAPTURE_DIR, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(CAPTURE_DIR, f"handshake_{bssid.replace(':', '')}_{timestamp}")

    try:
        # Jalankan airodump-ng untuk target BSSID dan channel
        cmd_airodump = [
            "sudo", "airodump-ng",
            "--bssid", bssid,
            "--channel", channel,
            "--write", filename,
            interface
        ]

        # Beri info cara stop
        print("[!] Tekan Ctrl + C untuk menghentikan proses tangkap handshake.\n")
        subprocess.run(cmd_airodump)

    except KeyboardInterrupt:
        print("\n[✓] Proses tangkap handshake dihentikan oleh pengguna.")

    except Exception as e:
        print(f"[!] Error saat menangkap handshake: {e}")