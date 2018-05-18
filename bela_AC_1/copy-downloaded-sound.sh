#!/bin/bash

#-----------------------------------------------------------------------
# This shell script renames the file "downloaded.wav" to "current.wav"
# from the "wav_files" and then removes the original "downloaded.wav"
# from the "sound_files" folder
#

#__author__      = "Anna Xambo"
#__date__        = "March 15 2018"
#__copyright__   = "Copyright (C) 2018 Queen Mary University of London"

echo "moving file to wav_files"

mv wav_files/downloaded.wav wav_files/current.wav
sleep 6s
rm sound_files/downloaded.wav
