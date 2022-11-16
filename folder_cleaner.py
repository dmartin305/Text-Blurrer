import os
from zipfile import ZipFile

def is_unfiltered(str):
    split_file_name = str.split(".")
    num_of_filters = split_file_name[1]
    return num_of_filters == "0" 


def clear_old_filters():
    # file names are to be writen to memory as such:
    # 
    # {video section} / { <index in captions> . <number of filter passes> . png }
    # 
    # -images
    # ---1
    # -----0.0.png
    # -----0.1.png
    # -----0.2.png
    # -----0.3.png
    # ...
    # ...
    # ...
    # ---4
    # -----0.0.png
    # -----0.1.png
    # -----0.2.png
    # -----0.3.png
    #
    # In order to do this in img_filter
    # We first need to clear the older images with 
    # the unnormalized guassian filters.
    #
    # We need to retain all files formated as:
    # 
    # {*}/{*}.{0}.png
    
    section_1 = "images/1/1.zip"
    section_2 = "images/2/2.zip"
    section_3 = "images/3/3.zip"
    section_4 = "images/4/4.zip"
    
    folders = [ section_1 , section_2 , section_3 , section_4 ]
    
    
    for video_section in range(4):
        
        # vs                <- video section accounting for 0 index
        # new_folder_name   <- preparing folder 
        vs = video_section + 1
        new_folder_name = "images/" + str(vs) + "/" + str(vs) + "_clean.zip"
        
        # zin               <- our zip file that we need to read and clean
        # zout              <- our new zip file we will write the files without filters
        zin  = ZipFile(folders[video_section], "r")
        zout = ZipFile(new_folder_name, "w")
        for image in zin.infolist():
            if (is_unfiltered(image.filename)):
                buffer = zin.read(image.filename)
                zout.writestr(image, buffer)
        zin.close()
        zout.close()

    
clear_old_filters()
