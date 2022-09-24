import os
import random
import shutil

class RandomizeFiles():

    def __init__(self):
        self.directory = ''
        self.information = []
        self.file_name = ''
        self.current_directory = os.getcwd()

    def __remove_redundancies(self):

        length_of_info = len(self.information)

        for data in range(len(self.information)):
            if self.information[length_of_info - data - 1][1] == []:
                self.information.remove(self.information[length_of_info - data - 1])

    def __swap_files(self, first, second):

        dir1, fn1 = first
        dir2, fn2 = second

        if dir1 not in self.current_directory and dir2 not in self.current_directory:
            print(self.current_directory, dir1)
            shutil.copyfile(f'{dir1}/{fn1}', f'{self.file_name}{dir2[len(self.directory):]}/{fn2}')
            shutil.copyfile(f'{dir2}/{fn2}', f'{self.file_name}{dir1[len(self.directory):]}/{fn1}')
    # ------------------------------------------------------------------------------#
    def copy_folders(self, file_name):
        '''
            Creates a folder in your working directory that copies
            all of the folders with the input directory without data.

            File_Name: The name of the file you want to copy

            Used later in the shuffle() method.
        '''

        if self.directory == '': print('Please run the create_data method before running this method!')
        self.file_name = file_name

        final_directory = os.path.join(self.current_directory, fr'{file_name}')
        if not os.path.exists(final_directory): os.makedirs(final_directory)

        # Create a folder that replicates the heirarchy of the directory
        for root, dir, _ in os.walk(self.directory):
            for i in range(len(dir)):
                new_current_directory = f'{self.current_directory}/{file_name}{root[len(self.directory):]}'
                final_directory = os.path.join(f'{self.current_directory}/{file_name}', fr'{new_current_directory}/{dir[i]}')
                if not os.path.exists(final_directory): os.makedirs(final_directory)
            
    def create_data(self, directory, include=''):
        
        '''
            directory: PLEASE USE A RELATIVE PATH FOR THE DIRECTORY

            Include: List of file types to ignore shuffling. i.e. -> [".png", ".jpeg", ".txt"]
        '''

        if include == '':
            print('PLEASE SPECIFY A FILETYPE TO INCLUDE')
            return

        # Used for later funtions
        self.directory = directory
        
        for root, _, files in os.walk(self.directory):

            file_length = len(files)
            
            # Weed out file types we don't want to modify
            for file in range(len(files)):
                if include not in files[file_length - file - 1]:
                    files.remove(files[file_length - file - 1])

            # Create an array containing the root and files within that root directory
            vector = [root, files]
            self.information.append(vector)

    def shuffle(self):

        '''
            Shuffles the files after you've created the folder copy AND data.

            Keeps the file names for any compatibility issues to not appear.
        '''

        if self.information == []:
            print('Please call the "creating_data" method before running this function!')
            return
        
        if self.file_name == '':
            print('Please call the "copy_folders" method before running this function!')
            return

        while True:
            
            # Weed out the directories with no files
            self.__remove_redundancies()
            
            if self.information == []: break

            # Pick 2 random choices from the directories and find their index's
            first  = random.choice(self.information)
            second = random.choice(self.information)

            first_index  = self.information.index(first)
            second_index = self.information.index(second)

            # Pick a value in the array and find their index's
            file1 = random.choice(first[1])
            file2 = random.choice(second[1])

            file_index1 = first[1].index(file1)
            file_index2 = second[1].index(file2)

            if (first_index == second_index) and (file_index1 == file_index2):

                # File stays where it is and isn't detected anymore
                self.information[first_index][1].remove(first[1][file_index1])
            
            else:
                if second_index == first_index:

                    # Same Directory, Different Filename
                    if file_index1 > file_index2:
                        self.information[first_index][1].remove(first[1][file_index1])
                        self.information[second_index][1].remove(second[1][file_index2])
                    else:
                        self.information[second_index][1].remove(second[1][file_index2])
                        self.information[first_index][1].remove(first[1][file_index1])
                else:
                    self.information[first_index][1].remove(first[1][file_index1])
                    self.information[second_index][1].remove(second[1][file_index2])
                
            self.__swap_files((first[0], file1), (second[0], file2))

        print("Swapping Done: KEEP IN MIND, YOUR NEW SHUFFLED FOLDER IS IN THIS DIRECTORY, AND NOT IN YOUR ORIGINAL FOLDER.")