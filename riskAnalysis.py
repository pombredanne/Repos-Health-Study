#!/usr/bin/python

import sys, requests, zipfile, os, json
from pprint import pprint

# Function which looks for licensing
def checkLicensing(targetZip, zipDir):
	# Gather zip name
	zipName = targetZip[targetZip.rfind('/'):]
	hasLicenses = 0
	hasCopyrights = 0

	print(zipDir + "\n")

	# Run Scancode to gather licensing information
	os.system("./scancode-toolkit-1.6.0/scancode -f json -l -c " + zipDir + " > ./test/results" + zipName + ".json")

	# Read through JSON data
	with open("./test/results" + zipName + '.json') as data_file:    
    		data = json.load(data_file)

	# pprint(data)

	for item in data['results']:
		if(len(item['licenses']) > 0):
			if(hasLicenses == 0):
				print("There are licenses included!\nLicenses:")
			hasLicenses = 1
			for licns in item['licenses']:
   				print(" " + licns['short_name'])

	if(hasLicenses == 0):
    		print("No licensing included.\n")

   	for item in data['results']:
		if(len(item['copyrights']) > 0):
			if(hasCopyrights == 0):
				print("There are copyrights included!\nCopyrights:")
			hasCopyrights = 1
			for cpy in item['copyrights']:
   				print(" \"" + cpy['statements'] + "\"")

	if(hasCopyrights == 0):
   		print("No copyrights included.\n")
    

# Function that checks if the passed repository URL exists
def checkURL(targetURL):
   inZip = ''
   outAnalysis = ''

   request = requests.head(targetURL)
   if (request.status_code == 200):
      print("URL exists!\n")
      
   else:
      print("The passed URL does not exist! Please try again!\n")
      sys.exit()

# Function which extracts the contents of the zip file
def unzipFile(targetZip):
	# Directory where zip and corresponding unzipped file are located
	zipDirectory = targetZip[:targetZip.rfind('/')]
	
	# Extract contents of the zip file
	theZip = zipfile.ZipFile(targetZip, 'r')
	theZip.extractall(zipDirectory)
	theZip.close()

	return(targetZip[:-1])

def getZip(targetURL):
	#Grab the zip of the user passed in URL
	zipName = targetURL[targetURL.rfind('/')+1:]
	print(zipName + ".zip")
	os.system("curl -L " + targetURL + "/zipball > " + zipName + ".zip")
	return(zipName + ".zip")
	#os.system("curl -L https://api.github.com/repos/Dreizan/Repos-Health-Study/zipball > Repos-Health-Study.zip")
	#os.system("curl -L https://github.com/Dreizan/Repos-Health-Study/zipball > Repos-Health-Study.zip")

# Main
def main():
	checkURL(sys.argv[1])
	zipF = getZip(sys.argv[1])
	zipDir = unzipFile(zipF)
	checkLicensing(sys.argv[1], zipDir)

if __name__ == "__main__":
   main()
