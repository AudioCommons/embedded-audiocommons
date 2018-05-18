#!/bin/bash

#-----------------------------------------------------------------------
# This shell script transfers the file to Bela's folder "sound_files"
#

#__author__      = "Anna Xambo"
#__date__        = "March 15 2018"
#__copyright__   = "Copyright (C) 2018 Queen Mary University of London"

echo "scp subprogram"

sleep 10s
scp wav_files/downloaded.wav bela_AC_1:~/Bela/projects/tei_demo_bela_AC_1/sound_files
