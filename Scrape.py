import os
import sys
#Regex
import re
#Requests the website
import requests
#cleans up Request
from bs4 import BeautifulSoup

#Main Process
def main():
    #Ask User Input
    siteURL = URLInput()
    #Get Raw Page (User inputed)
    rawPage = getRequest(siteURL)
    #Pull Out page contents (raw page inputed)
    pageContent = getPageContent(rawPage)
    #Optional makes HTML pretty and easy to read (comment out when really running- thread eater)
    iFeelPretty = runBeautSoup(pageContent)
    #Runs Checks for a tags
    tagSearch = runTagSearch(iFeelPretty)
    #Checks for names inside of tagSearch
    itemName = titleChecker(tagSearch)
    #Print Results
    print(itemName)
    
#Get URL from user
def URLInput():
    userInputedURL = input("Please enter the URL you wish to search: ")
    return userInputedURL


#Request data from site
def getRequest(URL):
    try:
        #get page from user input URL
        page = requests.get(URL)
        return page
    except Exception as e:
        print("There Was An Error: ")
        try:
            #if page load failure, Return status code (Status Codes online, 200 is good)
            pageCode = page.status_code
            print("Page Status Code: " + str(pageCode))
            print("Error Desciption: " + str(e))
            raise SystemExit
        except:
            #if invalid URL Print - invalid - System.exit
            print("Invalid URL")
            raise SystemExit


#Get content of page
def getPageContent(rawPage):
    try:
        pageContent = rawPage.content
        return pageContent
    except Exception as e:
        print("The page contents were unavailable")
        print(str(e))
        raise SystemExit


#Makes Code HTML Human Readable
def runBeautSoup(pageContent):
    try:
        clamChowder = BeautifulSoup(pageContent, 'html.parser')
        return clamChowder
    except Exception as e:
        print("Something went wrong:")
        print(str(e))
        #No need to exit


#Searches for all tags inside html 
def runTagSearch(iFeelPretty):
    try:
        tagSearch = iFeelPretty.find_all("a")
        return tagSearch
    except Exception as e:
        print("Something went wrong:")
        print(str(e))
        raise SystemExit
    

#Checks for names of items inside the html -> a tag search
def titleChecker(tagSearch):
    #array to be passed by reference
    itemAndPrice = []
    for theString in tagSearch:
        try:
            #add items to array
            matches = re.search('title="(.+?)"', str(theString), re.IGNORECASE)
            itemAndPrice.append(str(matches.group(1)))
        except:
            pass
    
    return itemAndPrice



#this code will only run if this method is the entry point of the program
if __name__ == "__main__":
    #Scripts running directly
    #print("This code was invoked directly")
    #print(__name__)
    main()
else:
    #scripts that import will call this function
    print("Import of Scrape was successful")
    #main()
    #Adding in this comment to see if it auto carries over to my code at home
