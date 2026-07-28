import os
import sys
from openai import OpenAI

def compile_ados_repository():
    """Mengompilasi peta pohon folder dan ringkasan berkas ados-core"""
    print("[ADOS-DOCTOR] Sedang memindai kesehatan repositori lokal...")
    summary = []
    
    # 1. Petakan pohon folder untuk melihat kepatuhan arsitektur 5-lapisan
    summary.append("=== STRUKTUR FOLDER ADOS-CORE SAAT INI ===")
    for root, dirs, files in os.walk("./python/ados"):
        if any(x in root for x in ['.git', '__pycache__', '.aider']): continue
        level = root.replace("./python/ados", "").count(os.sep)
        indent = ' ' * 4 * level
        summary.append(f"{indent}{os.path.basename(root)}/")
        for f in files:
            if f.endswith('.py'):
                summary.append(f"{indent}    - {f}")
                
    # 2. Ambil baris-baris import untuk mendeteksi potensi Circular Import
    summary.append("\n=== BARIS IMPORT ANTAR-MODUL ===")
    for root, _, files in os.walk("./python/ados"):
        if any(x in root for x in ['.git', '__pycache__', '.aider']): continue
        for file in files:
            if file.endswith('.py') and file != 'ados_doctor.py':
                file_path = os.path.join(root, file)
                summary.append(f"\n--- Berkas: {file_path} ---")
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    for line in f:
                        if line.startswith('import ') or line.startswith('from '):
                            summary.append(line.strip())
                            
    return "\n".join(summary)

def run_diagnosis():
    # Pastikan API Key OpenRouter sudah disuntikkan ke Termux
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        print("❌ Error: OPENROUTER_API_KEY belum terpasang di terminal Termux Anda.")
        print("Silakan ketik: export OPENROUTER_API_KEY='key_anda'")
        sys.exit(1)
        
    repo_data = compile_ados_repository()
    
    # Menghubungkan ke OpenRouter Cloud API Gratis
    client = OpenAI(
        base_url="https://openrouter.ai",
        api_key=api_key
    )
    
    print("[ADOS-DOCTOR] Mengirimkan data repositori ke OpenRouter Cloud untuk audit medis...")
    
    prompt = (
        f"Anda adalah ADOS-Doctor Agent. Berikut adalah laporan kondisi internal repositori ADOS-Core:\n\n"
        f"{repo_data}\n\n"
        "Tugas Anda:\n"
        "1. Analisis apakah struktur folder di atas sudah mematuhi Arsitektur 5-Lapisan Bersih (Presentation, Kernel, Knowledge, Reasoning, Execution).\n"
        "2. Deteksi apakah ada berkas yang salah kamar atau ada potensi error 'Circular Import' (impor melingkar yang merusak bootstrap).\n"
        "3. Berikan rekomendasi langkah perbaikan teknis terperinci yang harus saya lakukan selanjutnya."
    )
    
    response = client.chat.completions.create(
        model="qwen/qwen-2.5-coder-32b-instruct:free",
        messages=[
            {"role": "system", "content": "Anda adalah dokter arsitektur software senior yang teliti dan terperinci. Berikan jawaban langsung ke poin masalah teknis menggunakan bahasa Indonesia."},
            {"role": "user", "content": prompt}
        ]
    )
    
    # Cetak hasil audit medis di layar terminal
    print("\n=======================================================")
    print(" 🏥 LAPORAN KESEHATAN TUBUH ADOS (ADOS DOCTOR REPORT) ")
    print("=======================================================")
    print(response.choices.message.content)
    print("=======================================================")

if __name__ == "__main__":
    run_diagnosis()
