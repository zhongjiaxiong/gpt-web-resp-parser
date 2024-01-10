# desc
目标是做一个基于gpt解析的通用爬虫框架


## 架构

```
-spider
  |- setting.py 读取配置文件并格式化
  |- .env 配置文件
  |- extractors
    |- image_extractor 通过 gpt 解析图片来提取信息
    |- text_extractor 通过 gpt 解析文本来提取信息
    |- xpath_extractor  通过 gpt 解析 xpath 来提取信息
  |- bridge
    |- bridge 用来通过配置选择 gpt 的不同接口
    |- context 存放当前内容信息的类型，比如是文本还是图像
    |- reply 存放回复信息的类型
  |- common
    |- const.py 存放一些常量
    |- utils.py 存放一些清洗html的工具函数
    |- default.py 存放一些默认配置
```

## Target

1. 将gpt接口封装成一个类
2. 配置文件的读取gpt的相关参数
3. image_extractor的初步想法是使用playwright等工具来截图，然后使用gpt来解读图像
4. text_extractor的初步想法是先清洗html，然后使用gpt解读文本提取信息，
目前有两个想法一个是将清洗好的html直接传给gpt，另一个是将html提取文本后再传给gpt
1. 写xpath_extractor的目的是为了gpt提取完一次信息的xpath后，可以通过xpath来提取下一次信息

想法：
1. 存储部分账号信息，让gpt来随机选择账号信息，然后使用账号信息来登录网站，然后爬取信息