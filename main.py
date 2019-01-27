import json
import os

list_json_file_name = ''#填入后缀为list.json的文件名
info_json_file_name = ''#填入后缀为info.json的文件名

with open('./'+list_json_file_name , 'rb') as load_file_list:
    with open('./'+info_json_file_name , 'rb') as load_file_info:
        load_dict_list = json.load(load_file_list)
        load_dict_info = json.load(load_file_info)
        files_path = str(load_dict_info['albumId'])
        title = (load_dict_info['title'])
        os.renames('./'+files_path,'./'+title)
        files_path = title
        for i in range(0 , len(load_dict_list)):
            obj = load_dict_list[i]
            file_name = str(obj['id'])
            rename = obj['title']
            os.renames('./'+files_path+'/'+file_name+'.m4a','./'+files_path+'/'+rename+'.m4a')
            
