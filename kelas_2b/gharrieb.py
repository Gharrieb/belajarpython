import csv
class gharrieb(object):
        def werehousing(self):
            with open('kelas_2b/gharrieb.csv') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                   print("stok sekarang:", row[0], row[1], row[2], row[3], row[4])