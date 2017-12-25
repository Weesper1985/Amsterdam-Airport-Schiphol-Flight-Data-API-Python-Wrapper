
import requests
import sys
import json
import pandas as pd

date = input("For which date would you like to extract flights [yyyy-mm-dd]? \n")
max_page = int(input("Up to which would you like to extract? \n"))

max_page += 1
pagerange = range (1, max_page)

# Insert API ID and API Key

api_id = ""
api_key = ""

data = []

# Call data & append to dictionary

for page in pagerange:

    try:
        url = "https://api.schiphol.nl/public-flights/flights"
        querystring = {"app_id": "%s" % api_id, "app_key": "%s" % api_key, "scheduledate": "%s" % date,
                       "page": "%s" % page}
        headers = {
            'resourceversion': "v3"
        }
        response = requests.request("GET", url, headers= headers, params=querystring)

        if response.status_code == 200:
            flightList = response.json()
            data.append(flightList)

            print("found {} flights.".format(len(flightList["flights"])))
            for flight in flightList["flights"]:
                print("Found flight with name: {} scheduled on: {} at {} with status {}".format(flight["flightName"],
                                                                                               flight["scheduleDate"],
                                                                                               flight["scheduleTime"],
                                                                                               flight["publicFlightState"][
                                                                                                   "flightStates"]))

        else:
            print("Oops something went wrong\nHttp response code: {}\n{}".format(response.status_code, response.text))

    except requests.exceptions.ConnectionError as error:
        print(error)
        sys.exit()

# Append data to Pandas Dataframe

df = pd.DataFrame()

for dic in data:
    for v in dic.values():
        if isinstance(v, list):
            dfstart = pd.DataFrame(v)
            route = dfstart["route"].apply(pd.Series)
            type = dfstart['aircraftType'].apply(pd.Series)
            state = dfstart["publicFlightState"].apply(pd.Series)
            dfstart.drop(['aircraftType', 'publicFlightState', 'route'], axis=1, inplace=True)
            final = pd.concat(
                [dfstart, route, type, state,], axis=1)
            df = df.append(final)

print(df.head())

# Export to CSV

df.to_csv("CSVOutput"+date+"Uptopage"+str(max_page)+".csv", sep=';', encoding='utf-8')

# Export to JSON

outfile = open("JSONOutput"+date+"Uptopage"+str(max_page)+".json", 'w')
json.dump(data, outfile)
outfile.close()

