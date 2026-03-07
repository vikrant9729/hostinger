from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from app.api.sections import router as section_router
from app.api.publish import router as publish_router
from app.api.generate import router as generate_router
from app.api.ai_sections import router as ai_section_router
from app.api.auth import router as auth_router
from fastapi.staticfiles import StaticFiles
from app.api.websites import router as website_router
from app.middleware.subdomain_router import subdomain_router
from app.api.ai_images import router as ai_image_router
from app.api.ai_generate_site import router as ai_site_router
from app.api.sites_api import router as sites_router
import os
from app.services.ai_section_modifier import modify_section_with_ai

app = FastAPI()

# uploads folder auto create
os.makedirs("uploads", exist_ok=True)

# CORS enable
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")
app.mount("/published", StaticFiles(directory="published"), name="published")
app.mount("/sites", StaticFiles(directory="sites"), name="sites")
app.include_router(section_router)
app.include_router(publish_router)
app.include_router(auth_router)
app.include_router(ai_section_router)
app.include_router(website_router)
app.middleware("http")(subdomain_router)
app.include_router(generate_router)
app.include_router(ai_image_router)
app.include_router(ai_site_router)

@app.post("/edit-with-ai")
async def edit_with_ai(data: dict):
    html = data.get("html")
    instruction = data.get("prompt")
    modified_html = modify_section_with_ai(html, instruction)
    return {"html": modified_html}
