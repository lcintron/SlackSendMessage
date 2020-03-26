![PyInstaller](https://github.com/lcintron/SlackSendMessage/workflows/PyInstaller/badge.svg)
# SlackSendMessage
Send Slack messages on behalf of you. Great for automating or scheduling messages on your Slack workspace.

## Arguments
```Arguments:
         -h             Help
         -m, --message  Message to send (required if no file)
         -c, --channel  Recipient Channel ID or User ID (required if no file)
         -t, --token    Slack App Authentication Token (required if no file)
         -f, --file     Path to configuration file (fetches message from json file)
```         
## How to use?
  Pass needed values as command-line arguments:
  
  ```python3 app.py -c <channel/user Id> -m "message to send" -t <Slack API token>```
  
  -or-
  
  Include them in a file (e.g., config.json in repository) where the JSON file has all the argumets needed as JSON objects:
  
  ```python3 app.py -f config.json```
  

## Getting a Slack API Token:
- You will need to create a Slack application in the respective workspace with chat:write and im:write permissions. Once created, you will be given the token you will utilize with this tool.
- [To be deprecated in May 2020] Request a legacy token at the following page: https://api.slack.com/legacy/custom-integrations/legacy-tokens
  
## Dependencies
  - Python3
