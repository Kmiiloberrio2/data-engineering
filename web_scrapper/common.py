import yaml

__config = None


def configuration():
    if not __config:
        with open('config.yaml', mode='r') as f:
            config = yaml.safe_load(f)
    return config
