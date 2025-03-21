from crewai import Crew, Process
from direct_approach.agent_task import *
from dotenv import load_dotenv

load_dotenv()

research_crew = Crew(
    agents=[research_agent, summarization_agent, fact_checker_agent],
    tasks=[research_task, summarization_task, fact_checking_task],
    process=Process.sequential,
    verbose=True
)

result = research_crew.kickoff(inputs={"topic": "The impact of AI on job markets"})
print("\nFinal Verified Summary:\n", result)