import os
import csv

def nvar_extractor(filepath):
    csvfile = "C:\\Users\\dfrc\\Desktop\\Result.csv"
    filename = filepath.split('.')[-2].split('\\')[-1] 
    print(filename)
    
    with open(filepath, "rb") as rf:
        content=rf.read()
        with open(csvfile, "a") as csvfd:
            
            value = [chr(ind) if 32 <= ind and ind <= 126 else '.' for ind in content[11:]]
            value = ''.join(value)
            tmplist = [value]
            print(tmplist)
            csvwriter = csv.writer(csvfd)
            csvwriter.writerow([filename] + tmplist)
             
if __name__ == '__main__':
    root = "Y:\\내 드라이브\\Lab\\Network Storage Artifact\\실험\\Firmware Analysis\\volume-0"
    dir_list = os.listdir(root)

    for dirname in dir_list:
        dir_path = os.path.join(root, dirname)
        if os.path.isdir(dir_path):
            file_list = os.listdir(dir_path)
            for file in file_list:
                if(file.split('.')[-1] == 'nvar'):
                    nvar_extractor(os.path.join(dir_path, file))