""" 
    Object Processor 
    Md Maruf
"""
import glob
import shutil
import os

source_path = '../source/*'
destination_path = '../destination/'
postfix = [ 1,2,3 ]

while True:
    source_obj = glob.glob(source_path)
    if len( source_obj ) > 0:
        object_path = source_obj[0]
        shutil.copy(  object_path, '.')
        object_name = object_path.split('/')[-1].split('\\')[-1].split('.')


        prefix = object_name[0]
        postfix2 = object_name[1]

        # print(type(object_name))

        for item in range( len(postfix) ):
            filename = prefix + '_' + str(item)+ '.' + postfix2
            print(filename)
            shutil.copy( object_path, f"{destination_path}/{filename}")

        os.remove(object_path)
        os.remove(object_path.split('/')[-1].split('\\')[-1])


# [ 22-1 Introduction To The Module ] [ 22-2 Planning The Solution ]  [22-3 Trigger The Event] [ 22-4 Name Changes ] [ 22-5 Move To Detination ] [ 22-6 True Event Driven Program ]

        