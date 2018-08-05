import subprocess
import os

prog_name = 'convert.exe'
PROG_PATH = (os.path.abspath(prog_name))

PROJECT_PATH = os.path.split(PROG_PATH)[0]
SOURCE_PATH = os.path.join(PROJECT_PATH, "Source")
files_list = os.listdir(SOURCE_PATH)


try:
	os.mkdir("Result")
except OSError:
	os.chdir("Result")

RESULT_PATH = os.path.join(PROJECT_PATH, "Result")
print(RESULT_PATH)

for file in files_list:
	subprocess.Popen(f"{PROG_PATH} {os.path.join(SOURCE_PATH, file)} -resize 200 {os.path.join(RESULT_PATH, file)}")
	

