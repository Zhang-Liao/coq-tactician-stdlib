import shutil, os                                                                                                               

dest_dir = '/home/zhangliao/Desktop/data_with_diff/'

data_dirs = ['theories', 'plugins']

for data_dir in data_dirs:
    for root, directory, files in os.walk(data_dir):  
        for file in files:  
            if file.endswith('.sexpr'):
                dir_obj = os.path.join(dest_dir,root)
                if os.path.exists (dir_obj) == False:
                    os.makedirs(dir_obj)
                shutil.move(root+ '/' +file, os.path.join(dir_obj, file))