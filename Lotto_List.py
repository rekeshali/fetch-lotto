import validators
import numpy as np
import pandas as pd
#COSC-505 Twall4 (Tristan Wall)
#Project B: Lotto data collection function
#This function checks validity of a user specified URL and parses the winning lotto and Mega-Ball numbers in lists for later use
def Lotto_List():
    #Reads in data from URL
    URL = input('Enter desire URL with Lotto data: ')
    valid = validators.url(URL)

    #Checks to see if the user URL is valid or not
    if valid == True:
        lotto_data_frame = pd.read_csv(URL)
        
        #Coverts the Mega-Ball numbers from an Array to a List
        #It is noteworthy that the entries are still .int64 datatype
        mega = np.array(lotto_data_frame['Mega Ball'])
        mega = list(mega)
        
        #Converts winning lotto numbers to a list of integers
        winn = np.array(lotto_data_frame['Winning Numbers'])
        for i in range(len(winn)):
            winn[i] = int(winn[i].replace(' ',''))
            winn = list(winn)
    
    else:
        print('Invalid URL, please check spelling or validity of URL')
    
    return winn , mega 


Lotto_List()
 
