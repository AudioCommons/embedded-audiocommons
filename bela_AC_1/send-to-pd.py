#-----------------------------------------------------------------------
# This script launches the shell script "copy_downloaded_sound.sh" to
# rename the file "downloaded.wav" to "current.wav"
# and then removes the original "downloaded.wav" from the "sound_files" folder
# 
__author__      = "Anna Xambo"
__date__        = "March 15 2018"
__copyright__   = "Copyright (C) 2018 Queen Mary University of London"

import os
import sys
import subprocess

print("Launched the OSC message to Pd")
subprocess.call(['./copy_downloaded_sound.sh'])
