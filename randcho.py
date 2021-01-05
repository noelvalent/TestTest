import os, random, shutil

path = r'D:\Shared Folder\새 폴더'
t_path = r'C:\Users\tama0\Desktop\새 폴더'
file_list = os.listdir(path)

count = 0

lst_already_copy = []

while True:
    _f = random.choice(file_list)
    if count == 20:
        break
    
#    if 'canedschoolgirls ' not in _f:
#       continue
    p = f'{path}\\{_f}'
    if p in  lst_already_copy:
        continue
    
    if os.path.isdir(p):
        for __f in os.listdir():
            if '.zip' in __f:
                print(f'{__f}')
                shutil.copy2(f'{path}\\{_f}\\{__f}', f'{t_path}')
                count = count + 1
                print(count)
    else:
        print(f'{_f}')
        shutil.copy2(f'{path}\\{_f}', f'{t_path}')
        count = count + 1
        print(count)
        
    lst_already_copy.append(p)
    
    
    


