import os, random, shutil

path = r'D:\Shared Folder\night24 megapack'
t_path = r'C:\Users\tama0\Documents\새 폴더'
file_list = os.listdir(path)

count = 0

while True:
    _f = random.choice(file_list)
    if count == 10:
        break


    if _f[-5:] == '.part':
        continue

    print(f'{_f}')
    shutil.copy2(f'{path}\\{_f}', f'{t_path}')
    count = count + 1
    print(count)

            
    
    
    


