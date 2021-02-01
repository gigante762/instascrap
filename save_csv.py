import sys
import os
import json
import shutil

#path = './' + sys.argv[1]
path = sys.argv[1]
sep  = ';'

with open(path + '_data.csv',"w") as file_csv:
    file_csv.write('date' + sep + 'typename' + sep + 'likes' + sep + 'comments' + '\n')# + sep + 'caption\n')
    for filename in os.listdir(path):
        if filename.endswith(".txt") and "old" not in filename:
            with open(os.path.join(path,filename),"r") as f:
                text = f.read()

            # print(text)
            text = '{' + text + '}'
            y = json.loads(text)
            #print(y)
            
            file_csv.write(y["date"] +sep+ y["typename"] + sep + y["likes"] + sep +y["comments"] + '\n') #sep + y["caption"] + '\n')

shutil.rmtree(sys.argv[1]);
