from crewai import Agent, Crew, Task, Process, LLM
from crewai.project import CrewBase, agent, task, crew
from crewai_tools import SerperDevTool
from research_crew import ResearchCrew
from dotenv import load_dotenv

load_dotenv()

@CrewBase
class ResearchCrew:
    """A crew for conducting research, summarizing findings, and fact-checking"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    def __init__(self, llm):
        self.search_tool = SerperDevTool()
        self.llm = llm

    @agent
    def research_agent(self) -> Agent:
        return Agent(config=self.agents_config['research_agent'],
                     llm=self.llm,
                     tools=[self.search_tool])

    @agent
    def summarization_agent(self) -> Agent:
        return Agent(config=self.agents_config['summarization_agent'],
                     llm=self.llm)

    @agent
    def fact_checker_agent(self) -> Agent:
        return Agent(config=self.agents_config['fact_checker_agent'],
                     llm=self.llm,
                     tools=[self.search_tool])

    @task
    def research_task(self) -> Task:
        return Task(config=self.tasks_config['research_task'],
                    tools=[self.search_tool])

    @task
    def summarization_task(self) -> Task:
        return Task(config=self.tasks_config['summarization_task'])

    @task
    def fact_checking_task(self) -> Task:
        return Task(config=self.tasks_config['fact_checking_task'],
                    tools=[self.search_tool])

    @crew
    def crew(self) -> Crew:
        return Crew(agents=self.agents,
                    tasks=self.tasks,
                    process=Process.sequential)
    

if __name__ == '__main__':
    
    llm = LLM(
        model="gemini/gemini-2.0-flash-lite",
        temperature=0.7,
        )

    load_dotenv()

    research_crew = ResearchCrew(llm)

    result = research_crew.crew().kickoff(inputs={"topic": "The impact of AI on job markets"})
    print(result)