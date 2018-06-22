# coding: utf-8

import requests
from urllib.parse import urlencode
import os
from hashlib import md5
from multiprocessing.pool import Pool


def get_page(offset):
    # https://www.toutiao.com/search_content/
    # ?offset=60&format=json&keyword=%E8%A1%97%E6%8B%8D&autoload=true&count=20&cur_tab=1&from=search_tab
    params = {
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
        'from': 'search_tab',
    }
    url = 'https://www.toutiao.com/search_content/?' + urlencode(params)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print('ERROR:', e.args)


def get_images(json):
    data = json.get('data')
    if data:
        for item in data:
            title = item.get('title')
            image_list = item.get('image_list')
            print('image_list:', image_list)
            if image_list is not None:
                for image in image_list:
                    yield {
                        'image': image.get('url'),
                        'title': title,
                    }


def save_image(item):
    '''
    :param item: 根据title来创建文件夹，然后请求这个图片的链接获取图片
    '''
    if not os.path.exists(item.get('title')):
        os.mkdir(item.get('title'))
    try:
        local_image_url = item.get('image')
        # 把list替换为large后保存的图片尺寸更大
        new_image_url = local_image_url.replace('list', 'large')
        # new_image_url = local_image_url.replace('list', 'origin')
        response = requests.get('http:' + new_image_url)
        if response.status_code == 200:
            file_path = '{}/{}.{}'.format(item.get('title'), md5(response.content).hexdigest(), 'jpg')
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(response.content)
            else:
                print('Already Download', file_path)
    except requests.ConnectionError as e:
        print('Failed to Save image!')


def main(offset):
    json = get_page(offset)
    for item in get_images(json):
        print(item)
        save_image(item)


GROUP_START = 1
GROUP_END = 20


if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END+1)])
    pool.map(main, groups)
    pool.close()
    pool.join()
