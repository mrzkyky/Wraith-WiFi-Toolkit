import os
import subprocess
from termcolor import colored # type: ignore
from core.utils import write_log

def crack_password(cap_file, wordlist_file):
    print(colored(f"[*] Memulai proses cracking dengan wordlist: {wordlist_file}", "cyan"))

    if not os.path.isfile(cap_file):
        print(colored("[!] File handshake (.cap) tidak ditemukan!", "red"))
        return

    if not os.path.isfile(wordlist_file):
        print(colored("[!] File wordlist tidak ditemukan!", "red"))
        return

    try:
        cmd = [
            "aircrack-ng",
            "-w", wordlist_file,
            cap_file
        ]

        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

        found_key = None
        for line in process.stdout:
            print(line.strip())
            if "KEY FOUND!" in line:
                found_key = line.strip()

        if found_key:
            write_log("output/logs/crack.log", f"[✓] {found_key} | File: {cap_file}")
            print(colored(f"[✓] Password ditemukan dan disimpan di log!", "green"))
        else:
            write_log("output/logs/crack.log", f"[✗] Crack gagal untuk file: {cap_file}")
            print(colored("[!] Crack selesai tapi password tidak ditemukan.", "red"))

    except Exception as e:
        print(colored(f"[!] Gagal menjalankan aircrack-ng: {e}", "red"))
