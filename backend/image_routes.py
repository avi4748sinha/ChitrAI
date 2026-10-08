import os
import httpx
from dotenv import load_dotenv
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

load_dotenv()

# .env se Cloudflare ki details padhte hain
ACCOUNT_ID = os.getenv("CLOUDFLARE_ACCOUNT_ID")
API_TOKEN = os.getenv("CLOUDFLARE_API_TOKEN")
MODEL = "@cf/black-forest-labs/flux-1-schnell"

# Cloudflare ka URL, jahan prompt bhejna hai
URL = f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/{MODEL}"

router = APIRouter()


class GenerateRequest(BaseModel):
    prompt: str = Field(min_length=3, max_length=1000)


@router.post("/generate-image")
def generate_image(req: GenerateRequest):
    # Agar .env mein key nahi mili to saaf error do
    if not ACCOUNT_ID or not API_TOKEN:
        raise HTTPException(status_code=500, detail="Cloudflare keys .env mein nahi mili.")

    try:
        # Authorization header: token se Cloudflare ko pata chalta hai ki request kaun bhej raha hai
        response = httpx.post(
            URL,
            headers={"Authorization": f"Bearer {API_TOKEN}"},
            json={"prompt": req.prompt},
            timeout=60,  # image banane mein time lagta hai, 60 sec tak ruko
        )
    except httpx.HTTPError as e:
        raise HTTPException(status_code=502, detail=f"Cloudflare se connect nahi hua: {e}")

    # Cloudflare ne error bheja (jaise galat token) to wahi aage bhej do
    if response.status_code != 200:
        raise HTTPException(status_code=502, detail=f"Cloudflare error {response.status_code}: {response.text}")

    # Jawab ka shape: {"result": {"image": "<base64>"}, "success": true}
    image_b64 = response.json().get("result", {}).get("image")
    if not image_b64:
        raise HTTPException(status_code=422, detail="Image nahi mili. Prompt badal ke try karo.")

    return {"image_base64": image_b64, "mime_type": "image/jpeg"}