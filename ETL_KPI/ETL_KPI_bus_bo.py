#ETL load data from file in local but synchronized with onedrive

import pandas as pd
import numpy as np
from datetime import date, datetime, timedelta


start = datetime.now()

print("start")


#Bus BO
source_path = "C:\\Users\\sclient\\CASA Transport SA\\Sécurité et Service Client - PowerBI Data\\BUS\\Datamart Bus"


old_ca_bus = source_path + "\Bus_CA.xlsx"
old_ca_bus = pd.read_excel(old_ca_bus)

new_ca_bus= source_path + "\RECETTE_new.xlsx"
new_ca_bus = pd.read_excel(new_ca_bus)

old_freq_bus = source_path + "\Bus_Freq.xlsx"
old_freq_bus = pd.read_excel(old_freq_bus)

new_freq_bus= source_path + "\VALIDATION_new.xlsx"
new_freq_bus = pd.read_excel(new_freq_bus)

#update Bus Ca file
updated_ca_bus = pd.concat([old_ca_bus,new_ca_bus]).drop_duplicates(['date','id_ligne','id_produit','id_operation_vente','id_site','id_equipement','montant vente','nombre vente'],keep='last')
updated_ca_bus.to_excel(source_path + '\Bus_CA.xlsx',index=False)
print("BO CA Bus updated")


#update Bus Freq file
updated_freq_bus = pd.concat([old_freq_bus,new_freq_bus]).drop_duplicates(['date','id_ligne','id_produit','1ere montee'],keep='last')
updated_freq_bus.to_excel(source_path + '\Bus_Freq.xlsx',index=False)
print("BO Frequentation Bus updated")


end = datetime.now()
print(end-start)

