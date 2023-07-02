class Database:
    def __init__(self, jsonfile):
        with open(jsonfile, 'r') as jsonfile1:
            import json
            self.jsonfile2 = json.load(jsonfile1)

    def output(self, acctid):
        result = self.jsonfile2[acctid]
        if result:
            test1 = float(result['sample2']) - float(result['sample1'])
            return "USD {test1:.2f}".format(test1=test1)
        return None


if __name__ == '__main__':
    x = Database('jsondata.json')
    print(x.output('ACCT100'))
