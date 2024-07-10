@client.on(events.NewMessage(pattern='\.import'))
async def handler(event):
    if event.is_group:
        if event.sender_id == (await client.get_me()).id:
            bot_dir = os.path.dirname(os.path.abspath(__file__)) 

            mods_dir = os.path.join(bot_dir, 'mods')

            if not os.path.exists(mods_dir):
                os.makedirs(mods_dir)
            previous_message = await event.get_reply_message() 
            if previous_message and previous_message.media:
                try:
                    await client.download_media(previous_message.media, mods_dir)
                    file_name = previous_message.media.document.attributes[0].file_name
                    await event.respond(f'Файл {file_name} успешно перемещен в директорию')
                except Exception as e:
                    await event.respond(f'Произошла ошибка при перемещении файла: {e}')
            else:
                await event.respond('Предыдущее сообщение не является файлом.')