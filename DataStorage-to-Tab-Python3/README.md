# Starter for downloading from Data Storage using Python3
## TheThingsStack-Integration-Starters

This requires a computer with access to the internet with Python 3 installed.

This script is designed for you to retrieve uplinks from Data Storage in bulk for further processing. As DS does not store any meta data such as gateways or signal strength, it's primary use is as a backup if your MQTT or WebHook integration goes offline and you need to fill in some of the data.


For debugging purposes you can choose to save the incoming JSON from TTS as an individual file in a debug (or any other directory you'd like). The files can be quite large.


The code will create a tab delimited file per day, formatted YYMMDD.txt plus one per device formatted APP-ID__DEVICE-ID.txt

If you have used a payload formatter, this code does not read the decoded fields and put them in to the tab file, but you can add that functionality yourself ;-) Or you could put the data in to a database.


Please use the TTN forum for community support.
