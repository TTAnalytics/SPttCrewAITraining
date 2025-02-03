from agenticos.connectors import BaseWorkflowConfig, CrewaiWorkflowConfig
from agenticos.node.models import AgenticConfig

workflows : dict[str,BaseWorkflowConfig] = {}

# Example workflow
# Import the Crew class. If you used the flow from CrewAI docs the following import should work
# If you are getting any erros please correct the import path
from database_extractor.crew import DatabaseExtractorCrew as Crew

# Define workflows here
# key is the workflow name
workflows["DATABASE_WORKFLOW"] = CrewaiWorkflowConfig(
    # Description of the workflow
    description="this workflow is a template workflow",
    # Inputs for the workflow
    inputs={"tablename": "The name of the table to look for",
            "schema": "Table schema"},
    # The crew class to be used
    crew_cls=Crew,
)

# Create the config object. Change the name to the name of your node
config = AgenticConfig(name="DATABASE_NODE", workflows=workflows)