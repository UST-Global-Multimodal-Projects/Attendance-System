import os
from dotenv import load_dotenv
import subprocess
from ImageExtractor import ROISaver


load_dotenv()

input_image_path = os.environ['input_image_path']
input_directory_path=os.environ['input_directory_path']
coordinates_file_path=os.environ['coordinates_file_path']
face_detection_model_path=os.environ['face_detection_model_path']


#run face detection
cmd = f'python FaceDetector.py -i "{input_image_path}" -m "{face_detection_model_path}" -at ssd'
p=subprocess.Popen(cmd,shell=True)
output, error = p.communicate() 
print(output)
print(error)
print("====================face detection module ended here=====================")


#run ROI extraction
obj=ROISaver(input_directory_path,input_image_path,coordinates_file_path)
obj.run()







# print(input_image_path)
# print(input_directory_path)
# print(face_detection_model_path)

