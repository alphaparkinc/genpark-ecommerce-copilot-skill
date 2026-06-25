import sys
from ecommerce_copilot import EcommerceCopilotClient

def main():
    # Reconfigure stdout to use UTF-8 to prevent UnicodeEncodeError on Windows terminals
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
        
    print("=== E-Commerce Copilot Client Example ===")
    
    # Initialize client in mock mode
    client = EcommerceCopilotClient()
    
    # 1. Trigger Visual Generation (Model Try-on)
    print("\n--- Testing Visual Generation: Model Try-on ---")
    visual_resp = client.generate_visual_task(
        image_url="https://images.example.com/products/sweater-flat.jpg",
        task="model_tryon",
        demographic="US Gen-Z"
    )
    print("Response payload:")
    for k, v in visual_resp.items():
        print(f"  {k}: {v}")

    # 2. Localize listing
    print("\n--- Testing Listing Localization/SEO Optimization ---")
    optimized = client.optimize_listing(
        title="Modern Minimalist Wool Sweater",
        bullets=[
            "100% fine merino wool construction",
            "Ethically sourced materials and fabrics",
            "Designed for breathability and thermal warmth"
        ],
        description="A beautiful modern minimalist wool sweater suited for all seasonal styles.",
        target_languages=["ja", "de"]
    )
    
    for item in optimized:
        print(f"\nTarget Language: {item['language']}")
        print(f"  Optimized Title: {item['title']}")
        print("  Bullet Points:")
        for b in item['bullets']:
            print(f"    - {b}")
        print(f"  Description: {item['description']}")

if __name__ == "__main__":
    main()

