#!/usr/bin/python env
# -*- coding: utf-8 -*-

"""
Description:
"""

from __future__ import absolute_import

from Davinci.utils import log

import tushare as ts
import pandas as ps

import time
import os
import datetime

__author__ = "joshliu"

_base_path = '/Users/joshualiu/dev/data/tushare/'
_tushare_todo_database_path = _base_path + str('tushare_todo1.json')
_tushare_done_database_path = _base_path + str('tushare_done1.json')
_tushare_database_name = 'tushare_database1'
_tushare_database_path = _base_path + _tushare_database_name
_tushare_database_list = _base_path + str('tushare_database_list1')
_encoding = 'utf-8'
_batch_num = 8000
_log = log.get_logger('root')


def init_tushare_database():
	with open(_tushare_database_list, mode='w+', encoding=_encoding) as fd:
		database_list = fd.read()
		if database_list.find(_tushare_database_path) < 0:
			database_list += _tushare_database_path + '\n'
			fd.write(database_list)

	if not os.path.exists(_tushare_todo_database_path):
		data = {'classify':[''], 'time':[''], 'url':[''], 'title':['']}
		placeholder = ps.DataFrame(data=data, columns=['classify', 'time', 'url', 'title'])
		with open(_tushare_todo_database_path, mode='w+', encoding=_encoding) as fd:
			placeholder.to_json(fd)


def request_tushare_database(when=None):
	df = ps.read_json(_tushare_todo_database_path, 'columns', encoding=_encoding)
	if when is not None:
		date = datetime.date(when.year, when.month, 1) if isinstance(when, datetime.date) else None
		#In order to support pulling at months, get_latest_news api has to be extended to date input.
		new_df = ts.get_latest_news(top=_batch_num, show_content=False, date=date.isoformat())
		for i in range(2, 31):
			try:
				new_df = new_df.append(ts.get_latest_news(top=_batch_num, show_content=False, date=date.replace(day=i).isoformat()))
			except Exception:
				continue
			_log.info('Fetch %d month'%(i))
			time.sleep(1)
	else:
		new_df = ts.get_latest_news(top=_batch_num, date='')
	new_df = new_df.drop_duplicates(subset='url', keep='first')
	new_df.index = range(1, len(new_df) + 1)
	done_df = ps.read_json(_tushare_done_database_path, 'columns', encoding=_encoding)
	_log.info('Old item: %d' % (len(df)))

	dup_df = new_df.append(done_df)
	dup_df = dup_df[dup_df.duplicated(subset='url', keep=False)].drop_duplicates(subset='url', keep='first')
	singular_df = ~new_df.isin(dup_df).all(1)
	singular_df = new_df[singular_df]
	_log.info('New item: %d' % (len(singular_df)))

	if len(singular_df) == 0:
		return

	merged_df = singular_df.merge(df, 'outer', on=['classify', 'time', 'url', 'title']).drop_duplicates(subset='url', keep='first')
	merged_df.index = range(1, len(merged_df) + 1)
	_log.info('Fetch entry: %d' % (len(merged_df)))

	with open(_tushare_todo_database_path, mode='w+', encoding=_encoding) as fd:
		merged_df.to_json(fd, force_ascii=False)


def pull_tushare_database():
	todo_df = ps.read_json(_tushare_todo_database_path, 'columns', encoding=_encoding)
	batch_num = _batch_num if len(todo_df) > _batch_num else len(todo_df)

	if len(todo_df) == 0:
		return

	# rows = df.head(_batch_num)
	contents = ''
	records = ps.DataFrame.from_dict(todo_df.head(batch_num))
	# records = ps.DataFrame.from_dict(todo_df.head(1))
	# records = records.drop(todo_df.index[0])
	for i in range(batch_num):
		# row = todo_df.head() #todo_df.loc[i, :]
		row = records.iloc[i, :]
		content = ts.latest_content(row['url'])
		if content is not None:
			contents += content.replace('\\n', '').replace('\n', '') + '\n'
		else:
			contents += '\n'
			_log.info('Empty content url:%s title:%s ' % (row['url'], row['title']))

		if i%100 == 0:
			_log.info('Processed %d items.' % i)
		# records = records.append(row, ignore_index=False)

	done_df = ps.read_json(_tushare_done_database_path, 'columns', encoding=_encoding)
	_log.info('Done size: %d doing size: %d' % (len(done_df), len(records)))
	done_df = done_df.append(records)

	todo_len = len(todo_df)
	todo_df = todo_df[~(todo_df.isin(records)).all(1)]
	_log.info('Origin todo size: %d now: %d' % (todo_len, len(todo_df)))

	done_df.index = range(1, len(done_df) + 1)

	with open(_tushare_done_database_path, mode='w+', encoding=_encoding) as fd:
		done_df.to_json(fd, force_ascii=False)

	with open(_tushare_database_path, mode='a+', encoding=_encoding) as fd:
		fd.write(contents)

	with open(_tushare_todo_database_path, mode='w+', encoding=_encoding) as fd:
		todo_df.to_json(fd, force_ascii=False)


if __name__ == '__main__':
	print(ts.__version__)
	init_tushare_database()
	request_tushare_database()
	pull_tushare_database()
