from spider.bots.aigc_bot.aigc_bot import AIGCBot
from spider.common import const


def create_bot(bot_type):
    if bot_type == const.AIGC:
        return AIGCBot()
