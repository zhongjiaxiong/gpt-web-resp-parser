'''
该项目是一个简单的基于gpt的爬虫demo
'''

import requests
import parsel


def get_page_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text


def parse_page(html):
    selector = parsel.Selector(html)
    return selector

def parse_data(html):
    url = "https://api.aigcbest.top/v1/chat/completions"
    api_key = "sk-bJGId3oyW6lE9sg8B8D74439Ed7844F2Ae7aCc722853E431"
    headers = {
        "Content-Type": "application/json",
        'Accept': 'application/json',
        "Authorization": f"{api_key}",
    }
    prompt = (f'你是一个数据提取小助手，能够从一大段新闻文本中提取有用的信息并以JSON格式返回。{html},'
              '请从上面的文本中提取有用信息，返回数据格式如下：{"title": "新闻标题", "content": "新闻内容", "author": "新闻作者", "publish_time": "发布时间"}')
    print(prompt)
    data = {
        "model": "gpt-4-all",
        'messages': [{'role': 'user',"content":prompt}]
    }

    response = requests.post(url, json=data, headers=headers)
    return response.text


if __name__ == '__main__':
    # url = "https://juejin.cn/"
    with open('test_html/去除注释.html', 'r', encoding='utf-8') as f:
        html = f.read()
    # normal_html = normalize_text(html)
    # element = html2element(normal_html)
    # element = pre_parse(element)
    # element = del_comment(element)
    # remove_noise_node(element, config.get('noise_node_list'))
    # html = element2html(element)
    data = parse_data(html)
    print(data)







