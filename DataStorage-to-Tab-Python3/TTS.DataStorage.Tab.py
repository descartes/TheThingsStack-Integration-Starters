#!/usr/bin/python3

theApplication = "YOUR-APPLICATION-ID"
theAPIKey = "NNSXS.T0P.53CR3T.AP1.K3Y"
theRegion = "EU1"		# The region you are using

# How many records you want, set to 0 if you want everything available
theNumberOfRecords = 0

# From which date you want the records returned. Note, DS only holds 7 days of data
theSinceDateTime = "2021-05-16T19:00:00Z" # Format is 2020-10-01T12:13:14Z



VER  = "2021-04-27 v1.1"
import os, sys, logging, time
print(os.path.basename(__file__) + " " + VER)

print("Imports:")
import requests
import json
import csv
from datetime import datetime


theURL  = "https://" + theRegion.lower() + ".cloud.thethings.network/api/v3/as/applications/"
theURL += theApplication + "/packages/storage/uplink_message?order=received_at&type=uplink_message"

if theNumberOfRecords:
	theURL += "&limit=" + str(theNumberOfRecords)

if theSinceDateTime:
	theURL += "&after=" + theSinceDateTime

# These are the headers required in the documentation.
theHeaders = { 'Accept': 'text/event-stream', 'Authorization': 'Bearer ' + theAPIKey }

print("\n\nFetching from data storage  ...\n")

r = requests.get(theURL, headers=theHeaders)

print("URL: " + r.url)
print("Status: " + str(r.status_code))
print()


# The text returned is one block of JSON per uplink with a blank line between.
# Event Stream (see headers above) is a connection type that sends a message when it 
# becomes available. This script is about downloading a bunch of records in one go
# So we have to turn the response in to an array and remove the blank lines.

theJSON = "{\"data\": [" + r.text.replace("\n\n", ",")[:-1] + "]}";

someJSON = json.loads(theJSON)
#print(json.dumps(someJSON, indent=4))
someUplinks = someJSON["data"]

# Output to timestamped file
now = datetime.now()
pathNFile = "DataStorage-" + theApplication + "-" + now.strftime("%Y%m%d%H%M%S") + ".txt"
print(pathNFile)
if (not os.path.isfile(pathNFile)):
	with open(pathNFile, 'a', newline='') as tabFile:
		fw = csv.writer(tabFile, dialect='excel-tab')
		fw.writerow(["received_at", "device_id", "f_port", "f_cnt", "frm_payload", "rssi", "snr", "data_rate_index", "consumed_airtime"])

for anUplink in someUplinks:
	someJSON = anUplink["result"]
	
	end_device_ids = someJSON["end_device_ids"]
	device_id = end_device_ids["device_id"]

	received_at = someJSON["received_at"]

	uplink_message = someJSON["uplink_message"];
	f_port = uplink_message["f_port"];
	f_cnt = uplink_message.get("f_cnt", "");	# first uplink is zero which is missing
	frm_payload = uplink_message["frm_payload"];
	rssi = uplink_message["rx_metadata"][0]["rssi"];
	snr = uplink_message["rx_metadata"][0]["snr"];

	# Simulated uplinks don't include these, hence the 'gets'
	data_rate_index = uplink_message["settings"].get("data_rate_index", "");
	consumed_airtime = uplink_message.get("consumed_airtime", "");	

	with open(pathNFile, 'a', newline='') as tabFile:
		fw = csv.writer(tabFile, dialect='excel-tab')
		fw.writerow([received_at, device_id, f_port, f_cnt, frm_payload, rssi, snr, data_rate_index, consumed_airtime])


