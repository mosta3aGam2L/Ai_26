#https://leetcode.com/studyplan/introduction-to-pandas/
#ALL problem in page.
import pandas as pd
'''
def createDataframe(student_data):
    # Create and return the DataFrame
    return pd.DataFrame(student_data, columns=['student_id', 'age'])

###############3333

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return list( players.shape)    
    
#######################3
    
def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return(employees.head(3))
    
#####################3

def selectData(students: pd.DataFrame) -> pd.DataFrame:
       return students.loc[students['student_id'] == 101, ['name', 'age']]    
    
#######################

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
     employees['bonus']=2*employees['salary']
     return employees    
    
    
#########################

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
  #  c= customers[customers.loc['customer_id = 4'],['name',age]]
     return customers.drop_duplicates("email")
    
    
###################

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
   return  students.dropna()

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
   return  students.dropna(subset='name')      
########################

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = employees['salary'] * 2
    

    return employees
###########33333333333

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
#    return(students.rename ['student_id','first_name','last_name','age_in_years']
 students.rename(columns = {'id':'student_id','first':'first_name','last':'last_name','age':'age_in_years'}, inplace = True)

 return students
################33333
# 
def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    #students['grade']=students['grade'.astype(int)]
    s=students.astype({'grade':int})
    return s

################################
 
def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products['quantity'].fillna(0, inplace = True)
    return products
    
#########################3
def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
   return pd.concat([df1,df2])
    
#####################3
def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot(index='month',columns='city',values='temperature')
    
########################3

#.melt
def meltTable(report: pd.DataFrame) -> pd.DataFrame:
 return report.melt(
        id_vars='product', 
        value_vars=['quarter_1', 'quarter_2', 'quarter_3', 'quarter_4'], 
        var_name='quarter', 
        value_name='sales')
    
##########################3
def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
# error return animals.loc[animals['weight']>100,['name']]
 return animals[animals['weight'] > 100].sort_values('weight', ascending=False)[['name']]




    
    '''