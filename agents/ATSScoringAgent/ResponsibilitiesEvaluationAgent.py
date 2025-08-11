from autogen_agentchat.agents import AssistantAgent
from autogen_core.tools import FunctionTool
from llm.llmModel import get_model_client

def GetResponsibilitiesEvaluationAgent():
    return AssistantAgent(
    name="Responsibilities_Agent",
    model_client=get_model_client(),
       system_message="""You are an expert talent acquisition specialist. Your task is to analyze the alignment between the responsibilities of a job description and the accomplishments listed on a candidate's resume.
Calculate an overall alignment score from 0.0 to 1.0.

Return ONLY a single JSON object with the following structure. You MUST use these exact keys:
{
  "overall_alignment_score": float, // The alignment score from 0.0 to 1.0
  "summary": "A brief, one-sentence summary of the overall alignment."
}""",
    description="An agent that evaluates the responsibilities of a candidate against a job description."
    )
