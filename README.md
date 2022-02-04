#Reads bitcoin ticker from Bitstamp.net Websocket API

This program uses the API provided by bitstamp.net, to retrive bitcoin ticker  
Based on project 05 - SOLYD Python training 


-It could be done using requests using the following sample parameters
-API URL sample: "https://www.bitstamp.net/api/ticker" returns JSON

-JSON return sample "{"volume": "1758.50382905", "last": "36653.77", "timestamp": "1643896835", "bid": "36631.32", "vwap": "37150.89", "high": "38451.62", "low": "36264.55", "ask": "36654.30", "open": 36924.5}"

However, it was decided to implementing the Websocket API provided by bitstamp
Bitstam Websocket docs: https://www.bitstamp.net/websocket/v2/

#In order to instal the lybraries Please run 
pip install -r .\requirements.txt  
- python 3.9.7  
- Websocket library:  "https://pypi.org/project/websocket-client/"  
pip install BitstampClient
- https://github.com/kmadac/bitstamp-python-client