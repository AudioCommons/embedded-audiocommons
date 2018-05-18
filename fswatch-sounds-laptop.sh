#!/bin/bash

#-----------------------------------------------------------------------
# This shell script watches for new files in the folder "sound_files"
#

#__author__      = "Anna Xambo"
#__date__        = "March 15 2018"
#__copyright__   = "Copyright (C) 2018 Queen Mary University of London"

echo "fswatch running"

fswatch -0 -x --event Created --latency 5 /Users/annaxambo/Downloads/sound_files | xargs -0 -n 1 -I {} /Users/annaxambo/Downloads/soundmanager.sh "{}"
