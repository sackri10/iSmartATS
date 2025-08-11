from autogen_agentchat.agents import AssistantAgent
from autogen_core.tools import FunctionTool
from llm.llmModel import get_model_client

def GetSkillsEvaluationAgent():
    return AssistantAgent(
    name="Skills_Agent",
    model_client=get_model_client(),
    system_message="""You are an expert technical recruiter. Your task is to compare a list of required skills from a job description with a list of skills from a candidate's resume.
Analyze the two lists and determine how many of the required skills are present in the candidate's skills.

Return ONLY a single JSON object with the following structure. You MUST use these exact keys:
{
  "matched_skills": ["list of skills"],
  "missing_skills": ["list of skills"],
  "match_percentage": float  // A score from 0.0 to 100.0
}""",
    description="An agent that evaluates the skills of a candidate against a job description."
    )
