#!/usr/bin/python3
# 1cintron
# Send Message to Slack channel as user. Requires a Slack application with the following
# user token scopes: chat:write, im:write

from urllib import request, parse
import json
from os import path
import sys
import getopt


def parseArguments(argv):
   message = ''
   channel = ''
   token = ''
   configFile = ''
   try:
       opts, args = getopt.getopt(argv, "hm:f:c:t:", ["file=", "message=", "channel=", "token="])
   except getopt.GetoptError:
       printHelp()
       sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         printHelp()
         sys.exit()
      elif opt in ("-f", "--file"):
          configFile = arg
      elif opt in ("-m", "--message"):
          message = arg
      elif opt in ("-c", "--channel"):
          channel = arg
      elif opt in ("-t", "--token"):
          token = arg

   return channel, configFile, message, token


def extractMessageParamsFromJson(jsonElement):
   message = jsonElement['message']
   channel = jsonElement['channel']
   token = jsonElement['token']
   return channel, message, token


def sendMessage(channel, message, token):
    try:
        url = "https://slack.com/api/chat.postMessage"

        data = {
            "channel": channel,
            "text": message,
            "as_user": True
        }

        jsonData = json.dumps(data)
        jsonDataAsBytes = jsonData.encode('utf-8')
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer ' + token,
                'Content-Length': len(jsonDataAsBytes)}
        messageRequest = request.Request(url, headers=headers, data=jsonDataAsBytes)
        response = request.urlopen(messageRequest)
        responseData = response.read()
        jsonResponse = json.loads(responseData.decode('utf-8'))
        return jsonResponse
    except:
        e = sys.exc_info()[0]
        print("Error sending message: "+e)
        return ''


def printHelp():
    print('Arguments:')
    print('\t -h\t\tHelp')
    print('\t -m, --message\tMessage to send (required if no file)')
    print('\t -c, --channel\tRecipient Channel ID or User ID (required if no file)')
    print('\t -f, --file\tConfiguration File (required if no file)')
    print('\t -t, --token\tSlack App Authentication Token (optional, other arguments ignored when set)')


def main(argv):
   channel, configFile,message,token = parseArguments(argv)

   if len(configFile) >2 and path.isfile(configFile):

        with open(configFile) as jsonFile:
            jsonData = None
            try:
                jsonData = json.load(jsonFile)
                for messageInfo in jsonData:
                    message, channel, token = extractMessageParamsFromJson(messageInfo)
                    response = sendMessage(message, channel, token)
                    print(json.dumps(response))
            except:
                print('Unable to read/parse file: ' + configFile)



   elif len(message) >1 and len(channel)>1 and len(token)>10:
       response = sendMessage(channel, message, token)
       print(json.dumps(response))


if __name__ == "__main__":
   main(sys.argv[1:])