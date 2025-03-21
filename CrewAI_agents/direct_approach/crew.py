from crewai import Crew, Process  # Import Crew and Process classes from the crewai library
from direct_approach.agent_task import *  # Import all definitions from the agent_task module
from dotenv import load_dotenv  # Import the load_dotenv function from the dotenv library

load_dotenv()  # Load environment variables from a .env file

# Define the research crew
research_crew = Crew(
    agents=[research_agent, summarization_agent, fact_checker_agent],  # List of agents in the crew
    tasks=[research_task, summarization_task, fact_checking_task],  # List of tasks for the crew
    process=Process.sequential,  # Define the process as sequential
    verbose=True,  # Enable verbose mode for detailed output
)

# Kick off the research crew with a specific input
result = research_crew.kickoff(inputs={"topic": "The impact of AI on job markets"})
print("\nFinal Verified Summary:\n", result)  # Print the final verified summary