#!/bin/env python

import os
import tinys3

# globals
HOME = os.path.expanduser("~")
CONFIG_FILE = ".s3consul.config"
CONFIG_FILE = HOME + "/" + CONFIG_FILE
CONFIG_FILE_EXIST =  os.path.isfile(CONFIG_FILE)


# read the configs
def read_config(CONFIG_FILE) :
    '''
    CONFIG_FILE ==> string

    returns the dictionary of configurations after reading the config file
    '''
    temp_dict = dict()
    s3_config_read = open(CONFIG_FILE, 'r')
    response = s3_config_read.readlines()
    s3_config_read.close()
    # creating temp dictionary of configs {variable_name: value }
    for item in response :
        s = item.split()
        temp_dict[s[0]] = s[1]

    return temp_dict


# upload the file on s3 bucket
def upload_S3(FILENAME):
    '''
    FILENAME ==> string

    returns True if FILENAME uploaded to bucket properly
    '''

    if CONFIG_FILE_EXIST :

        try:
            configs = read_config(CONFIG_FILE)
            UPLOAD_BUCKET_NAME = configs["UPLOAD_BUCKET_NAME"]
            AWS_ACCESS_KEY_ID = configs["AWS_ACCESS_KEY_ID"]
            AWS_SECRET_ACCESS_KEY = configs["AWS_SECRET_ACCESS_KEY"]
            # UPLOAD_FILENAME = FILENAME
            UPLOAD_FILENAME = FILENAME


            conn = tinys3.Connection(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, tls=True)
            f = open(UPLOAD_FILENAME,'rb')
            conn.upload(UPLOAD_FILENAME,f,UPLOAD_BUCKET_NAME)

        except Exception as e:
            raise
    else :
        print "FILE ERROR : Config file not found "
        print "Run 'consul-s3-config' to generate config "

if __name__ == '__main__':
    FILENAME = "{YOUR_FILENAME_HERE}"
    UPLOAD_FILE_PATH = os.getcwd() + "/" + FILENAME
    print "uploading file to s3 : " + str(UPLOAD_FILE_PATH)
    upload_S3(FILENAME)
