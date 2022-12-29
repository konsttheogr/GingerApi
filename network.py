import asynctio, nextcord, json

class Network:
    async def __init__(self, client, bots, channel_id):
        if client.user==None:
            raise Exception("client.user can't be None")
        self.client = client
        self.bot = [[bots[i] for i in bots if bots[i]==self.client.user.id][0], self.client.user.id]
        self.bots = {k:v for k,v in bots if v!=self.client.user.id}
        self.channel = await self.client.fetch_channel(channel_id)

    async def request(self, method, content, rec=None):
        rec = self.bots[0] if rec==None
        if type(rec)==type(''):
            rec = self.bots[req]
        dictn = {"receiver": f"<@{rec}>", "method": method, "content": content}
        await channel.send(str(dictn))
        if method=="GET":
            def check(m: nextcord.Message):
                return m.author.id!=self.client.user.id and self.client.user in m.mentions
            try:
                m = await self.client.wait_for('message', check=check, timeout=10.0)
                return m
            except asyncio.TimeoutError: 
                raise Exception("TimeoutError")
    async def on_message(self, msg: nextcord.Message):
        if msg.channel.id==self.channel.id and self.client.user in msg.mentions and msg.reference==None:
            dictn = json.loads(msg.content)
            text = eval(dictn['content'])
            method = dictn['method']
            if method=="GET":
                await msg.reply(text)
            elif method=="POST"
                return text