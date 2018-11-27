def XMLDBCSV_csv_with_header_2_ordered_dict(csv_file):
	import csv
	new_dict = {}
	with open(csv_file, 'r') as f:
		reader = csv.reader(f, delimiter=',')
		fieldnames = next(reader)#read the first row 
		#reader = csv.DictReader(f, fieldnames=fieldnames, delimiter=',')
		for row in reader:
			print(next(reader))

	
print(XMLDBCSV_csv_with_header_2_ordered_dict('DB.csv'))
