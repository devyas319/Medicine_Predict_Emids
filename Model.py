
##Team:Evolve
##Dev Vyas
##Dhruvrajsinh Solanki
##Sarabh Sharma


##Importing Libraries

import pandas as pd
from sklearn.linear_model import LogisticRegression

#######
##Function For taking Inputs
def take_input():

        def check_age(Age):
            if(Age<20):
                return [1,0,0,0,0,0,0]
            if(Age>=20 and Age<30):
                return [0,1,0,0,0,0,0]
            if(Age>=30 and Age<40):
                return [0,0,1,0,0,0,0]
            if(Age>=40 and Age<50):
                return [0,0,0,1,0,0,0]
            if(Age>=50 and Age<60):
                return [0,0,0,0,1,0,0]
            if(Age>=60 and Age<70):
                return [0,0,0,0,0,1,0]
            if(Age>=70):
                return [0,0,0,0,0,0,1]

        def check_gender(Gender):
            if(Gender=="M"):
                return [1,0]
            if(Gender=="F"):
                return [0,1]

        def check_BP(BP):
            if(BP=="H"):
                return [1,0,0]
            if(BP=="L"):
                return [0,1,0]
            if(BP=="N"):
                return [0,0,1]

        def check_Cholesterol(Cholesterol):
            if(Cholesterol=="H"):
                return [1,0]
            if(Cholesterol=="N"):
                return [0,1]
        def check_NA2K(Na2K):
            if(Na2K<10):
                return [0,1,0,0]
            if(Na2K>=10 and Na2K<20 ):
                return [0,1,0,0]
            if(Na2K>=20 and Na2K<30 ):
                return [0,0,1,0]
            if(Na2K>=40):
                return [0,0,1,0]
            
                
        list=[]
        inp=[]
        Age=input("EnterYout Age: ")
        Age=int(Age)
        Gender=input("Enter your Gender M/F: ")
        BP=input("Enter you BP High/Low/Normal(H/L/N): ")
        Cholesterol=input("Enter you Cholesterol High/Normal(H/N): ")
        Na2K=input("EnterYout Na_to_K: ")
        Na2K=int(Na2K)


        list.append(check_age(Age))
        list.append(check_gender(Gender))
        list.append(check_BP(BP))
        list.append(check_Cholesterol(Cholesterol))
        list.append(check_NA2K(Na2K))


        for i in range(len(list)):
            for j in range(len(list[i])):
                if list[i][j]==0:
                    inp.append(0)
                else:
                    inp.append(1)
        return inp

user_input=take_input()
#print(user_input)
#reading data
#reading data
#reading data
df_drug = pd.read_csv("Drugs.csv")
#print(df_drug)


#Adding dataset with deseace name
#Adding dataset with deseace name
#Adding dataset with deseace name
df_medicine = pd.read_csv("dataset.csv")

#Adding dataset with deseace name
#Adding dataset with deseace name
#Adding dataset with deseace name
df_medicine = pd.read_csv("dataset.csv")

# print(df_medicine.head())


#Data Binnig
#Data Binnig
#Data Binnig
#Data Binnig
#Data Binnig
bin_age = [0, 19, 29, 39, 49, 59, 69, 80]
category_age = ['<20s', '20s', '30s', '40s', '50s', '60s', '>60s']
df_drug['Age_binned'] = pd.cut(df_drug['Age'], bins=bin_age, labels=category_age)
df_drug = df_drug.drop(['Age'], axis = 1)

bin_NatoK = [0, 9, 19, 29, 50]
category_NatoK = ['<10', '10-20', '20-30', '>30']
df_drug['Na_to_K_binned'] = pd.cut(df_drug['Na_to_K'], bins=bin_NatoK, labels=category_NatoK)
df_drug = df_drug.drop(['Na_to_K'], axis = 1)

#copy of data frame
df_drug2=df_drug.copy(deep=True)
df_drug3=df_drug.copy(deep=True)



#Removing 2 columns which will not be used at this time
df_drug = df_drug.drop(['Dosage','Frequency'], axis = 1)
#Takinf Disease and selecting rows based on that
Disease=input("Enter disease: ")

df_medicine=df_medicine.loc[df_medicine['Disease']== Disease]
# print(df_medicine)

list_med=df_medicine['Drug name'].to_list()
# print(list_med)

df_drug=df_drug.loc[df_drug['Drug'].isin(list_med)]
# print(df_drug.head())


# [0,1,0,0,0,0,0,1,0,0,1,0,1,0,0,0,1,0]

#Splitting the dataset
X = df_drug.drop(["Drug"], axis=1)
y = df_drug["Drug"]

X = pd.get_dummies(X)
# print(X)



#MOdel to predict decease
#MOdel to predict decease
#MOdel to predict decease
#MOdel to predict decease
#MOdel to predict decease
LRclassifier = LogisticRegression(solver='liblinear', max_iter=5000)
LRclassifier.fit(X, y)

#Prediction Medicine as per given User Input
y_pred = LRclassifier.predict([user_input])
# print(y_pred)


#to predictdosage 
#to predictdosage 
#to predictdosage 
#to predictdosage 
#to predictdosage 


#finiding related drug only

#select if you want more detailed but will need more deetailed dataset
#Because it will take consideration of only relatable and founded medicines but now
#due to limited dataset not taking this feature into consideration
# df_drug2=df_drug2.loc[df_drug2['Drug'].isin(y_pred)]

df_drug2=df_drug2.drop(['Drug'],axis=1)

#make x and y
y1 = df_drug2["Dosage"]
X1 = df_drug2.drop(["Dosage","Frequency"], axis=1)


#get dummies

X1 = pd.get_dummies(X1)



#MOdel to predict dosage
#MOdel to predict dosage
#MOdel to predict dosage
#MOdel to predict dosage
#MOdel to predict dosage

LRclassifier2 = LogisticRegression(solver='liblinear', max_iter=5000)
LRclassifier2.fit(X1, y1)

y_pred2 = LRclassifier2.predict([user_input])
#print(y_pred2)



#to predictdosage frequency
#to predictdosage frequency
#to predictdosage frequency
#to predictdosage frequency
#to predictdosage frequency




#make x and y
df_drug3=df_drug3.drop(['Drug'],axis=1)
df_drug3=df_drug3.drop(['Dosage'],axis=1)

X2 = df_drug3.drop(["Frequency"], axis=1)
y2 = df_drug3["Frequency"]

#get dummies

X2 = pd.get_dummies(X2)
# print(X2)


LRclassifier3 = LogisticRegression(solver='liblinear', max_iter=5000)
LRclassifier3.fit(X2, y2)

y_pred3 = LRclassifier3.predict([user_input])
# print(y_pred3)


##Converting output into string from integer
##Converting output into string from integer

y_pred=str(y_pred)
y_pred2=str(y_pred2)
y_pred3=str(y_pred3)

##Printring Output
##Printring Output
##Printring Output
##Printring Output
print("--------------------------------------------------------------")
print("--------------------------------------------------------------")
print("--------------------------------------------------------------")
print("--------------------------------------------------------------")
print("Medicine needed to gave is "+y_pred+" with dosage: " +y_pred2+" mg and freqency of "+y_pred3+" doses per day")
print("Medicine needed to gave is "+y_pred+" with dosage: " +y_pred2+" mg and freqency of "+y_pred3+" doses per day")
print("Medicine needed to gave is "+y_pred+" with dosage: " +y_pred2+" mg and freqency of "+y_pred3+" doses per day")
print("Medicine needed to gave is "+y_pred+" with dosage: " +y_pred2+" mg and freqency of "+y_pred3+" doses per day")
print("Medicine needed to gave is "+y_pred+" with dosage: " +y_pred2+" mg and freqency of "+y_pred3+" doses per day")
print("Medicine needed to gave is "+y_pred+" with dosage: " +y_pred2+" mg and freqency of "+y_pred3+" doses per day")
print("Medicine needed to gave is "+y_pred+" with dosage: " +y_pred2+" mg and freqency of "+y_pred3+" doses per day")

print("--------------------------------------------------------------")
print("--------------------------------------------------------------")
print("--------------------------------------------------------------")
print("--------------------------------------------------------------")