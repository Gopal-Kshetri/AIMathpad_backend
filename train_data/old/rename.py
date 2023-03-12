import os
from PIL import Image
import shutil
from padding import pad

# root_dir = './renamed_images/'
# new_dir = './combined_images/'
# #creating directory for words
# if not(os.path.exists(new_dir)):
#     os.mkdir(new_dir) 

# file_num = 0

# with open("label.txt", "w") as file:
#     for each in os.listdir(root_dir):
#         for photo in os.listdir(root_dir+each):
#             # print(f'{root_dir} {people} {each} {photo}')
#             complete_path = root_dir+each+'/'+photo

#             image =Image.open(complete_path)
#             # cv2.imshow("Image", image)
#             # cv2.waitKey(0)
#             padded_image = pad(image)
#             new_path = new_dir+str(file_num)+".png"
#             padded_image.save(new_path)

#             # print(new_path, complete_path)
#             # shutil.copy(complete_path, new_path)

#             file.write(each +"\n")
#             file_num += 1


root_dir = './combined_images/'
new_dir = './test_images/'
#creating directory for words
if not(os.path.exists(new_dir)):
    os.mkdir(new_dir) 

for photo in os.listdir(root_dir):
    # print(f'{root_dir} {people} {each} {photo}')
    complete_path = root_dir+photo

    image =Image.open(complete_path)
    # cv2.imshow("Image", image)
    # cv2.waitKey(0)
    padded_image = pad(image)
    new_path = new_dir+photo
    padded_image.save(new_path)
        
