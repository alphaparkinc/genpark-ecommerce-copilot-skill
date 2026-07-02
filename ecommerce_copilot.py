import os
import requests
from typing import List, Dict, Any, Optional

class EcommerceCopilotError(Exception):
    """Base exception class for E-Commerce Copilot Client."""
    pass

class EcommerceCopilotAPIError(EcommerceCopilotError):
    """Exception raised when the API returns an error response."""
    def __init__(self, status_code: int, message: str):
        super().__init__(f"API Error {status_code}: {message}")
        self.status_code = status_code
        self.message = message

class EcommerceCopilotClient:
    """
    Client for automating e-commerce visual enhancements and copy localization.
    Supports a mock mode for local testing.
    """
    def __init__(self, api_key: Optional[str] = None, base_url: str = "https://api.ecom-copilot.ai/v1"):
        self.api_key = api_key or os.environ.get("ECOM_COPILOT_API_KEY")
        self.base_url = base_url.rstrip("/")
        self.mock_mode = self.api_key is None or self.api_key == "mock"
        
        if self.mock_mode:
            print("[EcommerceCopilotClient] API Key not set. Running in MOCK Mode.")

    def _request(self, method: str, path: str, json_data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        if self.mock_mode:
            raise EcommerceCopilotError("Network request made in mock mode. Use specific mock return methods.")
        
        url = f"{self.base_url}/{path.lstrip('/')}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        try:
            resp = requests.request(method, url, json=json_data, headers=headers, timeout=30)
            if not (200 <= resp.status_code < 300):
                raise EcommerceCopilotAPIError(resp.status_code, resp.text)
            return resp.json()
        except requests.RequestException as e:
            raise EcommerceCopilotError(f"HTTP Request failed: {e}")

    def generate_visual_task(self, image_url: str, task: str, demographic: str) -> Dict[str, Any]:
        """
        Request AI visual model try-on or scene swapping.
        """
        if self.mock_mode:
            print(f"[Mock API] Generating '{task}' visual for {demographic} based on {image_url}")
            # Simulate a realistic response
            postfix = "model_applied" if task == "model_tryon" else "new_scene"
            return {
                "task_id": "job_vis_908123741",
                "status": "completed",
                "input_image": image_url,
                "output_image": f"https://cdn.ecom-copilot.ai/renders/{postfix}_result_0.jpg",
                "task_type": task,
                "demographic": demographic
            }
        
        payload = {
            "image_url": image_url,
            "task": task,
            "demographic": demographic
        }
        return self._request("POST", "/visuals/generate", payload)

    def optimize_listing(self, title: str, bullets: List[str], description: str, target_languages: List[str]) -> List[Dict[str, Any]]:
        """
        Optimize, rewrite, and translate catalog listings for specified markets.
        """
        if self.mock_mode:
            print(f"[Mock API] Translating and optimizing listing for: {target_languages}")
            results = []
            for lang in target_languages:
                if lang.lower() == "ja":
                    results.append({
                        "language": "ja",
                        "title": f"[NEW] {title} - Premium Grade",
                        "bullets": [f"[Premium Material] {b} - Built for lasting durability" for b in bullets],
                        "description": f" {description}"
                    })
                elif lang.lower() == "de":
                    results.append({
                        "language": "de",
                        "title": f"Premium {title} - Neuheit 2026",
                        "bullets": [f"Premium Qualität: {b}" for b in bullets],
                        "description": f"Entwickelt für höchste Ansprüche: {description}"
                    })
                else:
                    results.append({
                        "language": lang,
                        "title": f"Localized {title} in {lang}",
                        "bullets": [f"[{lang}] {b}" for b in bullets],
                        "description": f"[{lang}] Localized description: {description}"
                    })
            return results
        
        payload = {
            "title": title,
            "bullets": bullets,
            "description": description,
            "target_languages": target_languages
        }
        return self._request("POST", "/listings/localize", payload)["translations"]
