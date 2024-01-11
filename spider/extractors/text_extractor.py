from spider.extractors.extractor import Extractor


class TextExtractor(Extractor):
    def __init__(self):
        super().__init__()

    def extract(self):
        pass

    def _extract_to_text(self, html,key_list):
        '''
        该方法用于从html中提取文本信息
        :param html: 简化后的html
        :param key_list: 需要提取的信息的关键词列表
        :return: json格式？
        '''

