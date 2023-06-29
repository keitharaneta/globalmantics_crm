class Database:
    def __init__(self, jsonfile):
        with open(jsonfile, 'r') as jsonfile1:
            import json
            self.jsonfile2 = json.load(jsonfile1)

    def output(self, acctid):
        result = self.jsonfile2[acctid]
        if result:
            return int(result['sample2']) - int(result['sample1'])
        return None


if __name__ == '__main__':
    x = Database('jsondata.json')
    print(x.output('ACCT100'))
