from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.ollama import Ollama
from agno.os import AgentOS
from agno.tools.calculator import CalculatorTools


# Create the Agent
agno_agent = Agent(
    name="Agno Agent",
    model=Ollama(id="qwen3:4b-instruct"),
    # Add a database to the Agent
    db=SqliteDb(db_file="agno.sqlite3"),
    # Add the Agno MCP server to the Agent
    tools=[CalculatorTools()],
    # Add the previous session history to the context
    add_history_to_context=True,
    markdown=True,
)


# Create the AgentOS
agent_os = AgentOS(agents=[agno_agent])
# Get the FastAPI app for the AgentOS
app = agent_os.get_app()
