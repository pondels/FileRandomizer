from fileRandomizer import RandomizeFiles

directory = 'exampleSkinFolder'
RF = RandomizeFiles(directory)

RF.help()

# Lists all file-types and how many of those files were found
types = RF.list_file_types()
print(types) 
# >>> {'TOTAL': 511, 'png': 422, 'wav': 53, 'PNG': 24, 'ini': 7, 'mp3': 3, 'bat': 1, 'JPG': 1}

# Copying over the folders of the directory
RF.copy_folders('randomizedTest')

# Takes a file-type and swaps similar file-types
include = ['.png', '.PNG', '.wav', '.mp3', '.JPG']
for item in include:
    RF.create_data(item)
    RF.true_random()

# Transferring Files that I don't want randomized, but still need shifted over
include = ['.ini', '.bat']
for item in include:
    RF.create_data(item)
    RF.transfer_file_types(item)

# Checking to see if both files have the same total file items
#   This ensures everything was tranferred correctly
types_orig = RF.list_file_types('exampleSkinFolder')
types_copy = RF.list_file_types('randomizedTest')

print(f'ORIGINAL TOTAL: {types_orig["TOTAL"]} \
\nCOPIED TOTAL:   {types_copy["TOTAL"]}')