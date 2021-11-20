
import requests
from bs4 import BeautifulSoup
import datetime
from time import sleep


def main():     #* Initiating the main function

    print("\nWelcome to coronavirus Tracker..!")
    print()
    print("Select where from do you want to get the cases")
    print("1.India\n2.Enter a state[Full Name]\n3.Exit")

    try:
        ask = int(input(">>> "))

        if ask == 1:
            location = 'India'  #* 1st option whole india
            india(location)     #* Call the function India
            again()

        elif ask == 2:
            state = input("Enter name of the state: ").lower()  #* User inputs the state
            
            if len(state)>0:
                location = state
                url = f'https://coronaclusters.in/{state}'
                states(url, location)
                again()

            elif len(state)==0:     #* If user doesn't enter something
                print("Enter something\n")
                sleep(1)
                main()

        elif ask == 3:
            exit()
        
        else:
            print("Select Correct Option\n")    
            sleep(2)
            main()

    except ValueError:          #* If wrong input entered
        print("Check your input and try again\n")
        sleep(2)
        main()


def states(url, location):

    try:
        r = requests.get(url).text          #* Request the html from the website
        soup = BeautifulSoup(r, 'lxml')     #* BeautifulSoup object creation
        finder(soup, location)              #* Call the Finder function 

    except AttributeError:                  #* If state not found 
        print("No such state found, Make sure you spelled correctly")
        sleep(2)
        print()
        main()              #* Call the main frunction again


def india(location):            #* Function to get india's cases
    r = requests.get("https://coronaclusters.in/").text   #* Request the html from the website
    soup = BeautifulSoup(r, 'lxml')     #* BeautifulSoup object creation
    finder(soup, location)      #* Call the Finder function


def finder(soup, location):     #* Finder function to fetch data
    print()
    print("Initiating the coronavirus tracker...")  
    sleep(2)
    print()

    dt = datetime.datetime.now()    #* Print the current datetime
    
    print(dt.strftime('Date: %d %B %Y, Time: %I:%M %p'))    #* Format the datetime
    print()

    under = "  "+ "\u0332".join( location)   #* Underline the text
    print("\033[1m".join(under.upper()));print("\033[0;0m")     #* Bold the text


    #*Confirmed Cases fetcher*#
    confirmed_Tab = soup.find('div', class_="card bg-light mb-3 text-danger")
    confirmed = confirmed_Tab.find('h5', class_="card-title text-md text-md-lg").text
    print(f"Total Confirmed cases: {confirmed}")
    
    try:
        new_confirmed = confirmed_Tab.find('small').text
        print(f"New Confirmed cases:{new_confirmed}")
    
    except AttributeError:
        new_confirmed = ""
        pass
    #*End of confirmed cases fetcher**
    

    #*Active Cases fetcher*#
    active_Tab = soup.find('div', class_="card bg-light mb-3 text-primary")
    active = active_Tab.find('h5', class_="card-title text-md text-md-lg").text
    print(f"Total Active cases: {active}")
    
    try:
        new_active = active_Tab.find('small').text
        print(f"New active cases:{new_active}")
    
    except AttributeError:
        new_active = ""
        pass

    #*End of Active cases fecther*#
    

    #*Recovered cases fetcher*#
    recovered_Tab = soup.find('div', class_="card bg-light mb-3 text-success")
    recovered = recovered_Tab.find('h5', class_="card-title text-md text-md-lg").text
    print(f"Total Recovered cases: {recovered}")
    
    try:
        new_recovered = recovered_Tab.find('small').text
        print(f"New Recovered cases:{new_recovered}")
    
    except AttributeError:
        new_recovered=""
        pass
    #*End of recovered cases fetcher*#
    

    #*Deaths fethcer*#
    deaths_Tab = soup.find('div', class_="card bg-light mb-3 text-dark")
    deaths = deaths_Tab.find('h5', class_="card-title text-md text-md-lg").text
    print(f"Total Deaths: {deaths}")
    
    try:
        new_deaths = deaths_Tab.find('small').text
        print(f"New deaths: {new_deaths}")
    
    except AttributeError:
        new_deaths=""
        pass

    sleep(4)
    #*End of deaths fetcher*#


def again():
    new = input("Do you want to get data for another state?[y/n] >>>")
    if new == 'y':
        main()
    elif new == 'n':
        exit()
    else:
        print("Wrong choice!")
        again()


try:
    main()

except Exception:           #* An exception occuring (Mainly due to no internet connection)
    print("An exception occured and we couldn't initiate the Tracker..")
    print("Probable fix: Check your internet connection")
# main()
