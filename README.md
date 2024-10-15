# Text-to-Image Generator

This is a web-based application that generates images based on user-provided text prompts using Stable Diffusion. The project is built using Flask for the backend and a frontend interface built with HTML, CSS, and JavaScript. It is deployed on Google Cloud Platform (GCP) using Cloud Run.

## Features

- Text-to-image generation using the state-of-the-art **Stable Diffusion** model.
- Responsive frontend with a clean user interface.
- **Loader animation** to indicate progress while the image is being generated.
- Ability to download the generated image.
- Deployed using **Google Cloud Platform**'s **Cloud Run** for scalability.

## Technologies Used

- **Backend**: Flask (Python), Stable Diffusion (via Hugging Face Diffusers library)
- **Frontend**: HTML, CSS, JavaScript
- **Deployment**: Google Cloud Platform (Cloud Run), Docker, Docker Hub

## Model

The Stable Diffusion model was selected for its ability to generate high-quality images from textual descriptions. It is integrated into the project using the Hugging Face Diffusers library. The model runs on a GPU when available, which speeds up image generation.

## Project Structure

```bash
.
├── app.py
├── static
│   ├── images
│   ├── styles.css
├── templates
│   └── index.html
├── Dockerfile
├── README.md
└── requirements.txt
```

## Usage

### Local Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/abhimaurya-dev/text_to_image_gen.git
   cd text_to_image_gen
   ```

2. Create a virtual environment and install dependencies:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Run the Flask app:

   ```bash
   python app.py
   ```

4. Open your browser and navigate to `http://localhost:8080` to use the application.

### Local Setup (Alternative with Docker)

1. Ensure you have Docker Engine installed. You can download it from [Docker's official website](https://www.docker.com/get-started).
2. Pull the Docker image:
   ```bash
   docker pull abhimauryadev/text_to_image_gen-main:tagname
   ```
3. Run the Docker container:
   ```bash
   docker run --gpus all -p 8080:8080 abhimauryadev/text_to_image_gen-main:tagname
   ```
4. Open your browser and navigate to `http://localhost:8080` to use the application.

### Cloud Deployment

The project is deployed on **Google Cloud Run** using **Docker Hub** for image storage. Below are the steps for deployment:

1. **Dockerize the Application**:

   - A Dockerfile is included in the project. Use it to build the Docker image:
     ```bash
     docker build -t text-to-image-generator .
     ```

2. **Push the Docker Image** to Docker Hub:

   ```bash
   docker tag text_to_image_gen-main:tagname your-dockerhub-username/text_to_image_gen-main:tagname
   docker push your-dockerhub-username/text_to_image_gen-main:tagname
   ```

3. **Deploy on Cloud Run**:

   - Google Cloud Run pulls the image from Docker Hub and hosts it:
     ```bash
     gcloud run deploy --image docker.io/your-dockerhub-username/text_to_image_gen-main:tagname --platform managed
     ```

4. Your application will now be live on Cloud Run. Access the deployed app using the provided URL.

## Acknowledgements

- [Stable Diffusion](https://huggingface.co/CompVis/stable-diffusion-v1-4)
- [Hugging Face Diffusers](https://huggingface.co/docs/diffusers/index)
- [Google Cloud Run](https://cloud.google.com/run)
