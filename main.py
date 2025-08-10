from agents.ResumePreProcessingAgent import ResumePreProcessingAgent
from agents.JobDescriptionAgent import JobDescriptionAgent
import os
from llm.llmModel import get_model_client
from dotenv import load_dotenv
import typing
load_dotenv()

import asyncio
model_client = get_model_client()
file_path = "path/to/resume.pdf"  # Update with the actual path to the resume file
kwargs = {
    "supported_file_types": ["pdf", "docx", "txt"],
    "output_format": "json",
    "max_file_size": 10 * 1024 * 1024,  # 10 MB
    "language": "en"
}

# agent = ResumePreProcessingAgent(model_client, file_path, kwargs)
# assistant_agent = agent.getAssistantAgent()

agent = JobDescriptionAgent(model_client=model_client,
                             isFile=False)  # Set isFile to True if you want to process a file
assistant_agent = agent.GetJobDescriptionAgent()
# Update with the actual path to the job description file
print(f"Agent Name: {assistant_agent.name}")
print(f"Description: {assistant_agent.description}")

async def main(): 
    result = await assistant_agent.run(task = 
                                    """Extract the job description from the provided text and return a json object with 
                                    with Requirements and Qualifications as keys and the values as  json Object" \
                                    . Here is the job description text:' \
    'We are seeking a highly skilled and motivated GenAI and Agent Developer to join our growing AI team. The ideal candidate is a strong programmer with a deep understanding of software development life cycle (SDLC), and has hands-on experience building, integrating, and optimizing Generative AI and agent-based systems. This is an individual contributor role requiring strong ownership, fast execution, and the ability to deliver high-quality outcomes independently.

What You’ll Do 
Design, develop, and deploy GenAI applications and autonomous agents using modern AI frameworks.
Integrate LLMs (e.g., GPT-4, Claude, Mistral) into products or workflows.
Build robust, scalable, and efficient backend components to support GenAI features.
Work with prompt engineering, tool usage, and memory management for agents.
Participate in the full SDLC process: requirements analysis, design, implementation, testing, deployment, and maintenance.
Write clean, modular, well-documented, and testable code.
Troubleshoot, debug, and optimize systems for performance and scalability.
Collaborate closely with cross-functional teams including product, design, and QA.
Experience in End-to-End implementation/POCS in Agentic AI framework

What You Bring 
Programming Languages: Strong proficiency in Python (primary), with good command of OOP and design patterns.
GenAI Frameworks: Experience with LangChain, LlamaIndex, or similar agent orchestration libraries.
LLM Integration: Hands-on experience working with OpenAI, Anthropic, or similar APIs.
Prompt Engineering: Proven ability to write and optimize effective prompts.
SDLC Awareness: Strong understanding of software development methodologies, version control (Git), CI/CD, and agile processes.
Problem Solving: Strong analytical and debugging skills.
Independence: Ability to work independently, manage tasks, and deliver under tight timelines.
Experience building RAG (Retrieval Augmented Generation) systems.
Exposure to vector databases (e.g., FAISS, Pinecone, Weaviate).
Familiarity with containerization (Docker, Kubernetes).
Knowledge of cloud platforms (AWS/GCP/Azure) and deployment of GenAI models at scale.
Experience with front-end technologies (React.js, Next.js) for building interactive GenAI apps.
Exposure to MLOps/LLMops or tools like MLflow, Weights & Biases.
Experience working with knowledge graphs or semantic search systems.
Background in NLP or machine learning fundamentals.

What We Offer
At Newpage, we’re building a company that works smart and grows with agility—where driven individuals come together to do work that matters. We offer:
A people-first culture – Supportive peers, open communication, and a strong sense of belonging. § Smart, purposeful collaboration – Work with talented colleagues to create technologies that solve meaningful business challenges.
Balance that lasts – We respect your time and support a healthy integration of work and life.
Room to grow – Opportunities for learning, leadership, and career development, shaped around you.
Meaningful rewards – Competitive compensation that recognizes both contribution and potential.',
                                    """   )

    print(result.messages)

if (__name__ == "__main__"):
    asyncio.run(main())