#!/bin/sh

#To generate Combination
python combination.py eng.txt h1 h2 h3 h4 dict

cp temp_output.txt /home/chirag/Desktop/Major_Project/Convert_utf_wx

cd /home/chirag/Desktop/Major_Project/Convert_utf_wx/

#To  convert utf8 to wx
sh utf8_to_wx.sh < temp_output.txt > temp_output_wx

cp temp_output_wx /home/chirag/Desktop/Major_Project

cd /home/chirag/Desktop/Major_Project/

#To check and remove matra
python remove_matra.py

cp removed_matra.txt /home/chirag/Desktop/Major_Project/Convert_utf_wx

cd /home/chirag/Desktop/Major_Project/Convert_utf_wx/

#To convert wx to utf8
sh wx_to_utf8.sh < removed_matra.txt > temp_output_utf8

cp temp_output_utf8 /home/chirag/Desktop/Major_Project

cd /home/chirag/Desktop/Major_Project/

#To combine English - Translations - Combined output - Final output
python run.py


