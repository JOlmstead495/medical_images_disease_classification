import pickle
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import cv2
import math

# read in the model
pixel_model = pickle.load(open("/**Random_Forest_Pixel_Model**.p","rb"))
moment_model = pickle.load(open("**Random_Forest_Moment_Model**.p","rb"))
ensemble_model = pickle.load(open("**Logistic_Ensemble_Model**.p","rb"))

# create a function to take in user-entered amounts and apply the model
def drusen_or_normal(pix_X,mom_X, pix_model=pixel_model,mom_model=moment_model,ens_model=ensemble_model):
    
    print(mom_X)
    moment_prediction = mom_model.predict_proba(mom_X)
    pixel_prediction = pix_model.predict_proba(pix_X)
    

    df_prediction=pd.DataFrame(pixel_prediction[:,1],columns=['Pix'])
    df_prediction['Mom']=moment_prediction[:,1]

    # make a prediction
    
    logit_prediction=ens_model.predict_proba(df_prediction)
    
    if logit_prediction[0,1]>.95:
        prediction=1
    if logit_prediction[0,1]<=.95:
        prediction=0

    if prediction==1:
        est_pred=logit_prediction[0,1]
    if prediction==0:
        est_pred=logit_prediction[0,0]
    
    # return a message
    message_array = ["You have diseased eyes!",
                    "You have normal eyes!"]
    message_array2=["are affected by Drusen!",
                    "are not affected by Drusen!"]

    return [message_array[prediction],int(est_pred*100),message_array2[prediction]]

def crop_image_img(img):
    '''
    '''
    shape=img.shape
    y_crop=int(shape[0]/8)
    x_crop=int(shape[1]/20)
    img = img[y_crop:-y_crop,x_crop:-x_crop]
    ret,thresh = cv2.threshold(img,127,255,0)
    M = cv2.moments(thresh)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    top_y=int(cY/2)
    bot_y=int(((img.shape[0]-cY)/2)+cY)
    crop_img = img[top_y:bot_y,0:img.shape[1]]
    crop_thresh = thresh[top_y:bot_y,0:img.shape[1]]
    return crop_img,crop_thresh,M


def horiz_structure(img):
    horiz = np.copy(img)
    horiz_col = horiz.shape[1]
    horiz_size = int(horiz_col / 20)
    horiz_Structure = cv2.getStructuringElement(cv2.MORPH_RECT, (horiz_size,1))
    horiz = cv2.erode(horiz, horiz_Structure)
    horiz = cv2.dilate(horiz, horiz_Structure)
    return np.mean(horiz)/horiz_col

def get_sorted_pixel_column_list():
    col=[]
    for i in range(1,1801):
        col=np.append(col,'P'+str(i))

    col = tuple(col)
    return col