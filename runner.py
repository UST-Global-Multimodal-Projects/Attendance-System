import os
from dotenv import load_dotenv
import subprocess
from ImageExtractor import ROISaver
import os
import glob


load_dotenv()

input_image_path = os.environ['input_image_path']
input_directory_path=os.environ['input_directory_path']
coordinates_file_path=os.environ['coordinates_file_path']
face_detection_model_path=os.environ['face_detection_model_path']
face_reidentification_model_path=os.environ['face_reidentification_model_path']
landmark_regression_model_path=os.environ['landmark_regression_model_path']
face_database_path=os.environ['face_database_path']
face_gallary_crop_flag=os.environ['face_gallary_crop_flag']
debug_flag=os.environ['debug_flag']


#clear the input folder so that all the cropped images from the previous execution are deleted
# files = glob.glob(input_directory_path)
# for f in files:
#     os.remove(f)



#crop all images in face database if the face_gallary_crop_flag is set to 1
if face_gallary_crop_flag=="1":
    print("[ INFO ] Cropping each image in the database to increase accuracy")
    files = os.listdir(face_database_path)
    counter=0
    for file in files:
        counter+=1
        file_path = os.path.abspath(os.path.join(face_database_path, file))
        cmd = f'python FaceDetector.py -i "{file_path}" -m "{face_detection_model_path}" -at ssd'
        p=subprocess.Popen(cmd,shell=True)
        output, error = p.communicate() 
        print(output)
        print(f"error= {error}")
        print(f"====================Cropped image {counter} from the face database=====================")

        #this module stores the cropped images in the face gallery
        obj=ROISaver(face_database_path,file_path,coordinates_file_path)
        obj.databaseCrop()

        #clear the coordinates file after each use
        with open(coordinates_file_path, 'w') as coordinates_file:
            coordinates_file.truncate()





#run face detection
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++face detection module++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
cmd = f'python FaceDetector.py -i "{input_image_path}" -m "{face_detection_model_path}" -at ssd'
p=subprocess.Popen(cmd,shell=True)
output, error = p.communicate() 
print(output)
print(f"error= {error}")
print("----------------------------------------------------------face detection module ended here------------------------------------------------------------------")




#run ROI extraction: saves indivisual images in the input directory. Each image in this directory acts a input to the face recognizer
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Reading coordinates file++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
obj=ROISaver(input_directory_path,input_image_path,coordinates_file_path)
obj.run()
print("-----------------------------------------------------------Stored insivisual images in the input directory-----------------------------------------------------")


#run face recognizer for every image in the input directory
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ face recognition module $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
files = os.listdir(input_directory_path)
counter=0
for file in files:
    if file==".placeholder":
        continue
    counter=counter+1
    file_path = os.path.abspath(os.path.join(input_directory_path, file))
    cmd = f'python face_recognition.py -i "{file_path}" -fg "{face_database_path}" -m_fd "{face_detection_model_path}" -m_lm "{landmark_regression_model_path}" -m_reid "{face_reidentification_model_path}"'
    p=subprocess.Popen(cmd,shell=True)
    output, error = p.communicate() 
    print(output)
    print(f"error= {error}")
    print(f"#################################################### face recognition module for img{counter} ends here ################################################")


#clear the coordinates file for next use
print("--------------------------------------------------------Clearing the coordinates files --------------------------------------------------")
with open(coordinates_file_path, 'w') as coordinates_file:
    coordinates_file.truncate()


#clearing the Input_Images directory for the next image if dubug flag is set to 0
# if debug_flag==0:
#     print("-----------------------------clearing the inputs directory---------------------------------")
#     dir_path = input_directory_path

#     for filename in os.listdir(dir_path):
#         file_path = os.path.join(dir_path, filename)
#         try:
#             if os.path.isfile(file_path) or os.path.islink(file_path):
#                 os.unlink(file_path)
#             elif os.path.isdir(file_path):
#                 shutil.rmtree(file_path)
#         except Exception as e:
#             print('Failed to delete %s. Reason: %s' % (file_path, e))
#     print("-----------------------------cleared the inputs directory---------------------------------")






# print(input_image_path)
# print(input_directory_path)
# print(face_detection_model_path)


