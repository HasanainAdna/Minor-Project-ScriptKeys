from flask import Flask, render_template, request
import openai
from dotenv import load_dotenv  # Import the function
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Set up OpenAI API credentials
openai.api_key = os.environ.get('OPENAI_API_KEY')  # Load API key from environment variable

# Instructions for the AI model
INSTRUCTIONS = """You are an AI Assistant that is an expert in Coding for roblox and Unity and Garry mods scripts and Lua and C# and C++ and python and Html. You know about roblox scripting,Lua. You can provide code for people that need help with anything else related to coding.
can you also fix their script when they say can you fix this script for me then you will read it then fix it and you can tell them if theres anything wrong with it and give them advice how to make it better and advanced. I can also make discord bots. When you give them the code, specify where to place it in a script or a local script and where to put it in ServerScriptService, StarterPlayer, StarterCharacterScripts, StarterPlayerScripts, ServerStorage, ReplicatedStorage, ReplicatedFirst, Workspace.
If you are unable to provide an answer to a question, please respond with the phrase "I'm just a simple coder, I can't help with that."
Do not use any external URLs in your answers. Do not refer to any blogs in your answers. Display all the code in format. You can make HTML websites and scripts and can create websites like ChatGPT and more."""

# Define the default route to return the index.html file
@app.route("/")
def index():
    return render_template("index.html")

# Define the /api route to handle POST requests
@app.route("/api", methods=["POST"])
def api():
    # Get the message from the POST request
    message = request.json.get("message")
    # Send the message to OpenAI's API and receive the response
    
    
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": message}
    ]
    )
    if completion.choices[0].message!=None:
        return completion.choices[0].message

    else :
        return 'Failed to Generate response!'
    

if __name__=='__main__':
    app.run()

