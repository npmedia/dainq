import discord
import random
import os


client = discord.Client()
voice = 734432949369307136  ##게임보이스 코드
lol = 736037996205441095  ##롤 코드




##유저코드





@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("매니저 일하는 중")
    await client.change_presence(status=discord.Status.online, activity=game)




@client.event   ###
async def on_message(message):

##도움말

    if message.content.startswith("=롤"):
        embed = discord.Embed(title="롤 닉네임 / 티어 / 라인", description="설명", color=0x62c1cc)
        embed.set_footer(text="롤 맴버")
        embed.add_field(name="다인", value="아케이드 코르키 / 실버 / 정글빼고 (서폿 탑 선호)", inline=True)
        embed.add_field(name="명탐정비밥", value="음주가렌 / 실버 / 서폿 탑", inline=True)
        embed.add_field(name="조갱", value="HCI / 플레 / 미드 원딜 서폿", inline=True)
        embed.add_field(name="금동", value="집사야 물좀다오 / 실버 / 탑 원딜 서폿", inline=True)
        embed.add_field(name="하초", value="싱거움 / 플레2 / ALL (서폿은 싫어함)", inline=True)
        embed.add_field(name="호구맛", value="이번판 찐마임 / 플4 / 원딜 서폿 정글", inline=True)
        embed.add_field(name="현이", value="IlIllllIIIllII / 플레1 / ALL", inline=True)
        embed.add_field(name="포로맛쿠키", value="포로맛쿠키 / 골드 / ALL", inline=True)
        embed.add_field(name="펜지", value="IIIPenIII / 마스터 / ALL", inline=True)
        embed.add_field(name="사신의시", value="시인이잠든 숲 / 플레 / 정글", inline=True)
        #embed.add_field(name="", value="", inline=True)
        await client.get_channel(int(lol)).send(embed=embed)

##역할 랜덤 정하기

    if message.content.startswith("=순서"):
        team = message.content[4:]
        peopleteam = team.split("/")
        people = peopleteam[0]
        team = peopleteam[1]
        person = people.split(" ")
        teamname = team.split(" ")
        random.shuffle(teamname)
        for i in range(0, len(person)):
            await message.channel.send(person[i] + "/" + teamname[i])

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)

