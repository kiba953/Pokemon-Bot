import discord
from discord.ext import commands
import sqlite3
import random
import math
import typing
from typing import Union


bot = commands.Bot(command_prefix=['p!','P!'],case_insensitive = True,intents = discord.Intents.all())




s= False
mc = 1
name=''
url=''
@bot.event
async def on_message(message):
	global mc
	global s
	
	if not message.author.bot:
		if message.content.lower().startswith('p!catch'):
			yoy=1
		else:
			mc+=1
		if (mc%7==0):
			conn=sqlite3.connect('./database.db')
			cur=conn.cursor()
			global name
			global url
			global fname
			global gname
			global g
			global Channel
			global jname
			global jname2
			global jname3
			global other
			global oN
			global id
			Channel =bot.get_channel(796240947000246294)
			#replace with your channel id
			g = random.randint(1,151)
			cur.execute('''SELECT * FROM pokedex WHERE id =? and Shiny='No';''',(g,))
			for rows in cur:
				id = rows[0]
				name = rows[1]
				gname = rows[2].lower()
				fname= rows[4].lower()
				url=rows[12]
				jname=rows[3].lower()
				jname2=rows[16].lower()
				jname3 = rows[17].lower()
				oN=rows[15].lower()
				embed = discord.Embed(color=discord.Color(0xFFFDD0),title= 'A wild poke woah')
				file= discord.File(url,filename='poke.png')
				embed.set_image(url='attachment://poke.png')
				await Channel.send(embed=embed,file=file)
				s = True
			conn.commit()
			conn.close()
				

		if mc==500:
			mc=1
		await bot.process_commands(message)
				
@bot.command()
async def catch(ctx,arg):
		global Channel
		if ctx.channel == Channel:
			global g
			global gname
			global name
			global s
			global mc
			global fname
			global jname
			global url
			global U
			global id
			global jname2
			global jname3
			global oN
			mc+=1
			go =False
			conn=sqlite3.connect('./database.db')
			cur4 = conn.cursor()
			cur4.execute('''SELECT * FROM people WHERE id =?;''',(ctx.author.id,))
			for rows in cur4:
				go = True
			if go==True:
				if s == True:
					if arg.lower() in (name.lower(),gname,fname,jname,jname2,jname3,oN):
						x=random.randint(1,2)
						z1=random.randint(1,11)#spatk
						z2=random.randint(1,11)#atk
						z3=random.randint(1,11) #speed
						z4=random.randint(1,10) #def
						z5=random.randint(1,11)#spdef
						z6=random.randint(1,10)#hp
						n1,n2,n3,n4,n5,n6 = randomIV(z1,z2,z3,z4,z5,z6)
						total = n1+n2+n3+n4+n5+n6
						m = total*10000
						n=m/186            #(186= sum of ivs)
						u= (math.floor(n))
						h=u/100
						user = ctx.author.id
						cur2 = conn.cursor()
						cur2.execute('''SELECT * FROM info WHERE user_id=? LIMIT 1 OFFSET 0;''',(user,))
						for rows in cur2:
							so=rows[12]
						if x==2:
							cur = conn.cursor()
							cur.execute('''SELECT COUNT(*) FROM info WHERE user_id=?;''',(user,))
							for rows in cur:
								num = rows[0]
							cur.execute('''INSERT INTO info(dex_id,user_id,Hp,Atk,Def,SpAtk,SpDef,Speed,Number,Shiny,url,name,sort,num)VALUES(?,?,?,?,?,?,?,?,?,'No',?,?,?,?);''',(id,user,n1,n2,n3,n4,n5,n6,h,url,name,so,num+1,))
							member = ctx.author
							await ctx.send('Congratulations '+ member.mention+'! You caught a level 3 '+name+'!')
						else:
							cur3 = conn.cursor()
							cur1 = conn.cursor()
							cur3.execute('''SELECT COUNT(*) FROM info WHERE user_id=?;''',(user,))
							for rows in cur3:
								num = rows[0]
							cur1.execute('''SELECT URL FROM pokedex WHERE id =? and Shiny ='Yes';''',(id,) )
							for rows in cur1:
								ur = rows[0]
							cur = conn.cursor()
							cur.execute('''INSERT INTO info(dex_id,user_id,Hp,Atk,Def,SpAtk,SpDef,Speed,Number,Shiny,url,name,sort,num)VALUES(?,?,?,?,?,?,?,?,?,'Yes',?,?,?,?);''',(id,user,n1,n2,n3,n4,n5,n6,h,ur,name,so,num+1,))
							member = ctx.author
							await ctx.send('Congratulations '+ member.mention+'! You caught a level 3 Shiny '+name+'!')
							s = False
					else:
						await ctx.send('Try again')
				else:
					await ctx.send('You need to pick a starter!')
				conn.commit()
				conn.close()

				if (mc%3==0):
					conn=sqlite3.connect('./database.db')
					cur=conn.cursor()
					Channel =bot.get_channel(796240947000246294)
					g = random.randint(1,151)
					cur.execute('''SELECT * FROM pokedex WHERE id =? and Shiny='No';''',(g,))
					for rows in cur:
						id = rows[0]
						name = rows[1]
						gname = rows[2].lower()
						fname= rows[4].lower()
						url=rows[12]
						jname=rows[3].lower()
						jname1=rows[16].lower()
						jname2 = rows[17].lower()
						oN=rows[15].lower()
						embed = discord.Embed(color=discord.Color(0xFFFDD0),title= 'A wild poke woah')
						file= discord.File(url,filename='poke.png')
						embed.set_image(url='attachment://poke.png')
						await ctx.send(embed=embed,file=file)
						s = True
					conn.commit()
					conn.close()
						
	  

					
					
					
					
					
					
					
					


@bot.command(aliases=['pokedex'])
async def dex(ctx,*args):
	if not ctx.message.author.bot:	
		print(args)
		conn = sqlite3.connect('./database.db')
		cur = conn.cursor()
		if args[0].lower() == 'shiny':
			a = (args[1].lower())
			b=(a,a,a,a,a,a,a)
			cur.execute('''SELECT * FROM pokedex WHERE (LOWER(name) =? or LOWER(German_name)=? or LOWER(Japanese_name)=? or LOWER(French_name)=? or LOWER(Japanese_name2)=? or LOWER(Japanese_name3)=? or LOWER(Other)=?)and Shiny = 'Yes';''',b)
			for rows in cur:
				embed = discord.Embed(colour=discord.Colour(0x00FFFF),title=' Professor Oak\n#'+str(rows[0])+' - '+rows[1]+' ⭐',description=rows[11])
				embed.add_field(name='Alternative Names',value='🇩🇪 '+rows[2] +'\n🇯🇵 '+rows[3] +'/'+rows[16]+'/'+rows[17]+'\n🇲🇫 '+rows[4])
				embed.add_field(name='Base Stats',value='**HP: **'+str(rows[5])+'\n**Attack: **'+str(rows[6])+'\n**Defense: **'+str(rows[7])+'\n**Sp. Atk: **'+str(rows[8])+'\n**Sp. Def: **'+str(rows[9])+'\n**Speed: **'+str(rows[10]))
				if rows[18] !='No':
					embed.add_field(name='Types:',value=rows[13]+' | '+rows[18])
				else:
					embed.add_field(name='Types:',value=rows[13])
				file=discord.File(rows[12],filename='poke.png')
				embed.set_image(url='attachment://poke.png')
				cur1 = conn.cursor()
				cur1.execute('''SELECT COUNT(*) FROM info WHERE dex_id=?;''',(rows[0],))
				for row in cur1:
					tot = row[0]
				embed.set_footer(text='You\'ve caught'+str(tot)+' of this pokémon!')
				member = ctx.message.author
				mem = str(member)
				name = mem.split('#')
				embed.set_author(name=f"{name[0]}", icon_url=member.display_avatar)
				await ctx.send(embed=embed,file=file)
		
		else:
			a=args[0].lower()
			print(a)
			b=(a,a,a,a,a,a,a)
			cur.execute("""SELECT * FROM pokedex WHERE (LOWER(name) =? or LOWER(German_name)=? or LOWER(Japanese_name)=? or LOWER(French_name)=? or LOWER(Japanese_name2)=? or LOWER(Japanese_name3)=? or LOWER(Other)=?)and Shiny = 'No';""",b)
			for rows in cur:
				embed = discord.Embed(colour=discord.Colour(0x00FFFF),title=' Professor Oak\n#'+str(rows[0])+' - '+rows[1],description=rows[11])
				embed.add_field(name='Alternative Names',value='🇩🇪 '+rows[2] +'\n🇯🇵 '+rows[3]+'/'+rows[16]+'/'+rows[17]+'\n🇲🇫 '+rows[4])
				embed.add_field(name='Base Stats',value='**HP: **'+str(rows[5])+'\n**Attack: **'+str(rows[6])+'\n**Defense: **'+str(rows[7])+'\n**Sp. Atk: **'+str(rows[8])+'\n**Sp. Def: **'+str(rows[9])+'\n**Speed: **'+str(rows[10]))
				if rows[18] != 'No':
					embed.add_field(name='Types:',value=rows[13]+' | '+rows[18])
				else:
					embed.add_field(name='Types:',value=rows[13])
				file=discord.File(rows[12],filename='poke.png')
				embed.set_image(url='attachment://poke.png')
				cur1 = conn.cursor()
				cur1.execute('''SELECT COUNT(*) FROM info WHERE dex_id=?;''',(rows[0],))
				for row in cur1:
					tot = row[0]
				embed.set_footer(text='You\'ve caught '+str(tot)+' of this pokémon!')
				member = ctx.message.author
				mem = str(member)
				name = mem.split('#')
				embed.set_author(name=f"{name[0]}", icon_url=member.display_avatar)
				await ctx.send(embed=embed,file=file)
		conn.commit()
		conn.close()
	




@bot.command()
async def info(ctx,arg:Union[int,str]):
	if (isinstance(arg,int)):
		conn = sqlite3.connect('./database.db')
		user = ctx.author.id
		cur = conn.cursor()
		cur1 = conn.cursor()
		cur1.execute('''SELECT COUNT(*) FROM info WHERE user_id=?;''',(user,))
		for row in cur1:
			tp = row[0]
		cur.execute('''SELECT * FROM info WHERE user_id=? LIMIT 1 OFFSET ?;''',(user,arg-1,))
		for rows in cur:
			ag=rows[13]
			embed = discord.Embed(color=discord.Color(0xFFFDD0),description='\n**HP: **'+str(rows[2])+'/31\n**Attack: **'+str(rows[3])+'/31\n**Defense: **'+str(rows[4])+'/31\n**Sp. Atk: **'+str(rows[5])+'/31\n**Sp. Def: **'+str(rows[6])+'/31\n**Speed: **'+str(rows[7])+'/31\n**Total IV: **'+str(rows[8]))
			member = ctx.message.author
			mem = str(member)
			name = mem.split('#')
			embed.set_author(name=f"{name[0]}", icon_url=member.display_avatar)
			file = discord.File(rows[10],filename='pok.png')
			embed.set_image(url='attachment://pok.png')
			embed.set_footer(text='Displaying Pokémon: '+str(ag)+'/'+str(tp)+'among all your pokémons')
			await ctx.send(embed=embed,file=file)
		conn.commit()
		conn.close()
	elif(isinstance(arg,str)):
		if arg.lower() == 'latest':
			conn = sqlite3.connect('./database.db')
			user = ctx.author.id
			cur = conn.cursor()
			cur1 = conn.cursor()
			cur1.execute('''SELECT COUNT(*) FROM info WHERE user_id=?;''',(user,))
			for rows in cur1:
				tp = rows[0]
			cur.execute('''SELECT * FROM info WHERE user_id=? LIMIT 1 OFFSET ?;''',(user,tp-1,))
			for rows in cur:
				if rows[9]=='Yes':
					embed = discord.Embed(color=discord.Color(0xFFFDD0), title='⭐'+ rows[11],description='\n**HP: **'+str(rows[2])+'/31\n**Attack: **'+str(rows[3])+'/31\n**Defense: **'+str(rows[4])+'/31\n**Sp. Atk: **'+str(rows[5])+'/31\n**Sp. Def: **'+str(rows[6])+'/31\n**Speed: **'+str(rows[7])+'/31\n**Total IV: **'+str(rows[8]))
				else:
					embed = discord.Embed(color=discord.Color(0xFFFDD0), title= rows[11],description='\n**HP: **'+str(rows[2])+'/31\n**Attack: **'+str(rows[3])+'/31\n**Defense: **'+str(rows[4])+'/31\n**Sp. Atk: **'+str(rows[5])+'/31\n**Sp. Def: **'+str(rows[6])+'/31\n**Speed: **'+str(rows[7])+'/31\n**Total IV: **'+str(rows[8]))
				

				member = ctx.message.author
				mem = str(member)
				name = mem.split('#')
				embed.set_author(name=f"{name[0]}", icon_url=member.display_avatar)
				file = discord.File(rows[10],filename='pok.png')
				embed.set_image(url='attachment://pok.png')
				embed.set_footer(text='Displaying Pokémon: '+str(tp)+'/'+str(tp)+'among all your pokémons')
				await ctx.send(embed=embed,file=file)
   	    	

   		
   		





@bot.command()
async def pokemon(ctx,*args):
	if len(args) != 0:
		try:
			arg=int(args[0])
		except:
			arg=args[0]
		if type(arg)==int:
			conn = sqlite3.connect('./database.db')
			Shiny1 ='Yes'
			Shiny2 ='No'
			cur = conn.cursor()
			for i in range(0,len(args)):
				if (args[i]).lower() in('--s','--shiny'):
					Shiny2='Yes'
			mem = ctx.author.id
			cur1 = conn.cursor()
			cur1.execute('''SELECt COUNT(*),sort FROM info WHERE Shiny IN(?,?) and user_id=?;''',(Shiny1,Shiny2,mem))
			for row in cur1:
				j = row[0]
				e = row[1]
			op = (arg -1)*20
			if e=='id':
				cur.execute('''SELECT * FROM info WHERE Shiny IN(?,?) and user_id =? LIMIT 20 OFFSET ?;''',(Shiny1,Shiny2,mem,op,))
			if e =='iv':
				cur.execute('''SELECT * FROM info WHERE Shiny IN(?,?) and user_id=? ORDER BY Number Desc LIMIT 20 OFFSET ?;''',(Shiny1,Shiny2,mem,op,))
			g =''
			x= ((arg-1)*20)+1
			f = x
			for rows in cur:
				if rows[9] =='No':
					g = g +'**'+ rows[11]+'** | Number: '+str(rows[13])+' | '+'IV: '+str(rows[8])+'%\n'
				if rows[9]=='Yes':
					g = g +'**'+ rows[11]+'** ⭐ | Number: '+str(rows[13])+' | '+'IV: '+str(rows[8])+'%\n'
				i=rows[13]
			embed = discord.Embed(color = discord.Color(0xFFFDD0),title='Your Pokemon',description=g)
			embed.set_footer(text='Showing'+str(f)+'-'+str(x-1)+' of '+str(j) +' pokémon (page '+str(f)+' of '+str(int((j-(j%20))/20)+1)+' ) matching this search.')
			await ctx.send(embed=embed)
			conn.commit()
			conn.close()

		elif type(arg)==str:
			arg = 1
			conn = sqlite3.connect('./database.db')
			Shiny1 ='Yes'
			Shiny2 ='No'
			cur = conn.cursor()
			for i in range(0,len(args)):
				if (args[i]).lower() in('--s','--shiny'):
					Shiny2='Yes'
				if (args[i].lower())=='--n':
					name = args[i+1].lower()
			mem = ctx.author.id
			cur1 = conn.cursor()
			cur1.execute('''SELECt COUNT(*),sort FROM info WHERE Shiny IN(?,?) and user_id=? and LOWER(name)=?;''',(Shiny1,Shiny2,mem,name,))
			for row in cur1:
				j = row[0]
				e = row[1]
			op = (arg -1)*20
			if e=='id':
				cur.execute('''SELECT * FROM info WHERE Shiny IN(?,?) and user_id =? and LOWER(name)=? LIMIT 20 OFFSET ? and name=?''',(Shiny1,Shiny2,mem,name,op,))
			if e =='iv':
				cur.execute('''SELECT * FROM info WHERE Shiny IN(?,?) and user_id=? and LOWER(name)=? ORDER BY Number Desc LIMIT 20 OFFSET ?;''',(Shiny1,Shiny2,mem,name,op,))
			g =''
			x= ((arg-1)*20)+1
			f = x
			for rows in cur:
				if rows[9] =='No':
					g = g +'**'+ rows[11]+'** | Number: '+str(rows[13])+' | '+'IV: '+str(rows[8])+'%\n'
				if rows[9]=='Yes':
					g = g +'**'+ rows[11]+'** ⭐ | Number: '+str(rows[13])+' | '+'IV: '+str(rows[8])+'%\n'
				i=rows[13]
				
			embed = discord.Embed(color = discord.Color(0x00FFFF),title='Your Pokemon',description=g)
			embed.set_footer(text='Showing'+str(f)+'-'+str(x-1)+' of '+str(j) +' pokémon (page '+str(f)+' of '+str(int((j-(j%20))/20)+1)+' ) matching this search.')
			await ctx.send(embed=embed)
			conn.commit()
			conn.close()
		
		elif len(args)==0:
			arg=1
			conn = sqlite3.connect('./database.db')
			Shiny1 ='Yes'
			Shiny2 ='No'
			cur = conn.cursor()
			for i in range(0,len(args)):
				if (args[i]).lower() in('--s','--shiny'):
					Shiny2='Yes'
			mem = ctx.author.id
			cur1 = conn.cursor()
			cur1.execute('''SELECt COUNT(*),sort FROM info WHERE Shiny IN(?,?) and user_id=?;''',(Shiny1,Shiny2,mem,))
			for row in cur1:
				j = row[0]
				e = row[1]
			op = (arg -1)*20
			if e=='id':
				cur.execute('''SELECT * FROM info WHERE Shiny IN(?,?) and user_id =? LIMIT 20 OFFSET ?;''',(Shiny1,Shiny2,mem,op,))
			if e =='iv':
				cur.execute('''SELECT * FROM info WHERE Shiny IN(?,?) and user_id=? ORDER BY Number Desc LIMIT 20 OFFSET ?;''',(Shiny1,Shiny2,mem,op,))
			g =''
			x = ((arg-1)*20)+1
			f = x
			for rows in cur:
				if rows[9] =='No':
					g = g +'**'+ rows[11]+'** | Number: '+str(rows[13])+' | '+'IV: '+str(rows[8])+'%\n'
				if rows[9]=='Yes':
					g = g +'**'+ rows[11]+'** ⭐ | Number: '+str(rows[13])+' | '+'IV: '+str(rows[8])+'%\n'
				i=rows[13]
				x+=1
			embed = discord.Embed(color = discord.Color(0xFFFDD0),title='Your Pokemon',description=g)
			embed.set_footer(text='Showing'+str(f)+'-'+str(x-1)+' of '+str(j) +' pokémon (page '+str(f)+' of '+str(int((j-(j%20))/20)+1)+' ) matching this search.')
			await ctx.send(embed=embed)
			conn.commit()
			conn.close()
   					
   					
 
   					
   			
   			
   			
@bot.command()
async def sort(ctx,arg):
	conn = sqlite3.connect('./database.db')
	if arg.lower() =='iv':
		id = ctx.author.id
		cur = conn.cursor()
		cur.execute('''UPDATE info SET sort=? WHERE user_id =?;''',('iv',id,))
		await ctx.send('Your Pokemon have been sorted by there iv')

	if arg.lower() =='id':
		id = ctx.author.id
		cur = conn.cursor()
		cur.execute('''UPDATE info SET sort=? WHERE user_id =?;''',('id',id,))
		await ctx.send('Your Pokemon have been sorted by their id')
	conn.commit()
	conn.cursor()
   			
@bot.command()
async def pick(ctx,args):
	conn = sqlite3.connect('./database.db')
	cur = conn.cursor()
	g = False
	arg = args.lower()
	cur3 = conn.cursor()
	cur3.execute('''SELECT * FROM people WHERE id =?;''',(ctx.author.id,))
	for rows in cur3:
		g = True
	if g ==False:
		if arg in('charmander','squirtle','bulbasaur'):
			cur.execute('''SELECT * FROM pokedex WHERE (LOWER(name)=?) and Shiny='No';''',(arg,))
			for rows in cur:
				cur1 = conn.cursor()
				cur1.execute('''INSERT INTO info(dex_id,user_id,Hp,Atk,Def,SpAtk,SpDef,Speed,Number,Shiny,url,name,sort,num)VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?);''',(rows[0],ctx.author.id,15,15,15,15,15,15,48.38,'No',rows[12],rows[1],'id',1,))
				name = rows[1]
				cur4 = conn.cursor()
				cur4.execute('''INSERT INTO people(id)VALUES (?);''',(ctx.author.id,))
				await ctx.send('Congratulations u got a level 1 '+name)
		else:
			await ctx.send(arg+' is not a valid starter!')
	else:
		await ctx.send('You have already picked a starter')
	conn.commit()
	conn.close()
   				
   				
@bot.command()
async def start(ctx):
	member = ctx.message.author
	mem = str(member)
	names= mem.split('#')
	name=names[0]
	embed = discord.Embed(color=discord.Color(0xFFFDD0))
	embed.add_field(name='Welcome to the world of pokémon!',value='To begin play,choose one of these pokémon\n with the `p!pick <pokémon>`'+' command,like this:\n`p!pick squirtle`',inline=True)
	embed.add_field(name='Generation I:',value='Bulbasaur | Squirtle | Charmander',inline=True)
	embed.set_author(name=f'Hello {name} !',icon_url=member.display_avatar)
	await ctx.send(embed=embed)
 	
   			
   			
   			
   			

@bot.command()
async def redeem(ctx,*args):
	conn = sqlite3.connect('./database.db')
	cur = conn.cursor()
	if args[0].lower()=='shiny':
		cur.execute('''SELECT * FROM pokedex WHERE Shiny ='Yes' and lower(name)=?;''',(args[1].lower(),))
		neme = args[1].lower()
	else:
		cur.execute('''SELECT * FROM pokedex WHERE Shiny ='No' and lower(name)=?;''',(args[0].lower(),))
		neme = args[0].lower()
	for rows in cur:
		url = rows[12]
		names=rows[1]
		id = rows[0]
	if (neme in (names.lower())):
		x=random.randint(1,2)
		z1=random.randint(1,11)#spatk
		z2=random.randint(1,11)#atk
		z3=random.randint(1,11) #speed
		z4=random.randint(1,10) #def
		z5=random.randint(1,11)#spdef
		z6=random.randint(1,10)#hp
		n1,n2,n3,n4,n5,n6 = randomIV(z1,z2,z3,z4,z5,z6)
		total = n1+n2+n3+n4+n5+n6
		m = total*10000
		n=m/186            #(186= sum of ivs)
		u= (math.floor(n))
		h=u/100
		user = ctx.author.id
		cur2 = conn.cursor()
		cur2.execute('''SELECT * FROM info WHERE user_id=? LIMIT 1 OFFSET 0;''',(user,))
		for rows in cur2:
			so=rows[12]
		cur= conn.cursor()
		cur.execute('''SELECT Count(*) FROM info WHERE user_id=?;''',(user,))
		for rows in cur:
			g=rows[0]
		cur.execute('''INSERT INTO info(dex_id,user_id,Hp,Atk,Def,SpAtk,SpDef,Speed,Number,Shiny,url,name,sort,num)VALUES(?,?,?,?,?,?,?,?,?,'No',?,?,?,?);''',(id,user,n1,n2,n3,n4,n5,n6,h,url,names,so,g+1))
		member = ctx.author
		await ctx.send('Congratulations '+member.mention+'You have been given a '+names)
	conn.commit()
	conn.close()

		
def randomIV(x1,x2,x3,x4,x5,x6):
	if 1==x1 or x3 ==2:
		n1=random.randint(22,31)
	elif 5 ==x1 or 9==x1:
		n1=random.randint(18,25)
	elif x1==6 or x1==4:
		n1 =random.randint(0,8)
	elif x1 ==10 or x1==8:
		n1= random.randint(6,13)
	else:
		n1 =random.randint(10,19)
	if 1==x2 or x2==2:
		n2=random.randint(24,31)
	elif 5 ==x2 or x3==3:
		n2=random.randint(18,25)
	elif x2==6 or x2 ==4:
		n2=random.randint(0,8)
	elif x2==10 or x2==8:
		n2= random.randint(6,13)
	else:
		n2 =random.randint(10,19)
	if 1==x3 or x3==2:
		n3=random.randint(22,31)
	elif 5 ==x3 or x3==3:
		n3=random.randint(18,25)
	elif x3==6 or x3==4:
		n3 =random.randint(0,8)
	elif x3==10 or x3==8:
		n3= random.randint(7,13)
	else:
		n3 =random.randint(10,19)
	if 1==x4 or x4 ==2:
		n4=random.randint(24,31)
		
	elif 5 ==x4 or  x4==3:
		n4=random.randint(18,26)
	elif x4==6 or x4==4:
		n4 =random.randint(0,8)
	elif x4==7 or x4==8:
		n4= random.randint(8,13)
	else:
		n4 =random.randint(10,20)
	if 1==x5 or x5==2:
		n5=random.randint(24,31)
	elif 5 ==x5 or 9==x5:
		n5=random.randint(19,26)
	elif x5==6 or x5==4:
		n5 =random.randint(0,7)
	elif x5==10 or x5==8:
		n5= random.randint(7,13)
	else:
		n5 =random.randint(10,20)
	if 1==x6 or x6==2:
		n6=random.randint(24,31)
	elif 5 ==x6 or 9==x6:
		n6=random.randint(19,26)
	elif x6==6 or x6==4:
		n6 =random.randint(0,7)
	elif x6==7 or x6==10:
		n6= random.randint(7,13)
	else:
		n6 =random.randint(10,19)
	return n1,n2,n3,n4,n5,n6
					
					
					
					
bot.run('insert bot token here')
			
