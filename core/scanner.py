import os
import subprocess
import datetime
from termcolor import colored # type: ignore
from core.utils import write_log

CAPTURE_DIR = "output/capture"

def scan_wifi(interface):
    print(f"[*] Memulai scan WIFI di interface: {interface}")

    os.makedirs(CAPTURE_DIR, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(CAPTURE_DIR, f"scan_{timestamp}")

    try:
        cmd = [
            "sudo", "airodump-ng",
            "--output-format", "csv",
            "-w", filename,
            interface
        ]
        print(colored("[!] Tekan Ctrl + C untuk menghentikan scan.\n", "yellow"))
        subprocess.run(cmd)

        write_log("output/logs/scan.log", f"Scan dijalankan di interface {interface}, hasil disimpan ke {filename}-01.csv")

    except KeyboardInterrupt:
        print(colored("\n[✓] Scan dihentikan oleh pengguna.", "green"))
    except Exception as e:
        print(colored(f"[!] Error saat scanning: {e}", "red"))


def capture_handshake(interface: str, bssid: str, channel: str):
    os.makedirs(CAPTURE_DIR, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join(CAPTURE_DIR, f"handshake_{bssid.replace(':', '')}_{timestamp}")

    print(colored(f"[*] Mulai menangkap handshake pada BSSID {bssid} di channel {channel}", "yellow"))
    print(colored("[!] Tekan Ctrl + C untuk berhenti menangkap handshake.\n", "yellow"))

    try:
        subprocess.run([
            "sudo", "airodump-ng",
            "--bssid", bssid,
            "-c", channel,
            "-w", output_file,
            interface
        ])
        write_log("output/logs/handshake.log", f"Handshake capture: BSSID={bssid}, Channel={channel}, Output={output_file}-01.cap")

    except KeyboardInterrupt:
        print(colored("\n[•] Proses tangkap handshake dihentikan oleh pengguna.", "cyan"))
    except Exception as e:
        print(colored(f"[!] Terjadi error saat menangkap handshake: {e}", "red"))
    else:
        print(colored(f"[✓] Capture handshake tersimpan di {output_file}-01.cap", "green"))
