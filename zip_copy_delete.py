#import filecmp
import os
import zipfile

#7/23/18 - need to make it easier to modify the script for different months?
#7/23/18 - 

def get_zipped_files(file_path):
	"""
	Constructs a dictionary with (fileName:fileSize) key:value pairs

	:param file_path: path to zipped folder in string format
	"""
	zf = zipfile.ZipFile(file_path)
	#zf: an object created from the zipped files
	#print(zf.infolist()[1:])

	zipped_files = {}

	for info in zf.infolist()[1:]:#info: the attributes of all the files in the zf objects
		zipped_files[info.filename] = info.file_size
		#print('\File Name\t', info.filename)
		#print( '\tUncompressed\t', info.file_size, 'bytes')

	#print(len(zipped_files))
	return zipped_files


def get_orig_files(file_path):
	"""
	Constructs a dictionary with (fileName:fileSize) key:value pairs

	:param file_path: path to original folder in string format
	"""
	orig_files = {}

	for file in os.listdir(file_path):
		#print(os.path.getsize(filePath1 + '\\' + file))
		orig_files[file] = os.path.getsize(file_path + '\\' + file)

	return orig_files
	#print(len(orig_files))

filePath1 = 'Z:\\syslog\\PIX-SF\\2018-05-01'
filePath2 = 'U:\\PIX-SF\\2018-05\\2018-05-01.zip'
print("ORIGINAL FILES")
print(get_orig_files(filePath1))
print("ZIPPED FILES")
print(get_zipped_files(filePath2))


#-------------------------------------------------------------------#
# filecmp method of comparing directories, not sure if it's capable #
# of comparing files from a zipped folder and a regular folder      #
#-------------------------------------------------------------------#

'''
d2_contents = [info.filename for info in zf.infolist()[1:]]
print("list contents:")
print(d2_contents)

d1_contents = os.listdir(filePath1)
print("list contents:")
print(d1_contents)

match, mismatch, errors = filecmp.cmpfiles(filePath1, filePath2, d2_contents,shallow = True)
print("matches:")
print(match)
print("mismatches:")
print(mismatch)
print("errors:")
print(errors)
'''