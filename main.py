from flask import Flask, url_for, render_template, request
#from requests_html import HTML
import os, nextcord
from network import Network


app = Flask(__name__)
client = nextcord.ext.commands.Bot(command_prefix='.api', intents=nextcord.Intents.all())


#https://flask.palletsprojects.com/en/2.2.x/quickstart/#a-minimal-application

psw = os.environ['psw']
@app.route(f"/{psw}/hello/<name>")
def hello(name):
    return f"<p>Hello, {name}!</p>"
    
@app.route(f"/{psw}/check")
def check():
    return '200'
 
###

@client.event
async def on_ready():
    bots={
        "main":972872922106576956,
        "beta":986629067681955860
    }
    network = await Network(client, bots, 1058042029336186891)
    await network.request("POST", 'print("api connected")', 'main')

###

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv("PORT", default=5000))
client.run(os.environ['token'])