import logging
import os.path
import extract_from_pdf as e
import zipfile as z
import data_handling as d
import json as j
import csv

"""...........................append_csv............................

Function Description: Appends rows to the csv file

Input: rows        (rows to be appended)
       source_file (name of source pdf file)

..................................................................."""

def append_csv(rows, source_file):
    with open("Extracted_Data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    print("Successfully extracted relevant data from json file of "+ source_file)



"""......................Main Code Begins here......................"""

"""Write headings on csv file"""
try:
    with open("Extracted_Data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Bussiness__City", "Bussiness__Country", "Bussiness__Description",	"Bussiness__Name",	"Bussiness__StreetAddress",	"Bussiness__Zipcode",	"Customer__Address__line1",	"Customer__Address__line2"	,"Customer__Email",	"Customer__Name"	,"Customer__PhoneNumber",	"Invoice__BillDetails__Name",	"Invoice__BillDetails__Quantity",	"Invoice__BillDetails__Rate",	"Invoice__Description",	"Invoice__DueDate",	"Invoice__IssueDate",	"Invoice__Number",	"Invoice__Tax"] )
except:
    print()


"""Access TestCase Directory"""
logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
base_path = os.path.dirname(os.path.abspath(__file__))
dir_list = os.listdir(base_path + "/TestDataSet")


"""convert json file to csv"""
for pdf in dir_list:
    e.get_zipped_json(pdf, base_path)
    print(pdf)
    with z.ZipFile(base_path + "/Zippedoutput/"+ pdf[:-4]+".zip") as myzip:
        with myzip.open('structuredData.json') as myfile:

            data = j.load(myfile)

    raw_business_details, business_name, raw_invoice_details, raw_customer_details, table_Details_id, table_path, tax = d.extract_initial_data(data)
    business_details = d.get_Business_Details(raw_business_details, business_name)
    invoice_details = d.get_Invoice_Details(raw_invoice_details)
    customer_details = d.get_customer_details(raw_customer_details)
    items_name, items_qty, items_rate = d.get_Items_Info(data, table_path, table_Details_id)

    rows = d.combine_details(business_details, invoice_details, customer_details, items_name, items_qty, items_rate, tax)
    append_csv(rows, pdf[:-4])















    
