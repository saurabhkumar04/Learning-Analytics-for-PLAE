#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Saurabh kumar
#
# Created:     23/03/2017
# Copyright:   (c) Saurabh kumar 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#imports
import re
import glob
import os
import sys
import csv
import datetime
import logging
import json
import codecs
from pprint import pprint
from datetime import datetime
from datetime import timedelta


default = "viz_" #Default log file name
log_file_name =  default + datetime.now().strftime("%Y_%m_%d_%H.%M.%S")+ ".log"
logger = logging.getLogger('myapp')
hdlr = logging.FileHandler("../logs/"+log_file_name)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.DEBUG)
print = logger.info


filenames = []
rec_list = []
uuids = []


def fetch_filenames():


    logdir = "../input/*.rec" # path to your input directory
    all_files = glob.glob("../input/*.rec")\

    for file in all_files:
        #path = file.split('/')  #for linux
        file = file.split('\\') #for windows
        filenames.append(file[-1])

    print ("Fetch Filenames Complete")
    sys.stdout.write(str(filenames))


def stitch_files():

    fetch_filenames()

    data = []
    output_filename = "../output/output_" + datetime.now().strftime("%Y_%m_%d_%H.%M.%S") + ".csv"

    with open(output_filename, 'w',newline='') as csv_write:
        a = csv.writer(csv_write)
        a.writerow(['timestamp', 'data', 'message'])  # header row

    for filename in filenames:
        with codecs.open("../input/" + filename, 'rU', 'utf-8') as f:

            for line in f:

                data.append(json.loads(line))

        #pprint (data)

        """for file in filenames:
            with open("../input/" + file) as data_file:
                data = json.load(data_file)
            with open("../input/" + file,"r") as ofile:
                rec_list.append(ofile.read())"""

        #pprint ("\n")
        #pprint (data[0].keys())
        #pprint (data)


######### Acessing UUID and X,Y coordinates
        for row in data:
            try:

                for dic in row["data"]["visuals"]:

                    #pprint(dic["uuid"])
                    uuids.append(dic["uuid"])
            except Exception as e:
                continue

        # WRITING TO CSV
        """with open(output_filename, 'a',newline='') as csv_write:
            a = csv.writer(csv_write)
            #a.writerow(data[0].keys())  # header row

            for row in data:
                a.writerow(row.values())"""

    """with open(output_filename, 'w') as csv_write:
        print ("Writing to Output")
        a = csv.writer(csv_write)
        a.writerows(data)"""
    pprint ("\n")
    pprint (len(set(uuids)))


if __name__ == '__main__':
    stitch_files()
