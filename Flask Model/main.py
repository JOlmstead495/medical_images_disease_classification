from flask import Flask, request, render_template, url_for, redirect,flash
from predict_eye_disease import drusen_or_normal,crop_image_img,horiz_structure,get_sorted_pixel_column_list
import os
import cv2
import mahotas
import numpy as np
import pandas as pd

#ALLOWED_EXTENSIONS = set(['jpeg'])

# create a flask object
app = Flask(__name__)

UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# creates an association between the / page and the entry_page function (defaults to GET)
@app.route('/')
def entry_page():
    url_for('static', filename='style.css')
    return render_template('/index.html')

# creates an association between the /predict_recipe page and the render_message function
# (includes POST requests which allow users to enter in data via form)
@app.route('/upload/', methods=['GET', 'POST'])
def render_message():
    
    file = request.files['eye_dis']
    f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    
    file.save(f)
    img=cv2.imread(f,0)
    
    # Crop Image
    img,thresh,M=crop_image_img(img)

    # GRAB MOMENT INFO
        #Zernike Moments
    z_mom=mahotas.features.zernike_moments(img,radius=2)
        # Horizontal Count
    h_count=horiz_structure(img)

    moment_list=cv2.HuMoments(M).flatten()
    moment_list=np.append(moment_list,h_count)
    moment_list=np.append(moment_list,z_mom)
    moment_list=np.array(moment_list).reshape(1,-1)


    # GRAB PIXEL INFO
    pixel_img=cv2.resize(thresh,(60,30)).flatten()

    column=get_sorted_pixel_column_list()
    df_dict={column[i]:pixel_img[i] for i in range(0,len(column))}
    df_list=[]
    df_list.append(df_dict)
    df_pix=pd.DataFrame(df_list)
    df_pix=np.array(df_pix)
    # show user final message
    #drusen_or_normal(df_pix,moment_list)
    return_list=drusen_or_normal(df_pix,moment_list)
    return render_template('/index.html', message1=return_list[0],message2=return_list[1],message3=return_list[2])

if __name__ == '__main__':
    app.run(debug=True)