from spider.bridge.context import Context
from spider.bridge.reply import Reply


class Bot(object):

    def reply(self, query, context: Context = None) -> Reply:
        """
        bot auto-reply content
        :param req: received message
        :return: reply content
        """
        raise NotImplementedError