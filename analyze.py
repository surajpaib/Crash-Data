import csv
import re
import pycountry

mapping = {country.name: country.alpha2 for country in pycountry.countries}

ifile=open("AirplaneData.csv",'r+b')
reader=csv.reader(ifile)
location=[]
location_data=[]
d=[]

ofile=open('AnalyzedData.csv','wb')
writer=csv.writer(ofile,delimiter=',')

cfile=open('states.csv','rb')
array1=csv.reader(cfile)

for i in array1:
	location.append(i[0])







for row in reader:

	location_data=row[2]
	d=location_data.split(",")


	for j in location:

		if (len(d)==3):
			if (d[2].strip()==str(j)):
				row[2]='US'
		if (len(d)==2):
			if (d[1].strip()==str(j)):
				row[2]='US'

		if (len(d)==1):
			if (d[0].strip()==str(j)):
				row[2]='US'










	### To map countries to country codes
	if (len(d)==3):
		if(row[2]!='US'):
			row[2]=mapping.get(d[2].strip())
	if (len(d)==2):
		if(row[2]!='US'):
			row[2]=mapping.get(d[1].strip())
	else:
		if(row[2]!='US'):
			row[2]=mapping.get(d[0].strip())


	### To analyze the summary and find estimated reasons


	if re.search(r'(.*)[cC]ontrol(.*)',row[6]):
		row[6]='Loss of control'
	if re.search(r'(.*)[Ll]anding(.*)',row[6]):
		row[6]='Crashes during Landing and Take-off'
	if re.search(r'(.*)[lL]ightning(.*)',row[6]):
		row[6]='Weather conditions'
	if re.search(r'(.*)[sS]hot(.*)',row[6]):
		row[6]='Aircraft shot down'
	if re.search(r'(.*)[hH]ijack(.*)',row[6]):
		row[6]='Terrorist Acts'
	if re.search(r'(.*)[bB]omb(.*)',row[6]):
		row[6]='Terrorist Acts'
	if re.search(r'(.*)[mM]echanical(.*)',row[6]):
		row[6]='Mechanical component Failure'
	if re.search(r'(.*)[eE]ngine(.*)',row[6]):
		row[6]='Engine Failure'
	if re.search(r'(.*)[pP]ilot(.*)',row[6]):
		row[6]='Pilot Error'
	if re.search(r'(.*)[rR]unway(.*)',row[6]):
		row[6]='Runway overshoot or undershoot'
	if re.search(r'(.*)[fF]og(.*)',row[6]):
		row[6]='Weather conditions'
	if re.search(r'(.*)[rR]ain(.*)',row[6]):
		row[6]='Weather conditions'
	if re.search(r'(.*)[sS]now(.*)',row[6]):
		row[6]='Weather conditions'
	if re.search(r'(.*)[tT]hunder(.*)',row[6]):
		row[6]='Weather conditions'
	if re.search(r'(.*)[wW]ind(.*)',row[6]):
		row[6]='Weather conditions'
	if re.search(r'(.*)[vV]isibility(.*)',row[6]):
		row[6]='Weather conditions'
	if re.search(r'(.*)[cC]ontroller(.*)',row[6]):
		row[6]='ATC error'
	if re.search(r'(.*)[fF]ire(.*)',row[6]):
		row[6]='Fire'
	if re.search(r'(.*)[dD]isappear(.*)',row[6]):
		row[6]='Disappearances'
	if re.search(r'(.*)[cC]rash(.*)',row[6]):
		row[6]='Accidental Crashes'
	if re.search(r'(.*)[aA]ccident(.*)',row[6]):
		row[6]='Accidental Crashes'
	if re.search(r'(.*)[eE]xplode(.*)',row[6]):
		row[6]='Explosions on board'
	if re.search(r'(.*)[sS]truck(.*)',row[6]):
		row[6]='Accidental Crashes'




	
	writer.writerow(row)

	








ifile.close()
ofile.close()

