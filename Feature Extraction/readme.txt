This is a feature extraction model. It takes images as input and then it classifies most similar images in same categories

the first file Feature extactor extract features from classic caltech 101 dataset. After that, it uses model to extract features from each images and store
it into a pickle model. Now in 2nd file we load the model pickle and we use KNN to compute distance between the images and then function is there to plot images
with similar images 