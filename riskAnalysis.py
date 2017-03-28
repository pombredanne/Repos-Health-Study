#!/usr/bin/python

import sys, requests, zipfile

def checkURL():
   inZip = ''
   outAnalysis = ''

   request = requests.head(sys.argv[1])
   if (request.status_code == 200):
      print("URL exists!\n")
      
   else:
      print("The passed URL does not exist! Please try again!\n")
      sys.exit()

def unzipFile(targetZip):
	# Directory where zip and corresponding unzipped file are located
	zipDirectory = targetZip[:targetZip.rfind('/')]
	
	# Extract contents of the zip file
	theZip = zipfile.ZipFile(targetZip, 'r')
	theZip.extractall(zipDirectory)
	theZip.close()

	print("Wallah\n")

def main():
	# checkURL()
	unzipFile(sys.argv[1])

if __name__ == "__main__":
   main()