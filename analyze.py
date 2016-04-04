import csv
import re
import pycountry

mapping = {country.name: country.alpha2 for country in pycountry.countries}

ifile=open("AirplaneData.csv",'r+b')
reader=csv.reader(ifile)
location=[]
location_data=[]
d=[]

ofile=open('AnalyzedData2.csv','wb')
writer=csv.writer(ofile,delimiter=',')


for row in reader:

	location_data=row[2]
	d=location_data.split(",")
	if (len(d)==3):
		row[2]=mapping.get(d[2].strip(),'US')
	if (len(d)==2):
		row[2]=mapping.get(d[1].strip(),'US')
	else:
		row[2]=mapping.get(d[0].strip(),'US')


	### To analyze the summary and find estimated reasons


	if re.search(r'(.*)[cC]ontrol(.*)',row[6]):
		row[6]='Control'
	if re.search(r'(.*)[Ll]anding(.*)',row[6]):
		row[6]='Landing'
	if re.search(r'(.*)[lL]ightning(.*)',row[6]):
		row[6]='Lightning'
	if re.search(r'(.*)[sS]hot(.*)',row[6]):
		row[6]='Shot Down'
	if re.search(r'(.*)[hH]ijack(.*)',row[6]):
		row[6]='Terrorist Acts'
	if re.search(r'(.*)[bB]omb(.*)',row[6]):
		row[6]='Terrorist Acts'
	if re.search(r'(.*)[mM]echanical(.*)',row[6]):
		row[6]='Mechanical Failure'
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
		row[6]='Accident'



	
	writer.writerow(row)

	








ifile.close()
ofile.close()

