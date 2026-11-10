from fastapi import FastAPI
app = FastAPI(
    title="Conecta Novo Recreio API",
    description="API do sistema Conecta Novo Recreio",
    version="0.1.0"
)
@app.get("/")
def root():
    return {
        "message": "Conecta Novo Recreio API",
        "status": "online"
    }
@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
