class JsonYamltesting:
    def __init__(self, json1, yaml1, xml1):
        with open(json1, 'r') as json2:
        # import json and load the json file - json.load(<X>)
            import json
            json21 = json.load(json2)
            self.json3 = json21

        with open(yaml1, 'r') as yaml2:
        # import yaml and load the yaml file - yaml.safe_load(<X>)
            import yaml
            yaml21 = yaml.safe_load(yaml2)
            self.yaml3 = yaml21

        with open(xml1, 'r') as xml2:
        # import xmltodict and load the xml file - xmltodict.parse(<X>.read())["root"]
            import xmltodict
            xml21 = xmltodict.parse(xml2.read())["root"]
            self.xml3 = xml21

    def testing123(self, json1, yaml1, xml1):
        self.notify1 = (int(self.json3[json1]['sample1']) - int(self.yaml3[yaml1]['sample2'])) - int(self.xml3[xml1]["paid"])
        print(self.notify1)


if __name__ == '__main__':
    x = JsonYamltesting('Test1.json', 'Test1.yml', 'Test1.xml')
    x.testing123('TEST1', 'ACCT100', 'ACCT100')