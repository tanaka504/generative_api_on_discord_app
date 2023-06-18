import os
import discord
from lib.manager import BotManager


TOKEN = os.environ.get('DISCORD_APP_TOKEN')

# 接続に必要なオブジェクトを生成
client = discord.Client(intents=discord.Intents.all())
bot_manager = BotManager()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
        
    elif '/chat' in message.content:
        question = message.content[6:]
        answer = bot_manager.get_rwkvchat(question)
        await message.channel.send(answer)
    
    elif '/img' in message.content:
        prompt = message.content[5:].split('!')
        negative_prompt = '' if len(prompt) == 1 else prompt[1]
        filenames = bot_manager.get_generated_imagepath(prompt=prompt[0], negative_prompt=negative_prompt)
        files = [discord.File(f'tmp/{fname}') for fname in filenames]
        await message.channel.send(
            files=files
        )

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
