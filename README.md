# earnings-calls
Earnings calls of all S&amp;P500 companies from 1995 to 2015 

Dropbox link: [be sure to verify link location's full url](https://www.dropbox.com/sh/udpi0spsdfeq4dj/AAAeDrSNFsQghqgSguHc9tpra?dl=0)

The dropbox folder contains:
 - call-txt.tar.gz
 
     5+ GB of .txt files in zipped format. 
     
     Each file is a transcript of a conference call and usually an earnings call report.
     
 - cfo-qa_section-each_call.tar.gz
 
     2+ GB of .txt files in zipped format. 
     
     Each file has the answers by a CFO during Q&A section extracted from the call.
     
 - lightning-chaser.txt
 
## Parse the text files
Use the sloppy example codes along with CEO or CFO aliases to extract different types of data.

- Particularly look for the keyword "fall" or "falling" or "failed" in the texts 

    Using machine learning techniques, analyze the speech of analysts and chief officers before, during and after recession periods. Just before and during recessions or market upsets, the chief officers tend to speak about the fall in profits or falling outputs, or failed projects or failing investments, etc. etc. 
    
 - Analyst names and titles (employer details) can be graphed from this dataset. The ones from Merrill Lynch and banks tend to downgrade the stock market price of certain companies right after a call even if the call was extrememly positive and the company was doing better than expected. The bosses and analysts from Goldman Sachs are even worse, they short highly positive and effective companies associated with US and UK public sectors expecially vendors to civil services. All these people with their golden parachutes, seem to be way too enthusiastic to "slash and burn" as much of the galaxy as possible!
 
 - Unscrupulous CEOs and CFOs who tanked their company by misdirecting public investments and pension funds or by shifting to a competitor company with trade secrets can be found in this dataset. They tend to speak about key technology projects having unique project names during the conference calls of companies they were preveiously and later a part of. 
 
 - The good guys simply follow through with their feduciary duties and that is evident from their speech that doesn't use unnecessary idoms. They don't put a positive spin on bad news. They answer questions without evasion. Good analysts, some even from the gangrenous banks like CitiGroup and Bank Of America, ask a question repeatedly to get a sensible answer if the reporting chiefs try to be evasive. First step in the NLP technique for identifying this type of dodgy behavior from company managers in Q&A section merely requires identifying a sequence where an analyst's subsequent text has more than 66% similarity in semantic content as identifiable by an algorithm like GloVe. Try:
   - https://github.com/guillaumegenthial/sequence_tagging
   - https://github.com/plasticityai/magnitude
   - https://github.com/google-research/google-research/tree/master/model_pruning
