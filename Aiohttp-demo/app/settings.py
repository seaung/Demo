import pathlib
import yaml

BASE_DIR = pathlib.Path(__file__).parent.parent

config_path = BASE_DIR / 'config' / 'demo.yaml'


def get_config(path):
    with open(path) as fs:
        config = yaml.load(fs)
    return config


config = get_config(config_path)

