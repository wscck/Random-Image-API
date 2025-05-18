from flask import Flask, send_file
from flask import Flask, send_file
import os
import random

app = Flask(__name__)

IMAGE_FOLDER = "/app/images"
SUPPORTED_FORMATS = (".jpg", ".jpeg", ".png", ".webp", ".gif", ".bmp", ".tiff")

@app.route("/")
def get_random_image():
    images = [f for f in os.listdir(IMAGE_FOLDER) if f.lower().endswith(SUPPORTED_FORMATS)]
    if not images:
        return "No images found!", 404
    random_image = random.choice(images)
    mime_type = get_mime_type(random_image)
    return send_file(os.path.join(IMAGE_FOLDER, random_image), mimetype=mime_type)

def get_mime_type(filename):
    ext = filename.lower().split('.')[-1]
    return {
        "jpg": "image/jpeg",
        "jpeg": "image/jpeg",
        "png": "image/png",
        "webp": "image/webp",
        "gif": "image/gif",
        "bmp": "image/bmp",
        "tiff": "image/tiff"
    }.get(ext, "application/octet-stream")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


