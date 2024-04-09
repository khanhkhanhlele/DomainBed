import glob
from PIL import Image
import os


# pip install tqdm, pilow before running

def resize_images_in_folder(root_folder, save_folder, new_size):
    file_paths = []
    for root, dirs, files in os.walk(root_folder):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                file_paths.append(os.path.join(root, file))

    # file_paths = glob.glob(os.path.join(root_folder, '/'))

    if len(file_paths) == 0:
        raise ValueError("No Images")

    if not os.path.exists(save_folder):
        os.mkdir(save_folder)

    for file_path in file_paths:
        image = Image.open(file_path)
        # print(image.size)

        image = image.resize(new_size)

        filename = os.path.basename(file_path)

        # print(file_path)
        print(file_path.split("/"))

        domain_name = file_path.split("/")[-4]
        type_name = file_path.split("/")[-3]
        class_name = file_path.split("/")[-2]

        domain_dir = save_folder + f"/{domain_name}"
        if not os.path.exists(domain_dir):
            os.mkdir(domain_dir)
        type_dir = domain_dir + f"/{type_name}"
        if not os.path.exists(type_dir):
            os.mkdir(type_dir)
        class_dir = type_dir + f"/{class_name}"
        if not os.path.exists(class_dir):
            os.mkdir(class_dir)

        save_path = (save_folder + f"/{domain_name}" + f"/{type_name}"
                     + f"/{class_name}" + f"/{filename}")

        image.save(save_path)


print(os.getcwd())
folder_path = "/home/duong/Documents/git/DomainGeneralization/DomainBed/domainbed/data/VLCS"
save_directory = "/home/duong/Documents/git/DomainGeneralization/KhanhLe/DomainBed/domainbed/data/VLCS"

new_size = (64, 64)
resize_images_in_folder(folder_path, save_directory, new_size)


def create_clone(self, device, n_domain):
    self.network_specific = []
    self.optimizer_specific = []
    for i_domain in range(n_domain):
        self.network_specific.append(nn.Sequential(networks.Featurizer(self.input_shape, self.hparams),
                                                   networks.Classifier(
                                                       self.featurizer.n_outputs,
                                                       self.num_classes,
                                                       self.hparams['nonlinear_classifier']
                                                   )).to(device))
        self.network_specific[i_domain].load_state_dict(copy.deepcopy(self.network.state_dict()))
        self.optimizer_specific.append(torch.optim.Adam(
            self.network_specific[i_domain].parameters(),
            lr=self.hparams["lr"],
            weight_decay=self.hparams['weight_decay']
        ))
        if self.optimizer_specific_state[i_domain] is not None:
            self.optimizer_specific[i_domain].load_state_dict(self.optimizer_specific_state[i_domain])