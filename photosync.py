import os

print("Will move all RAW files, which doesn't have it's JPG file anymore")

photos_dir = '/Users/tomasz/Desktop/gwiazdka-selected'
raw_dir = photos_dir + '/./' + 'RAW'
deleted_dir = raw_dir + "/deleted"
jpg_file_format = 'JPG'
raw_file_format = 'ORF'

files = [file for file in os.listdir(photos_dir) if file.endswith("." + jpg_file_format)]
file_numbers = [os.path.splitext(file)[0] for file in files]

if not file_numbers:
    raise Exception("No jpg files?")

if not os.path.exists(deleted_dir):
    os.makedirs(deleted_dir)

raw_files = [raw_file for raw_file in os.listdir(raw_dir)]
print ('File numbers: ')
print (file_numbers)
for raw_file in raw_files:
    # if raw_file.endswith("." + raw_file_format):
    print ('File:')
    print (raw_file)
    print (os.path.splitext(raw_file)[0])
    if raw_file.endswith("." + raw_file_format) and os.path.splitext(raw_file)[0] not in file_numbers:
        print("Moving: " + raw_file)
        os.rename(raw_dir + "/" + raw_file, deleted_dir + "/" + raw_file)

print("Finished moving RAW files")
