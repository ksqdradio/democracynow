# democracynow

Download the latest mp3s for various syndicated shows and copy to Dropbox folder for use on the air room studio computer. These scripts are run by cronjobs:

```
35 6 * * 1-5 cd /home/dan/dn && ./dn.py
# run the Thom Hartmann download earlier on Wednesday and at ~15:00 the other days
55 14 * * 1,2,4,5 cd /home/dan/dn && ./th.py
35 14 * * 3 cd /home/dan/dn && ./th.py
# download economic update on friday afternoon. it is uploaded on thursdays and is on KSQD schedule on mondays
35 14 * * 5 cd /home/dan/dn && ./eu.py
```

You'll need a working Dropbox API token in the file `dropbox.apitoken`.
