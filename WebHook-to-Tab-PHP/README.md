# WebHook integration using PHP
## TheThingsStack-Integration-Starters

This requires a web host on the internet that supports PHP.

The huge benefit of this integration is that web servers have been around for a very long time so the technology is proven, it does not need any startup script or configuration, just upload to your web hosting and set the web address of the PHP file in to a new custom WebHook entry.

The code will create a tab delimited file per day, formatted `YYMMDD.txt` plus one per device formatted `APP-ID__DEVICE-ID.txt`

If you have used a payload formatter, this code does not read the decoded fields  and put them in to the tab file, but you can add that functionality yourself ;-) Or you could put the data in to a database.

For debugging purposes you can choose to save the incoming JSON from TTS as an individual file in a debug (or any other directory you'd like). Be sure to turn this off when you have finished because it is very easy to find you have tens of thousands of files to delete via your file transfer client.

This script will not work on a home (internal) network unless you configure your router to allow that to happen. Please don't ask how to do that, Google is your friend. If you need to run something inside your network, the MQTT\_Python3\_Tab script is what you need.

Please use the TTN forum for community support.
