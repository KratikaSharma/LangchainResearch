# ...existing code...
from dotenv import load_dotenv
import os
import sys

load_dotenv()

# Require OPENAI_API_KEY because some crewai_tools validate at import time.
OPENAI_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_KEY:
    print("openAI key missing")
    sys.exit(
        "Missing OPENAI_API_KEY. Add it to a .env file or set the OPENAI_API_KEY environment variable and re-run.\n"
        "Get a key at https://platform.openai.com/ (Account → View API keys)."
    )
os.environ["OPENAI_API_KEY"] = OPENAI_KEY


from crewai import Agent
from crewai import LLM
from tools import yt_tool


llm = LLM(
    model="openai/gpt-4o-mini",      # switch to an OpenAI model
    api_key=OPENAI_KEY,
    temperature=0.2,
    max_tokens=400
)

# Create a senior blog content researcher
blog_researcher = Agent(
    role="Blog researcher from YouTube videos",
    goal="get the relevant content for the topic {topic} from YT channel",
    verbose=True,
    memory=False,
    backstory=(
         "You are an expert in understanding videos in AI, data science, "
        "Machine Learning and generative AI and providing concise suggestions."
    ),
    tools=[yt_tool],
    llm=llm,
    allow_delegation=True,
)

# Create a senior blog content writer agent with YT tool
blog_writer = Agent(
    role="Senior blog content writer",
    goal="Narrate compelling tech stories about the videos {topic} from YT channel",
    verbose=True,
    memory=False,
    backstory=(
        "With a flair for simplifying complex topics, you craft "
        "engaging narratives that captivate and educate."
    ),
    tools=[yt_tool],
    llm=llm,
    allow_delegation=False,
)
