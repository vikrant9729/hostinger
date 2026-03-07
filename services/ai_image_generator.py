import requests
import uuid
import os

IMAGE_DIR = "uploads"
os.makedirs(IMAGE_DIR, exist_ok=True)

def generate_image(prompt):

    try:

        prompt = prompt.replace(" ", "%20")

        url = f"https://image.pollinations.ai/prompt/{prompt}"

        response = requests.get(url, timeout=30)

        if response.status_code != 200:
            return None

        file_name = str(uuid.uuid4()) + ".png"
        file_path = os.path.join(IMAGE_DIR, file_name)

        with open(file_path, "wb") as f:
            f.write(response.content)

        return f"/uploads/{file_name}"

    except Exception as e:

        print("IMAGE ERROR:", e)

        return None