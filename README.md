# Instructions to use 

## General workflow

- The runner script takes parameters from the .env file to make the process simpler for the user
- The Env file has the following parameters
    - input_image_path
    - input_directory_path
    - coordinates_file_path
    - face_detection_model_path
    - face_reidentification_model_path
    - landmark_regression_model_path
    - face_database_path
    - face_gallary_crop_flag

- Once the parameters are set in the env file you have to run runner.py by executing
```
python3 runner.py
``` 
- All the logs mentioning the details of all the Openvino modules will be displayed in the console and the final output would be printed in the **Attendance.csv** file


## Understanding the .env file parameters

- **input_image_path** : 
    - This is the path of the input image which has the pictures of all the people whose attendance has to be marked
- **input_directory_path** : 
    - This is used for internal working of the module. Once the face detection model runs on the input image it creates seperate images that have to passed to the face recognition module and this is the directory where the intermediate results are stored
    - As a user you don't have to add anything in this directory and this directory will be automatically deleted after each use.
    - **Input_Images** directory has been used for this purpose in this repository
- **coordinates_file_path** : 
    - This is used for internal working of the module. Before savinf indivisual images to the input directory the coordinates of the bounding boxes for each face is stored in this file
    - **coordinates.txt** file has been used for this purpose in this repository
- **face_detection_model_path** : 
    - Path of the Openvino face detection model
- **face_reidentification_model_path** :
    - Path of the Openvino face reidentification model
- **landmark_regression_model_path** :
    - Path of Openvino Landmark Regression model
- **face_database_path** :
    - Path of the directory that stores the all the images of known identites that the face recognition model should recognize
    - **Face Database** directory has been used for this purpose in this repository
- **face_gallary_crop_flag** : 
    - Discussed in the next section

## Setting up Face Database
- This repository should contain all the images of the known entities that the face recognition module should identify
- You can have multiple images of the same purpose. The more the number of images of an indivisual, the more is the accuracy of the face recognition module
- A naming scheme has to be strictly followed for naming all the image
    - ```<name of the person>-<number of images with starting index 0>```
    - example : aditya-0.jpg, aditya-1.jpg, atharva-0.jpg
- The images have to very tighty croped for the face recognition module produce accurate results
- Manually cropping each image would be a tedious job, therefore I have implemented an automatic cropping utility 
- Put the uncropped images in the face Database directory and set the **face_gallary_crop_flag** to **1**. This will automatically crop the images in the Face Database beofre proceeding
- Note : You have to Manually set the **face_gallary_crop_flag** to **0** for the second run otherwise the cropping utility would recrop the already cropped images and this can generate inaccurate results.