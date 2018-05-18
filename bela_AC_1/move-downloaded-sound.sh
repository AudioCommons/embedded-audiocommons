#!/bin/bash

#-----------------------------------------------------------------------
# This shell script copies the transferred file from the folder
# "sound_files" to the folder "wav_files"
#

#__author__      = "Anna Xambo"
#__date__        = "March 15 2018"
#__copyright__   = "Copyright (C) 2018 Queen Mary University of London"

echo "moving file to wav_files"

cp sound_files/downloaded.wav wav_files
