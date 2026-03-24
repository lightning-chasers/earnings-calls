# earnings-calls

Earnings calls of all S&amp;P500 companies from 1995 to 2015. 

Dropbox link to: [conf-calls](https://www.dropbox.com/scl/fo/sbd6e8cl0pvhkx55r2izf/AABVAAiciqq4W-kD4FNAlS8?rlkey=r88511tr99suox3fx0zauz9y6&st=brpcz5jq&dl=0) (be sure to verify this link's full URL)

The given Dropbox folder contains:

 - call-txt.tar.gz (1.3 GB)
 
     5+ GB of .txt files in zipped format. 
     
     Each file is a transcript of a conference call and usually an earnings call report.
     
 - cfo-qa_section-each_call.tar.gz (113.6 MB)
 
     2+ GB of .txt files in zipped format. 
     
     Each file has the answers by a CFO during Q&A section extracted from the call.
     
 - lightning-chaser.md (3.5 KB) 
 
	A story about those who wish to get close to lightning, close enough to catch it. LOLs.
 
## Parse the text files

Use the sloppy py codes (e.g. `parse-txt-ceo-qa.py`) along with CEO or CFO aliases, to extract different types of data. (Those were the grueling, yet good old days in Machine Learning, in the year of Jan-2016 to Dec-2019.)

Better yet, now in the year of 2026 with the advent of General Artificial Intelligence (GAI), feed the downloadable dataset to any AI-platform of your choice (Qwen, Hermes, OpenClaw, Claude, NotebookLM, etc.) and run queries on it. 

### For example

- Particularly look for the keyword "fall" or "falling" or "failed" in the texts: 

    Using machine learning (or AI prompt engineering) techniques. Analyze the speech of analysts and chief officers before, during, and after recession periods. Just before and during recessions or market upsets, the chief officers tend to speak about the fall in profits or falling outputs, or failed projects or failing investments, etc. 
    
- Analyst names and titles (employer details) can be graphed from this dataset. You may find that the ones from Merrill Lynch and various banks  had downgraded the stock market price of certain companies, right after an earnings call with that company, even if the call was extremely positive and the company was doing better than expected. The bosses and analysts from Goldman Sachs are even worse, they shorted highly positive and effective companies associated with US and UK public sectors, especially vendors to civil services. All those people with their golden parachutes,were way too enthusiastic to "slash and burn" as much of the galaxy as possible! 
 
- Unscrupulous CEOs and CFOs who tanked their company by misdirecting public investments and pension funds, or by shifting to a competitor company with trade secrets can be found in this dataset. They tend to speak about key technology projects having unique project names during the conference calls of companies that they were previously and later associated with. 
 
- The good guys simply follow through with their fiduciary duties and that is evident from their speech which, doesn't have unnecessary idioms. They don't put a positive spin on bad news. They answer questions without evasion. Good analysts, some even from the gangrenous banks like CitiGroup and Bank Of America, ask a question repeatedly to get a sensible answer if the reporting chiefs try to be evasive. 

	First step in the NLP technique for identifying this type of dodgy behavior from company managers in Q&A section merely requires identifying a sequence where an analyst's subsequent text has more than 66% similarity in semantic content, as identifiable by an algorithm like GloVe. 
 
Try:
- 2019:
	- https://github.com/guillaumegenthial/sequence_tagging
	- https://github.com/plasticityai/magnitude
	- https://github.com/google-research/google-research/tree/master/model_pruning
	
- 2026: https://github.com/microsoft/agent-lightning/tree/main/examples/chartqa

## Note from March-2026:
	
Most probably the above types of links for sequence tagging or "semantic content" analysis, can be achieved in better ways, using agentic tasks. 

So, cheers! Have fun! :v: :smiley: