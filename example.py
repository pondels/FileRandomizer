from fileRandomizer import RandomizeFiles

RF = RandomizeFiles()
directory = './exampleSkinFolder'

# Creating a dataset to use for the PNG's
include = '.png'
RF.create_data(directory, include)
RF.copy_folders('TestCopyFile')
RF.shuffle()

# Adding in the .ini file
RF = RandomizeFiles()
include = '.ini'

# Must always call these 3 functions in order for it all to work
RF.create_data(directory, include)
RF.copy_folders('TestCopyFile')
RF.shuffle()