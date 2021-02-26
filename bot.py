import slack
import os
from pathlib import Path
from dotenv import load_dotenv

# Loading environment variable
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

client = slack.WebClient(token=os.environ['SLACK_TOKEN'])

client.chat_postMessage(channel='#test', text="I need to o now")