import pytest

from spider.bots.aigc_bot.aigc_bot import AIGCBot
from spider.bridge.reply import ReplyType
from spider.bridge.context import ContextType, Context


@pytest.fixture
def demo_class():
    return AIGCBot()


def test_chat_retry_count_greater_than_two(mocker, demo_class):
    context = Context(ContextType.TEXT, "Hello")
    mocker.patch("requests.post", side_effect=Exception("Test Exception"))
    reply = demo_class._chat(context, retry_count=3)
    assert reply.content == "我好像出了点问题，等我修复一下再来找我聊天吧"


def test_chat_success(mocker, demo_class):
    context = Context(ContextType.TEXT, "Hello")
    mock_post = mocker.patch("requests.post")
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {
        "choices": [
            {
                "message": {
                    "content": "Hello",
                },
            },
        ],
        "usage": {
            "total_token": 100,
        },
    }
    reply = demo_class._chat(context)
    assert reply.content == "Hello"
    assert reply.type == ReplyType.TEXT
    assert mock_post.call_count == 1
