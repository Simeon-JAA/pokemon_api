# Pokemon_api

### Functionality
My attempt to demonstrate some skills I have acquired while training and learning to code. This repository gets its data by making calls to the [Pokemon API](https://pokeapi.co/). The script can be run through a terminal (ETL). 

The vision is that all relevant data is extracted from the API, loaded into a local postgres database. From this, a data visualisation tool such as streamlit can access the database to visually represent the data I have chosen to extract from the API.

### ETL Pipeline

The ETL pipeline finds all URLs of the pokemon and extracts, cleans and polishes the data before moving into a local db.


### .env file

You will need an environment file

### Commands
+ Run the commands below to successfully run the script (macOS) - assuming you have python installed on your device.

Create a virtual environment

```python3 -m venv venv```

Activate the virtual environment file with the following variables for the script to work (locally in this current build)

| Variable Name | Value |
| - | - |
| USER | user |
| PASSWORD | password |
| PORT | 5432 | 
| DBNAME | pokemon_api | 
| HOST | localhost |


```source activate venv```

Install requirements for the scripts to run

```pip install -r requirements```

Create Database

```psql postgres -f db_components/schema.sql```

Change to correct directory (ETL)

```cd etl_pipeline```

Run Pipeline

```python3 main.py```

