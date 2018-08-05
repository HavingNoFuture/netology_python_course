import glob
import os.path
import json
import chardet
import codecs
import operator
from pprint import pprint

def predict_encoding(file_path, n_lines=20):
    with open(file_path, 'rb') as f:
        rawdata = b''.join([f.readline() for _ in range(n_lines)])
    return chardet.detect(rawdata)['encoding']

def length_check(word, words):
	if len(word) >= 6:
		if word.lower() not in words.keys():
			words[word.lower()] = 1
		else:
			words[word.lower()] += 1

SOURCE_PATH = r"E:\Python_course\PY1_Lesson_2.3"
files_list = glob.glob(os.path.join(SOURCE_PATH , "*.json"))

words = dict()
for file in files_list:
	encod = predict_encoding(file)
	with codecs.open(file, 'r', encoding=encod, errors='ignore') as f:
		data = json.loads(f.read())
		for paragraph in data["rss"]["channel"]["items"]:
			words_list = paragraph["description"].split(" ")
			for word in words_list:
				length_check(word, words)


sorted_words = sorted(words.items(), key=operator.itemgetter(1))
sorted_words.reverse()
pprint(sorted_words[:10])




