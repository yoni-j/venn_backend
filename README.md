# Intro
This app tkaed data from this public api - https://data.cityofnewyork.us/City-Government/Census-Demographics-at-the-Neighborhood-Tabulation/rnsn-acs2, for each record calculates the business rate by the business logic definition and stores in the db


# Run

- install latest version of python
- run "pip install poetry"
- run "poetry install"
- run "flask run"


# Api

- The endpoint to get the data: http://localhost:8000
- query filters: min2000, max2000, min2010, max2010, min_total_change, max_total_change, min_percent_change, max_percent_change

# Project map

- **api.py** - The main file of the app
- **venapp/model.py** - defines the db model - in this case just one "Record" model
- **import_db.py** - helper to initilize the db data
- **business_logic.py** - helper for the business_logic for rating - more explanation in the file