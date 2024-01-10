import json
import os

available_setting = {
    'aigc_base_url': 'https://api.aigcbest.top'
}

class Config:
    def __init__(self, d=None):
        super().__init__()
        if d is None:
            d = {}
        for k, v in d.items():
            self[k] = v

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError as e:
            return default
        except Exception as e:
            raise e


config = Config()


def load_config():
    global config
    config_path = "./config.json"
    config_str = read_file(config_path)
    config = Config(json.loads(config_str))

    for name, value in os.environ.items():
        name = name.lower()
        if name in available_setting:
            try:
                config[name] = eval(value)
            except:
                if value == 'true':
                    config[name] = True
                elif value == 'false':
                    config[name] = False
                else:
                    config[name] = value

def read_file(path):
    with open(path, mode="r", encoding="utf-8") as f:
        return f.read()


def conf():
    return config
