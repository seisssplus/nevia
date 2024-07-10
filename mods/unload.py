mods_folder = "./mods"
sys.path.append(mods_folder)

forbidden_files = ["ping.py", "unload.py", "import.py", "pattrn.py"]


@client.on(events.NewMessage(pattern='^.unload (.*)'))
async def unload_file(event):
    if event.is_group:
        if event.sender_id == (await client.get_me()).id:
            file_name = event.pattern_match.group(1)

            if file_name + ".py" in forbidden_files:
                await event.reply("Нельзя удалить этот файл!")
                return

            file_path = os.path.join(mods_folder, f"{file_name}.py")
            try:
                with open(file_path, 'r'):
                    pass
            except FileNotFoundError:
                await event.reply("Файл не найден!")
                return

            try:
                os.remove(file_path)
                importlib.invalidate_caches()
                await event.reply(f"Файл {file_name}.py успешно удален!")
            except Exception as e:
                await event.reply(f"Ошибка удаления файла: {e}")