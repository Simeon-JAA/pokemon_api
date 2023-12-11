"""Streamlit dashboard main file"""


from os import environ

from dotenv import load_dotenv
import pandas as pd
from pandas import DataFrame
import streamlit as st

from db_components.db_queries import get_db_connection


def display_header(header_text: str) -> None:
    """Displays header"""

    if not isinstance(header_text, str):
        raise TypeError("Error: Function input should be a string type!")

    st.header(header_text)


def display_text(input_text: str) -> None:
    """Displays text in argument"""

    st.text(input_text)


def display_bar_chart(data_df: DataFrame, x_axis: str = None, y_axis: str = None) -> None:
    """Displays basic bar chart information"""

    st.bar_chart(data=data_df,)


if __name__ == "__main__":

    load_dotenv()

    config = environ

    conn = get_db_connection(config)

    display_header("example header")
    display_text("example text")

    conn.close()
