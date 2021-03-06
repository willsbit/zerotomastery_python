import os
import sys
from PIL import Image

# grab first and second argument
folder = sys.argv[1]
new_folder = sys.argv[2]

# check if new/ exists, and if not, create it
isExist = os.path.exists(new_folder)

if not isExist:
    os.makedirs(new_folder)
    print("New directory created.")

# loop through the Pokedex and convert images to png
# save them to the new folder
for file in os.listdir(folder):
    img = Image.open(os.path.join(folder, file))
   # print(str(os.path.join(new_folder, file)))
    new_img = img.save(str(os.path.join(new_folder, os.path.splitext(file)[0]) + '.png'), format="png")
    print("Done!")




