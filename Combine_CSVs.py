# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 06:56:16 2019

@author: Chris
"""
#https://stackoverflow.com/questions/9234560/find-all-csv-files-in-a-directory-using-python/12280052
import glob

#import os
#os.chdir("/mydir")

#find all csv files in the folder
#use glob pattern matching -> extension = 'csv'
#save result in list -> all_filenames

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
print(all_filenames)

#combine all files in the list
import pandas as pd
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])