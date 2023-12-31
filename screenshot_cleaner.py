
import shutil
import os

screenshot_dir = 'Users/    Desktop/screenshots'
desktop_dir = '/Users/  /Desktop'

#if screenshots folder doesn't exist, create it

if not os.path.exists(screenshot_dir):
    os.makedirs(screenshot_dir)

#check all files on desktop, if its a screenshot, move it to screenshot folder
files_on_desktop = os.listdir(desktop_dir)
for file in files_on_desktop:
    if file.startswith('Screen Shot') and file.endswith('.png'):
        file_dir = desktop_dir + '/' + file
        shutil.move(file_dir, screenshot_dir)
        print(f'Moving {file}...')
    

