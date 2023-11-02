# Pokemon_api

### Functionality
My attempt to demonstrate some skills I have acquired while training and learning to code. This repository gets its data by making calls to the [Pokemon API](https://pokeapi.co/). Currently, the script is built to run only in a terminal. 
When the script is run, it will show the basic stats of the pokemon you input when prompted to, providing they exist within the API.

The ETL pipeline folder is a work in progress. The vision is that all relevant data is extracted from the API, loaded into  a local postgres database. From this, a local data visualisation tool such as streamlit can access the database to visually represent the data I have chosen to use in the API. 

### ETL Pipieline

_WORK IN PROGRESS!_

### Commands
+ Run the commands below to successfully run the script (macOS) - assuming you have python installed on your device.

Create a virtual environment

```python3 -m venv venv```

Activate the virtual environment

```source activate venv```

Install requirements for the scripts to run

```pip install -r requirements```

Run Script

```python3 build_team.py```

