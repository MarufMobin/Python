import glob
import shutil
import zipfile
import csv
import os

""" 
    Source to server file Copy and Delete file in source folder 
    Only Source File Copy in server
    and Source file Delete 
"""

source_file = '../source/*'
file_found = glob.glob(source_file)
shutil.copy( file_found[0], '.' )
os.remove(file_found[0])

text_file = []
with open('./source.txt', 'r') as file:
    lines = csv.reader(file)
    for index,line in enumerate(lines):
        text_file.append(line)
file.close()

""" 
    Server stay our Modified files
"""
first_text = text_file[0:10]
second_text = text_file[0:20]
third_text = text_file[0:30]

filesrc = file_found[0].split('\\')[1].split('.')

for i in range(1,4):
    setFileName = filesrc[0] + '_'+ str(i) +'.'+ filesrc[1]
    with open( setFileName, 'w',encoding = 'utf-8') as file:
        if i == 1 :
            file.write( str(first_text) )
        elif i == 2 : 
            file.write( str(second_text) )
        elif i == 3 : 
            file.write( str(third_text) )
    file.close()

""" 
    Make a zip File and Transfer the All file in Destination folder
"""
comprace_file_name = []
comprace_file_main_path = './*'
comprace_file_path = glob.glob(comprace_file_main_path)

for i in range( len(comprace_file_path) ):
    if comprace_file_path[i].split('\\')[1].split('.')[1] == 'txt':
        comprace_file_name.append(comprace_file_path[i].split('\\')[1])
    elif comprace_file_path[i].split('\\')[1].split('.')[1]  == 'py':
        print( comprace_file_path[i].split('\\')[1] )

""" 
    Files are Actual Zipping here 
"""

with zipfile.ZipFile('final.zip', 'w') as zipfiles:
    for file in comprace_file_name:
        zipfiles.write( file, compress_type=zipfile.ZIP_DEFLATED)
zipfiles.close()

""" 
    Zip file send to destination and unzip file there 
"""
destination_path = '../destination/'
zip_file_path = glob.glob('./*')

for file in range( len( zip_file_path) ):
    if zip_file_path[file].split('\\')[1] == 'final.zip':
        with zipfile.ZipFile( './final.zip', 'r') as zip_ref:
            zip_ref.extractall(destination_path)

""" 
    Server Files Delete are here
"""
delete_file_source_path = './*'
delete_file_source = glob.glob( delete_file_source_path )

for i in range(len(delete_file_source)):
    if delete_file_source[i].split('\\')[1].split('.')[1] == 'txt':
        os.remove(delete_file_source[i].split('\\')[1])
