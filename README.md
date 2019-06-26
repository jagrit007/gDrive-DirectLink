# Google Drive Permanent Direct Link Generator
### Requirements:
1. Python3
2. Google Account

### HOW-TO: 
1. Getting API Key:

   * Visit the [Google Cloud Console](https://console.developers.google.com/apis/credentials)
   * Go to the OAuth Consent tab, fill it, and save.
   * Go to the Credentials tab and click Create Credentials -> API KEY
   * Choose Other and Create.
   * Copy your API KEY
   * In terminal, `nano main.py`
   * Replace `PasteHere` with the api you got.
     ```api = "PasteHere"```

2. Enable the Drive API:

   * Visit the [Google API Library](https://console.developers.google.com/apis/library) page.
   * Search for Drive.
   * Make sure that it's enabled. Enable it if not.

3. CD into the cloned for and open up and terminal and type > 
      ```python3 main.py```
	*Paste as many links as your wish to and enter ```q``` to exit and get direct links.*
