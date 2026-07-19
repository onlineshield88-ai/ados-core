import os
import socket
import subprocess
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import OpenAI

app = FastAPI(title="ADOS - OpenRouter Agent Core v4.5")

class PseudocodeRequest(BaseModel):
    prompt: str
    target_files: list[str] = []

def is_online():
    """Sensor Sinyal: Pastikan internet HP aktif"""
    try:
        socket.setdefaulttimeout(1.5)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("8.8.8.8", 53))
        return True
    except socket.error:
        return False

def call_openrouter_agent(prompt: str, context_code: str):
    """Memanggil Otak AI Terkuat di Cloud OpenRouter secara GRATIS"""
    client = OpenAI(
        base_url="https://openrouter.ai",
        api_key=os.environ.get("OPENROUTER_API_KEY")
    )
    
    system_instruction = (
        "Anda adalah ADOS-Agent Utama (Kombinasi Coder & Reviewer). Tugas Anda adalah menerjemahkan "
        "instruksi pseudocode manusia menjadi kode pemrograman yang utuh, bersih, dan siap pakai. "
        "Tanggapi HANYA dengan kode pemrograman mentah yang valid tanpa penjelasan, "
        "tanpa kata pembuka, dan tanpa tanda petik tiga markdown (```)."
    )
    
    full_prompt = f"Struktur/Kode Saat Ini:\n{context_code}\n\nInstruksi Pseudocode Baru:\n{prompt}"
    
    # Menembak model koding open-source gratis terbaik di dunia saat ini
    response = client.chat.completions.create(
        model="qwen/qwen-2.5-coder-32b-instruct:free",
        messages=[
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": full_prompt}
        ]
    )
    return response.choices.message.content

@app.post("/api/v1/execute")
async def execute_ados_pipeline(request: PseudocodeRequest):
    try:
        if not os.environ.get("OPENROUTER_API_KEY"):
            raise HTTPException(status_code=500, detail="OPENROUTER_API_KEY belum terpasang di Termux.")

        # 1. Kumpulkan Konteks File Lama (Jika ada)
        context_code = ""
        for file_path in request.target_files:
            if os.path.exists(file_path):
                with open(file_path, 'r', encoding='utf-8') as f:
                    context_code += f"--- FILE: {file_path} ---\n{f.read()}\n"

        # 2. Eksekusi Menggunakan Kekuatan Cloud Bebas Lag HP
        if is_online():
            print("[ADOS-AGENT] Menghubungi OpenRouter Cloud Model...")
            generated_code = call_openrouter_agent(request.prompt, context_code)
            
            # Bersihkan teks kotor sisa AI jika ada
            clean_code = generated_code.replace("```python", "").replace("```", "").strip()

            # 3. Tulis Langsung ke File di Termux
            for file_path in request.target_files:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(clean_code)
                print(f"[ADOS-AGENT] Berhasil memperbarui file: {file_path}")
            
            # 4. Git Auto-Commit Otomatis ke GitHub
            try:
                subprocess.run(["git", "add", "."], check=True)
                subprocess.run(["git", "commit", "-m", f"[ADOS-AGENT] Fitur: {request.prompt[:30]}"], check=True)
                print("[ADOS-AGENT] Sukses melakukan Auto-Commit.")
            except Exception as git_err:
                print(f"[ADOS-GIT-WARN] Lewati commit: {git_err}")

            return {
                "status": "success",
                "message": "ADOS Agent sukses mengeksekusi perintah pseudocode Anda di Cloud!",
                "modified_files": request.target_files
            }
        else:
            raise HTTPException(status_code=503, detail="HP Anda sedang offline. Hubungkan ke internet untuk memakai OpenRouter Agent.")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"ADOS Agent Error: {str(e)}")
