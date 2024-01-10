import logging
import time
from urllib.parse import urljoin

import requests

from bridge.context import Context, ContextType
from bridge.reply import Reply, ReplyType
from config import conf


class AIGCBot:
    def __init__(self):
        pass

    def reply(self, context: Context = None) -> Reply:
        '''
        :param context: 询问内容
        :return: 回复内容
        '''
        if context is ContextType.TEXT:
            return self._chat(context)
        if context is ContextType.IMAGE:
            return self._process_image(context)

    def _chat(self, context: Context, retry_count=0) -> Reply:
        if retry_count > 2:
            return Reply(ReplyType.TEXT, "我好像出了点问题，等我修复一下再来找我聊天吧")
        try:
            aigc_api_key = conf().get('aigc_api_key')
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "Authorization": f"{aigc_api_key}"
            }
            body = {
                "model": conf().get('aigc_model'),
                "messages": [{"role": "user", "content": context}],
                "top_p": conf().get('aigc_top_p', 1),
                "temperature": conf().get('aigc_temperature', 1),
                "frequency_penalty": conf().get('frequency_penalty', 0.0),
                "presence_penalty": conf().get('presence_penalty', 0.0),
            }

            base_url = conf().get('aigc_base_url')
            func_url = "/v1/chat/completions"
            res = requests.post(url=urljoin(base_url, func_url), json=body, headers=headers)

            if res.status_code == 200:
                response = res.json()
                content = response['choices'][0]['message']['content']
                total_token = response['usage']['total_token']
                logging.info(f"total_token: {total_token}")
                return Reply(content, ReplyType.TEXT)
        except Exception as e:
            logging.error(e)
            time.sleep(2)
            logging.warning('正在重试...')
            return self._chat(context, retry_count + 1)

    def _process_image(self, context: Context) -> Reply:
        pass
