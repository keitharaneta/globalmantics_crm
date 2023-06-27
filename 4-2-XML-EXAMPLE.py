class XmlTesting:

    def __init__(self, xml1):
        with open(xml1, 'r') as testing1:
            import xmltodict
            self.testing2 = xmltodict.parse(testing1.read())['root']

    def balancecalculations(self, xml1):
        testing3 = self.testing2[xml1]
        if testing3:
            return int(testing3["due"]) - int(testing3["paid"])


if __name__ == '__main__':
    x = XmlTesting('Test1.xml')
    y = x.balancecalculations('ACCT100')
    print(y)