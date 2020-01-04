# インストールした discord.py を読み込む
#import discord

# 自分のBotのアクセストークンに置き換えてください
#TOKEN = 'NjYyMDEwMjgzMDQ0MjQxNDIz.XgzvXg.clgqw1RvdAMJEFEvUHpBOKBQjuY'

# 接続に必要なオブジェクトを生成
#client = discord.Client()

# 起動時に動作する処理
#@client.event
#async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
#    print('ログインしました')

# メッセージ受信時に動作する処理
# 武器データ読み込み
import loadouts as l
import random

def main_rand():
    main_category = random.choice( l.main )
    main_weapon = random.choice( main_category )
    if type( main_weapon ) == str:
        print_main_weapon = main_weapon

        return print_main_weapon, ""

    else:
        main_weapon_name = main_weapon.pop(0)
        print_main_weapon = main_weapon_name[0]

        main_attach_category =  random.sample( main_weapon, 5 )
        attachments = []
        for i in range( len( main_attach_category ) ):
            attach_category = main_attach_category[i].pop(0)
            main_attach_names = random.choice( main_attach_category[i] )
            attachments.append( "{0}:  {1}".format(attach_category,
                                                         main_attach_names))
        print_attachment = "\n".join(attachments)


        return print_main_weapon, print_attachment



def sub_rand():
    sub_category = random.choice( l.sub )
    sub_weapon = random.choice( sub_category )
    if type( sub_weapon ) == str:
        print_sub_weapon = sub_weapon

        return print_sub_weapon, ""

    else:
        sub_weapon_name = sub_weapon.pop(0)
        print_sub_weapon = sub_weapon_name[0]

        sub_attach_category =  random.sample( sub_weapon, 5 )
        attachments = []
        for i in range( len( sub_attach_category ) ):
            attach_category = sub_attach_category[i].pop(0)
            main_attach_names = random.choice( sub_attach_category[i] )
            attachments.append( "{0}:  {1}".format(attach_category,
                                                         main_attach_names))
        print_attachment = "\n".join(attachments)


        return print_sub_weapon, print_attachment



def park_lethal_tactical():
    park1 = random.choice( l.park1 )
    park2 = random.choice( l.park2 )
    park3 = random.choice( l.park3 )

    lethal = random.choice( l.lethal )
    tactical = random.choice( l.tactical )

    return park1, park2, park3, lethal, tactical




def streak_upgrade():
    streaks = random.sample( l.kill_s, 3 )
    streak_list = []
    for s in streaks:
        if type(s) == str:
            streak_list.append( s )
        else:
            streak_list.append ( random.choice( s ) )
    streak = " ".join( streak_list )

    #streak = "{0} {1} {2}".format( streak01, streak02, streak03 )

    upgrade= random.choice( l.field_u )

    return streak, upgrade




main = main_rand()
main_weapon = main[0]
main_weapon_attachments = main[1]
print(main_weapon)
print(main_weapon_attachments)
print( "----------------------------------------------------" )
sub = sub_rand()
sub_weapon = sub[0]
sub_weapon_attachments = sub[1]
print(sub_weapon)
print(sub_weapon_attachments)
print( "----------------------------------------------------" )
park_lethal_tactical = park_lethal_tactical()
park1 = park_lethal_tactical[0]
park2 = park_lethal_tactical[1]
park3 = park_lethal_tactical[2]
print( park1 )
print( park2 )
print( park3 )
print( "----------------------------------------------------" )
streak_upgrade = streak_upgrade()
streak = streak_upgrade[0]
upgrade = streak_upgrade[1]
print(streak)
print(upgrade)









#@client.event
#async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    #if message.author.bot:
    #    return
    # 「??rand」と発言したら「にゃーん」が返る処理
#    if message.content == '??rand':
#        await message.channel.send('')

# Botの起動とDiscordサーバーへの接続
#client.run(TOKEN)
