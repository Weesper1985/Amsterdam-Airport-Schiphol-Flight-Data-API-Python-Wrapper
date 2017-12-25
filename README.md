# Amsterdam-Airport-Schiphol-Flight-Data-API-Python-Wrapper
Basic Python wrapper for Amsterdam Airport Schiphol's flight data API, which enables one to extract flight data as a Pandas dataframe, or alternatively export to JSON or CSV

- Kindly make sure to have pyopenssl, ndg-httpsclient and pyasn1 installed in order to interact with the API
- Insert your API-id and API-key in the py.file, [which can be requested here](https://developer.schiphol.nl/)


Example of the resulting dataframe:

```
               actualLandingTime             actualOffBlockTime  \
0                           None                           None   
1  2017-12-25T05:29:00.000+01:00                           None   
2                           None  2017-12-25T05:31:20.000+01:00   
3                           None  2017-12-25T05:09:00.000+01:00   
4                           None  2017-12-25T05:31:20.000+01:00   

  aircraftRegistration  airlineCode baggageClaim  \
0                               148         None   
1                               148         None   
2                URGAT          100         None   
3                PHPXB          148         None   
4                URGAT          175         None   

                                  checkinAllocations  \
0                                               None   
1                                               None   
2  {'checkinAllocations': [{'endTime': '2017-12-2...   
3                                               None   
4  {'checkinAllocations': [{'endTime': '2017-12-2...   

                   codeshares           estimatedLandingTime  \
0                        None                           None   
1                        None  2017-12-25T05:17:12.000+01:00   
2  {'codeshares': ['KL3099']}                           None   
3                        None                           None   
4  {'codeshares': ['KL3099']}                           None   

  expectedTimeBoarding expectedTimeGateClosing     ...      scheduleDate  \
0                 None                    None     ...        2017-12-25   
1                 None                    None     ...        2017-12-25   
2                 None                    None     ...        2017-12-25   
3                 None                    None     ...        2017-12-25   
4                 None                    None     ...        2017-12-25   

  scheduleTime schemaVersion serviceType  terminal transferPositions  \
0     05:25:12             3           P       NaN              None   
1     05:25:12             3           P       NaN              None   
2     05:30:00             3           J       1.0              None   
3     05:30:00             3        None       NaN              None   
4     05:30:00             3           J       1.0              None   

   destinations iatamain iatasub flightStates  
0         [AMS]     None    None        [DEP]  
1         [AMS]     None    None        [LND]  
2         [KBP]      73E     73E        [DEP]  
3         [AMS]     None    None        [DEP]  
4         [KBP]      73E     73E        [DEP]
```
