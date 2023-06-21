# PapyrusNebulae_ExtractPDF
This repository contains the code for Adobe's Papyrus Nebuale Hackathon Round1. The goal of this project is to convert pdf elements to csv.

## Pre Requisites for running the code:

  1. pdfservices-sdk
  2. json 
  3. csv
  4. zipfile
     
Run the command:

`pip install pdfservices-sdk json csv zipfile`

## Code Structure:

There are three code files:

### extract_from_pdf.py
This file contains a function that connects the user to the API and then extracts text elements from the input pdf. It then saves the result in the Zippedoutput folder. The result is saved as a zip file with the same name as the input pdf.

### data_handling.py
This file extracts and segregates useful information from the raw json file. There are several functions in this file and their description is mentioned above the function. It's main job is to sort out relevant data and arrange them in the a suitable way, to be stored in the csv file.

### main.py
This file iterates over the TestDataSet folder and then calls onto extract_from_pdf to get the json file. Then it calls the functions from data_handling.py to get relevant data. Then it finaly writes the data to the "Extracted_Data.csv" file.

## How to run the code.

After satisfying the pre requisites and ensuring that test data is correctly stored, with no Extracted_Data.csv file in the same folder(To re run the code, one would have to relocate the existing Extracted_Data.csv file to some other location). Run the following command on the terminal:

`python ./main.py`






