# TheThingsStack-Integration-Starters
## Starter code for various The Things Stack (v3) integrations

This repro provides some quick-win get-you-going scripts for using with [The Things Stack](https://console.cloud.thethings.network/) (v3) integrations created by [The Things Industries](https://www.thethingsindustries.com) along with some data processing code to highlight some of the issues that come with some languagues.

--

The simplest integration to setup is a WebHook on web hosting. No configuration needed, just upload to some PHP enabled webspace and tell TTS the URL.

If you want to run something in your office, then the same results can be had with the MQTT Python 3 script on your computer.

The Data Storage integration provides a handy backup service to either of the above so once you have turned it on in TTS console, the Data Storage Python 3 script will grab recent payload data.

--

The payload formatter running on TTS is a convenience function & should not be relied on for production. There will be some notes & worked examples on writing decoders in JavaScript, Python & PHP that will help you expand upon these scripts.

--

All usage support for these scripts is via the TTN forum, if you find a bug, please file an issue here.