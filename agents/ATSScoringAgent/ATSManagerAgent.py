from autogen_agentchat.agents import AssistantAgent
from autogen_core.tools import FunctionTool
from tools.ATSScoreTool import calculate_final_score
from llm.llmModel import get_model_client

def GetATSManagerAgent():
    return AssistantAgent(
    name="ATS_Manager_Agent",
    model_client=get_model_client(),
    system_message="""You are the manager of an ATS scoring team. Your goal is to get a final ATS score for a resume and job description.
    Follow these steps precisely:
    1. First, ask the Skills_Agent to perform its analysis.
    2. Second, ask the Responsibilities_Agent to perform its analysis.
    3. Once you have the JSON outputs from both agents, you MUST call the `calculate_final_score` tool. Provide all four required JSON strings to this tool.
    4. The tool will return the final report. Present this final report as your concluding answer.
    Do not attempt to calculate the score yourself. Your only job is to orchestrate the specialists and the calculator tool.
    Ensure your final output is a single JSON object with the final score and any relevant details. returned from the tool.""",
    description="An agent that manages the ATS scoring process by coordinating with specialized agents and calculating the final score.",
    tools=[FunctionTool(
        calculate_final_score,
        description="Tool to calculate the final ATS score based on the outputs from Skills_Agent and Responsibilities_Agent."
    )],reflect_on_tool_use=False
    )
