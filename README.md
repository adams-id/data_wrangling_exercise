# Datopian Data Wrangling Junior Software Engineer Challenge
 This script is used to get a normalized CSV data file of Road Safety Facts and Figures in the EU..

## Setting up for this project
To use this project locally, [python](https://www.python.org/downloads/) must be installed.

1. **Clone the repository:**
    ```sh
    git clone -b master https://github.com/adams-id/data_wrangling_exercise.git
    ```

2. **Start the virtual environment:**
    Run the following commands in the project root folder.
    ```sh
    virtualenv env
    source env/Scripts/activate # for windows
    source env/bin/activate # for MacOs
    ```

3. **Install External Dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Running the script**
    Run this function to populate CSV 
    ```py
    get_data()
    ```

    In the project root directory, run:
    ```sh
    python road_safety_eu/scripts/normalize_csv
    ```

## Script - How it works  
    The function `get_data` contains the technique behind the csv normalization. <br>

    The  `get_data` function takes the wikipedia url and scrapes it for the data necessary by setting the specific table's class attribute. This data is then arranged and filtered according to the requiremnets of the challenge.<br>
    The resulting dataframe is then populated to a CSV file located in the [data folder 📂](road_safety_eu/data)  
