from crewai_tools import YoutubeChannelSearchTool

CHANNEL_URL = "https://www.youtube.com/@krishnaik06"
yt_tool = YoutubeChannelSearchTool(youtube_channel_url=CHANNEL_URL)

#yt_tool = YoutubeChannelSearchTool(youtube_channel_handle='@krishnaik06')