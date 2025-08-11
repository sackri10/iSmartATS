from autogen_agentchat.agents import AssistantAgent
from autogen_core.tools import FunctionTool
class JobDescriptionAgent:
    def __init__(self, model_client,isFile: bool = False, FilePath: str = None):
        self.model_client = model_client
        self.isFile = isFile
        self.FilePath = FilePath
        self.tools = []
        self.initialize_tools()
        self.system_prompt = """You are an expert HR analyst and data extraction agent. Your sole purpose is to read a job description text and convert it into a structured JSON object using the provided schema.

Your ONLY output should be a single, valid JSON object. Do not include any other text, explanations, or markdown formatting.

Based on the job description text provided, extract the following information. You must map the job's requirements to the specified keys, even if the key names seem more suited for a resume.

- "Title": The job title being advertised.
- "ExperienceInYears": The required years of professional experience as a string (e.g., "5+ years", "3-5 years"). If not stated, use "Not specified".
- "RoleType": Identify if the role is for an "Individual Contributor" or "Team Lead".
- "SeniorityLevel": The seniority of the role (e.g., "Junior", "Mid-Level", "Senior"). Infer from the title and experience if not stated.
- "Skills": A list of the required technical skills and technologies for the job.
- "KeyQualifications": A list of the mandatory qualifications, skills, and experience required for the role.
- "Education": A summary of the required educational qualifications (e.g., "Bachelor's degree in Computer Science required"). If not mentioned, use an empty list [].
- "WorkExperience": A summary of the primary duties, tasks, and responsibilities for this role. **Map the job's responsibilities to this key.**
- "Responsibilities": A list of the main responsibilities associated with the job.
- "keywords": A list of important, searchable keywords derived from the title, skills, and responsibilities (e.g., ["GenAI", "Agent Developer", "Python", "SDLC"]).

Ensure the JSON is well-structured, with no extra spaces or new lines. The keys should match the schema exactly, and the values should be concise and relevant to the job description provided.
                """
    
    def initialize_tools(self):
        """Initialize tools required for job description processing."""
        from tools.DocxProcessingTool import extract_text_docx
        from tools.PDFProcessingTool import extract_text_pdf
        if self.isFile:
            if self.FilePath.endswith('.pdf'):
                self.tools.append(FunctionTool(
                    extract_text_pdf,
                    description="Tool for processing PDF files to extract text."
                ))
            elif self.FilePath.endswith('.docx'):
                self.tools.append(FunctionTool(
                    extract_text_docx,
                    description="Tool for processing Word files to extract text."
                ))
            else:
                raise ValueError(f"Unsupported file type: {self.FilePath.split('.')[-1]}")

    def GetJobDescriptionAgent(self):
        """Get the AssistantAgent instance for this JobDescriptionAgent."""
        """Process the job description and return a cleaned version."""
        return AssistantAgent(
            name="JobDescriptionAgent",
            system_message=self.system_prompt,
            description="An agent that processes job descriptions to extract relevant information." \
            "It can handle various file formats and perform necessary transformations. " \
            "Identify key requirements and qualifications from the job description." ,    
            
            tools=self.tools,
            model_client=self.model_client,
            reflect_on_tool_use=True
            
        )