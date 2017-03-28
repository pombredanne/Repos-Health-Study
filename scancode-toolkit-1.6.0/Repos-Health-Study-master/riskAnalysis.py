#!/usr/bin/python

import sys, requests#, getopt

def main():
   inZip = ''
   outAnalysis = ''

   print(sys.argv[1])
   request = requests.head(sys.argv[1])
   if (request.status_code == 200):
      print(" exists!\n")
   else:
      print(" does not exist!\n")
      sys.exit()

if __name__ == "__main__":
   main()