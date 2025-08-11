from agents.ResumePreProcessingAgent import ResumePreProcessingAgent
from agents.JobDescriptionAgent import JobDescriptionAgent
from agents.ATSScoringAgent.ATSSocietyOfMindAgent import GetATSScoringAgent
import os
from llm.llmModel import get_model_client
from dotenv import load_dotenv
import typing
load_dotenv()
import json

import asyncio
model_client = get_model_client()
file_path = "path/to/resume.pdf"  # Update with the actual path to the resume file
kwargs = {
    "supported_file_types": ["pdf", "docx", "txt"],
    "output_format": "json",
    "max_file_size": 10 * 1024 * 1024,  # 10 MB
    "language": "en"
}

agent = ResumePreProcessingAgent(model_client, file_path, kwargs)
assistant_agent = agent.getAssistantAgent()

#agent = JobDescriptionAgent(model_client=model_client,
#                            isFile=False)  # Set isFile to True if you want to process a file
#assistant_agent = agent.GetJobDescriptionAgent()
# Update with the actual path to the job description file
print(f"Agent Name: {assistant_agent.name}")
print(f"Description: {assistant_agent.description}")

async def main(): 
#     result = await assistant_agent.run(task = 
#                                     """Extract the job description from the provided text and 
#                                     return a json object with 
#                                     with 
#                                     1. Title (ex: "GenAI and Agent Developer, Full Stack Developer, Machine Learning Engineer, platform Engineer, etc"),
#                                     2. Experience (ex: 5+ years, 3-5 years, etc),
#                                     3. Individual Contributor or Team Lead Role 
#                                     4. Seniority Level (ex: Junior, Mid, Senior, etc)
#                                     5. Skills (ex: Python, GenAI, LLMs, etc)
#                                     6. Requirements (ex: Strong proficiency in Python, Experience with LangChain, etc)                                    
#                                     7. Educational Qualifications (ex: Bachelor's degree in Computer Science, etc)
#                                     8. Responsibilities (ex: Design, develop, and deploy GenAI applications, etc)
#                                     9. Keywords (ex: GenAI, Agent Developer, Python, etc)
#                                     as  json Object" \
#                                     . Here is the job description text:' \
#     'We are seeking a highly skilled and motivated GenAI and Agent Developer to join our growing AI team. The ideal candidate is a strong programmer with a deep understanding of software development life cycle (SDLC), and has hands-on experience building, integrating, and optimizing Generative AI and agent-based systems. This is an individual contributor role requiring strong ownership, fast execution, and the ability to deliver high-quality outcomes independently.

# What You’ll Do 
# Design, develop, and deploy GenAI applications and autonomous agents using modern AI frameworks.
# Integrate LLMs (e.g., GPT-4, Claude, Mistral) into products or workflows.
# Build robust, scalable, and efficient backend components to support GenAI features.
# Work with prompt engineering, tool usage, and memory management for agents.
# Participate in the full SDLC process: requirements analysis, design, implementation, testing, deployment, and maintenance.
# Write clean, modular, well-documented, and testable code.
# Troubleshoot, debug, and optimize systems for performance and scalability.
# Collaborate closely with cross-functional teams including product, design, and QA.
# Experience in End-to-End implementation/POCS in Agentic AI framework

# What You Bring 
# Programming Languages: Strong proficiency in Python (primary), with good command of OOP and design patterns.
# GenAI Frameworks: Experience with LangChain, LlamaIndex, or similar agent orchestration libraries.
# LLM Integration: Hands-on experience working with OpenAI, Anthropic, or similar APIs.
# Prompt Engineering: Proven ability to write and optimize effective prompts.
# SDLC Awareness: Strong understanding of software development methodologies, version control (Git), CI/CD, and agile processes.
# Problem Solving: Strong analytical and debugging skills.
# Independence: Ability to work independently, manage tasks, and deliver under tight timelines.
# Experience building RAG (Retrieval Augmented Generation) systems.
# Exposure to vector databases (e.g., FAISS, Pinecone, Weaviate).
# Familiarity with containerization (Docker, Kubernetes).
# Knowledge of cloud platforms (AWS/GCP/Azure) and deployment of GenAI models at scale.
# Experience with front-end technologies (React.js, Next.js) for building interactive GenAI apps.
# Exposure to MLOps/LLMops or tools like MLflow, Weights & Biases.
# Experience working with knowledge graphs or semantic search systems.
# Background in NLP or machine learning fundamentals.

# What We Offer
# At Newpage, we’re building a company that works smart and grows with agility—where driven individuals come together to do work that matters. We offer:
# A people-first culture – Supportive peers, open communication, and a strong sense of belonging. § Smart, purposeful collaboration – Work with talented colleagues to create technologies that solve meaningful business challenges.
# Balance that lasts – We respect your time and support a healthy integration of work and life.
# Room to grow – Opportunities for learning, leadership, and career development, shaped around you.
# Meaningful rewards – Competitive compensation that recognizes both contribution and potential.',
#                                     """   )
    # result = await assistant_agent.run(task =
    #                                     """Extract the resume text from the provided file at temp/resume.pdf and return a json object as per the schema""")
                                        

    # print(result.messages)
    resume_json_str = json.dumps({
        "Name": "Datta Sai Krishna Somesula", "MobileNumber": "9491407399", "EmailAddress": "sackri10@gmail.com",
        "Title": ".NET Full Stack Developer with Cloud Native Expertise", "ExperienceInYears": 10.5, "RoleType": "Team Lead", "SeniorityLevel": "Senior",
        "Skills": ["C#", "ASP.NET Core", ".NET", "SQL Server", "Angular", "Azure", "Microservices", "Kubernetes", "HTML5", "CSS3", "JavaScript", "TypeScript", "Entity Framework", "Docker", "Nodejs", "GenAI", "OpenAI", "LangChain", "LlamaIndex", "LLMs", "OOP", "SDLC", "LanggChain", "LlamaIndex", "OpenAI", "Anthropic", "Docker", "Kubernetes", "AWS", "GCP", "Azure", "React.js", "Next.js"],
        "KeyQualifications": ["Azure Developer Associate", "Azure AI Fundamentals", "Leadership in code reviews and team management", "Blogger on C# Corner"],
        "Education": "Bachelor of Technology in Computer Science (B.Tech) from G. Pulla Reddy Engineering College (2010-2014) with 8.18 CGPA",
        "WorkExperience": "Wells Fargo India Solutions Pvt Ltd: Responsible for requirement understanding, design and implementation of Common Level Angular Components and polling services. Managed Change Request Process and utilized Kubernetes with OpenShift for deployments. Led integration of Splunk Log and implemented Harness for deployment. Deloitte Consulting Pvt. Ltd: Led a team for design and implementation of framework level code. Developed Azure Functions and integrated Push Notifications. Familiar with Microservices architecture CQRS pattern. Infosys Ltd: Worked on business requirements analysis, table structure design, custom authorization in Web API, and offshore deployment support. Microsoft Client, Cloud and Enterprise Security Reliability Engineering: Conducted application support for security concerns, maintenance of servers, automation tool creation, and scheduled task automation."
    })

    jd_json_str = json.dumps({
        "Title": "GenAI and Agent Developer", "ExperienceInYears": "Not specified", "RoleType": "Individual Contributor", "SeniorityLevel": "Mid-Level",
        "Skills": ["Python", "OOP", "LangChain", "LlamaIndex", "OpenAI", "Anthropic", "LLMs", "Docker", "Kubernetes", "AWS", "GCP", "Azure", "React.js", "Next.js"],
        "KeyQualifications": ["Strong proficiency in Python", "Experience with LangChain, LlamaIndex", "Hands-on experience with OpenAI, Anthropic APIs", "Strong understanding of SDLC and methodologies", "Experience building RAG systems", "Exposure to vector databases", "Familiarity with containerization", "Knowledge of cloud platforms", "Experience with front-end technologies", "Exposure to MLOps/LLMops"],
        "Education": [], "WorkExperience": "Experience in End-to-End implementation/POCS in Agentic AI framework",
        "Responsibilities": ["Design, develop, and deploy GenAI applications and autonomous agents", "Integrate LLMs into products or workflows", "Build backend components to support GenAI features", "Work with prompt engineering, tool usage, and memory management", "Participate in the full SDLC process", "Write clean, modular, and testable code", "Troubleshoot, debug, and optimize systems", "Collaborate with cross-functional teams"],
        "keywords": ["GenAI", "Agent Developer", "Python", "SDLC", "LangChain", "LLMs", "Docker", "AWS", "React.js"]
    })

    # --- Initiate the Chat ---
    # The initial message contains all the data the manager needs to start the process.
    initial_task = f"""
    Please calculate the ATS score for the following resume and job description.

    **Resume JSON:**
    {resume_json_str}

    **Job Description JSON:**
    {jd_json_str}
    """
    ats_manager_agent = GetATSScoringAgent()
    ats_manager_agent_response = await ats_manager_agent.run(task=initial_task)
    print(ats_manager_agent_response.messages)


if (__name__ == "__main__"):
    asyncio.run(main())