# Classifying Drusen Retinal Disease Through Medical Images

I classified retinal medical images that had Drusen composites which lead to eye diseases, compared to retinal images without Drusen composities. This project allowed me to work on classification algorithms and computer vision. This project was completed over 2 weeks, including time to prepare for a presentation. I stored over
25,000 medical images on Amazon Web Services and pulled in the images using Python. I used OpenCV and Mahotas
to pull in different moments from images and watershedding and thresholding the images. I ran a Random Forest
model, using RandomizedSearch to tune the hyperparameters, on image moments derived from the image, and on pixel
intensities of the resized medical images. I then ensembled those two models together using a Logistic Regression
model. I graphed some of the results using Seaborn and Matplotlib. I obtained an ROC-AUC score of .81 using this method. I also created a Flask Web App that allows you to upload a medical image to get classified.

## Tools Used During Project

Data Storage: AWS
Image Processing: Mahotas and OpenCV
Modeling: Sklearn
Graphing: Seaborn  

## Authors

* **Jack Olmstead** - [LinkedIn](https://www.linkedin.com/in/jolmstead495/)
