from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import PyPDF2
from docx import Document
import os

app = FastAPI(title="NPTEL Smart Assistant - Production Ready")

# Production Fix - CORS (Vercel + Render ke liye must hai)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB limit

def extract_text(file, filename):
    text = ""
    if filename.endswith(".pdf"):
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() or ""
    elif filename.endswith(".docx"):
        doc = Document(file)
        text = "\n".join([p.text for p in doc.paragraphs])
    else:
        raise HTTPException(status_code=400, detail="Only PDF and DOCX allowed")
    return text

@app.get("/")
def home():
    return {"status": "NPTEL Assistant is LIVE", "version": "1.0"}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    # Debugging 1: File check
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file selected")
    
    # Debugging 2: Size check
    contents = await file.read()
    if len(contents) > MAX_FILE_SIZE:
        raise HTTPException(status_code=413, detail="File too large (Max 10MB)")
    
    # Debugging 3: Extension check
    if not (file.filename.endswith(".pdf") or file.filename.endswith(".docx")):
        raise HTTPException(status_code=400, detail="Upload PDF or DOCX only")

    try:
        # Reset file pointer after reading size
        await file.seek(0)
        # For this demo, we will extract
        # Real extraction needs file-like object handling
        text = file.filename + " processed"
        
        # Production: Actual extraction
        # text = extract_text(file.file, file.filename)
        
        summary = text[:500] + "..." # Demo summary
        hindi_translation = "Ye NPTEL lecture ka Hindi anuvaad hai (Demo)"
        
        return {
            "filename": file.filename,
            "summary": summary,
            "translation": hindi_translation,
            "status": "success"
        }
    except Exception as e:
        # Production Logging
        print(f"ERROR: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Server Error: {str(e)}")
