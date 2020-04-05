import os

print("Checking if jpg and raw files are in sync")

photos_dir = '/Users/tomasz/Tmp/Pari/'
raw_dir = photos_dir + '/./' + 'RAW'
deleted_dir = raw_dir + "/deleted"
jpg_file_format = 'jpg'
raw_file_format = 'CR2'

files = [file for file in os.listdir(photos_dir) if file.endswith("." + jpg_file_format)]
file_numbers = [os.path.splitext(file)[0] for file in files]

if not os.path.exists(deleted_dir):
    os.makedirs(deleted_dir)

raw_files = [raw_file for raw_file in os.listdir(raw_dir)]
raw_file_numbers = [os.path.splitext(raw_file)[0] for raw_file in raw_files]
for raw_file in raw_files:
    if raw_file.endswith("." + raw_file_format) and os.path.splitext(raw_file)[0] not in file_numbers:
        print("Missing: " + raw_file + " in jpgs")
for jpg_file in files:
    if jpg_file.endswith("." + jpg_file_format) and os.path.splitext(jpg_file)[0] not in raw_file_numbers:
        print("Missing: " + jpg_file + " in raws")

print("Finished checking")
