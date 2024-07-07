import os
import sys
import time
import configparser
import random
import re
import importlib
from datetime import datetime, timedelta

from telethon import TelegramClient, events
from telethon.tl.types import Message, PeerChannel, InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.tl.functions.messages import GetHistoryRequest, SendMessageRequest, GetPeerDialogsRequest
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError


def load_mods():
    mod_dir = "mods"
    for filename in os.listdir(mod_dir):
        if filename.endswith(".py"):
            new_filename = filename.replace(" ", "_")
            if new_filename != filename:
                os.rename(os.path.join(mod_dir, filename), os.path.join(mod_dir, new_filename))

            print(new_filename) 
            with open(os.path.join(mod_dir, new_filename), "r") as f:
                exec(f.read())

client = TelegramClient("session", "23962937", "e247a38e5d7d45235018717e76920252")

@client.on(events.NewMessage(pattern='.mods'))
async def handler(event):
    mods_dir = 'mods'
    py_files = [f[:-3] for f in os.listdir(mods_dir) if f.endswith('.py')]
    py_files.sort(reverse=True)
    
    await event.reply(f"Список модов:\n\n" + "\n".join(py_files) + f"\n\nВсего модов:  {len(py_files)}")
    await event.delete()

if __name__ == "__main__":
    print(
        """
'　,,/　 ヽ ヽﾞ､、 ヽ　ヽ ＼ヽ　､
　 // 　 　 ﾞ､ヽヽ、 ﾞ､　 '､　＼'､ヽ
　!! !　　　　 ',　'､',ヽ、ヽ　'､　 ヽ', ＼
　l ',l　　　　　',　 'i_,.､ゝ','､ ', 　 ヽ!
　い'､＿　　　 X"､;==ミ_ ＼!　　 i!、
　ヽﾞ､_､,,,_ヽ　　 ｀'iﾞ､)::::ﾞi｀'　|　　 iﾄ､
ヽ､ヽ','ﾞﾄバ ,　　　ヽ:;;;;ノ ,　 !　　/,>
ヾ'､'､_',.ﾐ;;ｼﾉ　　　｀'''''´"　,'　/,/ム
　｀ヽい、　ヽ‐　 　 ,.．　　/ ,ｨ/_ゝr' ﾉ
　　　 ヾ'、 ﾌ７'"ﾌ´　　　/ ,ｲ,ヶ-‐ﾂ′
　　　　　ヽヽ-‐'′　 　 ,! i ! !{i　 {i（
　　　 　 　 ｀i ､_　_,、:.'':.:い!i ヾ､__ヾ
　　　　　　-'ノ / ） ,ﾊ　 :.ヽゝ､_ｯr''"
　　　 　 　 ｰ'∠ノ_,.,!　 　 r''ｒ' _,.-
　　　　　　 ,r;==´､ノ 　 〃/／


███╗░░██╗███████╗██╗░░░██╗██╗███████╗
████╗░██║██╔════╝██║░░░██║██║██╔════╝
██╔██╗██║█████╗░░╚██╗░██╔╝██║█████╗░░
██║╚████║██╔══╝░░░╚████╔╝░██║██╔══╝░░
██║░╚███║███████╗░░╚██╔╝░░██║███████╗
╚═╝░░╚══╝╚══════╝░░░╚═╝░░░╚═╝╚══════╝

    """
    )
    client.start()
    load_mods()
    client.run_until_disconnected()