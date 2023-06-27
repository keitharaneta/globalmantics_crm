import json


class Jsontesting:

    def __init__(self, json1):
        with open(json1, 'r') as testing1:
            import json
            self.testing2 = json.load(testing1)

    def balancecalculations(self, json2):
        testing3 = self.testing2[json2]
        if testing3:
            return int(testing3["sample1"]) - testing3["sample2"]

if __name__ == '__main__':
    x = Jsontesting('Test1.json')
    y = x.balancecalculations('TEST1')
    print(y)