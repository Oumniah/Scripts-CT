#ETL load data from file in local but synchronized with onedrive

import pandas as pd
import numpy as np
from datetime import date, datetime, timedelta

source_path = "C:\\Users\\Administrateur\\OneDrive - CASA Transport SA\\ETL Final"

start = datetime.now()

print("start")

old_ca = source_path + "\CA_Journalier.xlsx"
old_ca = pd.read_excel(old_ca)

new_ca = source_path + "\CA_Journalier_new.xlsx"
new_ca = pd.read_excel(new_ca)

updated_ca = pd.concat([old_ca,new_ca]).drop_duplicates(["Date","Ligne","Code Emplacement","Agence","Equipement","Produit"],keep="last")
updated_ca.to_excel(source_path + "\CA_Journalier.xlsx",index=False)




old_cab = source_path + "\CA_Bancaire.xlsx"
old_cab = pd.read_excel(old_cab)

new_cab = source_path + "\CA_Bancaire_new.xlsx"
new_cab = pd.read_excel(new_cab)

updated_cab = pd.concat([old_cab,new_cab]).drop_duplicates(["Date","Ligne","Equipement","Mode Paiment"],keep="last")
updated_cab.to_excel(source_path + "\CA_Bancaire.xlsx",index=False)




old_arr_ca = source_path + "\ARR_CA.xlsx"
old_arr_ca = pd.read_excel(old_arr_ca)

new_arr_ca = source_path + "\ARR_CA_new.xlsx"
new_arr_ca = pd.read_excel(new_arr_ca)

updated_arr_ca = pd.concat([old_arr_ca,new_arr_ca]).drop_duplicates(["Date","Ligne","Equipement","Libelle Site"],keep="last")
updated_arr_ca.to_excel(source_path + "\ARR_CA.xlsx",index=False)




old_arr_cab = source_path + "\ARR_CAB.xlsx"
old_arr_cab = pd.read_excel(old_arr_cab)

new_arr_cab = source_path + "\ARR_CAB_new.xlsx"
new_arr_cab = pd.read_excel(new_arr_cab)

updated_arr_cab = pd.concat([old_arr_cab,new_arr_cab]).drop_duplicates(["Date","Ligne","Equipement","Libelle Site", "Mode Paiment"],keep="last")
updated_arr_cab.to_excel(source_path + "\ARR_CAB.xlsx",index=False)




old_freq = source_path + "\Freq_Journaliere.xlsx"
old_freq = pd.read_excel(old_freq)

new_freq = source_path + "\Freq_Journaliere_new.xlsx"
new_freq = pd.read_excel(new_freq)

updated_freq = pd.concat([old_freq,new_freq]).drop_duplicates(["Date","Ligne","Station","Produit"],keep="last")
updated_freq.to_excel(source_path + "\Freq_Journaliere.xlsx",index=False)



end = datetime.now()
print(end-start)