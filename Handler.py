import subprocess
import os
import runpod

# Read the API key from the environment variable you set in Runpod
civitai_api_key = os.getenv("CIVITAI_API_KEY")

# Create the authorization header string if the key exists
auth_header = ""
if civitai_api_key:
    auth_header = f"--header='Authorization: Bearer {civitai_api_key}'"
    print("Civitai API Key found. Using for downloads.")

# List of files to download
files_to_download = {
    "/workspace/ComfyUI/models/checkpoints/JANKU.safetensors": "https://civitai.com/api/download/models/1772645",
    "/workspace/ComfyUI/models/loras/Disney.safetensors": "https://civitai.com/api/download/models/1416874",
    "/workspace/ComfyUI/models/loras/Niji.safetensors": "https://civitai.com/api/download/models/1896419",
    "/workspace/ComfyUI/models/loras/Incase.safetensors": "https://civitai.com/api/download/models/1189052",
    "/workspace/ComfyUI/models/loras/Offset.safetensors": "https://civitai.com/api/download/models/151806",
    "/workspace/ComfyUI/models/loras/SPO.safetensors": "https://civitai.com/api/download/models/567119",
    "/workspace/ComfyUI/models/embeddings/lazyNeg.safetensor": "https://civitai.com/api/download/models/1860747",
    "/workspace/ComfyUI/models/embeddings/cr1sp.safetensor": "https://civitai.com/api/download/models/1942120",
    "/workspace/ComfyUI/models/embeddings/lazyPos.safetensor": "https://civitai.com/api/download/models/1833157",
    "/workspace/ComfyUI/models/embeddings/f4st.safetensor": "https://civitai.com/api/download/models/1853982",
}

# The download logic now includes the authorization header
for path, url in files_to_download.items():
    if not os.path.exists(path):
        directory = os.path.dirname(path)
        filename = os.path.basename(path)
        # The {auth_header} is added to the command
        command = f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M {auth_header} '{url}' -d '{directory}' -o '{filename}'"
        
        print(f"Downloading {filename}...")
        subprocess.run(command, shell=True, check=True)

# The rest of your handler remains the same
def handler(job):
    print("Job passed to pre-running ComfyUI instance.")
    return {"message": "Job handled by ComfyUI."}

runpod.serverless.start({"handler": handler})