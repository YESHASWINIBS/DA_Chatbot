from fastapi import FastAPI
import time
from routing_model import route_prompt
from cache import check_cache, save_cache
from logger import log_request
from llm import call_fast_model, call_capable_model

app = FastAPI()

@app.post("/chat")
def chat(prompt: str):
    start = time.time()

    cached = check_cache(prompt)
    if cached:
        log_request(prompt, "CACHE", "cache_hit", 0, True)
        return {"response": cached, "source": "cache"}

    model, confidence, reason = route_prompt(prompt)

    if model == "FAST":
        response = call_fast_model(prompt)
    else:
        response = call_capable_model(prompt)

    latency = time.time() - start

    save_cache(prompt, response)
    log_request(prompt, model, reason, latency, False)

    return {
        "response": response,
        "model_used": model,
        "confidence": confidence,
        "reason": reason,
        "latency": latency
    }