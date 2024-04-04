import glob
from PIL import Image
import os
import tqdm


# pip install tqdm, pilow before running

def resize_images_in_folder(root_folder, save_folder, new_size):
    file_paths = glob.glob(os.path.join(root_folder, '/'))
    if len(file_paths) == 0:
        raise ValueError("No Images")

    if not os.path.exists(save_folder):
        os.mkdir(save_folder)

    for file_path in file_paths:
        image = Image.open(file_path)
        image = image.resize(new_size, Image.ANTIALIAS)

        filename = os.path.basename(file_path)
        class_name = file_path.split("/")[-2]

        sub_dir = save_folder + f"/{class_name}"
        if not os.path.exists(sub_dir):
            os.mkdir(sub_dir)

        save_path = sub_dir + f"/{filename}"

        image.save(save_path)


folder_path = "~/Documents/git/DomainGeneralization/DomainBed/domainbed/data/PACS"
save_directory = "~/Documents/git/DomainGeneralization/KhanhLe/DomainBed/domainbed/data/PACS"
new_size = (256, 256)

resize_images_in_folder(folder_path, save_directory, new_size)