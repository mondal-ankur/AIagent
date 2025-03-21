from crewai import Agent, Task, LLM  # Import necessary classes from the crewai library
import yaml  # Import the yaml library for reading YAML configuration files
from crewai_tools import SerperDevTool  # Import a custom tool for web search

# Instantiate the SerperDevTool
serper_dev_tool = SerperDevTool()

# Load YAML Configuration
with open("direct_approach\config.yaml", "r") as file:
    config = yaml.safe_load(file)

# Define the Large Language Model (LLM)
llm = LLM(
    model="gemini/gemini-2.0-flash-lite",
    temperature=0.7,
)

# Define Agents and Corresponding Tasks

######### research_agent #########

research_agent = Agent(
    role=config["agents"]["research_agent"]["role"],
    goal=config["agents"]["research_agent"]["goal"],
    backstory=config["agents"]["research_agent"]["backstory"],
    tools=[serper_dev_tool],
    llm=llm,
    verbose=True,
)

research_task = Task(
    description=config["tasks"]["research_task"]["description"],
    agent=research_agent,
    tools=[serper_dev_tool],
    expected_output=config["tasks"]["research_task"]["expected_output"],
)

######### summarization_agent #########

summarization_agent = Agent(
    role=config["agents"]["summarization_agent"]["role"],
    goal=config["agents"]["summarization_agent"]["goal"],
    backstory=config["agents"]["summarization_agent"]["backstory"],
    llm=llm,
    verbose=True,
)

summarization_task = Task(
    description=config["tasks"]["summarization_task"]["description"],
    agent=summarization_agent,
    expected_output=config["tasks"]["summarization_task"]["expected_output"],
)

######### fact_checker_agent #########

fact_checker_agent = Agent(
    role=config["agents"]["fact_checker_agent"]["role"],
    goal=config["agents"]["fact_checker_agent"]["goal"],
    backstory=config["agents"]["fact_checker_agent"]["backstory"],
    tools=[serper_dev_tool],
    llm=llm,
    verbose=True,
)

fact_checking_task = Task(
    description=config["tasks"]["fact_checking_task"]["description"],
    agent=fact_checker_agent,
    tools=[serper_dev_tool],
    expected_output=config["tasks"]["fact_checking_task"]["expected_output"],
)