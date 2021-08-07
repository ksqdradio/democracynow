# democracynow

Download the latest Democracy Now! mp3 and copy to Dropbox folder for use on the air room studio computer. This script is run by a cronjob every weekday morning:

`35 6 * * 1-5 cd /home/dan/dn && ./dn.py`

You'll need a working Dropbox API token in the file `dropbox.apitoken`.
