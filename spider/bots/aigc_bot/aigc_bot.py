import logging
import time
from urllib.parse import urljoin

import requests

from spider.bridge.context import Context, ContextType
from spider.bridge.reply import Reply, ReplyType
from spider.setting import (
    AIGC_API_KEY,
    AIGC_MODEL,
    FREQUENCY_PENALTY,
    PRESENCE_PENALTY,
    TEMPERATURE,
    TOP_P,
    API_DOMAIN,
)


class AIGCBot:
    def __init__(self):
        self.headers = {"Content-Type": "application/json", "Accept": "application/json", "Authorization": AIGC_API_KEY}
        self.body = {
                "model": AIGC_MODEL,
                "messages": [{"role": "user", "content": None}],
                "top_p": TOP_P,
                "temperature": TEMPERATURE,
                "frequency_penalty": FREQUENCY_PENALTY,
                "presence_penalty": PRESENCE_PENALTY,
            }

    def reply(self, context: Context = None) -> Reply:
        """
        :param context: 询问内容
        :return: 回复内容
        """
        if context is ContextType.TEXT:
            return self._chat(context)
        if context is ContextType.IMAGE:
            return self._process_image(context)

    def _chat(self, context: Context, retry_count=0) -> Reply:
        if retry_count > 2:
            return Reply(ReplyType.TEXT, "我好像出了点问题，等我修复一下再来找我聊天吧")

        try:
            self.body["messages"][0]["content"] = context.content
            base_url = API_DOMAIN
            func_url = "/v1/chat/completions"
            res = requests.post(url=urljoin(base_url, func_url), json=self.body, headers=self.headers)

            if res.status_code == 200:
                response = res.json()
                content = response["choices"][0]["message"]["content"]
                total_token = response["usage"]["total_token"]
                logging.info(f"total_token: {total_token}")
                return Reply(ReplyType.TEXT, content)
        except Exception as e:
            logging.error(e)
            time.sleep(2)
            logging.warning("正在重试...")
            return self._chat(context, retry_count + 1)

    def _process_image(self, context: Context) -> Reply:
        pass
