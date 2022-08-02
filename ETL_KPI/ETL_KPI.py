#ETL load data from file in local but synchronized with onedrive

import pandas as pd
import numpy as np
from datetime import date, datetime, timedelta

source_path = "C:\\Users\\sclient\\CASA Transport SA\\Sécurité et Service Client - PowerBI Data\\Tramway"


start = datetime.now()

print("start")



#update Ca file
old_ca = source_path + "\CA_Journalier.xlsx"
old_ca = pd.read_excel(old_ca)

new_ca = source_path +  "\CA_Journalier_new.xlsx"
new_ca = pd.read_excel(new_ca)

updated_ca = pd.concat([old_ca,new_ca]).drop_duplicates(['Date','Ligne','Code Emplacement','Agence','Equipement','Produit'],keep='last')
updated_ca.to_excel(source_path + '\CA_Journalier.xlsx',index=False)
updated_ca
print("CA Tramway updated")

#update Cab file
old_cab = source_path + "\CA_Bancaire.xlsx"
old_cab = pd.read_excel(old_cab)

new_cab = source_path + "\CA_Bancaire_new.xlsx"
new_cab = pd.read_excel(new_cab)

updated_cab = pd.concat([old_cab,new_cab]).drop_duplicates(['Date','Ligne','Equipement','Mode Paiment'],keep='last')
updated_cab.to_excel(source_path + '\CA_Bancaire.xlsx',index=False)
print("CAB Tramway updated")

#update ARR Ca file
old_arr_ca = source_path + "\ARR_CA.xlsx"
old_arr_ca = pd.read_excel(old_arr_ca)

new_arr_ca = source_path + "\ARR_CA_new.xlsx"
new_arr_ca = pd.read_excel(new_arr_ca)

updated_arr_ca = pd.concat([old_arr_ca,new_arr_ca]).drop_duplicates(['Date','Ligne','Equipement','Libelle Site'],keep='last')
updated_arr_ca.to_excel(source_path + '\ARR_CA.xlsx',index=False)
updated_arr_ca
print("ARR CA Tramway updated")


#update ARR Cab file
old_arr_cab = source_path + "\ARR_CAB.xlsx"
old_arr_cab = pd.read_excel(old_arr_cab)

new_arr_cab = source_path + "\ARR_CAB_new.xlsx"
new_arr_cab = pd.read_excel(new_arr_cab)

updated_arr_cab = pd.concat([old_arr_cab,new_arr_cab]).drop_duplicates(['Date','Ligne','Equipement','Libelle Site', 'Mode Paiment'],keep='last')
updated_arr_cab.to_excel( source_path + '\ARR_CAB.xlsx',index=False)
updated_arr_cab
print("ARR CAB Tramway updated")


#update Freq file
old_freq = source_path + "\Freq_Journaliere.xlsx"
old_freq = pd.read_excel(old_freq)

new_freq = source_path + "\Freq_Journalier_new.xlsx"
new_freq = pd.read_excel(new_freq)

updated_freq = pd.concat([old_freq,new_freq]).drop_duplicates(['Date','Ligne','Station','Produit'],keep='last')
updated_freq.to_excel(source_path + '\Freq_Journaliere.xlsx',index=False)
print("Frequentation Tramway updated")


end = datetime.now()
print(end-start)

