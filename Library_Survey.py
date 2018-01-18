#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 20:54:59 2018

@author: jillbudden
See Survey: https://docs.google.com/forms/d/e/1FAIpQLSdSSbWCvSlAZeH8W0gnQVC3DMt_Swofh4l3Nb5UJhPtJ9hIbA/viewform?usp=sf_link
"""

# libraries
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Import data
file = 'librarySurveyRaw.csv'

# Load spreadsheet
data = pd.read_csv(file, sep=',')

# Print the head of the DataFrame
print(data.head())

# rename columns
data.columns=['timestamp', 'age', 'gender', 'maritalStatus', 'children14', 'highestEducation', 'city', 'state', 
                    'brickmortarFreq', 'digitalresourcesFreq', 'websiteFreq', 'appFreq', 
                    'printedbooksEase', 'ebooksEase', 'internetwifiEase', 'musicEase', 'moviesEase', 
                    'educationprogramsEase', 'childprogEase', 'meetingspaceEase', 'practiceroomsEase', 
                    'jobsearchEase', 'librarianEase', 'bookclubsEase', 'renewalsEase',	
                    'payfeesEase', 'elaborate1','localbookstoreFreq', 'barnesnobleFreq', 'amazonFreq', 
                    'onlinelearnFreq', 'coffeeshopFreq', 'locallibFreq', 'elaborate2', 'improveUtil',]

# Print the head of the DataFrame
print(data.head())

########################Recode data###############################

# Define recode_age()
def recode_age(age_value):

    # Return 1 if age_value is 'Under_18'
    if age_value == 'Under 18':
        return 1
    
    # Return 2 if age_value is '18-24'
    elif age_value == '18 - 24':
        return 2
    elif age_value == '25 - 34':
        return 3
    elif age_value == '35 - 44':
        return 4
    elif age_value == '45 - 54':
        return 5
    elif age_value == '55 - 64':
        return 6
    elif age_value == '65 - 74':
        return 7
    elif age_value == '75 or older':
        return 8
    
    # Return np.nan    
    else:
        return 99999
    
# Apply the function to the sex column
# Apply your recode_age() function over data.age using the .apply() 
# method to create a new column: 'age_recode'

data['_age'] = data.age.apply(recode_age)


# Define recode_sex()
def recode_gender(gender_value):
    if gender_value == 'Female':
        return 1
    elif gender_value == 'Male':
        return 2

    # Return np.nan    
    else:
        return 99999

data['_gender'] = data.gender.apply(recode_gender)



# recode marital_status
def recode_maritalStatus(marital_value):
    if marital_value == 'Single, never married':
        return 1
    elif marital_value == 'Married or domestic partnership':
        return 2 
    elif marital_value == 'Widowed':
        return 3
    elif marital_value == 'Divored':
        return 4
    elif marital_value == 'Separated':
        return 5
    else:
        return 99999

data['_maritalStatus'] = data.maritalStatus.apply(recode_maritalStatus)


# recode children
def recode_children14(children_value):
    if children_value == 'Yes':
        return 1
    elif children_value == 'No':
        return 2 
    else:
        return 99999

data['_children14'] = data.children14.apply(recode_children14)


# recode education
def recode_highestEducation(education_value):
    if education_value == 'Some high school':
        return 1
    elif education_value == 'High school diploma or equivalent':
        return 2 
    elif education_value == 'Associate or technical degree':
        return 3
    elif education_value == 'Bachelor\'s degree':
        return 4
    elif education_value == 'Master\'s degree':
        return 5
    elif education_value == 'Professional degree (e.g., JD, MD, DNP, DVM, etc.)':
        return 6
    elif education_value == 'Doctorate':
        return 7
    else:
        return 99999

data['_highestEducation'] = data.highestEducation.apply(recode_highestEducation)


# recode city
def recode_city(city_value):
    if city_value == 'Chicago':
        return 1
    if city_value == 'Oak Park':
        return 1
    if city_value == 'Highland Park':
        return 1
    if city_value == 'Los Angeles':
        return 1
    if city_value == 'Naperville':
        return 1
    if city_value == 'Milwaukee':
        return 1
    if city_value == 'Irvine':
        return 1
    if city_value == 'Newark':
        return 1
    if city_value == 'New York':
        return 1
    if city_value == 'Orange County':
        return 1
    if city_value == 'San Francisco':
        return 1
    if city_value == 'Minneapolis':
        return 1
    if city_value == 'Brooklyn, NY':
        return 1
    if city_value == 'St. Louis':
        return 1
    if city_value == 'San Diego':
        return 1
    if city_value == 'Atlanta':
        return 1
    else:
        return 2

data['_city'] = data.city.apply(recode_city)


# recode brickmortar_freq
def recode_brickmortarFreq(brickmortarFreq_value):
    if brickmortarFreq_value == 'Daily':
        return 1
    if brickmortarFreq_value == 'Weekly':
        return 2
    if brickmortarFreq_value == 'Monthly':
        return 3
    if brickmortarFreq_value == 'A Few Months a Year':
        return 4
    if brickmortarFreq_value == 'Yearly':
        return 5
    if brickmortarFreq_value == 'Every Few Years':
        return 6
    if brickmortarFreq_value == 'Never':
        return 7
    if brickmortarFreq_value == 'My Library Doesn\'t Have This':
        return 8
    else:
        return 999999

data['_brickmortarFreq'] = data.brickmortarFreq.apply(recode_brickmortarFreq)


# recode digitalresourcesFreq
def recode_digitalresourcesFreq(digitalresourcesFreq_value):
    if digitalresourcesFreq_value == 'Daily':
        return 1
    if digitalresourcesFreq_value == 'Weekly':
        return 2
    if digitalresourcesFreq_value == 'Monthly':
        return 3
    if digitalresourcesFreq_value == 'A Few Months a Year':
        return 4
    if digitalresourcesFreq_value == 'Yearly':
        return 5
    if digitalresourcesFreq_value == 'Every Few Years':
        return 6
    if digitalresourcesFreq_value == 'Never':
        return 7
    if digitalresourcesFreq_value == 'My Library Doesn\'t Have This':
        return 8
    else:
        return 999999

data['_digitalresourcesFreq'] = data.digitalresourcesFreq.apply(recode_digitalresourcesFreq)


# recode websiteFreq
def recode_websiteFreq(websiteFreq_value):
    if websiteFreq_value == 'Daily':
        return 1
    if websiteFreq_value == 'Weekly':
        return 2
    if websiteFreq_value == 'Monthly':
        return 3
    if websiteFreq_value == 'A Few Months a Year':
        return 4
    if websiteFreq_value == 'Yearly':
        return 5
    if websiteFreq_value == 'Every Few Years':
        return 6
    if websiteFreq_value == 'Never':
        return 7
    if websiteFreq_value == 'My Library Doesn\'t Have This':
        return 8
    else:
        return 999999

data['_websiteFreq'] = data.websiteFreq.apply(recode_websiteFreq)


# recode appFreq
def recode_appFreq(appFreq_value):
    if appFreq_value == 'Daily':
        return 1
    if appFreq_value == 'Weekly':
        return 2
    if appFreq_value == 'Monthly':
        return 3
    if appFreq_value == 'A Few Months a Year':
        return 4
    if appFreq_value == 'Yearly':
        return 5
    if appFreq_value == 'Every Few Years':
        return 6
    if appFreq_value == 'Never':
        return 7
    if appFreq_value == 'My Library Doesn\'t Have This':
        return 8
    else:
        return 999999

data['_appFreq'] = data.appFreq.apply(recode_appFreq)


# recode printedbooksEase
def recode_printedbooksEase(printedbooksEase_value):
    if printedbooksEase_value == 'Very Easy':
        return 1
    if printedbooksEase_value == 'Easy':
        return 2
    if printedbooksEase_value == 'Neutral':
        return 3
    if printedbooksEase_value == 'Difficult':
        return 4
    if printedbooksEase_value == 'Very Difficult':
        return 5
    if printedbooksEase_value == 'My Library Doesn\'t Have This':
        return 6
    if printedbooksEase_value == 'Don\'t Know/Haven\'t Used':
        return 7
    else:
        return 999999

data['_printedbooksEase'] = data.printedbooksEase.apply(recode_printedbooksEase)


# recode ebooksEase
def recode_printedbooksEase(printedbooksEase_value):
    if printedbooksEase_value == 'Very Easy':
        return 1
    if printedbooksEase_value == 'Easy':
        return 2
    if printedbooksEase_value == 'Neutral':
        return 3
    if printedbooksEase_value == 'Difficult':
        return 4
    if printedbooksEase_value == 'Very Difficult':
        return 5
    if printedbooksEase_value == 'My Library Doesn\'t Have This':
        return 6
    if printedbooksEase_value == 'Don\'t Know/Haven\'t Used':
        return 7
    else:
        return 999999

data['_printedbooksEase'] = data.printedbooksEase.apply(recode_printedbooksEase)


# recode internetwifiEase
def recode_internetwifiEase(internetwifiEase_value):
    if internetwifiEase_value == 'Very Easy':
        return 1
    if internetwifiEase_value == 'Easy':
        return 2
    if internetwifiEase_value == 'Neutral':
        return 3
    if internetwifiEase_value == 'Difficult':
        return 4
    if internetwifiEase_value == 'Very Difficult':
        return 5
    if internetwifiEase_value == 'My Library Doesn\'t Have This':
        return 6
    if internetwifiEase_value == 'Don\'t Know/Haven\'t Used':
        return 7
    else:
        return 999999

data['_internetwifiEase'] = data.internetwifiEase.apply(recode_internetwifiEase)


# recode musicEase
def recode_musicEase(musicEase_value):
    if musicEase_value == 'Very Easy':
        return 1
    if musicEase_value == 'Easy':
        return 2
    if musicEase_value == 'Neutral':
        return 3
    if musicEase_value == 'Difficult':
        return 4
    if musicEase_value == 'Very Difficult':
        return 5
    if musicEase_value == 'My Library Doesn\'t Have This':
        return 6
    if musicEase_value == 'Don\'t Know/Haven\'t Used':
        return 7
    else:
        return 999999

data['_musicEase'] = data.musicEase.apply(recode_musicEase)


# recode moviesEase
def recode_moviesEase(moviesEase_value):
    if moviesEase_value == 'Very Easy':
        return 1
    if moviesEase_value == 'Easy':
        return 2
    if moviesEase_value == 'Neutral':
        return 3
    if moviesEase_value == 'Difficult':
        return 4
    if moviesEase_value == 'Very Difficult':
        return 5
    if moviesEase_value == 'My Library Doesn\'t Have This':
        return 6
    if moviesEase_value == 'Don\'t Know/Haven\'t Used':
        return 7
    else:
        return 999999

data['_moviesEase'] = data.moviesEase.apply(recode_moviesEase)


# recode educationprogramsEase
def recode_educationprogramsEase(educationprogramsEase_value):
    if educationprogramsEase_value == 'Very Easy':
        return 1
    if educationprogramsEase_value == 'Easy':
        return 2
    if educationprogramsEase_value == 'Neutral':
        return 3
    if educationprogramsEase_value == 'Difficult':
        return 4
    if educationprogramsEase_value == 'Very Difficult':
        return 5
    if educationprogramsEase_value == 'My Library Doesn\'t Have This':
        return 6
    if educationprogramsEase_value == 'Don\'t Know/Haven\'t Used':
        return 7
    else:
        return 999999

data['_educationprogramsEase'] = data.educationprogramsEase.apply(recode_educationprogramsEase)


# recode childprogEase
def recode_childprogEase(childprogEase_value):
    if childprogEase_value == 'Very Easy':
        return 1
    if childprogEase_value == 'Easy':
        return 2
    if childprogEase_value == 'Neutral':
        return 3
    if childprogEase_value == 'Difficult':
        return 4
    if childprogEase_value == 'Very Difficult':
        return 5
    if childprogEase_value == 'My Library Doesn\'t Have This':
        return 6
    if childprogEase_value == 'Don\'t Know/Haven\'t Used':
        return 7
    else:
        return 999999

data['_childprogEase'] = data.childprogEase.apply(recode_childprogEase)



# recode meetingspaceEase
def recode_meetingspaceEase(meetingspaceEase_value):
    if meetingspaceEase_value == 'Very Easy':
        return 1
    if meetingspaceEase_value == 'Easy':
        return 2
    if meetingspaceEase_value == 'Neutral':
        return 3
    if meetingspaceEase_value == 'Difficult':
        return 4
    if meetingspaceEase_value == 'Very Difficult':
        return 5
    if meetingspaceEase_value == 'My Library Doesn\'t Have This':
        return 6
    if meetingspaceEase_value == 'Don\'t Know/Haven\'t Used':
        return 7
    else:
        return 999999

data['_meetingspaceEase'] = data.meetingspaceEase.apply(recode_meetingspaceEase)


# recode practiceroomsEase
def recode_practiceroomsEase(practiceroomsEase_value):
    if practiceroomsEase_value == 'Very Easy':
        return 1
    if practiceroomsEase_value == 'Easy':
        return 2
    if practiceroomsEase_value == 'Neutral':
        return 3
    if practiceroomsEase_value == 'Difficult':
        return 4
    if practiceroomsEase_value == 'Very Difficult':
        return 5
    if practiceroomsEase_value == 'My Library Doesn\'t Have This':
        return 6
    if practiceroomsEase_value == 'Don\'t Know/Haven\'t Used':
        return 7
    else:
        return 999999

data['_practiceroomsEase'] = data.practiceroomsEase.apply(recode_practiceroomsEase)


# recode jobsearchEase
def recode_jobsearchEase(jobsearchEase_value):
    if jobsearchEase_value == 'Very Easy':
        return 1
    if jobsearchEase_value == 'Easy':
        return 2
    if jobsearchEase_value == 'Neutral':
        return 3
    if jobsearchEase_value == 'Difficult':
        return 4
    if jobsearchEase_value == 'Very Difficult':
        return 5
    if jobsearchEase_value == 'My Library Doesn\'t Have This':
        return 6
    if jobsearchEase_value == 'Don\'t Know/Haven\'t Used':
        return 7
    else:
        return 999999

data['_jobsearchEase'] = data.jobsearchEase.apply(recode_jobsearchEase)


# recode librarianEase
def recode_librarianEase(librarianEase_value):
    if librarianEase_value == 'Very Easy':
        return 1
    if librarianEase_value == 'Easy':
        return 2
    if librarianEase_value == 'Neutral':
        return 3
    if librarianEase_value == 'Difficult':
        return 4
    if librarianEase_value == 'Very Difficult':
        return 5
    if librarianEase_value == 'My Library Doesn\'t Have This':
        return 6
    if librarianEase_value == 'Don\'t Know/Haven\'t Used':
        return 7
    else:
        return 999999

data['_librarianEase'] = data.librarianEase.apply(recode_librarianEase)


# recode bookclubsEase
def recode_bookclubsEase(bookclubsEase_value):
    if bookclubsEase_value == 'Very Easy':
        return 1
    if bookclubsEase_value == 'Easy':
        return 2
    if bookclubsEase_value == 'Neutral':
        return 3
    if bookclubsEase_value == 'Difficult':
        return 4
    if bookclubsEase_value == 'Very Difficult':
        return 5
    if bookclubsEase_value == 'My Library Doesn\'t Have This':
        return 6
    if bookclubsEase_value == 'Don\'t Know/Haven\'t Used':
        return 7
    else:
        return 999999

data['_bookclubsEase'] = data.bookclubsEase.apply(recode_bookclubsEase)


# recode renewalsEase
def recode_renewalsEase(renewalsEase_value):
    if renewalsEase_value == 'Very Easy':
        return 1
    if renewalsEase_value == 'Easy':
        return 2
    if renewalsEase_value == 'Neutral':
        return 3
    if renewalsEase_value == 'Difficult':
        return 4
    if renewalsEase_value == 'Very Difficult':
        return 5
    if renewalsEase_value == 'My Library Doesn\'t Have This':
        return 6
    if renewalsEase_value == 'Don\'t Know/Haven\'t Used':
        return 7
    else:
        return 999999

data['_renewalsEase'] = data.renewalsEase.apply(recode_renewalsEase)


# recode payfeesEase
def recode_payfeesEase(payfeesEase_value):
    if payfeesEase_value == 'Very Easy':
        return 1
    if payfeesEase_value == 'Easy':
        return 2
    if payfeesEase_value == 'Neutral':
        return 3
    if payfeesEase_value == 'Difficult':
        return 4
    if payfeesEase_value == 'Very Difficult':
        return 5
    if payfeesEase_value == 'My Library Doesn\'t Have This':
        return 6
    if payfeesEase_value == 'Don\'t Know/Haven\'t Used':
        return 7
    else:
        return 999999

data['_payfeesEase'] = data.payfeesEase.apply(recode_payfeesEase)



# recode localbookstore_freq
def recode_localbookstoreFreq(localbookstoreFreq_value):
    if localbookstoreFreq_value == 'Daily':
        return 1
    if localbookstoreFreq_value == 'Weekly':
        return 2
    if localbookstoreFreq_value == 'Monthly':
        return 3
    if localbookstoreFreq_value == 'A Few Months a Year':
        return 4
    if localbookstoreFreq_value == 'Yearly':
        return 5
    if localbookstoreFreq_value == 'Every Few Years':
        return 6
    if localbookstoreFreq_value == 'Never':
        return 7
    else:
        return 999999

data['_localbookstoreFreq'] = data.localbookstoreFreq.apply(recode_localbookstoreFreq)


# recode barnesnoble_freq
def recode_barnesnobleFreq(barnesnobleFreq_value):
    if barnesnobleFreq_value == 'Daily':
        return 1
    if barnesnobleFreq_value == 'Weekly':
        return 2
    if barnesnobleFreq_value == 'Monthly':
        return 3
    if barnesnobleFreq_value == 'A Few Months a Year':
        return 4
    if barnesnobleFreq_value == 'Yearly':
        return 5
    if barnesnobleFreq_value == 'Every Few Years':
        return 6
    if barnesnobleFreq_value == 'Never':
        return 7
    else:
        return 999999

data['_barnesnobleFreq'] = data.barnesnobleFreq.apply(recode_barnesnobleFreq)


# recode amazonFreq
def recode_amazonFreq(amazonFreq_value):
    if amazonFreq_value == 'Daily':
        return 1
    if amazonFreq_value == 'Weekly':
        return 2
    if amazonFreq_value == 'Monthly':
        return 3
    if amazonFreq_value == 'A Few Months a Year':
        return 4
    if amazonFreq_value == 'Yearly':
        return 5
    if amazonFreq_value == 'Every Few Years':
        return 6
    if amazonFreq_value == 'Never':
        return 7
    else:
        return 999999

data['_amazonFreq'] = data.amazonFreq.apply(recode_amazonFreq)


# recode onlinelearnFreq
def recode_onlinelearnFreq(onlinelearnFreq_value):
    if onlinelearnFreq_value == 'Daily':
        return 1
    if onlinelearnFreq_value == 'Weekly':
        return 2
    if onlinelearnFreq_value == 'Monthly':
        return 3
    if onlinelearnFreq_value == 'A Few Months a Year':
        return 4
    if onlinelearnFreq_value == 'Yearly':
        return 5
    if onlinelearnFreq_value == 'Every Few Years':
        return 6
    if onlinelearnFreq_value == 'Never':
        return 7
    else:
        return 999999

data['_onlinelearnFreq'] = data.onlinelearnFreq.apply(recode_onlinelearnFreq)


# recode coffeeshopFreq
def recode_coffeeshopFreq(coffeeshopFreq_value):
    if coffeeshopFreq_value == 'Daily':
        return 1
    if coffeeshopFreq_value == 'Weekly':
        return 2
    if coffeeshopFreq_value == 'Monthly':
        return 3
    if coffeeshopFreq_value == 'A Few Months a Year':
        return 4
    if coffeeshopFreq_value == 'Yearly':
        return 5
    if coffeeshopFreq_value == 'Every Few Years':
        return 6
    if coffeeshopFreq_value == 'Never':
        return 7
    else:
        return 999999

data['_coffeeshopFreq'] = data.coffeeshopFreq.apply(recode_coffeeshopFreq)


# recode locallibFreq
def recode_locallibFreq(locallibFreq_value):
    if locallibFreq_value == 'Daily':
        return 1
    if locallibFreq_value == 'Weekly':
        return 2
    if locallibFreq_value == 'Monthly':
        return 3
    if locallibFreq_value == 'A Few Months a Year':
        return 4
    if locallibFreq_value == 'Yearly':
        return 5
    if locallibFreq_value == 'Every Few Years':
        return 6
    if locallibFreq_value == 'Never':
        return 7
    else:
        return 999999

data['_locallibFreq'] = data.locallibFreq.apply(recode_locallibFreq)


#export
data.to_csv('LibrarySurveyClean.csv', sep=',')


    


