class getHREF:
    def __init__(self):
        self.orgs = list()
        for line in open('href.txt', 'r', encoding='utf8'):
            if 'litecat' in line:
                self.orgs.append('http://fishretail.ru' + line.replace("\n", ""))

    def getOrgList(self):
        return self.orgs
