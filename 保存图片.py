import os
import urllib.request

image_url = 'http://img.jingtuitui.com/759fa20190115144450401.jpg'
file_path = './public/'

try:
    if not os.path.exists(file_path):
        os.makedirs(file_path) #如果没有这个path则直接创建
    file_suffix = os.path.splitext(image_url)[1]
    print(file_suffix)
    filename = '{}{}'.format(file_path, file_suffix)
    print(filename)
    urllib.request.urlretrieve(image_url, filename=filename)
    print("保存成功")

except IOError as e:
    print(e)

except Exception as e:
    print(e)