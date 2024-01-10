next step:
1. 将gpt接口封装成一个类
2. 配置文件的读取gpt的相关参数
3. image_extractor的初步想法是使用playwright等工具来截图，然后使用gpt来解读图像
4. text_extractor的初步想法是先清洗html，然后使用gpt解读文本提取信息，
目前有两个想法一个是将清洗好的html直接传给gpt，另一个是将html提取文本后再传给gpt
5. 写xpath_extractor的目的是为了gpt提取完一次信息的xpath后，可以通过xpath来提取下一次信息


想法：
1. 存储部分账号信息，让gpt来随机选择账号信息，然后使用账号信息来登录网站，然后爬取信息