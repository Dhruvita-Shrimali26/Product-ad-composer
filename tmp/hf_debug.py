import os
import requests
from dotenv import load_dotenv

load_dotenv()

HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

def test_hf_api():
    if not HUGGINGFACE_API_KEY:
        print("❌ HUGGINGFACE_API_KEY not found in .env")
        return

    print(f"Testing with Key: {HUGGINGFACE_API_KEY[:6]}...{HUGGINGFACE_API_KEY[-4:]}")
    
    prompt = "A high-quality product photo of a luxury watch"
    payload = {"inputs": prompt, "options": {"wait_for_model": True}}
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY.strip()}"}
    
    # Testing different variations
    endpoints = [
        "https://router.huggingface.co/hf-inference/models/black-forest-labs/FLUX.1-schnell",
        "https://router.huggingface.co/hf-inference/v1/models/black-forest-labs/FLUX.1-schnell",
        "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-schnell", # Original to confirm
    ]

    for url in endpoints:
        print(f"\n--- Testing Endpoint: {url} ---")
        try:
            response = requests.post(url, headers=headers, json=payload, timeout=30)
            print(f"Status Code: {response.status_code}")
            print(f"Response: {response.text[:200]}")
        except Exception as e:
            print(f"Exception: {e}")

if __name__ == "__main__":
    test_hf_api()
