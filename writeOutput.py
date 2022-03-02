import csv

class CsvWriter:
    def writeCSV(self, org_name, description, region, town, address, phone, email, url):
        with open('orgList.csv', 'a', encoding="utf8", newline='') as output:
            writer = csv.writer(output, delimiter=';')
            writer.writerow([org_name, description, region, town, address, phone, email, url])
