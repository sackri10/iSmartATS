from autogen_agentchat.agents import AssistantAgent
from autogen_core.tools import FunctionTool
class JobDescriptionAgent:
    def __init__(self, model_client,isFile: bool = False, FilePath: str = None):
        self.model_client = model_client
        self.isFile = isFile
        self.FilePath = FilePath
        self.tools = []
        self.initialize_tools()
    
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
            description="An agent that processes job descriptions to extract relevant information." \
            "It can handle various file formats and perform necessary transformations. " \
            "Identify key requirements and qualifications from the job description." \
            "If it is not a File Job Description Parameter will have the direct text else use tools which can extract the text based on the file_path that will be shared to the context" \
            "Once Job description is identified it will be used to extract the skills," \
            "experience and education details from qualifications and requirements from the job description as json object", 
            tools=self.tools,
            model_client=self.model_client,
            reflect_on_tool_use=True
            
        )