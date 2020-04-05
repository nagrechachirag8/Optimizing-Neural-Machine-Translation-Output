# Optimizing-Neural-Machine-Translation-Output
The purpose is to implement NMT on a system which currently works on rule based SMT translation system. Anusaaraka is intended to allow users to access text in any Indian language after translation from the source language (i.e. English or any other regional Indian language).

We have integrated NMT models Docker Sriram, nmt 550, nmt 300, and nmt 500 along with language model (SRILM). Each model has its own way of translating the English sentence into Hindi Sentence with their respective directories.With the help of an example it is better to understand. This english sentence is given as input to all 4 NMT Models.

Protesters in southern Iraq have blockaded the border with Kuwait and have also occupied several oilfields.

Then , their correspoinding outputs are-

दक्षिणी इराक के प्रोटेस्टर्स ने कुवैत के साथ सीमा पर रोक लगा दी है और कई तेल क्षेत्रों पर भी कब्जा कर लिया है .

दक्षिणी इराक के प्रोटेस्टरों ने कुवैत के साथ सीमा को अवरुद्ध कर दिया है और कई तेल क्षेत्रों पर कब्जा कर लिया है .

दक्षिणी इराक में प्रोटेस्टरों ने कुवैत से सीमा पर अवरोध कर दिया है और कई तेल क्षेत्रों पर भी कब्जा कर लिया है .

दक्षिणी इराक में प्रोटिस्टों ने कुवैत के साथ सीमा पर अवरोध कर दिया है और कई तेल क्षेत्रों पर कब्जा कर लिया है .

Now we have to generate a single sentence from the four outputs, which will be done with the help of indexing. The single sentence must contain all the words present in all the 4 sentences.


दक्षिणी इराक के में/0 प्रोटिस्टों/प्रोटेस्टरों/प्रोटेस्टर्स ने कुवैत से/0 साथ सीमा पर को/0 रोक/अवरोध अवरुद्ध/0 लगा दिया/0 दी है और कई तेल क्षेत्रों भी कब्जा कर लिया .

But it would be better if we place synonyms at a single index.This can be done with the help of indexing.Each word in a sentence is assigned with an index. So we have taken all the characters which are present in the same index. If all the words in a particular index are same then it will be printed as it is and if not then it will check that the words are synonyms with the help of dictionary and will be printed as:

word1/word2/word3/word4.

If the words are not synonym then they will be printed as each separate word. 

दक्षिणी इराक के में/० प्रोटिस्टों/प्रोटेस्टरों/प्रोटेस्टर्स ने कुवैत से/० साथ सीमा पर को/० रोक/अवरोध अवरुद्ध/० लगा दिया/० दी है और कई तेल क्षेत्रों भी कब्जा कर लिया ।

This is the optimized output, which we have made with the help of indexing and dictionaries. 
We have optimized around 1000 sentences , by taking 4000 outputs of the NMT Models.










  

