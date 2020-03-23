![PyInstaller](https://github.com/lcintron/SlackSendMessage/workflows/PyInstaller/badge.svg)
# SlackSendMessage
Send message on behalf of you. Great for automating or schedule messages.
## Arguments
```Arguments:
         -h             Help
         -m, --message  Message to send (required if no file)
         -c, --channel  Recipient Channel ID or User ID (required if no file)
         -f, --file     Configuration File (required if no file)
         -t, --token    Slack App Authentication Token (optional, other arguments ignored when set)
```         
## How to use?
  Pass needed values as command-line arguments:
  
  ```python3 app.py -c <channel/user Id> -m "message to send" -t <Slack API token>```
  
  -or-
  
  Include them in a file (e.g., config.json in repository) where the JSON file has all the argumets needed as JSON objects:
  
  ```python3 app.py -f config.json```
  

## Getting a Slack API Token:
<Instructions in Progress>
  
## Dependencies
  - Python3
