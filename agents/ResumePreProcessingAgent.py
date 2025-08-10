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
        return AssistantAgent(
            name=self.name,
            system_message="" \
            "You are a resume pre-processing agent. Your task is to extract and process information from resumes. You can handle various file formats and perform necessary transformations." \
            "You should ensure that the extracted information is accurate and well-structured as json format. From the text extracted by the tools" \
            "You should extract the name, contact information, skills, work experience, and education details from the resume." \
            "You should also ensure that the extracted information is accurate and well-structured as json format",
            tools=self.tools,
            description=self.description,
            model_client=self.model_client,
            reflect_on_tool_use=True,
        )
