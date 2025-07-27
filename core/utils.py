import os
from termcolor import colored  # type: ignore
import subprocess
import re
from datetime import datetime

def show_banner():
    banner = """
                                                                                
                                                                                
                                                                                
                                      &##&.                                     
                                    &/&&&&&&&.                                  
                         ,/#&&&&&&&/&&&&&&&&&&&.                                
                       ,*&&&&&///(&&&&&&&&&&&&&&                                
                       /////%&&&&&&&&&&&&&&&&&&&& .&&&&&&&                      
                       ,,///&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&                      
                        .///&&&&&&&&&&&&&&&&&&&&&&&&&&&&.                       
                        / //&&&&&&&&&&&&&&&&&&&&&&&&&&%                         
                     .*// */(&&&&&&&&&&&&&&&#*(&&&&&&&&                         
                ./    ///* */&&&&&&&&&(///*(&&&&&&&&&&.                         
                 *.   */////////////////%&&&&&&&&&&&&%&&&&                      
                .   %(/*         *//%&&&&&&&&&&&&&*&&&&%&#                      
                            &&&&&&&&&&&&&&&&&&&&&&%&&&&&&                       
                            &@/*//(&&&&&&&&&&&&&&&%&&&&&%.                      
                          (&&&&#//#///&&&&&&&&&&&&&&&&&&.                       
                        ,&&&&&&&//*/##&&&&&&&#&&&&&&&&&&&* .                    
                      %&&&&&&&&&&&/////&&&&&&&&&&&&&&&&&&&&&&.                  
                   /&&&&&&&&&&&&&&*,*////*#&&&&&&&&&&#&&&&&&&&&#                
                  /&&&&&&&&&&&&&&&%    .%&&%&&&&&&&&&&&&&&&&&&&%,               
                 &&&&&&&&&&&&&&&&&&,    /&&&&&&&&&%&&&&&&&&&&*                  
                     #&&&%&&&&&&&&&&  (####&&&&&%&&&&&&&&&&&&&                  
                     &&&&%&&&&&&&&&&  (###&&&&#&&&&&&&&&&&&&                    
                       #&&&%&&&&&&&&& ###&&&#&&&&&&&&&&&&/                      
                          .(&&&&&&&&&#((&&#&&&&&&&&&&&%                         
                             &&&&&&&&%#&&&&&&&&&&&&%                            
                              .&&&&&&@&&&&&&&&&&&*                              
                                     ./(##(*                                    
                                                                       .        
                                                                                
    """
    print(colored(banner, "cyan"))
    print(colored("      WiFi Recon & Attack Intelligence Terminal Hub", "yellow"))
    print("=" * 70)

def list_monitor_interfaces():
    print(colored("\n[*] Mengecek Interface Monitor Mode Yang Tersedia => => =>\n", "blue"))

    try:
        result = subprocess.run(['iw', 'dev'], capture_output=True, text=True)
        lines = result.stdout.split('\n')

        interfaces = []
        current_iface = None

        for line in lines:
            line = line.strip()
            if line.startswith("Interface"):
                current_iface = line.split()[1]
            elif line.startswith("type monitor") and current_iface:
                interfaces.append(current_iface)

        if interfaces:
            print(colored("[✓] Ditemukan interface monitor mode:", "green"))
            for i, iface in enumerate(interfaces):
                print(colored(f"  [{i+1}] {iface}", "cyan"))
        else:
            print(colored("[!] Tidak ada interface dengan mode Monitor terdeteksi.", "red"))

        return interfaces

    except Exception as e:
        print(colored(f"[!] Gagal mendeteksi interface: {e}", "red"))
        return []

def auto_enable_monitor_mode():
    print(colored("[•] Mendeteksi interface WiFi aktif...", "yellow"))
    try:
        result = subprocess.run(['iw', 'dev'], capture_output=True, text=True)
        lines = result.stdout.split('\n')
        current_iface = None
        for line in lines:
            line = line.strip()
            if line.startswith("Interface"):
                current_iface = line.split()[1]
            elif line.startswith("type managed") and current_iface:
                print(colored(f"[•] Mengaktifkan monitor mode pada: {current_iface}", "cyan"))
                subprocess.run(["sudo", "airmon-ng", "check", "kill"])
                subprocess.run(["sudo", "airmon-ng", "start", current_iface])
                return True
        print(colored("[!] Tidak ditemukan interface dengan mode managed (WiFi biasa).", "red"))
        return False
    except Exception as e:
        print(colored(f"[!] Gagal menjalankan auto enable monitor: {e}", "red"))
        return False
    
def is_valid_handshake(cap_file: str) -> bool:
    try:
        # Jalankan aircrack-ng untuk memeriksa isi file .cap
        result = subprocess.run(["aircrack-ng", cap_file],
                                capture_output=True, text=True)

        # Cek output apakah ada (1 handshake) atau lebih
        if "WPA (1 handshake)" in result.stdout or re.search(r"WPA \(\d+ handshake", result.stdout):
            return True
        else:
            return False

    except Exception as e:
        print(colored(f"[!] Gagal memvalidasi handshake: {e}", "red"))
        return False
    

def write_log(file_path: str, content: str):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    with open(file_path, "a") as f:
        f.write(f"{timestamp} {content}\n")

