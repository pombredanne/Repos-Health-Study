#!/usr/bin/python

import sys, requests, zipfile, os, json
from pprint import pprint

# Function which looks for licensing
def checkLicensing(targetZip, zipDir):
	# Gather zip name
	zipName = targetZip[targetZip.rfind('/'):-4]

	# Run Scancode to gather licensing information
	os.system("./scancode-toolkit-1.6.0/scancode -f json -l -c " + zipDir + " > " + zipName + ".json")

	# Read through JSON data
	with open(zipName + '.json') as data_file:    
    	data = json.load(data_file)

	pprint(data)

# Function that checks if the passed repository URL exists
def checkURL():
   inZip = ''
   outAnalysis = ''

   request = requests.head(sys.argv[1])
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

	print("Wallah\n")

	return(targetZip[:-1] + "/" + targetZip[targetZip.rfind('/'):-4])

# Main
def main():
	# checkURL()
	zipDir = unzipFile(sys.argv[1])
	checkLicensing(sys.argv[1], zipDir)

if __name__ == "__main__":
   main()