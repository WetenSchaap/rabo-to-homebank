#!/usr/bin/env python3
"""
RaboToHomebank.py: Convert Rabobank's .CSV file format into Homebank .csv format
Originally created on Sat Apr 28 18:47:44 2018

Usage:
From the terminal, run:
$ Python3 RaboToHomebank.py filename1 filename2 filename3
This will convert your .csv Rabobank files to the proper homebank .csv files, and put them in the same folder as this script is in.

Requirements:
- pandas
"""

__author__ = "Piet Swinkels"
__version__ = "0.2"
__status__ = "prototype"

import os
import csv
import time
import pandas as pd
import datetime
import copy
import sys

#%%variables
current_date = time.strftime("%Y%m%d")
todo = sys.argv[1:]

# The bank uses two letter codes to identify type of payments, we translate that to homebank types.
codedict = {'ac' : '4',
            'ba' : '6',
            'bc' : '6',
            'bg' : '4',
            'bv' : '4',
            'cb' : '4',
            'db' : '10',
            'eb' : '11',
            'ei' : '11',
            'ga' : '9',
            'gb' : '9',
            'id' : '4',
            'kh' : '4',
            'sb' : '7',
            'sp' : '4',
            'st' : '11',
            'tb' : '4',
            'te' : '4',
            'wb' : '4',
            'cc' : '1',
            }

for fn in todo:
    #load data
    rabo = pd.read_csv( os.path.join(os.getcwd(),fn) ,
                       encoding='ISO-8859-1',) #delimiter=",", decimal=",") # cause the number format at in/output is the same anyway, conversion just makes stuff harder.
    accountlist = pd.unique(rabo['IBAN/BBAN'])
    for account in accountlist:
        arabo = rabo[rabo['IBAN/BBAN'] == account]
        HBoutput = pd.DataFrame()
        HBoutput['fulldate'] = arabo['Datum']
        HBoutput['paymode'] = arabo['Code'].map(codedict)
        HBoutput['info'] = ''
        HBoutput['payee'] = arabo['Naam tegenpartij']
        HBoutput["memo"] = arabo["Omschrijving-1"]
        HBoutput["signedamount"] = arabo["Bedrag"]
        HBoutput["Category"] = ''
        HBoutput["label"] = "import" + current_date
        HBoutput.to_csv("{0}.csv".format(account + "_" + current_date),
                        sep = ';', index=False,header=False,
                        )
    print("Conversion of {0} complete, .csv saved in {1}." % (fn, os.cwd()) )
        
#%%Info
    
# ROW NAMES IN IMPORT FILE
#Row1 = IBAN/BBAN
#Row2 = Munt
#Row3 = BIC
#Row4 = Volgnr
#Row5 = Datum
#Row6 = Rentedatum
#Row7 = Bedrag
#Row8 = Saldo na trn
#Row9 = Tegenrekening IBAN/BBAN
#Row10 = Naam tegenpartij
#Row11 = Naam uiteindelijke partij
#Row12 = Naam initiërende partij
#Row13 = BIC tegenpartij	
#Row14 = Code 
#Row15 = Batch ID
#Row16 = Transactiereferentie
#Row17 = Machtigingskenmerk
#Row18 = Incassant ID
#Row19 = Betalingskenmerk
#Row20 = Omschrijving-1
#Row21 = Omschrijving-2
#Row22 = Omschrijving-3
#Row23 = Reden retour
#Row24 = Oorspr bedrag
#Row25 = Oorspr munt
#Row26 = Koers

# HOMEBANK PAYEMENT MODES
#0 = None
#1 = Credit Card
#2 = Cheque
#3 = Cash
#4 = Transfer
#5 = Internal transfer (NOT ALLOWED IN IMPORT)
#6 = Debit Card
#7 = Returning Transfer
#8 = Electronic Payment
#9 = Deposit
#10 = Bank Costs
#11 = Automatic Incasso 

#required order of data in HomeBank CSV: 
#fulldate, paymode, info (empty), payee, memo, signedamount, category(empty), labels
