#-----------------------------------------------------------------------
# This python script launches the shell script "move-downloaded-sound.sh" to copy
# the transferred file from "sound_files" to the folder "wav_files"
#
__author__      = "Anna Xambo"
__date__        = "March 15 2018"
__copyright__   = "Copyright (C) 2018 Queen Mary University of London"

import os
import sys
import subprocess

print("Launched moving sounds from 'sound_files' to 'wav_files'")
subprocess.call(['./move-downloaded-sound.sh'])
