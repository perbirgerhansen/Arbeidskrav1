# -*- coding: utf-8 -*-
"""
Arbeidskrav 1

Program som beregner og presenterer de årlige totalkostnadene for elbil 
og for bensinbil samt kostnadsdifferanse

Created on Tue Nov 06 18:34:45 2024
@author: Per Hansen, Perbirgerhansen@outlook.com



"""
KM = 10000 #Antall km Pr. År
Forsikring_EL = 5000 #Forsikring for elbil pr. år 
Forsikring_Bensin = 7500 #Forsikring for bensinbil pr. år
Trafikkavg = 8.38*365 #Trafikkforsikringsavgift år både for El og Bensin 
Strombruk_EL = 0.2 #Strømbruk pr. Kwh 
Strompris = 2.00*Strombruk_EL*KM #Strømpris * bruk * KM Elbil 
Bensinpris = 1.0*KM #Bensinpris * km bensinbil
Bomavgift_EL = 0.1*KM #Bomavgift * km Elbil 
Bomavgift_Bensin = 0.3*KM #Bomavgift * km Bensinbil
elbilsum = Forsikring_EL + Trafikkavg + Strompris + Bomavgift_EL #Summer elbil
Bensinbilsum = Forsikring_Bensin + Trafikkavg + Bensinpris + Bomavgift_Bensin #Summer Bensinbil

print ("Pris pr År for el-bil:", elbilsum)
print ("Pris pr. år for bensinbil:", Bensinbilsum)
print("Kostandsdifferansen", Bensinbilsum - elbilsum )

