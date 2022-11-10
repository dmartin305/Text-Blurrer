import cv2 as cv
from img_filter import *
import os
import sys

one = "images/1"
two = "images/2"
three = "images/3"
four = "images/4"

def main():
    # Iterate across images
    for img_path in os.listdir(one):
        
        # Load the image and check if the file is valid.
        # If valid resume,
        # If not valid exit script
        img = cv.imread(cv.samples.fineFile(img_path))
        if img is None:
            sys.exit("Image " + img_path + " could not be read.")

        # Split path name to use for writing filtered images
        # to approriate directories
        
        path_name = os.path.split(img_path)
        file_name = path_name[1]
        index = file_name.split(".")[1]
        
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

        first_pass = apply_guassian_filter(img)
        second_pass = apply_guassian_filter(first_pass)
        third_pass = apply_guassian_filter(second_pass)
        
        first_pass_file_name = "1." + index + ".png"
        second_pass_file_name = "2." + index + ".png"
        third_pass_file_name = "3." + index + ".png"
        
        cv.imwrite(first_pass_file_name, first_pass)
        cv.imwrite(second_pass_file_name, second_pass)
        cv.imwrite(third_pass_file_name, third_pass)
        
    return
    