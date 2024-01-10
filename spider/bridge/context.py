from enum import Enum


class ContextType(Enum):
    TEXT = 1  # 文本消息
    IMAGE = 2  # 图片消息
    FILE = 3  # 文件信息
    VIDEO = 4  # 视频信息


class Context:
    def __init__(self, type: ContextType = None, content=None):
        self.type = type
        self.content = content
