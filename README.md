
ـ بِسْمِ ٱللهِ ٱلرَّحْمٰنِ الرَّحِيْم ـ
تهدف هذه المدونه إلى خدمة الباحثين في علوم السنّة النبويّة الشريفة 

# LK-Hadith-Corpus
Leeds University and King Saud University (LK) Hadith Corpus

- Bilingual parallel corpus of English-Arabic Islamic Hadith
- Extracted from the six canonical Hadith books
- The corpus contains 39,038 annotated Hadiths that comprises more than 10 million tokens
- Each component of the Hadith is extracted and allocated to a specific column:
  1. Chapter_Number
  1. Chapter_English
  1. Chapter_Arabic
  1. Section_Number	
  1. Section_English
  1. Section_Arabic
  1. Hadith_number
  1. English_Hadith
  1. English_Isnad
  1. English_Matn
  1. Arabic_Hadith
  1. Arabic_Isnad
  1. Arabic_Matn
  1. Arabic_Comment
  1. English_Grade
  1. Arabic_Grade


### How to use it:
To open and view the csv files, DO NOT use 'Excel' because it will not show the correct structure. We have tried the 'Numbers' app on Mac and 'Google sheets' on windows and they work properly. 

To extract information (columns) from the LK Hadith corpus, use the starter code provided in {starter.py}.

### If you use this Hadith corpus, kindly site the paper: 

Altammami, S , Atwell, E and Alsalka. 'The Arabic–English Parallel Corpus of Authentic Hadith'. In: International Journal on Islamic Applications in Computer Science And Technology - IJASAT. International Conference on Islamic Applications in Computer Science and Technologies - IMAN 2019, 27-28 Dec 2019. 

[link to paper](http://www.sign-ific-ance.co.uk/index.php/IJASAT/article/view/2199/1908)

------------------------------------------------------------------------------------------

### Important Note: 
Bukhari folder was manually checked and is considered the gold standard of this corpus, while the other books(folders) were annotated automatically using a Hadith segmentation tool that segments the Isnad from the Matn with 92% accuracy. 

For further information about the automatic annotation refer to the paper: 

Altammami, S., Atwell, E., & Alsalka, A.(2020) 'Constructing a Bilingual Hadith Corpus Using a Segmentation Tool'. Proceedings of the 12th Conference on Language Resources and Evaluation (LREC 2020). Marseille, 11–16 May 2020. pages 3383–3391

[link to paper](https://www.aclweb.org/anthology/2020.lrec-1.415/)


------------------------------------------------------------------------------------------

If you would like to submit corrections or comments about the corpus please send an email to shatha.tammami@gmail.com
