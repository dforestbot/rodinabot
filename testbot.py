import discord
from discord.ext import commands
from discord.utils import get
import datetime
import random
import re
import config
import os

PREFIX = '.'

client = commands.Bot( command_prefix = PREFIX)

role_registr = [ 'роль', 'роли', 'дайте роль', 'хочу роль', 'роль дайте', 'выдайте роль', '-роль', 'Роль', 'Роли', 'Дайте роль', 'Хочу роль', 'Роль дайте', 'Выдайте роль', '-Роль', '!Роль', '!роль']

nick_registr = [ 'ГУВД', 'ГИБДД', 'Армия', 'ЦБ', 'РЦ', 'ВМУ', 'МЗ', 'Пра', 'КМ', 'СБ', 'ЧК', 'СТ', 'РМ', 'УМ', 'ФМ', 'ФСИН']

role_check = [ '★ ГУВД ★', '★ ГИБДД ★', '★ Армия ★', '★ ЦБ ★', '★ РЦ', '★ ВМУ ★', '★ МЗ', '★ Пра', '★ Кавказская Мафия ★', '★ Солнцевская Братва ★', '★ Чёрная Кошка ★', '★ Санитары ★', '★ Русская Мафия ★', '★ Украинская Маифя ★', '★ Фантомасы ★', '★ ФСИН ★']

@client.event

async def on_ready():
    print( 'Я подключился' )

@client.event
async def on_message(ctx):
    await client.process_commands( ctx)
    
    msg = ctx.content.lower()
    channel = client.get_channel(688735597157679146)

    if msg in role_registr:

        aname = ctx.author.display_name
        author = ctx.author.mention
        ath = re.findall(r'\w*', aname)
        arol = ctx.author.roles
        k = 0
        for i in range(len(arol)): 
            if not arol[i] in arol[0:i]:
                k += 1

        admrole = discord.utils.get(ctx.guild.roles, id=673481357657243649)

        if ath[1] in nick_registr:
            nad_role = discord.utils.get(ctx.guild.roles, id=config.ROLES[ath[1]])

            msg = await channel.send("Пользователь {} подал заявку на выдачу роли <@&{}>. Для одобрения нажмите на: ✅".format(author, config.ROLES[ath[1]]))
            await msg.add_reaction('✅')

            def check(reaction, user):
                return user == msg.author and str(reaction.emoji) == '✅'
            try:
                reaction, user = await client.wait_for('reaction_add', timeout=999999.0, check=check)
            except asyncio.TimeoutError:
                print('[ERR]: Time Out')
            else:
                if k > 1:
                    if arol[1] in role_check:
                        print('+')
                    sn_role = discord.utils.get(ctx.guild.roles, name = f'{arol[1]}' )
                    await ctx.author.remove_roles(sn_role)
                    await ctx.author.add_roles(nad_role)
                    now = datetime.datetime.now()
                    embed = discord.Embed(title = f'Ролевой бот Rodina RP | 04', url = 'https://vk.com/norimyxxxo1702', description = f'''Пользователь: {author}\nВыданная роль: <@&{config.ROLES[ath[1]]}>\nСервер: Восточный округ[04]\nЗапрос одобрил: {user.mention}\nВремя выдачи: {now.strftime("%H:%M")}''', color=0xFF0000)

                    embed.set_footer(text = f'Daniel_Moscovskiy © 2020 | Все права защищены', icon_url = 'https://avatars.mds.yandex.net/get-zen_doc/1857554/pub_5d06bf23f5dc000f8d03fb89_5d06bfcfaf8bd4147ddcb8b1/scale_1200')
                    embed.set_thumbnail(url = 'https://playntrade-a.akamaihd.net/375/u37556/066/7a0a2507.jpg')

                    await ctx.channel.send(embed = embed)
                else:
                    await ctx.author.add_roles(nad_role)
                    now = datetime.datetime.now()
                    embed = discord.Embed(title = f'Ролевой бот Rodina RP | 04', url = 'https://vk.com/norimyxxxo1702', description = f'''Пользователь: {author}\nВыданная роль: <@&{config.ROLES[ath[1]]}>\nСервер: Восточный округ[04]\nЗапрос одобрил: {user.mention}\nВремя выдачи: {now.strftime("%H:%M")}''', color=0xFF0000)

                    embed.set_footer(text = f'Daniel_Moscovskiy © 2020 | Все права защищены', icon_url = 'https://avatars.mds.yandex.net/get-zen_doc/1857554/pub_5d06bf23f5dc000f8d03fb89_5d06bfcfaf8bd4147ddcb8b1/scale_1200')
                    embed.set_thumbnail(url = 'https://playntrade-a.akamaihd.net/375/u37556/066/7a0a2507.jpg')

                    await ctx.channel.send(embed = embed)
        else:
            embed = discord.Embed(title = f'Ролевой бот Rodina RP | 04', url = 'https://vk.com/norimyxxxo1702', description = f'''Пользователь: {author}\nПричина отклонения: Ник не по форме\nПравильная форма: [Фракция Ранг/10] Nick Name\nСписок тэгов для роли: \nСБ, ЧК, ФМ, СТ, КМ, РМ, УМ, Пра-во, ГИБДД, ГУВД, Армия, ФСИН, МЗ-Ю, ВМУ, ЦБ, РЦ''', color=0xFF0000)

            embed.set_footer(text = f'Daniel_Moscovskiy © 2020 | Все права защищены', icon_url = 'https://avatars.mds.yandex.net/get-zen_doc/1857554/pub_5d06bf23f5dc000f8d03fb89_5d06bfcfaf8bd4147ddcb8b1/scale_1200')
            embed.set_thumbnail(url = 'https://playntrade-a.akamaihd.net/375/u37556/066/7a0a2507.jpg')
            await ctx.channel.send(embed = embed)


@client.command()
async def rep(stx):
    await stx.channel.purge(limit = 1)
    author = stx.message.author
    author3 = stx.author.mention
    guild = stx.message.guild
    creport = discord.utils.get(stx.guild.categories, name = 'rep')
    await guild.create_text_channel(f'Вопрос {author3}', overwrites = None, category = creport, reason = 'Создание нового Вопроса.')
    server = client.get_guild(577511138032484360)
    for channel in server.channels:
        if channel.name == f'вопрос {author.mention}':
            break
    await channel.set_permissions(author, read_messages = True, send_messages = True)
    mlmoder = discord.utils.get(stx.guild.roles, id = 577523815890944007)
    await channel.set_permissions(mlmoder, read_messages = True, send_messages = True, manage_channels = True)
    moder = discord.utils.get(stx.guild.roles, id = 577524969051914262)
    await channel.set_permissions(moder, read_messages = True, send_messages = True, manage_channels = True)
    stmoder = discord.utils.get(stx.guild.roles, id = 577524754798346261)
    await channel.set_permissions(stmoder, read_messages = True, send_messages = True, manage_channels = True)
    admin = discord.utils.get(stx.guild.roles, id = 577524866320826368)
    await channel.set_permissions(admin, read_messages = True, send_messages = True, manage_channels = True)
    alluser = discord.utils.get(stx.guild.roles, id = 577511138032484360)
    await channel.set_permissions(alluser, read_messages = False, send_messages = False)
    embed = discord.Embed(title = f'Техническая поддержка', url = 'https://vk.com/norimyxxxo1702', description = f'''**Здравствуйте {author3} !\nДля решения вашего вопроса создан отдельный канал.\nОн является первым в списке каналов данного Discord сервера.\nДальнейшее решение Вашей проблемы будет происходить там с модераторами сервера.\n\nДля перехода нажмите на название канала || {channel.mention} ||**''', color=0xFF0000)
    embed.set_footer(text = f'Daniel_Moscovskiy © 2020 | Все права защищены', icon_url = 'https://avatars.mds.yandex.net/get-zen_doc/1857554/pub_5d06bf23f5dc000f8d03fb89_5d06bfcfaf8bd4147ddcb8b1/scale_1200')
    embed.set_thumbnail(url = 'https://playntrade-a.akamaihd.net/375/u37556/066/7a0a2507.jpg')
    msgdel = await stx.channel.send(embed = embed)
    emb = discord.Embed(title = 'Технический раздел Rodina RP | Восточный округ', colour = discord.Color.dark_red())
    emb.add_field(name = f'Снова здравствуйте!\nДля решения Вашей проблемы мы создали отдельный чат с нашими модераторами, которые получили оповещение о вашем запросе.\nОпишите Вашу проблему полностью и развёрнуто, после чего дождитесь ответа одного из Support команды.',
    value = '\n' '**Постарайтесь описать вашу проблемму кратко и понятным для понимания языком.**\n\nПосле решения вопроса нажмите на - ✅')
    embed.set_footer(text = f'Daniel_Moscovskiy © 2020 | Все права защищены', icon_url = 'https://avatars.mds.yandex.net/get-zen_doc/1857554/pub_5d06bf23f5dc000f8d03fb89_5d06bfcfaf8bd4147ddcb8b1/scale_1200')
    embed.set_thumbnail(url = 'https://playntrade-a.akamaihd.net/375/u37556/066/7a0a2507.jpg')
    mes = await channel.send(embed = emb)
    await mes.add_reaction('✅')
    embe = discord.Embed(title = f'Техническая поддержка', url = 'https://vk.com/norimyxxxo1702', description = f'''<@&577523815890944007>\n<@&577524969051914262>\n<@&577524754798346261>\n<@&577524866320826368>\n**Внимание! Поступил новый репорт от пользователя {author3}.\nОн ждёт Вас в канале {channel.mention}**''', color=0xFF0000)
    embe.set_footer(text = f'Daniel_Moscovskiy © 2020 | Все права защищены', icon_url = 'https://avatars.mds.yandex.net/get-zen_doc/1857554/pub_5d06bf23f5dc000f8d03fb89_5d06bfcfaf8bd4147ddcb8b1/scale_1200')
    embe.set_thumbnail(url = 'https://playntrade-a.akamaihd.net/375/u37556/066/7a0a2507.jpg')
    achat = client.get_channel(577541992599388180)
    await achat.send(embed = embe)
    f=open("infa.txt","r+")
    s=(f.read())
    a=s.split(' ')  
    x = int(a[0]) + 1
    z = x - int(a[2])
    obfile = open('infa.txt', 'w')
    obfile.write(f'{x} {z} {a[2]}')
    message_id = 697757069586989126
    chans = client.get_channel(697518654140710964)
    message = await chans.fetch_message(message_id)
    emb23 = discord.Embed(colour = discord.Color.red())
    emb23.set_author(name = 'Rodina RP | Восточный округ | Support', url = 'https://vk.com/norimyxxxo1702', icon_url = 'https://psv4.userapi.com/c848128/u264775111/docs/d17/834dfb9d0e80/Bez_imeni-2.png?extra=ww_29uP9PkR5bjUsKFq_iu2I0KEv2QvRqU7TWBuWJfESZ1N691WUg-NpfOiV4-b7jYy0u6GDCmiEj2yNICLNi9-nQ5gQpXQZ7TMpuVUPiZqlL_R-ClahuosQAi5P_fPISQMJbAKIc6JsfQj9IlDl-N2CXcc')
    emb23.add_field(name = f'**Доброго времени суток! Вы попали в канал технической поддержки сервера `Rodina RP | Восточный округ`!\nТут Вы можете узнать, как получить техническую поддержку от наших модераторов Discord**\n\n ',
    value = '\n' f'ٴ\n**⚙ Общее количество вопросов: `{x}`\n⚙ Вопросы не обработанные модераторами: `{z}`\n⚙ Закрытые вопросы: `{a[2]}` **\n')
    emb23.set_image(url = 'https://i.ytimg.com/vi/l3Z8KSUltkQ/maxresdefault.jpg')
    emb23.set_footer(text = f'Daniel_Moscovskiy © 2020 | Все права защищены', icon_url = 'https://avatars.mds.yandex.net/get-zen_doc/1857554/pub_5d06bf23f5dc000f8d03fb89_5d06bfcfaf8bd4147ddcb8b1/scale_1200')
    emb23.set_thumbnail(url = 'https://psv4.userapi.com/c856336/u264775111/docs/d16/361841bb57ae/256kh256.png?extra=CdKRlvHHzIZQ2Sf6EZDC7xGxJeEQ7Bc_MpJF93mGTmr6OIFQK5pMldN12vqn-ofHpk_bG45rl6dqVI51r9a8Akxia5lebPhRg78DQLL9syvyA-UE70_u0VXyqUM-eQeohjgTg4YqGfov-YzS-5PMK8JxkXI')
    await message.edit(embed = emb23)
    obfile.close()
    f.close()
    
    def check(reaction, user):
        return user == stx.author and str(reaction.emoji) == '✅'
    try:
        reaction, user = await client.wait_for('reaction_add', timeout=999999.0, check=check)
    except asyncio.TimeoutError:
        print('[ERR]: Time Out')
    else:
        channel = client.get_channel(mes.channel.id)
        await channel.delete(reason = f'Вопрос {author} закрыт.')
        f=open("infa.txt","r+")
        s=(f.read())
        a=s.split(' ') 
        c = int(a[2]) + 1
        z = int(a[0]) - c
        obfile = open('infa.txt', 'w')
        obfile.write(f'{a[0]} {z} {c}')
        message_id = 697757069586989126
        chans = client.get_channel(697518654140710964)
        message = await chans.fetch_message(message_id)
        emb23 = discord.Embed(colour = discord.Color.red())
        emb23.set_author(name = 'Rodina RP | Восточный округ | Support', url = 'https://vk.com/norimyxxxo1702', icon_url = 'https://psv4.userapi.com/c848128/u264775111/docs/d17/834dfb9d0e80/Bez_imeni-2.png?extra=ww_29uP9PkR5bjUsKFq_iu2I0KEv2QvRqU7TWBuWJfESZ1N691WUg-NpfOiV4-b7jYy0u6GDCmiEj2yNICLNi9-nQ5gQpXQZ7TMpuVUPiZqlL_R-ClahuosQAi5P_fPISQMJbAKIc6JsfQj9IlDl-N2CXcc')
        emb23.add_field(name = f'**Доброго времени суток! Вы попали в канал технической поддержки сервера `Rodina RP | Восточный округ`!\nТут Вы можете узнать, как получить техническую поддержку от наших модераторов Discord**\n\n ',
        value = '\n' f'ٴ\n**⚙ Общее количество вопросов: `{a[0]}`\n⚙ Вопросы не обработанные модераторами: `{z}`\n⚙ Закрытые вопросы: `{c}` **\n')
        emb23.set_image(url = 'https://i.ytimg.com/vi/l3Z8KSUltkQ/maxresdefault.jpg')
        emb23.set_footer(text = f'Daniel_Moscovskiy © 2020 | Все права защищены', icon_url = 'https://avatars.mds.yandex.net/get-zen_doc/1857554/pub_5d06bf23f5dc000f8d03fb89_5d06bfcfaf8bd4147ddcb8b1/scale_1200')
        emb23.set_thumbnail(url = 'https://psv4.userapi.com/c856336/u264775111/docs/d16/361841bb57ae/256kh256.png?extra=CdKRlvHHzIZQ2Sf6EZDC7xGxJeEQ7Bc_MpJF93mGTmr6OIFQK5pMldN12vqn-ofHpk_bG45rl6dqVI51r9a8Akxia5lebPhRg78DQLL9syvyA-UE70_u0VXyqUM-eQeohjgTg4YqGfov-YzS-5PMK8JxkXI')
        await message.edit(embed = emb23)
        await stx.edit(content='```Вопрос был решён.```')
        obfile.close()
        f.close()



#mess v teh razdel
@client.command(pass_context = True)
async def tehtema(ctx):
    embed = discord.Embed(colour = discord.Color.red())
    embed.set_author(name = 'Rodina RP | Восточный округ | Support', url = 'https://vk.com/norimyxxxo1702', icon_url = 'https://psv4.userapi.com/c848128/u264775111/docs/d17/834dfb9d0e80/Bez_imeni-2.png?extra=ww_29uP9PkR5bjUsKFq_iu2I0KEv2QvRqU7TWBuWJfESZ1N691WUg-NpfOiV4-b7jYy0u6GDCmiEj2yNICLNi9-nQ5gQpXQZ7TMpuVUPiZqlL_R-ClahuosQAi5P_fPISQMJbAKIc6JsfQj9IlDl-N2CXcc')
    embed.add_field(name = f'**Доброго времени суток! Вы попали в канал технической поддержки сервера `Rodina RP | Восточный округ`!\nТут Вы можете узнать, как получить техническую поддержку от наших модераторов Discord**\n\n ',
    value = '\n' f'ٴ\n**⚙ Общее количество вопросов: `0`\n⚙ Вопросы не обработанные модераторами: `0`\n⚙ Закрытые вопросы: `0` **\n')
    embed.set_image(url = 'https://i.ytimg.com/vi/l3Z8KSUltkQ/maxresdefault.jpg')
    embed.set_footer(text = f'Daniel_Moscovskiy © 2020 | Все права защищены', icon_url = 'https://avatars.mds.yandex.net/get-zen_doc/1857554/pub_5d06bf23f5dc000f8d03fb89_5d06bfcfaf8bd4147ddcb8b1/scale_1200')
    embed.set_thumbnail(url = 'https://psv4.userapi.com/c856336/u264775111/docs/d16/361841bb57ae/256kh256.png?extra=CdKRlvHHzIZQ2Sf6EZDC7xGxJeEQ7Bc_MpJF93mGTmr6OIFQK5pMldN12vqn-ofHpk_bG45rl6dqVI51r9a8Akxia5lebPhRg78DQLL9syvyA-UE70_u0VXyqUM-eQeohjgTg4YqGfov-YzS-5PMK8JxkXI')
    message = await ctx.send(embed = embed) 

@client.command(pass_context = True)
async def obtema(ctx):
    f=open("infa.txt","r+")
    s=(f.read())
    a=s.split(' ')
    print(a)   
    x = int(a[0]) + 1
    c = int(a[2]) + 1
    z = x - c
    obfile = open('infa.txt', 'w')
    obfile.write(f'{x} {z} {c}')
    message_id = 697725140300988446
    chans = client.get_channel(697518654140710964)
    message = await chans.fetch_message(message_id)
    emb23 = discord.Embed(colour = discord.Color.red())
    emb23.set_author(name = 'Rodina RP | Восточный округ | Support', url = 'https://vk.com/norimyxxxo1702', icon_url = 'https://psv4.userapi.com/c848128/u264775111/docs/d17/834dfb9d0e80/Bez_imeni-2.png?extra=ww_29uP9PkR5bjUsKFq_iu2I0KEv2QvRqU7TWBuWJfESZ1N691WUg-NpfOiV4-b7jYy0u6GDCmiEj2yNICLNi9-nQ5gQpXQZ7TMpuVUPiZqlL_R-ClahuosQAi5P_fPISQMJbAKIc6JsfQj9IlDl-N2CXcc')
    emb23.add_field(name = f'**Доброго времени суток! Вы попали в канал технической поддержки сервера `Rodina RP | Восточный округ`!\nТут Вы можете узнать, как получить техническую поддержку от наших модераторов Discord**\n\n ',
    value = '\n' f'ٴ\n**⚙ Общее количество вопросов: `{x}`\n⚙ Вопросы не обработанные модераторами: `{z}`\n⚙ Закрытые вопросы: `{c}` **\n')
    emb23.set_image(url = 'https://i.ytimg.com/vi/l3Z8KSUltkQ/maxresdefault.jpg')
    emb23.set_footer(text = f'Daniel_Moscovskiy © 2020 | Все права защищены', icon_url = 'https://avatars.mds.yandex.net/get-zen_doc/1857554/pub_5d06bf23f5dc000f8d03fb89_5d06bfcfaf8bd4147ddcb8b1/scale_1200')
    emb23.set_thumbnail(url = 'https://psv4.userapi.com/c856336/u264775111/docs/d16/361841bb57ae/256kh256.png?extra=CdKRlvHHzIZQ2Sf6EZDC7xGxJeEQ7Bc_MpJF93mGTmr6OIFQK5pMldN12vqn-ofHpk_bG45rl6dqVI51r9a8Akxia5lebPhRg78DQLL9syvyA-UE70_u0VXyqUM-eQeohjgTg4YqGfov-YzS-5PMK8JxkXI')
    await message.edit(embed = emb23)
    obfile.close()
    f.close()

@client.command(pass_context = True)
async def redact(ctx):
    message = await ctx.send('redork')
    await message.edit(content="redpook")
    print(message)

@client.command( pass_context = True )

async def time( ctx ):
    emb = discord.Embed( title = 'Test', colour = discord.Color.green(), url = 'https://www.timeserver.ru')
    
    emb.set_author( name = client.user.name, icon_url = client.user.avatar_url )
    emb.set_footer( text = ctx.author.name, icon_url = ctx.author.avatar_url )
    emb.set_image( url = 'http://pngimg.com/uploads/clock/clock_PNG6658.png' )
    emb.set_thumbnail( url = 'http://pngimg.com/uploads/clock/clock_PNG6658.png' )

    now_date = datetime.datetime.now()

    emb.add_field( name = 'Time', value = 'Time : {}'.format( now_date ) )

    await ctx.send(embed = emb)


@client.command( pass_context = True )

async def rand(ctx):

    emb = discord.Embed( title = 'Random Function', colour = discord.Color.green(), url = 'https://vk.com/norimyxxxo1702')
    
    emb.set_author( name = client.user.name, icon_url = client.user.avatar_url )
    emb.set_footer( text = 'Отправлено по просье: {}'.format(ctx.author.name), icon_url = ctx.author.avatar_url )

    a = random.choices(['машинка(Шанс выпадения 8 процентов)', 'Скин(Шанс выпадения 15 процентов)', '10 миллионов(Шанс выпадения 20 процентов)'], weights=[8, 15, 20])[0]

    emb.add_field( name = 'Ваше рандомное число:', value = '{}'.format(a) )

    await ctx.send(embed = emb)


@client.command()
async def covid(ctx):
    import COVID19Py
    covid19 = COVID19Py.COVID19()
    location = covid19.getLocationByCountryCode("RU")
    date = location[0]['last_updated'].split("T")
    time = date[1].split(".")

    embed = discord.Embed(title = f'Случаи заболевания COVID-19 в России:', url = 'https://www.worldometers.info/coronavirus/', description = f'''Население: {location[0]['country_population']:,}\nПоследние обновление: {date[0]} {time[0]}\nПоследние данные:\nЗаболевших: {location[0]['latest']['confirmed']:,}\nСмертей: {location[0]['latest']['deaths']:,}''', color=0x0c0c0c)

    embed.set_footer(text = f'Daniel_Moscovskiy © 2020 | Все права защищены', icon_url = 'https://avatars.mds.yandex.net/get-zen_doc/1857554/pub_5d06bf23f5dc000f8d03fb89_5d06bfcfaf8bd4147ddcb8b1/scale_1200')
    embed.set_thumbnail(url = 'https://vestirossii.com/wp-content/uploads/epidemiologi-uznali-mnogo-novogo-o-kitajskom-koronaviruse_5e32cc478c9e1.jpeg%27')

    await ctx.send(embed = embed)


@client.command()
@commands.has_permissions( administrator = True )

async def user_mute( ctx, member: discord.Member ):
    await ctx.channel.purge( limit = 1 )

    mute_role = discord.utils.get( ctx.message.guild.roles, name = 'Muted' )

    await member.add_roles( mute_role )
    await ctx.send( f'У {member.mention} ограничен чат, за нарушение прав!' )

import asyncio
@client.command()
@commands.has_permissions( administrator = True )
async def muted(ctx,amount : int,member: discord.Member = None, reason = None,*,arg = None):
    mute_role = discord.utils.get( ctx.message.guild.roles, name = 'Muted' )
    channel_log = client.get_channel(696398807763779694) #Айди канала логов

    await member.add_roles( mute_role )
    await ctx.send(embed = discord.Embed(description = f'**:shield: Пользователю {member.mention} был ограничен доступ к чатам.\n:book: По причине: {reason}**', color=0x0c0c0c)) 
    await channel_log.send(embed = discord.Embed(description = f'**:shield: Пользователю {member.mention} был ограничен доступ к чатам.\n:book: По причине: {reason}**', color=0x0c0c0c))
    await asyncio.sleep(amount)
    await member.remove_roles( mute_role )   


@muted.error
async def muted_error(ctx, error):

    if isinstance( error, commands.MissingPermissions ):
        await ctx.send(embed = discord.Embed(description = f'**:exclamation: {ctx.author.name},у вас нет прав для использования данной команды.**', color=0x0c0c0c))

@client.command()
async def report(ctx,member: discord.Member = None,*,arg = None):

    channel = client.get_channel(577541992599388180) #Айди канала жалоб

    if member is None:

        await ctx.send(embed = discord.Embed(description = '**:grey_exclamation: Обязательно укажите: пользователя!**'))

    elif arg is None:

        await ctx.send(embed = discord.Embed(description = '**:grey_exclamation: Обязательно укажите: причину!**'))

    else:
        emb = discord.Embed(description =f'**:shield: На пользователя {member.mention} была отправлена жалоба.\n:bookmark_tabs: По причине: {arg}**', color=0x0c0c0c)
        emb.set_footer(text = f'Daniel_Moscovskiy © 2020 | Все права защищены', icon_url = 'https://avatars.mds.yandex.net/get-zen_doc/1857554/pub_5d06bf23f5dc000f8d03fb89_5d06bfcfaf8bd4147ddcb8b1/scale_1200')
        emb.set_thumbnail(url = 'https://vestirossii.com/wp-content/uploads/epidemiologi-uznali-mnogo-novogo-o-kitajskom-koronaviruse_5e32cc478c9e1.jpeg%27')
        await ctx.send(embed = emb)
        embed = discord.Embed(description =f'**:shield: На пользователя {member.mention} была отправлена жалоба.\n:bookmark_tabs: По причине: {arg}\n:bust_in_silhouette: Автор жалобы: {ctx.author.mention}**', color=0x0c0c0c)
        embed.set_footer(text = f'Daniel_Moscovskiy © 2020 | Все права защищены', icon_url = 'https://avatars.mds.yandex.net/get-zen_doc/1857554/pub_5d06bf23f5dc000f8d03fb89_5d06bfcfaf8bd4147ddcb8b1/scale_1200')
        embed.set_thumbnail(url = 'https://vestirossii.com/wp-content/uploads/epidemiologi-uznali-mnogo-novogo-o-kitajskom-koronaviruse_5e32cc478c9e1.jpeg%27')
        await channel.send(embed = embed)

@client.command(pass_context = True)
async def react(ctx):

    msg = await ctx.send("Нажми на меня")
    mute_role = discord.utils.get( ctx.message.guild.roles, name = 'Muted' )

    await msg.add_reaction('✅')
    await msg.add_reaction('❎')

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) == '✅'
    try:
        reaction, user = await client.wait_for('reaction_add', timeout=20.0, check=check)
    except asyncio.TimeoutError:
        print('[ERR]: Time Out')
    else:
        await user.add_roles( mute_role )
        await ctx.send(f'{user.mention}, Ваш запрос был одобрен. Роль выдана.')



token = os.environ.get('BOT_TOKEN')
client.run(token)