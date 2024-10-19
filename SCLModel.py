import pandas as pd
import numpy as np
import nltk 

# Load the CSV file
file_path = '~/Documents/AEPData/CORE_HackOhio_subset_cleaned_downsampled 1.csv'
data = pd.read_csv(file_path)

count = data.shape[0]

# Dictionary of High Energy 
HighEnergyDict = {
    1: "Gravity_Suspension_Load",
    2: "Motion_Motor_With_Worker_On_Foot",
    3: "Mechanical",
    4: "Temperature_Steam",
    5: "Pressure_Explosion",
    6: "Electrical_Contact_With_Source",
    7: "Chemical_Radiation",
    8: "Gravity_Fall_From_Elevation",
    9: "Motion_Motor_Incident",
    10: "Temperature_High",
    11: "Temperature_Fire_With_Sustained_Fuel_Source",
    12: "Pressure_Excavation",
    13: "Electrical_Arc_Flash"
}

IncidentClassification = {
    1: "HSIF",
    2: "LSIF",
    3: "PSIF",
    4: "Capacity",
    5: "Exposure",
    6: "Success",
    7: "Low-Severity"
}

for i in range(count):
    PNT_NM_TOKEN = nltk.word_tokenize(data["PNT_NM"][i])
    QUALIFIER_TEXT_TOKEN = nltk.word_tokenize(data["QUALIFIER_TXT"][i])
    PNT_ATRISKNOTES_TX_TOKEN = nltk.word_tokenize(data["PNT_ATRISKNOTES_TX"][i])

# TODO identify if there was high energy present
# TODO idenify if there was a high energy incident
# TODO identify if there was a serious injury sustained
# TODO identify if there was a direct control present
# 