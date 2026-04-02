import os
import requests
from dotenv import load_dotenv
import base64

load_dotenv()
NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY")

custom_prompt = "Professional high-end commercial photography of 3A Autocare Car Mat Honda City, Trendy, energetic, bold colors, vibrant pop-art style, studio lighting, 8k, highly detailed, sharp focus."

invoke_url = "https://ai.api.nvidia.com/v1/genai/black-forest-labs/flux.1-schnell"
headers = {"Authorization": f"Bearer {NVIDIA_API_KEY.strip()}", "Accept": "application/json"}
payload = {"prompt": custom_prompt, "width": 1024, "height": 1024, "seed": 0, "steps": 4}

response = requests.post(invoke_url, headers=headers, json=payload, timeout=120)
if response.status_code == 200:
    body = response.json()
    b64 = None
    if "artifacts" in body: 
        b64 = body["artifacts"][0].get("base64")
        print("Found artifacts")
    elif "data" in body: 
        b64 = body["data"][0].get("b64_json")
        print("Found data")
    
    if b64:
        print("Base64 string length:", len(b64))
        print("First 100 chars:", b64[:100])
        # decode 
        img_bytes = base64.b64decode(b64)
        print("Transformed to bytes, size:", len(img_bytes))
        with open("test_out.jpg", "wb") as f:
            f.write(img_bytes)
        print("Wrote test_out.jpg")
    else:
        print("No base64 found")
else:
    print("Error:", response.status_code, response.text)
