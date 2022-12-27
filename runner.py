import os
from dotenv import load_dotenv
import subprocess
from ImageExtractor import ROISaver


load_dotenv()

input_image_path = os.environ['input_image_path']
input_directory_path=os.environ['input_directory_path']
coordinates_file_path=os.environ['coordinates_file_path']
face_detection_model_path=os.environ['face_detection_model_path']
face_reidentification_model_path=os.environ['face_reidentification_model_path']
landmark_regression_model_path=os.environ['landmark_regression_model_path']
face_database_path=os.environ['face_database_path']



#run face detection
cmd = f'python FaceDetector.py -i "{input_image_path}" -m "{face_detection_model_path}" -at ssd'
p=subprocess.Popen(cmd,shell=True)
output, error = p.communicate() 
print(output)
print(f"error= {error}")
print("====================face detection module ended here=====================")


#run ROI extraction: saves indivisual images in the input directory. Each image in this directory acts a input to the face recognizer
obj=ROISaver(input_directory_path,input_image_path,coordinates_file_path)
obj.run()


#run face recognizer for every image in the input directory
files = os.listdir(input_directory_path)
counter=0
for file in files:
    counter=counter+1
    file_path = os.path.abspath(os.path.join(input_directory_path, file))
    cmd = f'python face_recognition.py -i "{file_path}" -fg "{face_database_path}" -m_fd "{face_detection_model_path}" -m_lm "{landmark_regression_model_path}" -m_reid "{face_reidentification_model_path}"'
    p=subprocess.Popen(cmd,shell=True)
    output, error = p.communicate() 
    print(output)
    print(f"error= {error}")
    print(f"====================face recognition module for img{counter} ends here=====================")







# print(input_image_path)
# print(input_directory_path)
# print(face_detection_model_path)

