from common import const


def create_bot(bot_type):
    if bot_type == const.AIGC:
        from bot.aigc_bot.aigc_bot import AIGCBot
        return AIGCBot()