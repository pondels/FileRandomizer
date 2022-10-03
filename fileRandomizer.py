import os
import random
import shutil

class RandomizeFiles():

    def __init__(self, directory):
        '''
            Directory: The directory to the file you want to randomize.
        '''
        self.directory = directory
        self.information = []
        self.file_name = ''
        self.current_directory = os.getcwd()

    def __remove_redundancies(self):

        length_of_info = len(self.information)

        for data in range(len(self.information)):
            if self.information[length_of_info - data - 1][1] == []:
                self.information.remove(self.information[length_of_info - data - 1])

    def __swap_files(self, first, second):

        '''
            First / Second: (directory, filename)
        '''

        dir1, fn1 = first
        dir2, fn2 = second

        if dir1 not in self.current_directory and dir2 not in self.current_directory:
            shutil.copyfile(f'{dir1}/{fn1}', f'{self.file_name}{dir2[len(self.directory):]}/{fn2}')
            shutil.copyfile(f'{dir2}/{fn2}', f'{self.file_name}{dir1[len(self.directory):]}/{fn1}')
    
    def __transfer(self, file):

        dir, fn = file
        shutil.copyfile(f'{dir}/{fn}', f'{self.file_name}{dir[len(self.directory):]}/{fn}')
    
    # ------------------------------------------------------------------------------#
    def list_file_types(self, directory=''):

        def find_types(directory):
            file_types = {'TOTAL': 0}

            for _, _, files in os.walk(directory):

                # Create an array containing the root and files within that root directory
                for file in files:
                    file_type = file.split('.')
                    if file_type[-1] not in file_types: file_types[file_type[-1]] = 1
                    else: file_types[file_type[-1]] += 1
                    file_types['TOTAL'] += 1
            return file_types

        if directory == '': file_types = find_types(self.directory)
        else: file_types = find_types(directory)

        return file_types
    
    def copy_folders(self, file_name):
        '''
            This should go without saying, but DO NOT call this method if your directory interacts
            with your working directory. You will infinitely make folders until you crash the program.
            Das a big no-no.

            If you want to avoid the above problem above, you can always copy the folder into your working directory
            to avoid replicating your directory itself, as demonstrated in example.py with exampleSkinFolder.

            ---

            Creates a folder in your working directory that copies
            all of the folders with the input directory without data.

            File_Name: The name of the file you want to copy

            Used later in the shuffle() method.
        '''

        self.file_name = file_name

        final_directory = os.path.join(self.current_directory, fr'{file_name}')
        if not os.path.exists(final_directory): os.makedirs(final_directory)

        # Create a folder that replicates the heirarchy of the directory
        for root, dir, _ in os.walk(self.directory):
            for i in range(len(dir)):
                new_current_directory = f'{self.current_directory}/{file_name}{root[len(self.directory):]}'
                final_directory = os.path.join(f'{self.current_directory}/{file_name}', fr'{new_current_directory}/{dir[i]}')
                if not os.path.exists(final_directory): os.makedirs(final_directory)
            
    def create_data(self, include=''):
        
        '''
            directory: PLEASE USE A RELATIVE PATH FOR THE DIRECTORY

            Include: List of file types to ignore shuffling. i.e. -> [".png", ".jpeg", ".txt"]
        '''

        if include == '':
            print('PLEASE SPECIFY A FILETYPE TO INCLUDE')
            return

        self.information = []
        
        for root, _, files in os.walk(self.directory):

            file_length = len(files)
            
            # Weed out file types we don't want to modify
            for file in range(len(files)):
                if include not in files[file_length - file - 1]:
                    files.remove(files[file_length - file - 1])

            # Create an array containing the root and files within that root directory
            vector = [root, files]
            self.information.append(vector)

    def full_swap(self):

        '''
            Takes 2 random files and swaps them.
            This happens until all files have been swapped and randomized

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
                self.__transfer((first[0], file1))

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

    def transfer_file_types(self, file_type):
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

            # Pick a random choice from the directories and find its index
            choice  = random.choice(self.information)
            first_index  = self.information.index(choice)

            # Pick a value in the array and find its index
            file = random.choice(choice[1])
            file_index = choice[1].index(file)
            self.information[first_index][1].remove(choice[1][file_index])
                
            self.__transfer((choice[0], file))

    def help(self):
        '''
            A method to understand the methods of RandomizeFiles()
        '''

        print('Hello! You are probably trying to get help using this class.\nNo worries! Since I have no documentation, '
        'I\'m going to place it in the program itself, so listen carefully!'
        '\n\nThere are a few methods that you need to be aware of, as well as some variables that you may not know the syntax of.'
        '\n\nThe first place to go is simply hover over the method and it will tell you a general basis of what that function does.'
        '\n\nAs for variables, there are a few that you need to be wary of how you call them.'
        '\n     - __init__            -> directory: The absolute path from your root drive to the desired folder you wish to randomize its contents.'
        '\n     - copy_folders        -> file_name: The name of the copied folder you wish to be labeled as.'
        '\n     - create_data         -> include:   Used to obtain information of the files of the given type. Only can use one type at a time.'
        '\n     - transfer_file_types -> file_type: Similar to include, but used to just transfer over files of the given type.'
        '\n\nMethods to Use:'
        '\n     - list_file_types:     Lists all the file types and how many of the type were found in the directory.'
        '\n     - copy_folders:        Creates a copy of the folder hierarchy in your working directory.'
        '\n     - create_data:         Creates an array of information to be used to randomize the data.'
        '\n     - full_swap:           Takes 2 files from the directory, swaps them, keeps the original names, and continues til finished.'
        '\n     - true_random:         A different method of "random" than full_swap. (Not yet implemented)'
        '\n     - transfer_file_types: Transfers file types that you don\'t want randomized, but easily transferred.')

    # TODO
    '''
        Other forms of randomizing files
            - Single file replacement
            - Categorizing. i.e., Backgrounds with background, tilesets with tilesets, etc..
    '''