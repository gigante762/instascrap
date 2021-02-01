  
#!/bin/bash
instaloader --no-pictures --no-videos --no-metadata-json --post-metadata-txt="\"date\":\"{date_local}\";\"typename\":\"{typename}\";\"likes\":\"{likes}\";\"comments\":\"{comments}\"" $1;

python save_csv.py $1;

