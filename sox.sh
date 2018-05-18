#!/bin/bash

#-----------------------------------------------------------------------
# This shell script converts the audio file to wav and stores it in the folder "wav_files"
#

#__author__      = "Anna Xambo"
#__date__        = "March 15 2018"
#__copyright__   = "Copyright (C) 2018 Queen Mary University of London"

echo "sox subprogram"
echo $1
sox "$1" wav_files/downloaded.wav

sleep 4s
source scp.sh
