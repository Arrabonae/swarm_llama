import requests

# Define the URL of your running web UI
url = "http://127.0.0.1:7860/sdapi/v1/txt2img"  # Change to your local IP if needed

# Define the payload for the request
payload = {
    "prompt": "A fantasy landscape with mountains and a sunset",
    "negative_prompt": "",
    "width": 512,
    "height": 512,
    "samples": 1,
    "seed": None,
    "num_inference_steps": 50,
    "guidance_scale": 7.5,
}

# Send a POST request to generate an image
response = requests.post(url, json=payload)

# Check if the request was successful
if response.status_code == 200:
    image_data = response.json()
    # Save or process the generated image
    with open("output.png", "wb") as f:
        f.write(requests.get(image_data['images'][0]).content)
else:
    print("Error:", response.status_code, response.text)