# Instructions to use 

## General workflow
- Clone the repository using 
```
git clone https://github.com/aditya-gitte/Attendance-System.git
```
- setup a new python virtual environment so that the dependencies are not installed globally. you can use Conda, pyenv ,etc

- Install the requirements.py file in the newly created python virtual environment by running 
```
pip install -r 'requirements.py'
```

- The runner script "runner.py" has to be executed to use the applicaton. The script takes parameters from the .env file to make the process simpler for the user
- The Env file has the following parameters
    - group_images_directory
    - input_directory_path(internal)
    - coordinates_file_path
    - face_detection_model_path
    - face_reidentification_model_path
    - landmark_regression_model_path
    - face_database_path
    - debug_flag

- Once the parameters are set in the env file you have to run runner.py by executing
```
python3 runner.py
``` 
- All the logs mentioning the details of all the Openvino modules will be displayed in the console and the final output would be printed in the **Attendance.csv** file


## Understanding the .env file parameters

- **group_images_directory** : 
    - This is the path of the directory that contains all the group images which have the pictures of all the people whose attendance has to be marked
- **input_directory_path** (for internal use only) : 
    - This is used for internal working of the module. Once the face detection model runs on the input image it creates seperate images that have to passed to the face recognition module and this is the directory where the intermediate results are stored
    - As a user you don't have to add anything in this directory and this directory will be automatically deleted after each use.
    - **Input_Images** directory has been used for this purpose in this repository
- **coordinates_file_path** (for internal use only): 
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
- **debug_flag** : 
    - In the workflow all the intermediate images are deleted to prepare the module for next iteration, if this flag is set 1 the intermediate images are not deleted

## Setting up Face Database
- This repository should contain all the images of the known entities that the face recognition module should identify 

- You can have multiple images of the same purpose. The more the number of images of an indivisual, the more is the accuracy of the face recognition module

- A naming scheme has to be strictly followed for naming all the image 
    - for automatic cropping:
        - ```c_<name of the person>-<number of images with starting index 0>```
        -  example : c_aditya-0.jpg, c_aditya-1.jpg, c_atharva-0.jpg
    - for manually crop
         - ```<name of the person>-<number of images with starting index 0>```
         -  example : aditya-0.jpg, aditya-1.jpg, atharva-0.jpg
- The images have to tightly croped for the face recognition module produce accurate results
- Manually cropping each image would be a tedious job, therefore we have built an automatic cropping utility that crops all the images with the prefix ```c_``` 
- You can name the images in the face Database without the ```c_``` prefix if you don't want the automatic cropping utility to crop the image, but it is recommended to use the cropping tool as it tightly crops the images which is cruicial for maximum accuracy
