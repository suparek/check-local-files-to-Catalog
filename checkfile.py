# -*- coding:utf-8 -*-
import os
import sqlite3

def search_file(path,file_type):  
        queue = []
        queue.append(path);
        fpath=[]
        tmpid = 2
        while len(queue) > 0:  
            tmp = queue.pop(0)  
            if(os.path.isdir(tmp)):  
                for item in os.listdir(tmp):  
                    queue.append(os.path.join(tmp, item))  
            elif(os.path.isfile(tmp)):
                tmpid = tmpid + 1
                name = os.path.basename(tmp)#获取文件名
                dirname = os.path.dirname(tmp)#获取文件目录
                full_path = os.path.join(dirname,name)#将文件名与文件目录连接起来，形成完整路径
                creatime = os.path.getctime(tmp)#获取文件创建时间
                modifytime = os.path.getmtime(tmp)#获取文件修改时间
                size = os.path.getsize(tmp)#获取文件大小
                putinsql(tmpid,name,full_path,creatime,modifytime,size)
                abspath = os.path.abspath(tmp);
                if name[-1*len(file_type):] == file_type:
                       fpath.append(name+' + '+full_path)
        print fpath

def putinsql(id,name,route,maketime,modifytime,space):
    cx = sqlite3.connect("E:\\xiaoming_assist\\db.sqlite3")
    cu = cx.cursor()
    cu.execute("insert into takefiles_file_message(id, Files_name, Files_route, Files_maketime, Files_modifytime, Files_space)values(%d,'%s','%s',%d,%d,%d)"%(id, name, route, maketime, modifytime, space)) 
    cx.commit()
    

def search_real():
    path1='E:\\hmictrl'
    file_type1=''
    search_file(path1,file_type1)


if __name__ == '__main__':
    search_real()
