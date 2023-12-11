# Pokemon_api

### Functionality
My attempt to demonstrate some skills I have acquired while training and learning to code. This repository gets its data by making calls to the [Pokemon API](https://pokeapi.co/). The script can be run through a terminal (ETL). 

The vision is that all relevant data is extracted from the API, loaded into a local postgres database. From this, a data visualisation tool such as streamlit can access the database to visually represent the data I have chosen to extract from the API.

### ETL Pipeline

The ETL pipeline finds all URLs of the pokemon and extracts, cleans and polishes the data before moving into a local db.


### .env file

You will need an environment file with the following variables for this repository to work. I have listed below the variables and corresponding values to go in your .env file below:

| Variable Name | Value |
| - | - |
| USER | user |
| PASSWORD | password |
| PORT | 5432 | 
| DBNAME | pokemon_api | 
| HOST | localhost |


### Commands
+ Run the commands below to successfully run the script (macOS) - assuming you have python installed on your device.

Create a virtual environment

```python3 -m venv venv```

Activate the virtual environment file with the following command for the script to work

```source venv/bin/activate```

Install requirements for the script to run

```pip install -r requirements```

Create Database

```psql postgres -f db_components/schema.sql```

Change to correct directory (ETL)

```cd etl_pipeline```

Run Pipeline
(the current build will add approximately 300 pokemon before crashing due to a void ability link - I will fix this in a later update but this is enough data to work with)

```python3 main.py```


#### Streamlit (commands)

For the initial data visualisation tool, I have chosen to use streamlit to host. This currently includes basic information, visualisation and some filters given the data. Commands to run the dashboard locally can be seen below!g

Change to correct directory (streamlit_dashboard)

```cd ../streamlit_dashboard```

Run data visualisation

```python3 main.py```


