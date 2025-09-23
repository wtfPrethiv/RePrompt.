from fastapi import APIRouter
from backend.app.schemas import Prompt
from backend.app.services import RePrompter


router = APIRouter()

@router.post('/reprompt')
def optimize_prompt(prompt: Prompt):
    reprompter = RePrompter(prompt.prompt, prompt.llm)
    
    opt_prompt = reprompter.RePrompt()
    
    return {'optimized_prompt': opt_prompt}