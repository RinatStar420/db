import yaml
with open('mcintyre.yaml', 'rt') as fin:
    text = fin.read()
data = yaml.load(text, Loader=yaml.BaseLoader)
print(data['details'])