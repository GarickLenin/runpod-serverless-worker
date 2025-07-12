# Start from the official Runpod image
FROM runpod/stable-diffusion:comfy-ui-6.0.0

# Copy your custom handler into the container, replacing the default one.
# This ensures your script with the download logic is used.
COPY Handler.py /app/src/handler.py