from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# FIX: Use absolute imports
from schemas import RecoveryPlan, UserInput
# FIX: Import the new, real workflow function
from agents import run_full_agent_workflow


app = FastAPI()
origins = [
    "http://localhost:5173",    # React dev server
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/run_agents", response_model=RecoveryPlan)
async def run_agents(user_input: UserInput):
    """
    Endpoint that runs the full multi-agent recovery workflow.
    """
    # FIX: Call the real workflow that uses the Gemini API
    # The function is synchronous (not async), so we call it directly.
    return run_full_agent_workflow(user_input)