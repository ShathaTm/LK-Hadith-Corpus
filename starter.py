# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 12:06:08 2019
This is a starter code to facilitate reading information from the Leeds and King Saud University Hadith Corpus 
@author: Shatha Altammami
"""

import pandas
import glob

colnames=['Chapter_Number',	'Chapter_English',	'Chapter_Arabic',	'Section_Number',	'Section_English',	'Section_Arabic',	'Hadith_number','English_Hadith',	'English_Isnad',	'English_Matn',	'Arabic_Hadith'	,'Arabic_Isnad',	'Arabic_Matn',	'Arabic_Comment',	'English_Grade',	'Arabic_Grade']


#if you want to read all corpus files 
path ="C://Desktop//LKHC" # Path of the corpus file
book_filenames = sorted(glob.glob(path +'//**//*.csv', recursive=True)) # read all csv files in all books 

#If you want to read all files in the corpus. 
for book_filename in book_filenames:
    print("Reading '{0}'...".format(book_filename))
    data=pandas.read_csv(book_filename, names= colnames, skiprows=1)
     
    
#--------------------------------------------------------
#Else if only one book is requried, use the following code to read its files
# for example, to read Albukhari book 

for x in range(1,98): # this will loop 97 times since Albukhari contain 97 chapters = csv files. 
    data=pandas.read_csv('Bukhari//Chapter{}.csv'.format(x))    
   


#Then save every column you will use in a dedicated list. 
    Chapter_Num =data.Chapter_Number.tolist()
    Chapter_Title_E =data.Chapter_English.tolist()
    Chapter_Title_Ar =data.Chapter_Arabic.tolist()
    
    Section_Num =data.Section_Number.tolist()
    Section_En =data.Section_English.tolist()
    Section_Ar =data.Section_Arabic.tolist()
    
    Hadith_num =data.Hadith_number.tolist()
    
    En_hadith=data.English_Hadith.tolist()
    En_Isnad =data.English_Isnad.tolist()
    En_Matn =data.English_Matn.tolist()
    
    Ar_Hadith =data.Arabic_Hadith.tolist()
    Ar_Isnad =data.Arabic_Isnad.tolist()
    Ar_Matn =data.Arabic_Matn.tolist()
    
    Ar_Comment =data.Arabic_Comment.tolist()
    En_Grade =data.English_Grade.tolist()
    Ar_Grade= data.Arabic_Grade.tolist() 
    

#Do the requried processing.. a simple example: print 
    for Hadith in Ar_Hadith: 
        print(Hadith)
    print('finished reading chapter:', x)