#JavaScript Object Notation, a light weight data format with many similarities to python dictionaries
import json
#Numerical Python
import numpy as np
#Paneled Data
import pandas as pd
import math
from matplotlib import pyplot as plt
from pandas.core.arrays.string_ import StringArray




def bmical(hgCM,wtkg):
    hgM=hgCM/100
    bmival=(wtkg/(hgM**2))   
    return(bmival)  


def bmicatcal(bmif64):    
    bmival1=np.float64(bmif64)

    if(bmival1<=18.4 and bmival1>0):
       bmicat="Under Weight"         
    elif (bmival1>=18.5 and bmival1<=24.9):        
        bmicat="Normal Weight"          
    elif (bmival1>=25 and bmival1<=29.9):
        print(bmival1)
        bmicat="Over Weight"          
    elif (bmival1>=30 and bmival1<=34.9):
        bmicat="Moderately obese"            
    elif (bmival1>=35 and bmival1<=39.9):
        bmicat="Severely obese"         
    elif(bmival1>=40):
        bmicat="VerySeverelyobese"     
    elif(bmival1<=0):
        raise Exception("Sorry,no numbers below zero")     

    return(str(bmicat))


def bmihealthcal(bmif1): 
    bmival2=np.float64(bmif1)   
    if (bmival2<=18.4 and bmival2>0):        
        bmihealth="Malnutrition Risk"
    elif (bmival2>=18.5 and bmival2<=24.9):
         bmihealth="Low Risk"
    elif (bmival2>=25 and bmival2<=29.9):          
        bmihealth="Enhanced Risk"   
    elif (bmival2>=30 and bmival2<=34.9):        
        bmihealth="Medium Risk"     
    elif (bmival2>=35 and bmival2<=39.9):        
        bmihealth="High risk" 
    elif(bmival2>=40):        
        bmihealth="Very High risk"
    elif(bmival2<=0):
        raise Exception("Sorry,no numbers below zero")    

    return(str(bmihealth))    


#Given List of Dictionaries
person_ld=[
    {"Gender":"Male","HeightCm":171,"WeightKg":96}, 
    {"Gender":"Male","HeightCm":161,"WeightKg":85},
    {"Gender":"Male","HeightCm":180,"WeightKg":77}, 
    {"Gender":"Female","HeightCm":166,"WeightKg":62},
    {"Gender":"Female","HeightCm":150,"WeightKg":70},
    {"Gender":"Female","HeightCm":167,"WeightKg":82}
        ] 


#print(type(person_ld))
dataframe_person=pd.DataFrame(person_ld)
#print(dataframe_person)
Table1=dataframe_person
print(Table1)
print(len(Table1.index))
iteratevalue=len(Table1.index)
Table1["BMI"]=bmical(Table1["HeightCm"],Table1["WeightKg"])
print(Table1["BMI"])

arrBMI=pd.DataFrame(Table1["BMI"])
print(arrBMI)
c4=pd.Series([iteratevalue], dtype="string")
c5=pd.Series([iteratevalue], dtype="string")
print(bmicatcal(Table1.iloc[0]["BMI"]))

for i in range(iteratevalue):
    c4[i]=bmicatcal(Table1.iloc[i]["BMI"])
    c5[i]=bmihealthcal(Table1.iloc[i]["BMI"])

print(c4)
Table1["BMI Category"]=c4
Table1["Health Risk"]=c5
print(Table1)

wt= Table1["WeightKg"].head(5)
BMIVal = Table1["BMI"].head(5)
 
# Figure Size
fig = plt.figure(figsize =(5,5)) 
# Horizontal Bar Plot
plt.bar(wt[0:5], BMIVal[0:5]) 
# Show Plot
plt.show()






