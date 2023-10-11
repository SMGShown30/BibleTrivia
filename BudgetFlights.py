# Libraries
import time
from password import new_password
from email.message import EmailMessage
import smtplib, ssl
from selenium import webdriver

# Major Airports in US
major_airports = {
    "Atlanta": "ATL",
    "Anchorage": "ANC",
    "Austin": "AUS",
    "Baltimore": "BWI",
    "Boston": "BOS",
    "Charlotte": "CLT",
    "Chicago Midway": "MDW",  # Note: There are two airports for Chicago, I'm using the code for Chicago Midway Airport (MDW)
    "Chicago O'hare": "ORD",  # Note: There are two airports for Chicago, I'm using the code for Chicago O'Hare International Airport (ORD)
    "Cincinnati": "CVG",
    "Cleveland": "CLE",
    "Columbus": "CMH",
    "Dallas": "DFW",  # Note: There are two airports for Dallas, I'm using the code for Dallas/Ft. Worth International Airport (DFW)
    "Denver": "DEN",
    "Detroit": "DTW",
    "Fort Lauderdale": "FLL",
    "Fort Myers": "RSW",
    "Hartford": "BDL",
    "Honolulu": "HNL",
    "Houston Bush": "IAH",  # Note: There are two airports for Houston, I'm using the code for George Bush Intercontinental Airport (IAH)
    "Houston William": "HOU",  # Note: There are two airports for Houston, I'm using the code for William P. Hobby Airport (HOU)
    "Indianapolis": "IND",
    "Kansas City": "MCI",
    "Las Vegas": "LAS",
    "Louisville": "SDF",
    "Los Angeles": "LAX",
    "Memphis": "MEM",
    "Miami": "MIA",
    "Minneapolis": "MSP",
    "Myrtle Beach": "MYR",
    "Nashville": "BNA",
    "New Orleans": "MSY",
    "New York Kennedy": "JFK",  # Note: There are two airports for New York, I'm using the code for John F. Kennedy International Airport (JFK)
    "New York LaGuardia": "LGA",  # Note: There are two airports for New York, I'm using the code for LaGuardia International Airport (LGA)
    "Newark": "EWR",
    "Oakland": "OAK",
    "Orlando": "MCO",
    "Philadelphia": "PHL",
    "Phoenix": "PHX",
    "Pittsburgh": "PIT",
    "Portland": "PDX",
    "Raleigh": "RDU",
    "Sacramento": "SMF",
    "Salt Lake City": "SLC",
    "San Antonio": "SAT",
    "San Diego": "SAN",
    "San Francisco": "SFO",
    "San Jose": "SJC",
    "Santa Ana": "SNA",
    "Seattle": "SEA",
    "St. Louis": "STL",
    "Tampa": "TPA",
    "Washington D.C. Dulles": "IAD",  # Note: There are two airports for Washington D.C., I'm using the code for Dulles International Airport (IAD)
    "Washington D.C. Reagan": "DCA",  # Note: There are two airports for Washington D.C., I'm using the code for Ronald Reagan Washington National Airport (DCA)
}

print("Welcome to Budget Flights where we provide you with plane tickets that fit your budget!")
receiver_email = input("Enter you Email address: ")
# Budget
while True:
    budget = input("Enter your Max Budget (Numbers Only and Round to the nearest Dollar): $")
    if budget.isdigit():
        break
    else:
        input("Enter a valid number")
# Number of Passengers
while True:
    passengers = input("Enter number of passengers (Numbers Only): ")
    if passengers.isdigit():
        break
    else:
        input("Enter a valid number")
# Convert to url from
number = f"/{passengers}adults"
# Vacation Destination

while True:
    destination = input("Enter your desired Destination (US City): ")
    destination = destination.title()
    if destination in major_airports:
        break
    elif destination == "Chicago":
        destination = input("Chicago Midway or Chicago O'Hare: ")
        while destination.lower() not in ["chicago midway", "chicago o'hare"]:
            destination = input("Please enter either 'Chicago Midway' or 'Chicago O'Hare': ")
        break
    elif destination == "Houston":
        destination = input("Houston Bush or Houston William: ")
        while destination.lower() not in ["houston bush", "houston william"]:
            destination = input("Please enter either 'Houston Bush' or 'Houston William': ")
        break
    elif destination == "Washington D.C.":
        destination = input("Washington D.C. Dulles or Washington D.C. Reagan: ")
        while destination.lower() not in ["washington d.c. dulles", "washington d.c. reagan"]:
            destination = input("Please enter either 'Washington D.C. Dulles' or 'Washington D.C. Reagan': ")
        break
    elif destination == "New York":
        destination = input("New York Kennedy or New York LaGuardia: ")
        while destination.lower() not in ["new york kennedy", "new york laguardia"]:
            destination = input("Please enter either 'New York Kennedy' or 'New York LaGuardia': ")
        break
    else:
        print("That city is not in our database. Please enter again")

while True:
    origin = input("Enter the city where you are traveling from (US City): ")
    origin = origin.title()
    if origin in major_airports:
        break
    elif origin == "Chicago":
        origin = input("Chicago Midway or Chicago O'Hare: ")
        while origin.lower() not in ["chicago midway", "chicago o'hare"]:
            origin = input("Please enter either 'Chicago Midway' or 'Chicago O'Hare': ")
        break
    elif origin == "Houston":
        origin = input("Houston Bush or Houston William: ")
        while origin.lower() not in ["houston bush", "houston william"]:
            origin = input("Please enter either 'Houston Bush' or 'Houston William': ")
        break
    elif origin == "Washington D.C.":
        origin = input("Washington D.C. Dulles or Washington D.C. Reagan: ")
        while origin.lower() not in ["washington d.c. dulles", "washington d.c. reagan"]:
            origin = input("Please enter either 'Washington D.C. Dulles' or 'Washington D.C. Reagan': ")
        break
    elif origin == "New York":
        origin = input("New York Kennedy or New York LaGuardia: ")
        while origin.lower() not in ["new york kennedy", "new york laguardia"]:
            origin = input("Please enter either 'New York Kennedy' or 'New York LaGuardia': ")
        break
    else:
        print("That city is not in our database. Please enter again")


# date leaving
leaving = input("Enter your departure date. Format(YYYY-MM-DD): ")
# date returning
returning = input("Enter your return date. Format(YYYY-MM-DD): ")

# kayak url
kayak = f"https://www.kayak.com/flights/{major_airports[origin]}-{major_airports[destination]}/{leaving}/{returning}{number}?sort=bestflight_a&fs=price=0-{budget}"

driver = webdriver.Safari()

driver.get(kayak)
driver.maximize_window()
time.sleep(10)

# Separates each element of the flight
departures = []
arrivals = []
prices = []
ticket_link = []

cost = driver.find_elements_by_class_name("f8F1-price-text")
for price in cost:
    prices.append(price.text + "/per person")

legs = driver.find_elements_by_class_name("VY2U")
for i in range(len(legs)):
    if i % 2 == 0:
        departures.append(legs[i].text)
    else:
        arrivals.append(legs[i].text)

links = driver.find_elements_by_xpath("//a[@role='link']")
for link in links:
    flight_link = link.get_attribute("href")
    ticket_link.append(flight_link)

time.sleep(5)

trips = ""

for i in range(len(departures)):
    info = (f"""
            Flight {i + 1}
            Depature: {departures[i]}
            Arrival: {arrivals[i]}
            Price: {prices[i]}
            Link: {ticket_link[i]}
          """)
    trips += info

time.sleep(5)

driver.quit()


email_sender = "michaelcharles10904@gmail.com"
email_password = new_password

subject = "Flight Information"

body = f"""
{trips}
"""

em = EmailMessage()
em["From"] = email_sender
em["To"] = receiver_email
em["subject"] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, receiver_email, em.as_string())



