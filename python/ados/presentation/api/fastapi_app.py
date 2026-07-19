import os
import socket
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from aider.coders import Coder
from aider.models import Model
from aider.io import InputOutput

app = FastAPI(title="ADOS Core API - Layer Presentation v2.0")
io_orchestrator = InputOutput(yes=True, silent=True)

class PseudocodeRequest(BaseModel):
    prompt: str
    target_files: list[str] = []

def is_online():
    """Sensor Jaringan: Cek koneksi internet HP via DNS Google"""
    try:
        socket.setdefaulttimeout(1.5)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("8.8.8.8", 53))
        return True
    except socket.error:
        return False

@app.post("/api/v1/execute")
async def execute_ados_pipeline(request: PseudocodeRequest):
    try:
        # 1. SMART-SWITCHING ENGINE (HYBRID CAPABILITY)
        if is_online() and os.environ.get("GEMINI_API_KEY"):
            mode_status = "ONLINE"
            print(f"[ADOS-API] Status: {mode_status}. Mengaktifkan Cloud: Gemini 2.5 Pro")
            selected_model = Model("gemini/gemini-2.5-pro")
        else:
            mode_status = "OFFLINE"
            print(f"[ADOS-API] Status: {mode_status}. Mengalihkan ke Lokal: Ollama (Qwen2.5-Coder)")
            selected_model = Model("ollama/qwen2.5-coder:1.5b")

        # 2. PROMPT BINDING UNTUK BAHASA MANUSIA / PSEUDOCODE
        system_instruction = (
            f"Anda adalah ADOS Core Engine dalam mode {mode_status}. "
            f"User memberikan instruksi pseudocode santai: '{request.prompt}'. "
            "Terjemahkan menjadi arsitektur kode bersih, tulis langsung pada file target, "
            "dan lakukan auto-commit. Jangan berikan pertanyaan balik teknis ke user."
        )

        # 3. INITIALIZE CODER VIA AIDER PYTHON API
        coder = Coder.create(
            main_model=selected_model,
            fnames=request.target_files,
            io=io_orchestrator
        )

        print(f"[ADOS-API] Mengerjakan file: {request.target_files}")
        coder.run(system_instruction)

        return {
            "status": "success",
            "network_mode": mode_status,
            "engine_active": selected_model.name,
            "message": "Pseudocode sukses dieksekusi ke dalam repositori."
        }

    except Exception as e:
        print(f"[ADOS-API-ERROR] Kegagalan sistem: {str(e)}")
        raise HTTPException(status_code=500, detail=f"ADOS Engine Error: {str(e)}")
