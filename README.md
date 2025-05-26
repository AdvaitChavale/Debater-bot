🧠 Debater Chatbot
A multi-persona debater chatbot powered by OpenRouter's API. Users can start timed debates with up to three AI debaters, each following a unique speaking style and persona.

📁 Project Structure
graphql
Copy
Edit
debater/
│
├── main.py                      # FastAPI backend with OpenRouter integration
├── requirements.txt             # Python dependencies
│
├── static/
│   ├── index.html               # Frontend UI (HTML + JS)
│   ├── style.css                # Custom styling
│   └── script.js                # Handles frontend logic and API calls
│
└── README.md                    # Project documentation
⚙️ Prerequisites
✅ 1. Python (3.8 or higher recommended)
Install from https://www.python.org/downloads/

✅ 2. Install dependencies
Use a virtual environment (optional but recommended):

bash
Copy
Edit
python -m venv venv
source venv/bin/activate      # On Linux/macOS
venv\Scripts\activate         # On Windows
Then install required packages:

bash
Copy
Edit
pip install -r requirements.txt
requirements.txt should include:

nginx
Copy
Edit
fastapi
uvicorn
httpx
python-dotenv  # optional if using .env for API keys
✅ 3. OpenRouter API Key
Sign up at https://openrouter.ai and get your API key.

You can either:

Store it in an environment variable:

bash
Copy
Edit
export OPENROUTER_API_KEY=your_key_here       # macOS/Linux
set OPENROUTER_API_KEY=your_key_here          # Windows CMD
Or hardcode it (not recommended for production) inside main.py:

python
Copy
Edit
api_key = os.getenv("OPENROUTER_API_KEY") or "your_key_here"
🚀 Running the App
From the project root directory:

bash
Copy
Edit
uvicorn main:app --reload
Open your browser and go to:

cpp
Copy
Edit
http://127.0.0.1:8000
💬 Features
Choose 1–3 AI debaters

Set custom debate topics

Adjust debate time (2–10 minutes)

Debaters speak in turns with 4-sentence limits

Each debater has an intro and conclusion phase

Based on real-time API calls to OpenRouter

🔒 Notes
This app uses httpx for async requests to OpenRouter

Make sure your OpenRouter usage is within your token limits

You can replace the model name (mistral, gpt-3.5, etc.) in main.py based on available models

