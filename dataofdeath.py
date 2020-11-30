import csv
import datetime
import random

#grab the template diary entry and read it
diary_file = open("diary_entry.txt", "r") 
if diary_file.mode == 'r':
	diary_entry = diary_file.read()
diary_file.close

#grab the three types of feelings and read 'em in as lists
feelings_mild_file = open("feelings_mild.txt", "r") 
if feelings_mild_file.mode == 'r':
	feelings_mild = feelings_mild_file.readlines()
	# strip out newlines
	feelings_mild = [line.rstrip('\n') for line in feelings_mild]
feelings_mild_file.close

feelings_medium_file = open("feelings_medium.txt", "r") 
if feelings_medium_file.mode == 'r':
	feelings_medium = feelings_medium_file.readlines()
	feelings_medium = [line.rstrip('\n') for line in feelings_medium]
feelings_medium_file.close

feelings_full_file = open("feelings_full.txt", "r") 
if feelings_full_file.mode == 'r':
	feelings_full = feelings_full_file.readlines()
	feelings_full = [line.rstrip('\n') for line in feelings_full]
feelings_full_file.close

#make our novel
novel = open("dataofdeath.html", "a+")
novel.write("<html><head><title>Data of Death</title><link rel=\"stylesheet\" href=\"dataofdeath.css\"></head><body><h1>Data of Death: feelings in the machine, a tale of descent</h1>")

#grab csv data: worldwide COVID case counts by day, sourced from https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/L20LOT
with open('covid_data.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	line_count = 0
	day_count = 1
	
	#skip column names
	for row in csv_reader:
		if line_count == 0:
			line_count +=1  
			
		# each new line in our csv is a new day that needs a diary entry...
		else:
			# make a diary entry for today
			today_entry = diary_entry
			
			today_date = f'{row[0]}'	
			today_date = datetime.datetime.strptime(today_date, '%Y%m%d')
			today_date = today_date.strftime("%d %B %Y")
	
			case_count = f"{int(f'{row[1]}'):,d}"
			
			#update the date, case count and day number for this entry
			today_entry = today_entry.replace('DATE', today_date) 
			today_entry = today_entry.replace('CASECOUNT', case_count) 
			today_entry = today_entry.replace('DAYCOUNT', str(day_count))
			
			# add an emotion, and an overall assessment of the pandemic
			# the emotion is selected at random from a list, with increasing intensity of emotions as time passes
			if day_count < 100:
				today_entry = today_entry.replace('ZEITGEIST', 'confusion')
				today_entry = today_entry.replace('FEELING', random.choice(feelings_mild))
				today_entry = today_entry.replace('set_intensity', 'feelings_mild')
				

			elif day_count < 200:
				today_entry = today_entry.replace('ZEITGEIST', 'terror')
				today_entry = today_entry.replace('FEELING', random.choice(feelings_medium))
				today_entry = today_entry.replace('set_intensity', 'feelings_medium')

			else:
				today_entry = today_entry.replace('ZEITGEIST', 'madness')
				today_entry = today_entry.replace('FEELING', random.choice(feelings_full))
				today_entry = today_entry.replace('set_intensity', 'feelings_full')

			if day_count == 1:
				today_entry = today_entry.replace('1 days', '1 day')

			novel.write(today_entry)

			line_count += 1
			day_count += 1
			
novel.write("</body></html>")
novel.close()