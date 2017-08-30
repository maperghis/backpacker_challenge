# Backpacker Challenge

Every year Australia welcomes thousands of backpackers to its shores for work
and for holiday. The Government of Australia have asked me to develop a backend
web application to discover more about the backpackers and where they are
spending their time. They have provided me with two json files which give
information about some of the backpackers in Australia (i.e. name, gender,
nationality, states visited, days traveling) and the list of all the seven
states and territories in Australia. I am to implement the solution in Python
using the web framework Django.

The Australian Government asked me to provide the following endpoints:
* Given a backpacker; provide the list of transport they use, the colour of
their eyes and their nationality
* Given a state or territory, provide the list of people who have been there

## Data Files

### 1. Backpackers

- First name (string)
- Last name (string)
- Age (integer)
- Gender (male/female)
- Eye colour (blue/brown)
- Nationality (list) [British,French,German,Spanish,Italian,Swiss,Canadian]
- Email (string)
- Phone (string)
- States/Territories Visited (list)
- Distance travelled in kilometers (integer)
- Mode of transport (list) [car,bus,train,aeroplane,boat]
- Days spent travelling (integer)
- Working (boolean)

### 2. States/Territories

- New South Wales (NSW)
- Queensland (QL)
- Victoria (VIC)
- South Australia (SA)
- Western Australia (WA)
- Northern Australia (NT)
- Tasmania (TAS)

## Solution
