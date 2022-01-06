import yaml
from testdata.getpath import GetYamlDataPath

def read_yaml(yamlname):
    with open(GetYamlDataPath(yamlname=yamlname), 'r', encoding='utf-8') as f:
        return list(yaml.safe_load_all(f))
