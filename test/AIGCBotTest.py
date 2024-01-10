import unittest
from unittest.mock import patch, MagicMock
from bot.aigc_bot.aigc_bot import AIGCBot
from bridge.context import Context, ContextType
from bridge.reply import ReplyType


class TestDemoClass(unittest.TestCase):
    @patch('module.conf')
    @patch('module.requests.post')
    def test__chat_success(self, mock_post, mock_conf):
        # Mock configuration values
        mock_conf.side_effect = lambda key: {
            'aigc_api_key': 'api_key',
            'aigc_model': 'model',
            'aigc_top_p': 2,
            'aigc_temperature': 2,
            'frequency_penalty': 0.1,
            'presence_penalty': 0.1
        }.get(key)

        # Mock response from requests.post
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {
            'choices': [{'message': {'content': 'Hello'}}],
            'usage': {'total_token': 100}
        }

        # Create DemoClass instance
        demo = AIGCBot()
        context = Context(type=ContextType.TEXT, content='Hello')
        # Call _chat method
        reply = demo._chat(context)

        # Assert the return value
        self.assertEqual(reply.type, ReplyType.TEXT)
        self.assertEqual(reply.content, 'Hello')
        mock_conf.assert_called_with('aigc_api_key')
        mock_post.assert_called_with(
            url='http://example.com/v1/chat/completions',
            json={
                'model': 'model',
                'messages': [{'role': 'user', 'content': 'Hello'}],
                'top_p': 2,
                'temperature': 2,
                'frequency_penalty': 0.1,
                'presence_penalty': 0.1
            },
            headers={
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'Authorization': 'api_key'
            }
        )

    @patch('module.conf')
    @patch('module.requests.post')
    def test__chat_retry(self, mock_post, mock_conf):
        # Mock configuration values
        mock_conf.side_effect = lambda key: {
            'aigc_api_key': 'api_key',
            'aigc_model': 'model',
            'aigc_top_p': 2,
            'aigc_temperature': 2,
            'frequency_penalty': 0.1,
            'presence_penalty': 0.1
        }.get(key)

        # Mock response from requests.post
        mock_post.side_effect = Exception('Test exception')

        # Create DemoClass instance
        demo = AIGCBot()
        context = Context(type=ContextType.TEXT, content='Hello')
        # Call _chat method
        reply = demo._chat(context)

        # Assert the return value
        self.assertEqual(reply.type, ReplyType.TEXT)
        self.assertEqual(reply.content, '我好像出了点问题，等我修复一下再来找我聊天吧')
        mock_conf.assert_called_with('aigc_api_key')
        mock_post.assert_called_with(
            url='http://example.com/v1/chat/completions',
            json={
                'model': 'model',
                'messages': [{'role': 'user', 'content': 'Hello'}],
                'top_p': 2,
                'temperature': 2,
                'frequency_penalty': 0.1,
                'presence_penalty': 0.1
            },
            headers={
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'Authorization': 'api_key'
            }
        )

if __name__ == '__main__':
    unittest.main()
