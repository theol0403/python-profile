from simulation.bot import *

bot = Bot.default15()

print(bot.orientation)

bot.move(2, 2, 1)

print(bot.orientation)
