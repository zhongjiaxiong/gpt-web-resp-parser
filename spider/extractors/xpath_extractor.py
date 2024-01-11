from spider.extractors.extractor import Extractor


class XPathExtractor(Extractor):
    def __init__(self):
        super().__init__()

    def extract(self):
        pass

    def _extract_to_xpath(self, html,key_list):
        '''
        该方法用于从html中提取xpath信息
        :param html: 初始html？还是简化后的html？
        :param key_list: 需要提取的信息的关键词列表
        :return: 需要信息的xpath 例如：作者的xpath，标题的xpath，正文的xpath
        '''