from autogen_agentchat.agents import AssistantAgent, SocietyOfMindAgent
from .SkillsEvaluationAgent import GetSkillsEvaluationAgent 
from .ResponsibilitiesEvaluationAgent import GetResponsibilitiesEvaluationAgent
from .ATSManagerAgent import GetATSManagerAgent
from llm.llmModel import get_model_client
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination

def GetATSScoringAgent():


    inner_team = RoundRobinGroupChat([GetATSManagerAgent(), GetSkillsEvaluationAgent(), GetResponsibilitiesEvaluationAgent()],max_turns=10)

    return SocietyOfMindAgent(
    name="ATSScoringAgent",
    model_client=get_model_client(),
    team=inner_team,
    response_prompt="""You just need to return the final report as a single JSON object with the final score and any relevant details. what your inner team has returned to you.
    Do not attempt to calculate the score yourself. Your only job is to orchestrate the specialists""",
    description="An agent that manages the ATS scoring process by coordinating with specialized agents and calculating the final score."
    )