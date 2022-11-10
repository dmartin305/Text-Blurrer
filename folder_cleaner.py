import os

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
    
    pass_0 = "images/1"
    pass_1 = "images/2"
    pass_2 = "images/3"
    pass_3 = "images/4"
    
    folders = { pass_0 , pass_1 , pass_2 , pass_3 }
    
    for folder in folders:
        for img in os.listdir(folder):
            
            # TODO 
            # Check the number of filter passes 
            # If 0 passes do nothing
            # Otherwise 
            # delete the image    
            
            return 
    return