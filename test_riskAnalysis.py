#test_riskAnaylsis.py
import pytest, requests

def checkURL(targetURL):

   request = requests.head(targetURL)
   if (request.status_code == 200):
      return("URL exists!\n")
      
   else:
      return("The passed URL does not exist! Please try again!\n")
      sys.exit()

def getApiUrl(targetURL):
	urlPieces = targetURL.split('/') #Split on forward slash
	apiUrl = "https://api.github.com/repos/" + urlPieces[3] + '/' + urlPieces[4]
	return(apiUrl)


def test_check_Url():
	assert checkURL("https://github.com/Dreizan/Repos-Health-Study") == "URL exists!\n"

def test_check_Url_Invalid():
	assert checkURL("https://github.com/Dreizan/Repos-Health-Study1234ab") == "The passed URL does not exist! Please try again!\n"

def test_getApiUrl():
	assert getApiUrl("https://github.com/Dreizan/Repos-Health-Study") == "https://api.github.com/repos/Dreizan/Repos-Health-Study"

def test_getApiURLInvalid():
	assert getApiUrl("https://github.com/Dreizan/Repos-Health-Study/stuff") == "https://api.github.com/repos/Dreizan/Repos-Health-Study"
