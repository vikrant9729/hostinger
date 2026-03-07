from fastapi import APIRouter
from app.services.ai_page_generator import generate_multi_page

router = APIRouter()

@router.post("/generate-site")
def generate(data: dict):
    prompt = data["prompt"]
    pages = generate_multi_page(prompt)
    
    return {
        "html": pages.get("home", ""),
        "pages": pages
    }
