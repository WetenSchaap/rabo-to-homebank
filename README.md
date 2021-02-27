# RaboToHomebank
Converts Rabobank .csv files to Homebank .csv files using a simple Python script.

## Usage
1. Place the RaboToHomebank.py and the .csv file(s) downloaded from the Rabobank internetbankieren enviroment in the same folder
2. Open the terminal and go the the RaboToHomebank directory
3. Run: `python3 RaboToHomebank.py [CSVfilename1] [CSVfilename2] [etc.]`
4. The conversion takes place.
5. Thed csv file is/are outputted in the RaboToHomebank directory, and will be called `[account-IBAN-number]_[current-date].csv`. 
6. You can no import the .csv file into Homebank. Date formatting is y-m-d.

## Requirements
- Python3
- The `pandas` package.
