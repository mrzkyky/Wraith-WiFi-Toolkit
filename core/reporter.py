import os
import datetime
from termcolor import colored

def generate_report(bssid, essid, channel, crack_result=None):
    os.makedirs("output/reports", exist_ok=True)

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename = f"output/reports/report_{bssid.replace(':','')}.txt"

    content = f"""
===========================================
        WIFI ATTACK REPORT
===========================================

🕒 Tanggal/Waktu   : {timestamp}
📡 Target BSSID     : {bssid}
📶 Nama SSID        : {essid}
📻 Channel          : {channel}
🔓 Crack Result     : {crack_result or 'Belum ditemukan / gagal'}

-------------------------------------------
📁 File log detail ada di folder: output/logs/
"""

    with open(filename, "w") as f:
        f.write(content.strip())

    print(colored(f"[✓] Report berhasil dibuat di {filename}", "green"))
