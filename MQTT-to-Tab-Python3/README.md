# Starter for a MQTT integration using Python3
## TheThingsStack-Integration-Starters

This requires a computer with access to the internet with Python 3 installed.

This script is best suited for running locally on a machine for debugging. If you need it to run 24 / 7 you will need a machine that is on 24 / 7. If the machine is likely to be restarted, then you will benefit from creating a startup script to run this when the machine is started. You will not receive data whilst the machine is off or not connected to the internet.


For debugging purposes you can choose to save the incoming JSON from TTS as an individual file in a debug (or any other directory you'd like). Be sure to turn this off because it is very easy to find you have tens of thousands of files to delete.


The code will create a tab delimited file per day, formatted YYMMDD.txt plus one per device formatted APP-ID__DEVICE-ID.txt

If you have used a payload formatter, this code does not read the decoded fields and put them in to the tab file, but you can add that functionality yourself ;-) Or you could put the data in to a database.


If you need to reliably run something all of the time, then you should look at the WebHook_PHP_Tab script that will run just fine on low cost or free web hosting.

Please use the TTN forum for community support.
