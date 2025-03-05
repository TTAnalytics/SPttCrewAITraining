# BaseCrew Crew

Welcome to the BaseCrew Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

### Prerequisite

Install the following before starting the project:

- Python >=3.10 <=3.13<br>
  url: https://www.python.org/downloads/
- git<br>
  url: https://git-scm.com/downloads/win
- vscode<br>
  url: https://code.visualstudio.com/download

### Setup Instructions

1. **Install `uv`:**

   ```bash
   pip install uv
   ```
   
2. **Install `pipx` and `crewai`:**

   Depending on the system you can try below commands with `python3` or `python`
   
   ```bash
   python3 -m pip install --user pipx
   python3 -m pipx ensurepath
   pipx install crewai
   ```

   **Note**: Errors while installing crewai:
   
   ![image](https://github.com/user-attachments/assets/b546bf69-61f4-4150-b6ba-19b52002e6d4)

   **Solution**:
   
   Download and install `Microsoft C++ Build Tools`:
  Url: https://visualstudio.microsoft.com/visual-cpp-build-tools/

   Installation settings:
      
   ![image](https://github.com/user-attachments/assets/120f2aa4-20db-4194-adf6-3cabaa5f6290)

   
4. **Clone the Repository:**

   ```bash
   git clone https://github.com/TTAnalytics/SPttCrewAITraining.git
   cd SPttCrewAITraining
   ```

5. **Install Dependencies:**

   ```bash
   crewai install
   pip install -e .
   ```

6. **Set Up Environment Variables:**

   Rename `.env.example` to `.env` and fill in the missing values. Most importantly, you need to add Azure OpenAI API keys and Database connection details.


### Customizing

**Add relevant environment variables into the `.env` file at root folder**

- Modify `src/database_extractor/config/agents.yaml` to define your agents
- Modify `src/database_extractor/config/tasks.yaml` to define your tasks
- Modify `src/database_extractor/crew.py` to add your own logic, tools and specific args
- Modify `src/database_extractor/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
crewai run
```

## Support

For support, questions, or feedback regarding the TvVideoBriefing Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI. Looking forward to the Training!
