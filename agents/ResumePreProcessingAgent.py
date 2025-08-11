from autogen_agentchat.agents import AssistantAgent
from autogen_core.tools import FunctionTool

class ResumePreProcessingAgent():
    """
    Agent for pre-processing resumes.
    This agent is responsible for extracting and processing information from resumes.
    It can handle various file formats and perform necessary transformations.
    It uses tools to extract text and tables from resumes and can return the processed information in a structured format.
    This can include extracting name, contact information, skills, work experience, and education details from the resume.
    """

    def __init__(self,model_client, file_path,kwargs):
        self.model_client = model_client
        self.tools = []
        self.name = "ResumePreProcessingAgent"
        self.description = "An agent that processes resumes to extract relevant information. It can handle various file formats and perform necessary transformations." \
        "It uses tools to extract text and tables from resumes and can return the processed information in a structured format." \
        "This can include extracting name, contact information, skills, work experience, and education details from the resume."       
        self.file_path = file_path   
        self.supported_file_types = kwargs.get("supported_file_types", ["pdf", "docx", "txt"])
        self.output_format = kwargs.get("output_format", "json")
        self.max_file_size = kwargs.get("max_file_size", 10 * 1024 * 1024)
        self.language = kwargs.get("language", "en")
        self.pre_processing_steps = kwargs.get("pre_processing_steps", ["extract_text", "extract_tables"])
        self.post_processing_steps = kwargs.get("post_processing_steps", ["clean_data", "format_output"])
        self.status = "initialized"
        self.result = None
        self.error = None
        self.initialize_tools()
        self.system_prompt= """You are a specialized resume processing agent. Your primary task is to extract key information from resume text and structure it into a clean JSON format.

                        First, you MUST use the provided tools to get the text content from the resume file.

                        After you have the text, extract the following fields and format them as a single JSON object:
                        1.  **Name**: The full name of the candidate.
                        2.  **MobileNumber**: The candidate's mobile phone number.
                        3.  **EmailAddress**: The candidate's email address.
                        4.  **Title**: The most recent or prominent job title (e.g., "GenAI and Agent Developer", "Full Stack Developer").
                        5.  **ExperienceInYears**: Total years of professional experience. If "6+" is mentioned, interpret it as 6.5.
                        6.  **RoleType**: Infer if the role is primarily "Individual Contributor" or "Team Lead" based on the work description.
                        7.  **SeniorityLevel**: Infer the seniority level (e.g., "Junior", "Mid-Level", "Senior") based on the years of experience if not explicitly stated.
                        8.  **Skills**: A list of key technical skills (e.g., ["Python", "GenAI", "LLMs", "AWS"]).
                        9.  **KeyQualifications**: A list of the candidate's most important qualifications or strengths mentioned.
                        10. **Education**: A summary of educational qualifications (e.g., "Bachelor's degree in Computer Science").
                        11. **WorkExperience**: A summary of key roles and accomplishments from past jobs.

                        Ensure the final output is only the well-structured JSON and should not contain \n or white spaces.
                        """

       

    def initialize_tools(self):
        """Initialize tools required for resume processing."""
        from tools.PDFProcessingTool import extract_text_pdf
        from tools.DocxProcessingTool import extract_text_docx
      

        if self.file_path:
            if self.file_path.endswith('.pdf'):
                self.tools.append(FunctionTool(
                    extract_text_pdf,
                    description="Tool for processing PDF files to extract text and tables.",
                    
                ))
            elif self.file_path.endswith('.docx'):
                self.tools.append(FunctionTool(
                    extract_text_docx,
                    description="Tool for processing Word files to extract text."                    
                ))
            else:
                self.error = f"Unsupported file type: {self.file_path.split('.')[-1]}"
                self.status = "error"
                self.log(self.error)
    
    def getAssistantAgent(self):
        """Get the AssistantAgent instance for this ResumePreProcessingAgent."""
        return AssistantAgent (
            name=self.name,
            system_message=self.system_prompt,
            tools=self.tools,
            description=self.description,
            model_client=self.model_client,
            reflect_on_tool_use=True
        )