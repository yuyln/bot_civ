import discord
import json
from discord.ext import commands
import datetime
import os

prefix = ">"
bot = commands.Bot(prefix)
arquivo = {}
try:
	with open("arquivo.json", "r") as arq:
		arquivo = json.loads(arq.read())
except FileNotFoundError:
	print("arquivo não encontrado, sera criado um novo")

@bot.command(name='tabela')
@commands.has_permissions(manage_roles=True)
async def tabela(ctx):
	global prefix
	global arquivo
	guild = ctx.guild
	mensagem = ctx.message.content
	linhas = mensagem.split("\n")
	role1 = guild.get_role(783745705616474172)
	role2 = guild.get_role(783745719207067708)
	role3 = guild.get_role(783745728928415755)
	#role3> role2> role1
	for linha in linhas:
		args = linha.split(" ")
		if args[0] == f"{prefix}tabela":
			try:
				arquivo[args[1]] += int(args[-1])
			except KeyError:
				arquivo[args[1]] = 1000
				arquivo[args[1]] += int(args[-1])
			id_ = int(args[1].split("!")[1].split(">")[0])
			pessoa = await guild.fetch_member(id_)
			if arquivo[args[1]] > 1010: 
				await pessoa.add_roles(role1, role2, role3)
			elif arquivo[args[1]] > 1005: 
				await pessoa.add_roles(role1, role2)
				await pessoa.remove_roles(role3)
			elif arquivo[args[1]] > 1000:
				await pessoa.add_roles(role1)
				await pessoa.remove_roles(role2, role3)
			with open("log.txt", "a") as log:
				try:
					log.write(f"User: {ctx.author.name}\nUserID: {ctx.author.id}\nData: {datetime.datetime.now().strftime('%H:%M:%S - %d/%m/%Y')}\nAção: {pessoa.name} -> {args[-1]}\n----------------------\n")
				except:
					log.write(f"UserID: {ctx.author.id}\nData: {datetime.datetime.now().strftime('%H:%M:%S - %d/%m/%Y')}\nAção: {pessoa.id} -> {args[-1]}\n----------------------\n")
		else:
			try:
				arquivo[args[0]] += int(args[-1])
			except KeyError:
				arquivo[args[0]] = 1000
				arquivo[args[0]] += int(args[-1])
			id_ = int(args[0].split("!")[1].split(">")[0])
			pessoa = await guild.fetch_member(id_)
			if arquivo[args[0]] > 1010: 
				await pessoa.add_roles(role1, role2, role3)
			elif arquivo[args[0]] > 1005: 
				await pessoa.add_roles(role1, role2)
				await pessoa.remove_roles(role3)
			elif arquivo[args[0]] > 1000:
				await pessoa.add_roles(role1)
				await pessoa.remove_roles(role2, role3)
			with open("log.txt", "a") as log:
				try:
					log.write(f"User: {ctx.author.name}\nUserID: {ctx.author.id}\nData: {datetime.datetime.now().strftime('%H:%M:%S - %d/%m/%Y')}\nAção: {pessoa.name} -> {args[-1]}\n----------------------\n")
				except:
					log.write(f"UserID: {ctx.author.id}\nData: {datetime.datetime.now().strftime('%H:%M:%S - %d/%m/%Y')}\nAção: {pessoa.id} -> {args[-1]}\n----------------------\n")
	print(arquivo)
	with open("arquivo.json", "w") as arq:
		arq.write(json.dumps(arquivo))
		
@bot.command(name='scores')
async def scores(ctx):
	global arquivo
	mensagem = ''
	aux = {k: v for k, v in sorted(arquivo.items(), key=lambda x: -x[1])}
	i = 1
	for pessoa, score in aux.items():
		mensagem += f'{i}°: {pessoa} - {score}\n'
		i += 1
	await ctx.channel.send(mensagem)

@bot.command(name='score')
async def score(ctx):
	global arquivo
	try:
		await ctx.channel.send(f"<@!{ctx.message.author.id}> - {arquivo[f'<@!{ctx.message.author.id}>']}")
	except KeyError:
		await ctx.channel.send("Você ainda não foi registrado, peça para o admin te incluir na tabela")


@bot.command(name='tabela_')
async def tabela_(ctx):
	global prefix
	global arquivo
	guild = ctx.guild
	mensagem = ctx.message.content
	linhas = mensagem.split("\n")
	role1 = guild.get_role(783745705616474172)
	role2 = guild.get_role(783745719207067708)
	role3 = guild.get_role(783745728928415755)
	#role3> role2> role1
	if 783005043334840350 not in ctx.author.roles:
		await ctx.channel.send("Você não tem permissão para fazer isso")
	else:
		for linha in linhas:
			args = linha.split(" ")
			if args[0] == f"{prefix}tabela":
				try:
					arquivo[args[1]] += int(args[-1])
				except KeyError:
					arquivo[args[1]] = 1000
					arquivo[args[1]] += int(args[-1])
				id_ = int(args[1].split("!")[1].split(">")[0])
				pessoa = await guild.fetch_member(id_)
				if arquivo[args[1]] > 1010: 
					await pessoa.add_roles(role1, role2, role3)
				elif arquivo[args[1]] > 1005: 
					await pessoa.add_roles(role1, role2)
					await pessoa.remove_roles(role3)
				elif arquivo[args[1]] > 1000:
					await pessoa.add_roles(role1)
					await pessoa.remove_roles(role2, role3)
				with open("log.txt", "a") as log:
					try:
						log.write(f"User: {ctx.author.name}\nUserID: {ctx.author.id}\nData: {datetime.datetime.now().strftime('%H:%M:%S - %d/%m/%Y')}\nAção: {pessoa.name} -> {args[-1]}\n----------------------\n")
					except:
						log.write(f"UserID: {ctx.author.id}\nData: {datetime.datetime.now().strftime('%H:%M:%S - %d/%m/%Y')}\nAção: {pessoa.id} -> {args[-1]}\n----------------------\n")
			else:
				try:
					arquivo[args[0]] += int(args[-1])
				except KeyError:
					arquivo[args[0]] = 1000
					arquivo[args[0]] += int(args[-1])
				id_ = int(args[0].split("!")[1].split(">")[0])
				pessoa = await guild.fetch_member(id_)
				if arquivo[args[0]] > 1010: 
					await pessoa.add_roles(role1, role2, role3)
				elif arquivo[args[0]] > 1005: 
					await pessoa.add_roles(role1, role2)
					await pessoa.remove_roles(role3)
				elif arquivo[args[0]] > 1000:
					await pessoa.add_roles(role1)
					await pessoa.remove_roles(role2, role3)
				with open("log.txt", "a") as log:
					try:
						log.write(f"User: {ctx.author.name}\nUserID: {ctx.author.id}\nData: {datetime.datetime.now().strftime('%H:%M:%S - %d/%m/%Y')}\nAção: {pessoa.name} -> {args[-1]}\n----------------------\n")
					except:
						log.write(f"UserID: {ctx.author.id}\nData: {datetime.datetime.now().strftime('%H:%M:%S - %d/%m/%Y')}\nAção: {pessoa.id} -> {args[-1]}\n----------------------\n")
		print(arquivo)
		with open("arquivo.json", "w") as arq:
			arq.write(json.dumps(arquivo))


@bot.event
async def on_ready():
	print("o bot ta rodando")
bot.run(os.environ["BOT_CIV"])
