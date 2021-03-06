This project ties together the Textblob sentiment analysis tool, and Botometer Pro API. The purpose of this repository is to
facilitate tiwtter user sentiment analysis and to be able to see if the user is a bot, all in one easy to use place. 

This easy to use web-app can be applied to the current state of politial discourse, news, and world events to check the credibility of your 
information sources, as well as gauge a sense of the overall tone and demeanor of the user. 

Using the Code:

1. Fork, clone, or download the repository
2. Make sure that you have FLASK installed. 
3. In terminal:
  4. type "set FLASK_APP=app.py"
  5. type "flask run" 
6. The website should now be hosted on your computer.
7. Copy the the url. 
8. Paste url and use tool!


Some things to note when using this tool:

1. Enter in the "@" symbol for best performance.
2. Keep queries under a few hundred tweets per the API's requirements. 
3. It might take a few seconds to load given the functionality of the web-based API's that it uses. 
4. The sentiment analysis library Textblob, is optimized for social media texts such as twitter, however, it is not perfect.  The    
   sentiment analysis function will provide you with data that should inform and complement your analysis/review of a twitter user. 
5. The Botometer API returns a composite "universal" bot score. This score ranges from "0-1". A score of  "0" means that the user has no 
   bot like attributes. Generally, a score under "0.10" means that you can be confident that the user is not a bot. A score over this   
   indicates that you  should be cautious when analyzing/reading tweets from this account. The score will not return 1 even if the user 
   is a known bot. This is becasue not all of its attibutes will be botlike. It will, however, return a high composite score like  
   "0.40". These score are a good tool to add context to the discourse on twitter and identifying bots. 

Future goals:

1. Implement data visulizations. 
2. Implement keyword sentiment anlaysis searches, filtering out only a bot's tweets. 
3. Make the website more user friendly, UI & UX more appealing. 
4. Further parse & filter tweets for more accurate findings. 
5. Display the tweets with the highest sentiment and botometer scores. 


