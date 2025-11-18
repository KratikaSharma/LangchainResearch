from crewai import Task
from agents import blog_researcher, blog_writer
from tools import yt_tool

#Reaserch Task 
research_task=Task(
    description=(
         "Identify the video {topic}. "
        "Get detailed information about the video from the channel."
    ),
    expected_output="A detailed research notes on the topic {topic} from YT channel",
    tools=[yt_tool],
    agent=blog_researcher,
)

#Writing Task
writing_task=Task(
    description=(
        "Write a comprehensive blog post"
    "Narrate compelling tech stories about the videos {topic} from YT channel"
    ),
    expected_output="A well-structured blog post on the topic {topic} from YT channel",
    tools=[yt_tool],
    async_execution=False,
    agent=blog_writer,
    output_file="blog_post_{topic}.md",
)