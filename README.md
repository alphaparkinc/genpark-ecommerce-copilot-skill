# genpark-ecommerce-copilot-skill

> **GenPark AI Agent Skill** -- # E-Commerce Visuals & Catalog Enrichment Copilot Skill

This repository contains the **E-Commerce Visuals & Catalog Enrichment Copilot Skill** — a modular developer Python client SDK wrapper, agent skill definition, and runnable example workflows designed to automate the generation of high-quality product images, model try-on visual changes, background scene adjustments, and localized catalog SEO copywriting translation.

---

## 🚀 Capabilities

* **AI Visual Modeling Tasks:** Automatically apply models onto clothing items, switch background scenes for lifestyle branding, remove backgrounds, or scale image resolution.
* **Localized Catalog Translations:** Translate listing content (Title, Bullet Points, Descriptions) into target regional languages while dynamically restructuring layout details according to local SEO guidelines.
* **Agent Integration Interface:** Expose structured inputs and outputs (`skill.json`) that allow other AI agents to execute product catalog enrichment autonomously.

---

## 🛠️ Setup & Installation

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Configuration:
   Set your API environment variables if executing requests against the live production server (otherwise, client executes in mock mode):
   * **PowerShell**:
     ```powershell
     $env:ECOM_COPILOT_API_KEY="your_api_key"
     ```
   * **bash**:
     ```bash
     export ECOM_COPILOT_API_KEY="your_api_key"
     ```

---

## 💻 SDK Usage Reference

```python
from ecommerce_copilot import EcommerceCopilotClient

# Initialize Client (runs in mock mode without API key)
client = EcommerceCopilotClient(api_key="your_api_key")

# Perform Model Try-on visual replacement
visual_resp = client.generate_visual_task(
    image_url="https://images.example.com/sweater.jpg",
    task="model_tryon",
    demographic="US Gen-Z"
)
print(visual_resp["output_image"])

# Perform local listing rewrite & translation
optimized = client.optimize_listing(
    title="Minimalist Merino Wool Sweater",
    bullets=["100% fine merino wool", "Thermal regulation warmth"],
    description="Beautiful wool sweater.",
    target_languages=["ja", "de"]
)
```

---

## 📜 License
This project is licensed under the MIT License.