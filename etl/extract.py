import csv

def extract_data(path=”data/input.csv”):
	rows = []
	with open(path, newline=””) as f:
		reader = csv.DictReader(f)
		for row in reader:
			rows.append(row)
	## New comment for feature branch
    ## This is the 2nd Comment
	return rows
