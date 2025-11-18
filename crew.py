from crewai import Crew,Process
from agents import blog_researcher, blog_writer
from task import research_task, writing_task   
import time
import sys


#Forming the tech focued crew with some enhanced configurations
crew = Crew(
    agents=[blog_researcher, blog_writer],
    tasks=[research_task, writing_task],
    process=Process.sequential,
    memory=False,
    cache=True,
    max_rpm=5,
    share_crew=True
)

#Start the task execution process

try:
    results = crew.kickoff({"topic": "AI VS ML VS DL VS DATASCIENCE"})
    print(results)
except Exception as e:
    # catch rate-limit / quota errors and show friendly guidance
    msg = str(e)
    if "quota" in msg.lower() or "rate limit" in msg.lower() or "429" in msg:
        sys.exit("OpenAI quota exceeded or rate-limited. Check billing at https://platform.openai.com/account/billing and reduce usage.")
    raise
