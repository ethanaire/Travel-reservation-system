import pandas as pd
from datetime import datetime 

# Convert customer_birth_date of customers.csv to datetime format 
cus = pd.read_csv(r'Data\dataset\customers.csv', sep='\t', engine="openpyxl")
cus['customer_birth_date'] = pd.to_datetime(cus['customer_birth_date'], format='%d/%m/%Y').dt.strftime('%Y-%m-%d')
cus.to_csv(r'Data\customers.csv', index=False)

# Convert departure_date of flight_bookings.csv to datetime format 
fb = pd.read_csv(r'Data\dataset\flight_bookings.csv', sep='\t', engine="openpyxl")
fb['departure_date'] = pd.to_datetime(fb['departure_date'], format='%d/%m/%Y').dt.strftime('%Y-%m-%d')
fb.to_csv(r'Data\flight_bookings.csv', index=False)

# Convert check_in_date and check_out_date of hotel_bookings.csv to datetime format 
hb = pd.read_csv(r'Data\dataset\hotel_bookings.csv', sep='\t', engine="openpyxl")
hb['check_in_date'] = pd.to_datetime(hb['check_in_date'], format='%d/%m/%Y').dt.strftime('%Y-%m-%d')
hb['check_out_date'] = pd.to_datetime(hb['check_out_date'], format='%d/%m/%Y').dt.strftime('%Y-%m-%d')
hb.to_csv(r'Data\hotel_bookings.csv', index=False)

# Handle delimiter and quotechar in hotels.csv
ht = pd.read_csv(r'Data\dataset\hotels.csv', delimiter='\t', quotechar="'", engine="openpyxl")
ht.to_csv(r'Data\hotels.csv', index=False, quoting=1)  # quoting=1 for QUOTE_ALL