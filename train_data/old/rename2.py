import os
from PIL import Image
import shutil
from padding import pad

root_dir = './renamed_images/'
new_dir = './test_images/'
# new_prefix = 'new_prefix_'

if not(os.path.exists(new_dir)):
    os.mkdir(new_dir)
    
for each in os.listdir(root_dir):
    if not(os.path.exists(new_dir+each)):
        os.mkdir(new_dir+each)
    for count, filename in enumerate(os.listdir(root_dir+each)):
        # if filename.endswith('.jpg') or filename.endswith('.png'):
            # Rename the file
        if(count>=2000):
            break;
        complete_path = root_dir+each+'/'+filename
        image =Image.open(complete_path)
        # cv2.imshow("Image", image)
        # cv2.waitKey(0)
        padded_image = pad(image)
        new_path = new_dir+each+'/'+str(count)+".jpg"
        padded_image.save(new_path)
        # cv2.imshow("Padded Image", padded_image)
        # shutil.copy(complete_path, new_path)
        # print(new_path)