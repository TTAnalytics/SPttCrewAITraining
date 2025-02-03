from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
import os
from dotenv import load_dotenv
from database_extractor.tools import CustomSQLTool
from urllib.parse import quote


load_dotenv()

AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_API_BASE = os.getenv("AZURE_OPENAI_API_BASE")
AZURE_OPENAI_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")

llm_azure = LLM(
    model=f'azure/{AZURE_OPENAI_DEPLOYMENT}',  # The deployment name of your Azure OpenAI model
    base_url=AZURE_OPENAI_API_BASE,  # Azure API base URL
    api_version=AZURE_OPENAI_API_VERSION  # Azure API version
)

# slm = LLM(model="ollama/llama3", base_url="http://10.253.4.163:11434")

# Get database details from environment variables
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = quote(os.getenv("DB_PASSWORD"))
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
ODBC_DRIVER = os.getenv("ODBC_DRIVER")

# For SQL server connection
# Build the connection string

# if DB_PASSWORD:  # SQL Authentication
#      DATABASE_URL = (
#          f"mssql+pyodbc://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
#          f"?driver={ODBC_DRIVER.replace(' ', '+')}"
#      )
# else:  # Windows Authentication
#      DATABASE_URL = (
#          f"mssql+pyodbc://@{DB_HOST}/{DB_NAME}"
#          f"?driver={ODBC_DRIVER.replace(' ', '+')}&Trusted_Connection=yes"
#      )


# For Postgres SQL
DATABASE_URL = f"postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}?sslmode=prefer"

# Initialize the tool
sql_tool = CustomSQLTool(db_uri=DATABASE_URL)


@CrewBase
class DatabaseExtractorCrew():
    """Database extractor crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def database_extractor_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['database_extractor_agent'],
            allow_delegation=False,
            max_iter=3,
            tools=[sql_tool],
            verbose=True,
            llm=llm_azure
            )

    @task
    def database_extractor_task(self) -> Task:
        return Task(
            config=self.tasks_config['database_extractor_task']
            )

    @crew
    def crew(self) -> Crew:
        """Creates the Invoice crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            llm=llm_azure
            )
