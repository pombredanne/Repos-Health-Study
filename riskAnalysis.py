#!/usr/bin/python
# SPDX-License-Identifier: MIT
# Import required modules
import sys, requests, zipfile, os, json

# Function which looks for licensing
def checkLicensing(targetZip, zipDir, scanZipDir):
	# Gather zip name
	zipName = targetZip[targetZip.rfind('/'):]
	hasLicenses = 0
	hasCopyrights = 0
	listLicenses = []
	listCopyrights = []
	exists = False

	#Change the permissions so scan code can be executed
	os.system("chmod -R 755 " + scanZipDir)

	# Run Scancode to gather licensing information
	os.system("./" + scanZipDir + "/scancode -f json -l -c " + zipDir + " > ./test/results" + zipName + ".json")

	print("Finished scanning. Parsing through JSON results now:")
	#print("./test/results" + zipName + ".json")

	#Remove the first two lines of the JSON file as scancode places two statements that causes following code to break on first run
	with open("./test/results" + zipName + '.json', 'r') as fin:
			data = fin.read().splitlines(True)
	with open("./test/results" + zipName + '.json', 'w') as fout:
			fout.writelines(data[2:])

	# Read through JSON data and get the licenses and copyrights
	with open("./test/results" + zipName + '.json') as data_file:    
    		data = json.load(data_file)

    # Parse through licenses in the repo
	for item in data['files']:
		if(len(item['licenses']) > 0):
			if(hasLicenses == 0):
				print("There are licenses included!\nLicenses:")
			hasLicenses = 1
			for licns in item['licenses']:
				exists = False
				for currLic in listLicenses:
					if(currLic.split(' ') == licns['short_name'].split(' ')):
						exists = True
				if(not exists):
   					listLicenses.append(licns['short_name'])
   					print("* - " + licns['short_name'])

   	# If no licenses, says so
	if(hasLicenses == 0):
    		print("No licensing included.\n")

	# Parse through copyrights in the repo
   	for item in data['files']:
		if(len(item['copyrights']) > 0):
			if(hasCopyrights == 0):
				print("There are copyrights included!\nCopyrights:")
			hasCopyrights = 1
			for cpy in item['copyrights']:
				for stmts in cpy['statements']:
   					exists = False
					for currCop in listCopyrights:
						if(currCop.split(' ') == stmts.split(' ')):
							exists = True
					if(not exists):
   						listCopyrights.append(stmts)
   						print("* - " + stmts)

   	# If no copyrights, says so
	if(hasCopyrights == 0):
   		print("No copyrights included.\n")

   	# Reformats the output json file with new lines
   	with open("./test/results" + zipName + '.json', 'w') as outfile:
    		json.dump(data, outfile, indent=2)

	print("Parsing complete. Removing downloaded files:")
   	os.system("rm -rf " + zipDir)
    	os.system("rm -rf " + scanZipDir)

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
	theZip.extractall()
	zipDir = (theZip.namelist())[0]
	theZip.close()

   	os.system("rm -rf " + targetZip)

	return zipDir

#Function that given the target URL gets the zip file
def getZip(targetURL):
	#Grab the zip of the user passed in URL
	zipName = targetURL[targetURL.rfind('/')+1:]
	#print(zipName + ".zip")
	os.system("curl -L " + targetURL + "/zipball > " + zipName + ".zip")
	os.system("")
	return(zipName + ".zip")

#Function that takes user entered github URL and puts it into api.github.com/repos form of the repo
def getApiUrl(targetURL):
	urlPieces = targetURL.split('/') #Split on forward slash
	apiUrl = "https://api.github.com/repos/" + urlPieces[3] + '/' + urlPieces[4]
	return(apiUrl)

#Function that downloads the latest version of scan code
def getScanCode():
	scancodeURL = getApiUrl("https://github.com/nexB/scancode-toolkit")
	scanZipFile = getZip(scancodeURL)
	scanZipDir = unzipFile(scanZipFile)
	return scanZipDir

# Main
def main():
	print("Downloading ScanCode")
	scanZipDir = getScanCode()

	print("Checking if the URL passed exists:")
	checkURL(sys.argv[1])
	properURL = getApiUrl(sys.argv[1])

	print("Gathering the zip file and decompressing it.")
	zipF = getZip(properURL)
	zipDir = unzipFile(zipF)

	print("Attempting to collect licensing and copyright information on the following GitHub project - " + zipF + ":")
	print("(This may take a while, depending on how big the zip file is)\n")
	checkLicensing(sys.argv[1], zipDir, scanZipDir)

	print("Process complete. Thank you!")

if __name__ == "__main__":
   main()
