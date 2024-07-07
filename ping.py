@client.on(events.NewMessage(pattern='.ping'))
async def ping(event):
    start_time = datetime.now()
    message = await event.get_reply_message() 
    end_time = datetime.now()

    latency = (end_time - start_time).total_seconds()

    response = f"<b>⚡️пинг:</b>\n⬇️ <i>отклик платформы</i> <code>{latency:.2f}</code> s\n⬆️ <i>подробный отклик</i> <code>{latency * 1000:.2f}</code> ms"
    if message:
        await event.respond(response, parse_mode='html')
    else:
        await event.respond(response, parse_mode='html')
    await event.delete()