@client.on(events.NewMessage(pattern='^.pattrn'))
async def handler(event):
    await event.delete()  
    text = f"""

█▄─▀█▄─▄█▄─▄▄─█▄─█─▄█▄─▄█▄─▄▄─█
██─█▄▀─███─▄█▀██▄▀▄███─███─▄█▀█
▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▀▀▄▀▀▀▄▄▄▀▄▄▄▄▄▀
"""

    user = await event.get_sender()
    profile_photo = await client.get_profile_photos(user, limit=1)
    if profile_photo:
        await event.respond(text, file=profile_photo[0])
    else:
        await event.respond(text)