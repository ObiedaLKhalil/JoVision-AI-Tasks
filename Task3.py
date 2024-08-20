import os  # Imports the os module, which provides functions to interact with the operating system, such as file and directory operations.
import glob  # Imports the glob module, which is used for file pattern matching. It allows you to find all pathnames matching a specified pattern.
import cv2
import numpy as np
import pandas as pd
from PIL import Image
from openpyxl import Workbook, load_workbook

def analyze_image(image_path, pressure_threshold=50):
    file_name = os.path.basename(image_path)
    file_name, _ = os.path.splitext(file_name)
    output_file = 'C:\\Users\\obied\\OneDrive\\Desktop\\JoVision-AI-Tasks\\obieda.xlsx'
    
    # Ensure the directory exists
    output_dir = os.path.dirname(output_file)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    image = cv2.imread(image_path)
    pressure_data = image[:, image.shape[1]//2:]
    gray_pressure_data = cv2.cvtColor(pressure_data, cv2.COLOR_BGR2GRAY)
    finger_pressures = []
    finger_data = []

    Thumb_area = gray_pressure_data[0:25, :]
    Index_area = gray_pressure_data[49:75, :]
    Middle_area = gray_pressure_data[75:105, :]  
    Ring_area = gray_pressure_data[114:145,:]
    Pinky_area = gray_pressure_data[145:255, 198:235]
    
    areas = [Thumb_area, Index_area, Middle_area, Ring_area, Pinky_area]
    names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']


    for area, name in zip(areas, names):
        avg_brightness = np.mean(area)
        pressure_applied = 1 if avg_brightness > pressure_threshold else 0
        finger_pressures.append(pressure_applied)
        finger_data.append({
            'Finger': name,
            'Pressure': pressure_applied,
            'Brightness': avg_brightness
        })
   
    mode = 'a' if os.path.exists(output_file) else 'w'
    if mode=='a':
        with pd.ExcelWriter(output_file, mode=mode, engine='openpyxl', if_sheet_exists='replace') as writer:
            for i in range(len(finger_data)):  
                df = pd.DataFrame([finger_data[i]]) 
                df.to_excel(writer, sheet_name=f'({file_name}){name[i]}', index=False)
    else:
        with pd.ExcelWriter(output_file, mode=mode, engine='openpyxl') as writer:
            for i in range(len(finger_data)):  
                df = pd.DataFrame([finger_data[i]]) 
                df.to_excel(writer, sheet_name=f'({file_name}){name[i]}', index=False)


        
    return finger_pressures

def process_images_in_folder(folder_path):
    image_paths = glob.glob(os.path.join(folder_path, '*.[pj][np]g')) 
    image_paths += glob.glob(os.path.join(folder_path, '*.[pj][np]g')) 

    for image_path in image_paths:
        finger_pressures=analyze_image(image_path)
        print(finger_pressures)

folder_path = 'C:\\Users\\obied\\OneDrive\\Desktop\\JoVision-AI-Tasks\\task3Images\\task3' 
process_images_in_folder(folder_path)
