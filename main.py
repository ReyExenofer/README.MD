mport logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agent import interaction_graph  # Custom agent
from state import InteractionState  # Custom state
from fastapi.middleware.cors import CORSMiddleware

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI()

# Add CORS middleware to allow requests from different origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=[""],  # You can replace '' with specific domains
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

# Initialize global state for tracking interactions
state = InteractionState()

# Define the request model to parse incoming chat messages
class ChatRequest(BaseModel):
    message: str

# Define the /chat POST endpoint
@app.post("/chat")
def chat(req: ChatRequest):
    global state
    try:
        result = interaction_graph.invoke({
            "input": req.message,
            "state": state
        })
        state = result
        return result
    except Exception as e:
        import traceback
        traceback.print_exc()
        return {"error": str(e)}


# Optional: Root endpoint for basic health check
@app.get("/")
async def root():
    return {"message": "FastAPI server is running"}
