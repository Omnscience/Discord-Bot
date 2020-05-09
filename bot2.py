import re
import random
from discord.ext import commands
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import argparse

TOKEN =''
GUILD =''

bot = commands.Bot(command_prefix="!")
@bot.command (name='SEC', help = 'Responds with quote about Tennessee Football')
async def SEC (ctx):
	SEC_quotes = [
	'Touchdown !!!', 'Give Him Six',
	(
	'Peyton is the GOAT',
	'Neyland seates 102,000'
	),
	]
	response = random.choice (SEC_quotes)
	await ctx.send(response)

@bot.command (name = 'date', help = 'Responds with current date and time')
async def date (ctx):
	now = datetime.now()
	date = now.strftime ("%m/%d/%Y, %H:%M:%S")
	response = date
	await ctx.send (response)

@bot.command(name = "JobSearch", help = "Responds with a search from Monster.com")
async def JobSearch (ctx,args1,args2):
	q = args1
	where = args2
	URL =("https://www.monster.com/jobs/search/?q=%s&where=%s"% (q,where))
	page = requests.get(URL)
	soup = BeautifulSoup(page.content, "html.parser")
	results = soup.find(id='ResultsContainer')
	response = URL
	await ctx.send (response)




	i=0
	job_elems = results.find_all('section', class_ ='card-content')
	while i <1:
		for job_elem in job_elems:
			title_elem = job_elem.find('h2', class_ = 'title')
			company_elem = job_elem.find('div', class_ ='company')
			location_elem = job_elem.find('div', class_ ='location')
			if None in (title_elem, company_elem, location_elem):continue
		response =title_elem.text.strip(), company_elem.text.strip(),location_elem.text.strip()
                await ctx.send(response)

		i=i+1
	
bot.run(TOKEN)





