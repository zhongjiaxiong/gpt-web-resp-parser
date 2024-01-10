### 2024.1.10
新增extractor目录存放img,text,xpath等提取器 
主要构想是使用gpt的不同能力来提取信息 
1. image_extractor提取器使用gpt的解读图像能力通过图像来提取信息
2. text_extractor提取器使用gpt的解读文本能力通过文本来提取信息
3. xpath_extractor提取器使用gpt来提取xpath

next step:
1. 将gpt接口封装成一个类
2. 配置文件的读取gpt的相关参数
3. image_extractor的初步想法是使用playwright等工具来截图，然后使用gpt来解读图像
4. 

想法：
1. 存储部分账号信息，让gpt来随机选择账号信息，然后使用账号信息来登录网站，然后爬取信息
