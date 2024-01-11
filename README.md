# desc
目标是做一个基于gpt的通用爬虫解析框架


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

