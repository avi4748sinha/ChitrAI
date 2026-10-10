ChitrAI 🎨

<p align="center">
  <img src="frontend/public/chitrai-logo.png" alt="ChitrAI Logo" width="400"/>
</p><p align="center">
  <b>Generative AI Image Studio</b>
</p>ChitrAI is an AI-powered image generation web application that transforms text prompts into images using Cloudflare Workers AI.

✨ Features

- Generate images from text prompts.
- Preview generated images directly in the web interface.
- Handle loading states and API errors.
- React frontend connected to a FastAPI backend.

🛠️ Tech Stack

- Frontend: React.js
- Backend: Python, FastAPI, Pydantic
- AI Model: Cloudflare Workers AI — FLUX.1 Schnell
- Other: REST APIs, CORS, Git, GitHub

⚙️ How It Works

1. Enter a text prompt in the React interface.
2. The FastAPI backend sends the prompt to Cloudflare Workers AI.
3. The generated image is returned to the frontend and displayed.

🚀 Getting Started

1. Clone the repository.
2. Install frontend and backend dependencies.
3. Configure Cloudflare credentials in the backend ".env" file.
4. Start the FastAPI backend and React frontend.

Note: Never commit API tokens or secrets to GitHub.

👨‍💻 Author

Avinash Sinha
