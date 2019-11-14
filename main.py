import os

if __name__ == '__main__':
    root = "Y:\\내 드라이브\\Lab\\Network Storage Artifact\\실험\\Firmware Analysis\\volume-0"
    dir_list = os.listdir(root)

    for dir in dir_list:
        print("dir : ", dir)
        dir_path = os.path.join(root, dir)
        if os.path.isdir(dir_path):
            file_list = os.listdir(dir_path)
            for file in file_list:
                if(file.split('.')[-1] == "nvar"):
                    print(file)
    