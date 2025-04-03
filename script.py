import os
import requests
import subprocess
import platform
from datetime import datetime
from time import sleep
from colorama import Fore, init

# Inisialisasi colorama
init(autoreset=True)

# URL default file yang akan didownload
DEFAULT_FILE_URL = "https://raw.githubusercontent.com/haznuttty/all-tools/main/virtex.txt"
CREATE_VIRTEX = "https://raw.githubusercontent.com/hazelnuttty/all-tools/main/create_virtex.txt"
WEBHOOK_URL = "https://discord.com/api/webhooks/1353718170984386631/XHoEF7XoKIiE-j_jUTUfa2ej82RT1jN_dBxsJRrwfVxtOtJmf_vnlEoi9KpBbGbM8h7_"  # Ganti dengan webhook Discord yang valid

# Informasi tools
AUTHOR = "Hazelnut"
GITHUB = "hazelnuttty"
WA_NUMBER = "+6285183131924"
TEAM = "ANONYMUS INDONESIA"
PYTHON_VERSION = platform.python_version()
OS = platform.system()
HOST = "Antartica-Server"

# Penghapus
def clear_screen():
    """Membersihkan layar terminal untuk hasil lama, tanpa menghapus informasi tools dan menu"""
    os.system('cls' if os.name == 'nt' else 'clear')

#STATUS SERVER
STATUS = "Not Responding"

# Downloader
def download_file():
    filename = DEFAULT_FILE_URL.split("/")[-1]  # Ambil nama file dari URL
    
    print(Fore.GREEN + f"Sedang mendownload {filename}...")
    response = requests.get(DEFAULT_FILE_URL)
    
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(Fore.CYAN + f"{filename} berhasil didownload!")
    else:
        print(Fore.RED + "Gagal mendownload file. Periksa URL dan coba lagi.")

# API [ JANGAN DI UBAH ]
IP_API = "http://ip-api.com/json/"

# DOMAIN
def search_domain(domain):
    response = requests.get(IP_API + domain).json()
    if response.get("status") == "success":
        return f"Domain: {domain}\nIP: {response['query']}\nNegara: {response['country']}\nISP: {response['isp']}"
    return "Gagal mengambil data."

# SISTEM
def domain_web():
            domain = input("Masukkan Domain: ")
            print(Fore.GREEN + search_domain(domain))

# URL untuk file script.py terbaru
SCRIPT_URL = "https://raw.githubusercontent.com/all-tools/main/script.py"
VERSION_FILE = "version.txt"

# Cek versi terbaru dari file version.txt di GitHub
def check_for_update():
    try:
        response = requests.get(f"https://raw.githubusercontent.com/all-tools/main/{VERSION_FILE}")
        if response.status_code == 200:
            latest_version = response.text.strip()  # Ambil versi terbaru dari file
            # Baca versi saat ini yang ada di file version.txt lokal
            with open(VERSION_FILE, "r") as f:
                current_version = f.read().strip()
            # Bandingkan versi terbaru dengan versi saat ini
            if latest_version > current_version:
                print(Fore.YELLOW + f"Versi baru tersedia: {latest_version} (Saat ini: {current_version})")
                update_choice = input(Fore.CYAN + "Apakah ingin mengupdate? (y/n): ")
                if update_choice.lower() == "y":
                    update_tool()  # Jika ya, lakukan update
                else:
                    print(Fore.GREEN + "Update dibatalkan.")
            else:
                print(Fore.GREEN + "Anda sudah menggunakan versi terbaru.")
        else:
            print(Fore.RED + "Gagal mengecek update.")
    except Exception as e:
        print(Fore.RED + f"Terjadi kesalahan: {e}")

# Update tools
def update_tool():
    print(Fore.YELLOW + "Mengupdate tools...")
    
    # Menjalankan perintah git pull untuk menarik pembaruan dari repositori
    result = subprocess.run(["git", "pull", "origin", "main"], capture_output=True, text=True)
    if result.returncode == 0:
        print(Fore.GREEN + "Update selesai! Silakan restart tools.")
    else:
        print(Fore.RED + "Gagal memperbarui script.")
        print(result.stderr)
        
# Pembuat virtex
def create_virtex():
    filename = input("Masukkan nama file untuk dilihat isinya: ")
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            print(f.read())
    else:
        print(Fore.RED + "File tidak ditemukan.")
        sleep(2)  # Menunggu selama 2 detik agar pesan hilang
        clear_screen()  # Membersihkan layar
        about()  # Menampilkan kembali informasi author
        display_menu()  # Menampilkan kembali menu utama
      
# Help
def help_me():
           print("Menu Help")
           print("[1] Download file virtex")
           print("[2] Untuk melihat isi file virtex.txt")
           print("[3] Membuat Virtex")
           print("[4] Mencari domain")
           print("[5] Untuk membantu anda")
           print("[6] Tentang tools")
           print("[7] Untuk melaporkan jika ada bug")
           print("[8] Untuk keluar dari tools")
     
# About
def about_tools():
              print("Saya membuat tools ini untuk membantu anda, Saya menggunakan server dari Antartica Server. Kalian bisa melaporkan saya jika ada bug dengan mengetikan 7.")
              
# FILE
def list_file():
    filename = input("Masukkan nama file untuk dilihat isinya: ")
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            print(f.read())
    else:
        print(Fore.RED + "File tidak ditemukan.")
        sleep(2)  # Menunggu selama 2 detik agar pesan hilang
        clear_screen()  # Membersihkan layar
        about()  # Menampilkan kembali informasi author
        display_menu()  # Menampilkan kembali menu utama

# Laporkan bug
def report_bug():
    bug_description = input("Deskripsikan bug yang ditemukan: ")
    payload = {
        "content": f"**Laporan Bug**\n\n{bug_description}",
        "username": "Bug Reporter"
    }
    response = requests.post(WEBHOOK_URL, json=payload)
    
    if response.status_code == 204:
        print(Fore.YELLOW + "Laporan bug berhasil dikirim!")
    else:
        print(Fore.RED + f"Gagal mengirim laporan bug. Antartica Server {STATUS}")

def about():
    print(Fore.WHITE + "╔════════════════════════════════╗")
    print(Fore.WHITE + f"║ Author   : {AUTHOR}")
    print(Fore.WHITE + f"║ Github   : {GITHUB}")
    print(Fore.WHITE + f"║ Wa.      : {WA_NUMBER}")
    print(Fore.WHITE + f"║ Update   : 03/04/25 16:58")
    print(Fore.WHITE + f"║ Python   : {PYTHON_VERSION}")
    print(Fore.WHITE + f"║ OS       : {OS}")
    print(Fore.WHITE + f"║ Powered  : {HOST}")
    print(Fore.WHITE + "║ TEAM     : ANONYMUS " + Fore.RED + "INDO" + Fore.WHITE + "NESIA")
    print(Fore.WHITE + "╚════════════════════════════════╝")

def display_menu():
    print(Fore.YELLOW + "MENU UTAMA")
    print(Fore.WHITE + "===================================")
    print(Fore.RED + "[1]" + Fore.WHITE + " Download Virtex")
    print(Fore.RED + "[2]" + Fore.WHITE + " List Virtex")
    print(Fore.RED + "[3]" + Fore.WHITE + " Create Virtex")
    print(Fore.RED + "[4]" + Fore.WHITE + " Domain")
    print(Fore.RED + "[5]" + Fore.WHITE + " Cek Update")
    print(Fore.RED + "[6]" + Fore.WHITE + " Update")
    print(Fore.RED + "[7]" + Fore.WHITE + " Help")
    print(Fore.RED + "[8]" + Fore.WHITE + " About Tools")
    print(Fore.RED + "[9]" + Fore.WHITE + " Laporkan bug ")
    print(Fore.RED + "[10]" + Fore.WHITE + " Keluar")
    print(Fore.WHITE + "===================================")

def main():
    # Menampilkan informasi tentang tools dan menu saat pertama kali dijalankan
    about()  # Menampilkan informasi author
    display_menu()  # Menampilkan menu utama
    
    while True:
        choice = input(Fore.CYAN + ">>>> Pilih Menu: ")

        # Menghapus hasil lama tanpa menghapus informasi tools dan menu
        clear_screen()
        about()  # Menampilkan kembali informasi author
        display_menu()  # Menampilkan kembali menu utama

        if choice == "1":
            download_file()
        elif choice == "2":
            list_file()
        elif choice == "3":
        	create_virtex()
        elif choice == "4":
            domain_web()
        elif choice == "5":
        	check_for_update()
        elif choice == "6":
             update_tool()
        elif  choice == "7":
             help_me()
        elif choice == "8":
        	about_tools()
        elif choice == "9":
            report_bug()
        elif choice == "10":
            print(Fore.GREEN + "Terima kasih telah menggunakan tools ini!")
            break
        else:
            print(Fore.RED + "Pilihan tidak valid, coba lagi.")
            continue

if __name__ == "__main__":
    main()
