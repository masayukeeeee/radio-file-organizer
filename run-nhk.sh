# This shell script for a task described below.
# 1. Copy all mp3 files from outer hard disk to local disk.
# 2. Run a python script to process the files.
# How to run: sh run.sh

cp -r /Volumes/Untitled/AM/NHK第二放送/*.MP3 /Users/sakaimasayuki/Dropbox/radio/uncategorized/
poetry run python file_organize.py
