import cv2
import numpy as np
import skimage.color 
import skimage.filters
import matplotlib.pyplot as plt



def apply_guassian_filter_2(image):
#if (True):

    #image = cv2.imread("0.0.png")
    #cv2.imshow('Original', image)
    #cv2.waitKey(0)

    gray_image = skimage.color.rgb2gray(image)
    blurred_image = skimage.filters.gaussian(gray_image, sigma=1.0)

    t = 0.5
    binary_mask = blurred_image < t

    selection = image.copy()
    selection[~binary_mask] = 255


    #cv2.imshow('Final', selection)
    #cv2.waitKey(0)

    return selection




#OLD CODE
def apply_guassian_filter(img, blur_level, offset):
    # Image is passed in as an cv::Mat object
    # https://docs.opencv.org/4.x/d3/d63/classcv_1_1Mat.html
    # 
    # Apply the filter here and return the image post-filter

    ##img = cv2.imread("0.0.png")

    ##cv2.imshow('original', img)
    ##cv2.waitKey(0)

    grey_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    blur_grey_img = cv2.medianBlur(grey_img, 5)
    edges = cv2.Canny(blur_grey_img, 100, 200)

    contours, hierarchy = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    #red contours
    for contour in contours:
        cv2.drawContours(img, [contour], 0, (255, 255, 255))

    ##cv2.imshow('Canny', img)
    ##cv2.waitKey(0)

    mask = np.zeros(img.shape, np.uint8)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    (rv, thresh) = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    ##blur_level = 3

    img_blur = cv2.GaussianBlur(img, (blur_level,blur_level), offset)

    cv2.drawContours(mask, contours, -1, (255,255,255),0)
    output = np.where(mask==np.array([255, 255, 255]), img_blur, img)

    ##cv2.imshow('Final', output)
    ##cv2.waitKey(0)
    return output