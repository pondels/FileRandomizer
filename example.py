#%%

from fileRandomizer import RandomizeFiles

#%%

RF = RandomizeFiles()

#%%

directory = 'exampleSkinFolder'

# Lists all file-types and how many of those files were found
types = RF.list_file_types(directory)
print(types)

#%%

# Setting the directory and copying over the folders
RF.directory = directory
RF.copy_folders('randomizedExample')

#%%

include = ['png', 'PNG', 'wav', 'mp3', 'JPG']
for item in include:
    RF.create_data(directory, item)
    RF.shuffle()


#%%

# Transferring Files that I don't want randomized, but still need shifted over
include = ['.ini', '.bat']
for item in include:
    RF.create_data(directory, item)
    RF.transfer_file_types(item)

#%%

# Checking to see if both files have the same total file items
#   This ensures everything was tranferred correctly
types_orig = RF.list_file_types('exampleSkinFolder')
types_copy = RF.list_file_types('randomizedExample')

print(f'ORIGINAL TOTAL: {types_orig["TOTAL"]} \
\nCOPIED TOTAL:   {types_copy["TOTAL"]}')

# Another way of checking these values is by using this method.
if types_copy['TOTAL'] == types_orig['TOTAL']: print('FILE LENGTHS EQUAL')
else: print('FILE LENGTHS NOT EQUAL. POSSIBLE FILES MISSING.')

#%%