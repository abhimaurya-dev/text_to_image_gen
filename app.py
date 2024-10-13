import torch
from flask import Flask, request, render_template, send_file
from diffusers import StableDiffusionPipeline
import os

app = Flask(__name__)

# Configuration
class Config:
    DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
    HEIGHT = 360
    WIDTH = 360
    NUM_INFERENCE_STEPS = 20
    GUIDANCE_SCALE = 7.5
    BATCH_SIZE = 1
    SAVE_PATH = "static/images/"

# Initialize Stable Diffusion Pipeline
pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4")
pipe = pipe.to(Config.DEVICE)

def generate_img(prompt):
    images = pipe([prompt], num_inference_steps=Config.NUM_INFERENCE_STEPS).images
    return images[0]

@app.route('/')
def home():
    return render_template('index.html')

# @app.route("/", methods=["GET", "POST"])
# def index():
#     if request.method == "POST":
#         prompt = request.form.get("prompt")
#         image = generate_image(prompt)
#         file_path = os.path.join(Config.SAVE_PATH, f"{prompt.replace(' ', '_')}.png")
        
#         # Save image to static/images directory
#         image.save(file_path)
        
#         return render_template("index.html", generated_image=file_path, prompt=prompt)
#     return render_template("index.html", generated_image=None)

@app.route('/generate', methods=['POST'])
def generate_image():
    prompt = request.form.get("prompt")
    
    image = generate_img(prompt)
    file_path = os.path.join(Config.SAVE_PATH, f"{prompt.replace(' ', '_')}.png")
    
    # Save image to static/images directory
    image.save(file_path)
    return send_file(file_path, mimetype='image/png')

@app.route("/download/<filename>")
def download_image(filename):
    file_path = os.path.join(Config.SAVE_PATH, filename)
    return send_file(file_path, as_attachment=True)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    os.makedirs(Config.SAVE_PATH, exist_ok=True)
    app.run(host='0.0.0.0', port=port, debug=True)
