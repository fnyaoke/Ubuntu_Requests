import requests
import os
from urllib.parse import urlparse

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Prompt user for image URL
    url = input("Please enter the image URL: ").strip()

    # Validate URL
    if not url.lower().startswith(("http://", "https://")):
        print("Invalid URL. Please provide a valid http(s) link.")
        return

    try:
        # Fetch image
        response = requests.get(url, stream=True, timeout=10)
        response.raise_for_status()  # Raise error if status code is not 200

        # Extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path) or "downloaded_image.jpg"

        # Ensure directory exists
        save_dir = "Fetched_Images"
        os.makedirs(save_dir, exist_ok=True)

        # Save image
        file_path = os.path.join(save_dir, filename)
        with open(file_path, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)

        # Success message
        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {file_path}\n")
        print("Connection strengthened. Community enriched.")

    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch image: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
