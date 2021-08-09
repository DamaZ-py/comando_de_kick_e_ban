'• Commands to error handling'
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Por favor, passe todos os requerimentos  👀') # Please, pass all the requirements
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Você não possui todos requerimentos !! 😡" ) # You doesn't have all the requirements

'• Commands to kick users'
@client.command(name="kick", help="comando para expulsar usuários do servidor") 
@commands.has_permissions(ban_members=True)
async def _kick(self, member: discord.Member, *, reason=None):
    guild = member.guild
    channel = discord.utils.get(guild.channels, id=809233945945440256)
    try:
        await member.kick(reason=reason)
        await self.message.delete()
        await channel.send(f'🧨 {member.name} foi expulso de {self.guild.name}'
                        f'Motivo {reason}')
    except Exception:
        await self.channel.send(f"O bot não tem permissão suficiente para expulsar alguém. Atualize as permisiões")

'• Commands to banned users'
@client.command(name="ban", help="comando para banir usuários do servidor") # command to ban users from the server
@commands.has_permissions(ban_members=True)
async def _ban(self, member: discord.Member, *, reason=None):
    guild = member.guild
    channel = discord.utils.get(guild.channels, id=809233945945440256)
    try:
        await member.ban(reason=reason)
        await self.message.delete()
        await self.channel.send(f'🧨 {member.name} foi banido de {self.guild.name}' # <user.name> has been banned from <guild.name> 
                               f'Motivo: {reason}') 
    except Exception:
        await self.channel.send(f"O bot não tem permissão suficiente para banir alguém. Atualize as permissões !") # Bot doesn't enough permission to ban someone. Upgrade the permission!

'• Command to unbanned users'
@client.command(name="unban", help="comando para desbanir usuário do servidor") # command to unban users from the server
@commands.has_permissions(administrator=True)
async def _unban(self, *, member_id: int):
    await self.guild.unban(discord.Object(id=member_id))
    await self.send(f"🔨 Unban {member_id}")

'• Commands for ping bot'
@client.command()
async def ping(self):
    await self.send(f'🏓 Pong\n{client.latency :.0f}ms')
