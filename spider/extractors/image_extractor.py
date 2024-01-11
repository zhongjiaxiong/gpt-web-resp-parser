from spider.extractors.extractor import Extractor


class ImageExtractor(Extractor):
    def __init__(self):
        super().__init__()

    def extract(self):
        pass

    def _extract_by_image(self, web_screenshot_img,key_list):
        '''
        该方法用于从网页截图中提取图片信息
        :param img: 网页截图，但是不知道列表页面是否能顺利提取，有待测试
        :param key_list: 需要提取的信息的关键词列表
        :return: 图片中的信息
        '''
        pass