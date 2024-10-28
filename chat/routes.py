from fastapi import APIRouter
from chat.payloads import ChatDataModel
from database.config import remote_mongodb
from chat.agents import ToolBoundAgentBuilder

# Setup chatbot router
router = APIRouter(
    prefix="/chat",
    tags=["Sapphire Chat"],
)

# Setup database connection
db = remote_mongodb()


# --------------------------------
#             ROUTES
# --------------------------------


# Test router health
@router.get("/ping")
def test_router():
    return {
        "message": "Sapphire Chat router is up and running.",
    }


@router.post("/get-response/")
def get_response_from_chatbot(input: ChatDataModel):
    message = input.content
    agent = ToolBoundAgentBuilder()
    response = agent.invoke({"input": message})
    return {
        "data": response,
    }


# Make module safely exportable
if __name__ == "__main__":
    pass
