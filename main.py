import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import httpx
import asyncio
from pathlib import Path

app = FastAPI()

# Serve static folder if needed (optional)
app.mount("/static", StaticFiles(directory="static"), name="static")

API_KEY = "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"

PERSONAS = {
    "Alex": "a data-driven AI who uses statistics and verified research.",
    "Jamie": "a logical philosopher who values reason and debate rules.",
    "Sasha": "a compassionate thinker who respects human emotions and ethics.",
    "Riya": "an activist who is assertive and passionate about social issues.",
    "Ethan": "a calm mediator who highlights balance and harmony in arguments."
}

# Serve the HTML page
@app.get("/", response_class=HTMLResponse)
async def index():
    return Path("C:/Users/compu/Downloads/debater/static/index.html").read_text(encoding="utf-8")

async def query_openrouter(name: str, prompt: str) -> str:
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",
        "X-Title": "DebateBot"
    }
    payload = {
        "model": "deepseek/deepseek-r1:free",
        "messages": [
            {"role": "system", "content": f"You are {name}, {PERSONAS.get(name, '')}"},
            {"role": "user", "content": prompt}
        ]
    }
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.post(url, headers=headers, json=payload)
            resp.raise_for_status()
            data = resp.json()
            return data['choices'][0]['message']['content']
        except Exception as e:
            return f"⚠️ Error generating response for {name}: {e}"

@app.post("/start_debate")
async def start_debate(request: Request):
    data = await request.json()
    topic = data.get("topic", "")
    debaters = data.get("debaters", [])
    time_limit = int(data.get("time", 2))  # can use for timing logic if needed

    tasks = []
    for name in debaters:
        persona_desc = PERSONAS.get(name, "a knowledgeable debater.")
        prompt = (
            f"You are {name}, {persona_desc} Debate on the topic: '{topic}'. "
            f"Keep your reply to 4 sentences. Be respectful and informative."
        )
        tasks.append(query_openrouter(name, prompt))

    # Run all API calls concurrently
    results = await asyncio.gather(*tasks)

    # Format response
    response = [{"name": name, "text": text} for name, text in zip(debaters, results)]
    return JSONResponse(content=response)
