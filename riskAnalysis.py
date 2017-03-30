#!/usr/bin/python

import sys, requests, zipfile, os, json
from pprint import pprint

# Function which looks for licensing
def checkLicensing(targetZip, zipDir):
	# Gather zip name
	zipName = targetZip[targetZip.rfind('/'):]
	hasLicenses = 0
	hasCopyrights = 0

	# Run Scancode to gather licensing information
	os.system("./scancode-toolkit-1.6.0/scancode -f json -l -c " + zipDir + " > ./test/results" + zipName + ".json")

	print("Finsihed scanning. Parsing through JSON results now:")

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
   				print("* - " + licns['short_name'])

	if(hasLicenses == 0):
    		print("No licensing included.\n")

   	for item in data['results']:
		if(len(item['copyrights']) > 0):
			if(hasCopyrights == 0):
				print("There are copyrights included!\nCopyrights:")
			hasCopyrights = 1
			for cpy in item['copyrights']:
   				print("* - \"" + cpy['statements'] + "\"")

	if(hasCopyrights == 0):
   		print("No copyrights included.\n")

	print("Parsing complete. Removing downloaded files:")
   	os.system("rm -rf " + zipDir)
    

# Function that checks if the passed repository URL exists
def checkURL(targetURL):
   inZip = ''
   outAnalysis = ''

   request = requests.head(targetURL)
   if (request.status_code == 200):
      print("URL exists!")
      
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

   	os.system("rm -rf " + targetZip)

	return(targetZip[:-1])

def getZip(targetURL):
	#Grab the zip of the user passed in URL
	zipName = targetURL[targetURL.rfind('/')+1:]
	print(zipName + ".zip")
	os.system("curl -L " + targetURL + "/zipball > " + zipName + ".zip")
	os.system("ls -l")
	return(zipName + ".zip")

# Main
def main():
	print("Checking if the URL passed exists:")
	checkURL(sys.argv[1])

	print("Gathering the zip file and decompressing it.")
	zipF = getZip(sys.argv[1])
	zipDir = unzipFile(zipF)

	print("Attemptiing to collect licensing and copyright information on the following GitHub project - " + zipDir + ":")
	print("(This may take awhile, depending on how big the zip file is)\n")
	checkLicensing(sys.argv[1], zipDir)

	print("Process complete. Thank you!")

if __name__ == "__main__":
   main()
