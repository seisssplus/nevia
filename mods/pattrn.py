@client.on(events.NewMessage(pattern='^.pattrn'))
async def handler(event):
    await event.delete()  
    text = f"""
🐧pattrn: **nevie**
"""

    user = await event.get_sender()
    await event.respond(text)