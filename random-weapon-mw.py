# インストールした discord.py を読み込む
import discord
import random_methods as r

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'NjYyMDEwMjgzMDQ0MjQxNDIz.XgzvXg.clgqw1RvdAMJEFEvUHpBOKBQjuY'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
# 武器データ読み込み
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「??rand」と発言したら「にゃーん」が返る処理
    if message.content == '?loadout':
        # メイン武器取得
        main = r.main_rand()
        main_name = main[0]
        main_attach = main[1]
        # サブ武器取得
        sub = r.sub_rand()
        sub_name = sub[0]
        sub_attach = sub[1]
        # パーク、装備取得
        plt = r.park_lethal_tactical()
        park = plt[0]
        lethal = plt[1]
        tac = plt[2]
        # ストリーク、フィールドアップグレード
        su = r.streak_upgrade()
        streak = su[0]
        field = su[1]
        await message.channel.send(\
            '-------------main----------------------------------------\n\
            {0}\n\
            {1}\n\
            -------------sub------------------------------------------\n\
            {2}\n\
            {3}\n\
            -------------park, lethal, tactical-----------------------\n\
            {4}\n\
            {5}\n\
            {6}\n\
            -------------kill-streak, field-upgrade-------------------\n\
            {7}\n\
            {8}\n\
            '.format(main_name, main_attach, sub_name, sub_attach, park,\
            lethal, tac, streak, field) )

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
