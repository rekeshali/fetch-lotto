import numpy as np
import pandas as pd
#COSC-505 Twall4 (Tristan Wall)
#Project B: Lotto data collection function
#This function checks validity of a user specified URL and parses the winning lotto and Mega-Ball numbers in lists for later use

#Reads in data from URL
def Lotto_List():
    URL = input('Enter desire URL with Lotto data: ')
    checker = 0
    #tries to use the URL, if the URL is Invalid checker is set to one
    try:
        lotto_data_frame = pd.read_csv(URL)
    except:
        checker = 1
                        
    if checker == 0:
        #Coverts the Mega-Ball numbers from an Array to a List
        #It is noteworthy that the entries are still .int64  datatype
        mega = np.array(lotto_data_frame['Mega Ball'])
        mega = list(mega)
        #Converts winning lotto numbers to a list of integers
        winn = np.array(lotto_data_frame['Winning Numbers'])
        for i in range(len(winn)):
            winn[i] = int(winn[i].replace(' ',''))
            winn = list(winn)
        return winn , mega
    else:
        print(' ERROR: The provided URL contains an error, please recheck spelling and/or validity of the URL')
        return

winn , mega = Lotto_List()
