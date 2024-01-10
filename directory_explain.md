#### extractor
1. image_extractor提取器使用gpt的解读图像能力通过图像来提取信息
2. text_extractor提取器使用gpt的解读文本能力通过文本来提取信息
3. xpath_extractor提取器使用gpt来提取xpath

#### bridge
1. bridge是用来通过配置选择gpt的不同接口
2. context存放当前内容信息的类型，比如是文本还是图像
3. reply存放回复信息的类型

#### bot
1. bot就是每个gpt平台用来执行操作的类
2. bot.py是一个抽象类，用来定义bot的接口
3. bot_factory.py是一个工厂类，用来创建bot
4. aigc_bot就是钱多多的那个平台


#### common
1. const.py是一个常量类，用来存放一些常量
2. utils.py是一个工具类，用来存放一些工具函数


