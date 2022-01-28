import os
import shutil


# coded by Kc Emma

# code for the images
for filename in os.listdir():
    if filename.endswith(('.jpg','.png','.gif')):
        if not os.path.exists('Images'):
            os.makedirs('Images')
        shutil.copy(filename,'Images')
        os.remove(filename)
        print('Done')

    # code for the documents
    if filename.endswith(('.pdf','.doc','.docx','.txt')):
        if not os.path.exists('Documents'):
            os.makedirs('Documents')
        shutil.copy(filename, 'Documents')
        os.remove(filename)
        print('Done')

    # code for the Softwares
    if filename.endswith(('.exe','.apk')):
        if not os.path.exists('Softwares'):
            os.makedirs('Softwares')
        shutil.copy(filename,'Softwares')
        os.remove(filename)
        print('Softwares Done')


    if filename.endswith(('.html','.py','.js','.java')):
        if not os.path.exists('Programming'):
            os.makedirs('Programming')
        shutil.copy(filename,'Programming')
        os.remove(filename)
        print('Programming Done')

    if filename.endswith(('.mp4','.wmv',',mp3')):
        if not os.path.exists('Music'):
            os.makedirs('Music')
        shutil.copy(filename,'Music')
        os.remove(filename)
        print('Music Done')

print('All Done')
