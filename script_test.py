#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import re
import nltk
import pymorphy2
pd.set_option('display.max_colwidth', 0)
nltk.download('punkt')

if __name__ == "__main__":



	df = pd.read_csv('test_data - test_data.csv')
	df_copy = df.copy()
	pr = r'привет|здрав|доброе|добрый'
	df_copy.loc[df_copy['role']=='manager', 'hello'] = df_copy['text'].apply(lambda x: True if re.findall(pr, x.lower()) else False)
	print('Реплики где менеджер поздоровался')
	for i in df_copy.loc[df_copy['hello']==True,'text']:
		print(i)

	dfToList = df_copy['text'].tolist()
	row =''
	for i in dfToList:
		row += i + ' '
	list_name=[]
	prob_thresh = 0.4

	morph = pymorphy2.MorphAnalyzer()

	text =  row

	for word in nltk.word_tokenize(text):
		for p in morph.parse(word):
			if 'Name' in p.tag and p.score >= prob_thresh:
				if word not in list_name:
					list_name.append(word)
	name_men = r'ангелина|денис|дмитрий|максим|анастасия|дима|вячеслав'
	df_copy.loc[df_copy['role']=='manager','name'] = df_copy['text'].apply(lambda x: True if re.findall(name_men, x.lower()) else False)
	print()
	print('Реплики где менеджер представил себя')
	for i in df_copy.loc[df_copy['name']==True,'text']:
		print(i)
	print()
	print('Имена менеджеров')
	for i in list_name:
		print (i)
	(re.findall('компания[A-zА-я- ]+', ', '.join(dfToList)))
	#Список компаний маленький, из-за этого просто выбрал названия компаний
	print()
	print('Список компаний')
	list_company = r'диджитал бизнес|китобизнес'
	print()
	print('диджитал бизнес', 'китобизнес')
	df_copy.loc[df_copy['role']=='manager','company'] = df_copy['text'].apply(lambda x: True if re.findall(list_company, x.lower()) else False)
	bye = r'до свидан|пока|довстреч|до скорых|доброго'
	df_copy.loc[df_copy['role']=='manager','bye'] = df_copy['text'].apply(lambda x: True if re.findall(bye, x.lower()) else False)
	print()
	print('Реплики где менеджер попрощался')
	for i in df_copy.loc[df_copy['bye']==True,'text']:
	    print(i)
	df_copy = df_copy.fillna(False)
	print()
	print('Проверяем наличие менеджеров которые здоровались и прощались') 
	print(df_copy.loc[(df_copy['role']=='manager') & (df_copy['hello'] ==True) & (df_copy['bye'] ==True)].count()['dlg_id'])
