<?php

$ver  = "2021-05-26 v1.5";

ini_set("error_reporting", E_ALL);

// Get the incoming information from the raw input
$data = file_get_contents("php://input");
if ($data == "") { // So we can check the script is where we expect via a browser
	die("TTS.Webhook.Tab version: ".$ver);
}


// Save a raw copy of the message in a debug directory (you have to create it)
// This will fill up quickly so don't leave it turned on for too long!
//$pathNFile = "debug/".date('YmdHis')."-".uniqid().".txt"; 
//file_put_contents($pathNFile, $data);


$json = json_decode($data, true);

// Get selected values from the JSON
// Lines are partial indented to reflect the nesting of the data

$end_device_ids = $json['end_device_ids'];
	$device_id = $end_device_ids['device_id'];
	$application_id = $end_device_ids['application_ids']['application_id'];
		
$received_at = $json['received_at'];

$uplink_message = $json['uplink_message'];
	$f_port = $uplink_message['f_port'];
	$f_cnt = isset($uplink_message['f_cnt']) ? $uplink_message['f_cnt'] : 0;	// Zero & empty values are not included
	$frm_payload = $uplink_message['frm_payload'];
	$rssi = $uplink_message['rx_metadata'][0]['rssi'];
	$snr = $uplink_message['rx_metadata'][0]['snr'];
	$data_rate_index = isset($uplink_message['settings']['data_rate_index']) ? $uplink_message['settings']['data_rate_index'] : 0;
	$consumed_airtime = $uplink_message['consumed_airtime'];



// NOTE: Adding to the text files assumes that the server does not get two incoming
// requests at the exact same time, which for a handful of nodes is quite unlikely
// A production version of this would insert the data in to multiuser database.


// Daily log of all uplinks
$file = date('Ymd').".txt";

$output = "$received_at\t$application_id\t$device_id\t$f_cnt\t$f_port\t$frm_payload\t$data_rate_index\t$consumed_airtime\t$rssi\t$snr\n";

if (!file_exists($file)) {	// Put column headers at top of file
	file_put_contents($file, "received_at\tapplication_id\tdevice_id\tf_cnt\tf_port\tfrm_payload\tdata_rate_index\tconsumed_airtime\trssi\tsnr\n");
}

file_put_contents($file, $output, FILE_APPEND | LOCK_EX);


// Application log
$file = $application_id.".txt";

$output = "$received_at\t$device_id\t$f_cnt\t$f_port\t$frm_payload\t$data_rate_index\t$consumed_airtime\t$rssi\t$snr\n";

if (!file_exists($file)) {	// Put column headers at top of file
	file_put_contents($file, "received_at\tdevice_id\tf_cnt\tf_port\tfrm_payload\tdata_rate_index\tconsumed_airtime\trssi\tsnr\n");
}

file_put_contents($file, $output, FILE_APPEND | LOCK_EX);


// Device log
$file = $application_id."__".$device_id.".txt";

$output = "$received_at\t$f_cnt\t$f_port\t$frm_payload\t$data_rate_index\t$consumed_airtime\t$rssi\t$snr\n";

if (!file_exists($file)) {	// Put column headers at top of file
	file_put_contents($file, "received_at\tf_cnt\tf_port\tfrm_payload\tdata_rate_index\tconsumed_airtime\trssi\tsnr\n");
}

file_put_contents($file, $output, FILE_APPEND | LOCK_EX);

?>
