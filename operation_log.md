#### extractor
1. image_extractor提取器使用gpt的解读图像能力通过图像来提取信息
2. text_extractor提取器使用gpt的解读文本能力通过文本来提取信息
3. xpath_extractor提取器使用gpt来提取xpath

#### bridge
1. bridge是一个桥梁，用来通过配置选择不同平台的gpt接口
2. context存放当前内容信息的类型，比如是文本还是图像
3. reply存放回复信息的类型

#### bot
1. bot就是每个gpt平台用来执行操作的类
2. bot.py是一个抽象类，用来定义bot的接口
3. bot_factory.py是一个工厂类，用来创建bot
4. 已经添加了一个bot的实现类，aigc_bot就是钱多多的那个平台

next step:
1. 将gpt接口封装成一个类
2. 配置文件的读取gpt的相关参数
3. image_extractor的初步想法是使用playwright等工具来截图，然后使用gpt来解读图像


想法：
1. 存储部分账号信息，让gpt来随机选择账号信息，然后使用账号信息来登录网站，然后爬取信息
