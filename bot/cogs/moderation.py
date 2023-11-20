import asyncio
from discord import app_commands, Interaction, Member, Embed, Color, Object
from discord.utils import get
from discord.ext.commands import Cog, has_permissions
from typing import Optional
from datetime import datetime

from bot import bot, config


class Moderation(Cog):
    """Moderation cog for the bot"""

    def __init__(self, bot: bot.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="kick", description="Kicks a member", nsfw=False)
    @has_permissions(kick_members=True)
    async def kick(
        self,
        ctx: Interaction,
        *,
        member: Member,
        reason: Optional[str] = "You have been kicked!",
    ):
        """Kicks a user

        Args:
            ctx (Interaction): Command context
            member (Member): The member to be kicked
            reason (Optional[str], optional): The reason for the kick. Defaults to "You have been kicked!".
        """
        await ctx.guild.kick(member, reason=reason)
        embed = Embed(
            title="Kick Alert!",
            description="A user has been kicked from this server!",
            color=Color.blurple,
            timestamp=datetime.utcnow(),
        )
        embed.add_field(name="User", value=f"{member.name}", inline=True)
        embed.add_field(name="Reason", value=f"{reason}", inline=True)
        embed.set_footer(text="\u200b")
        await ctx.response.send_message(embed=embed)
        await ctx.response.defer()
        return

    @app_commands.command(name="ban", description="Bans a member", nsfw=False)
    @has_permissions(ban_members=True)
    async def ban(
        self,
        ctx: Interaction,
        *,
        member: Member,
        reason: Optional[str] = "You have been banned!",
    ):
        """Bans a member

        Args:
            ctx (Interaction): Command context
            member (Member): The member to be banned
            reason (Optional[str], optional): Reason for the ban. Defaults to "You have been banned!".
        """
        await ctx.guild.ban(member, reason=reason)
        embed = Embed(
            title="Ban Alert!",
            description="A user has been banned from this server!",
            color=Color.blurple,
            timestamp=datetime.utcnow(),
        )
        embed.add_field(name="User", value=f"{member.name}", inline=True)
        embed.add_field(name="Reason", value=f"{reason}", inline=True)
        embed.set_footer(text="\u200b")
        await ctx.response.send_message(embed=embed)
        await ctx.response.defer()
        return

    @app_commands.command(name="unban", description="Unbans a member", nsfw=False)
    @has_permissions(ban_members=True)
    async def unban(self, ctx: Interaction, *, member: Member):
        """Unbans a member

        Args:
            ctx (Interaction): Command context
            member (Member): The member to be unbanned
        """
        await ctx.guild.unban(member)
        embed = Embed(
            title="Unban Alert!",
            description="A user has been unbanned from this server!",
            color=Color.blurple,
            timestamp=datetime.utcnow(),
        )
        embed.add_field(name="User", value=f"{member.name}", inline=True)
        embed.set_footer(text="\u200b")
        await ctx.response.send_message(embed=embed)
        await ctx.response.defer()
        return

    @app_commands.command(
        name="tempban", description="Temporarily bans a member", nsfw=False
    )
    @has_permissions(ban_members=True)
    async def tempban(
        self,
        ctx: Interaction,
        *,
        member: Member,
        reason: Optional[str] = "You have been temporarily banned!",
        time: str,
    ):
        """Temporarily bans a member

        Args:
            ctx (Interaction): Command context
            member (Member): The member to be temporary banned
            reason (Optional[str], optional): Reason for the temporary ban . Defaults to "You have been temporarily banned!".
            time (converters.TimeConverter, optional): Time for the ban. Defaults to None.
        """
        await ctx.guild.ban(member, reason=reason)
        time_convert = {"s": 1, "m": 60, "h": 3600, "d": 86400}
        timee = int(time[0]) * time_convert[time[-1]]
        embed = Embed(
            title="Ban Alert!",
            description="A user has been temporarily banned from this server!",
            color=Color.blurple,
            timestamp=datetime.utcnow(),
        )
        embed.add_field(name="User", value=f"{member.name}", inline=True)
        embed.add_field(name="Reason", value=f"{reason}", inline=True)
        embed.add_field(name="Time", value=f"{time}", inline=True)
        embed.set_footer(text="\u200b")
        await ctx.response.send_message(embed=embed)
        if time:
            await asyncio.sleep(timee)
            await ctx.guild.unban(member)

        await ctx.response.defer()
        return

    @app_commands.command(
        name="mute", description="Temporarily mutes a member", nsfw=False
    )
    @has_permissions(kick_members=True)
    async def mute(
        self,
        ctx: Interaction,
        *,
        member: Member,
        reason: Optional[str] = "You have been temporarily muted!",
        time: str,
    ):
        """Temporarily bans a member

        Args:
            ctx (Interaction): Command context
            member (Member): The member to be temporary muted
            reason (Optional[str], optional): Reason for the temporary mute . Defaults to "You have been temporarily muted!".
            time (converters.TimeConverter, optional): Time for the mute. Defaults to None.
        """
        role = get(ctx.guild.roles, name="Muted")
        time_convert = {"s": 1, "m": 60, "h": 3600, "d": 86400}
        timee = int(time[0]) * time_convert[time[-1]]
        if role in member.roles:
            await member.add_roles(role)
            embed = Embed(
                title="Mute Alert!",
                description="A user has been temporarily muted from this server!",
                color=Color.blurple,
                timestamp=datetime.utcnow(),
            )
            embed.add_field(name="User", value=f"{member.name}", inline=True)
            embed.add_field(name="Reason", value=f"{reason}", inline=True)
            embed.add_field(name="Time", value=f"{time}", inline=True)
            embed.set_footer(text="\u200b")
            await ctx.response.send_message(embed=embed)
            if time:
                await asyncio.sleep(timee)
                await member.remove_roles(role)
            await ctx.response.defer()
            return
        else:
            await ctx.response.send_message("This member is already muted!")
            await ctx.response.defer()
            return

    @app_commands.command(name="unmute", description="Unmutes a member", nsfw=False)
    @has_permissions(kick_members=True)
    async def unmute(self, ctx: Interaction, *, member: Member):
        """Unmutes a member

        Args:
            ctx (Interaction): Command context
            member (Member): The member to be unmuted
        """
        role = get(ctx.guild.roles, name="Muted")
        if role in member.roles:
            embed = Embed(
                title="Mute Alert!",
                description="A user has been unmuted in this server!",
                color=Color.blurple,
                timestamp=datetime.utcnow(),
            )
            embed.add_field(name="User", value=f"{member.name}", inline=True)
            await ctx.response.send_message(embed=embed)
            await ctx.response.defer()
            return
        else:
            await ctx.response.send_message("This user is already unmuted!")
            await ctx.response.defer()
            return


async def setup(bot: bot.Bot):
    await bot.add_cog(Moderation(bot), guilds=[Object(id=config.SUPPORT_ID)])
