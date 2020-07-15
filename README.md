# LK-Hadith-Corpus
Leeds University and King Saud University (LK) Hadith Corpus


It is bilingual parallel corpus of Islamic Hadith, which is the set of narratives reporting different aspects of the prophet Muhammad's life. The Hadith collection is extracted from the six canonical Hadith books which possess unique linguistic features and patterns that are automatically extracted and annotated using a domain-specific tool for Hadith segmentation to seperate the two main components of Hadith, Isnad (narrators names) and Matn (actual teachings). The corpus contains 39,038 annotated Hadiths that comprises more than 10 million tokens. 


### How to use it:
To open and view the csv files, DO NOT use 'Excel' because it will not show the correct structure. We have tried the 'Numbers' app on Mac and 'Google sheets' on windows and they work properly. 

To extract information (columns) from the LK Hadith corpus, use the starter code provided in {starter.py}.

### If you use this Hadith corpus, kindly site the paper: 

Altammami, S , Atwell, E and Alsalka. 'The Arabic–English Parallel Corpus of Authentic Hadith'. In: International Journal on Islamic Applications in Computer Science And Technology - IJASAT. International Conference on Islamic Applications in Computer Science and Technologies - IMAN 2019, 27-28 Dec 2019.


------------------------------------------------------------------------------------------

### Important Note: 
Bukhari folder was manually checked and is considered the gold standard of this corpus, while the other books(folders) were annotated automatically using a Hadith segmentation tool that segments the Isnad from the Matn with 92% accuracy. 

For further information about the automatic annotation refer to the paper: 

Altammami, S., Atwell, E., & Alsalka, A.(2020) 'Constructing a Bilingual Hadith Corpus Using a Segmentation Tool'. Proceedings of the 12th Conference on Language Resources and Evaluation (LREC 2020). Marseille, 11–16 May 2020. pages 3383–3391

------------------------------------------------------------------------------------------

If you would like to submit corrections or comments about the corpus please send an email to shatha.tammami@gmail.com
