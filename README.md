# AVL_System
Automatic Vehicle Log System(AVL) is an automated system, used to track vehicles by detetcting the license plate automatically
Let's take a look how does avl works on this image.

![image](https://user-images.githubusercontent.com/60555992/208691000-46cee17d-2ab1-44c5-adc3-e5aed14f8819.png)


###We are having 4 stages :

1.Use openCV to detect the number plate.
 - OpenCV uses two types of classifiers, LBP (Local Binary Pattern) and Haar Cascades
 - A cascade classifier is a machine learning algorithm that is commonly used in automatic number plate recognition (ANPR) systems. ANPR systems use computer vision        techniques to identify and extract vehicle license plate numbers from images or video streams.
 - Haar Cascade classifier is based on the Haar Wavelet technique to analyze pixels in the image into squares by function. This uses “integral image” concepts to   compute    the “features” detected. Haar Cascades use the Ada-boost learning algorithm which selects a small number of important features from a large set to give an efficient      result of classifiers then use cascading techniques to detect plate in a image.

![image](https://user-images.githubusercontent.com/60555992/208689576-e8267290-eb4a-4075-a68e-925e524d0f59.png)


2.Processing the Image.
 - Read in Image, Grayscale and Blur

![image](https://user-images.githubusercontent.com/60555992/208690212-d895b544-ce00-4d68-9cd3-8f96ac9829c9.png)


 - Apply filter and find edges for localization

![image](https://user-images.githubusercontent.com/60555992/208690128-437ffc15-9f4b-4c91-b29e-7a78b78441fd.png)


3.Use EasyOCR to read the text.
 - After detecting the number and applying the mask we use EasyOCR to read the text from the number plate. EasyOCR can be used to extract text from a variety of image      formats 

![image](https://user-images.githubusercontent.com/60555992/208690487-1a5cae01-7971-4da5-9774-73466e4cb13c.png)


4.Enter the details in MsSQL database.
 - Now we maintain a log of vehicles. We maintain the entry time and exit time of vehicles. We also maintain the status of the car whether it is in or out.

![image](https://user-images.githubusercontent.com/60555992/208690552-6ed2b4f2-1973-4a26-a2ca-8b2295c5b55f.png)


## Here you can have live demonstration of AVL System.
https://user-images.githubusercontent.com/60555992/208688446-97044a36-7f8c-43d1-8036-29b30ad4bcba.mp4
