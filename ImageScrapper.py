"""
Created on Mon 24 Feb 2020
@author: Naveen Kumar D B
"""

from bs4 import BeautifulSoup as bs
import os
import json

class ImageScrapper:
    def delete_existing_image(self,list_of_images):
        for self.image in list_of_images:
            try:
                os.remove("./static/"+self.image)
            except Exception as e:
                print('error in deleting: 'e)
        return 0

    def list_only_jpg_files(self,folder_name):
        self.list_of_jpg_files=[]
        self.list_of_files=os.listdir(folder_name)
        print('list of files =')
        print(self.list_of_files)
        for self.file in self.list_of_files:
            self.name_array=self.file.split('.')
            if (self.name_array[1]=='jpg'):
                self.list_of_jpg_files.append(self.file)
            else:
                print('filename does not end with jpg')
        return self.list_of_jpg_files

    def createURL(keyWord):
        keyWord = keyWord.split()
        keyWord = '+'.join(keyWord)
        url = "https://vahan.nic.in/nrservices/faces/user/searchstatus.xhtml"
        return url

    def get_RawHtml(url,header):
        
        return html



