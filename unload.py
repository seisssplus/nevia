mods_folder = "./mods"
sys.path.append(mods_folder)

forbidden_files = ["ping.py", "unload.py", "import.py", "pattrn.py"]


@client.on(events.NewMessage(pattern='^.unload (.*)'))
async def unload_file(event):
    global mods_folder
    file_name = event.pattern_match.group(1)
    global forbidden_files
    
    # Проверяем, находится ли файл в списке запрещенных
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


@client.on(events.NewMessage(pattern='^.load (.*)'))
async def load_file(event):
    global mods_folder
    file_name = event.pattern_match.group(1)
    file_path = os.path.join(mods_folder, f"{file_name}.py")
    try:
        with open(file_path, 'r'):
            pass
    except FileNotFoundError:
        await event.reply("Файл не найден!")
        return

    try:
        module = importlib.import_module(file_name)
        await event.reply(f"Файл {file_name}.py успешно загружен!")
    except Exception as e:
        await event.reply(f"Ошибка загрузки файла: {e}")