import logging
import requests
import os
import threading


def download_gambar(url=None):
    if (url is None):
        return False
    ff = requests.get(url)
    tipe = dict()
    tipe['image/png']='png'
    tipe['image/jpg']='jpg'
    tipe['image/jpeg']='jpg'

    content_type = ff.headers['Content-Type']
    logging.warning(content_type)
    if (content_type in list(tipe.keys())):
        namafile = os.path.basename(url)
        ekstensi = tipe[content_type]
        logging.warning(f"writing {namafile}.{ekstensi}")
        fp = open(f"{namafile}.{ekstensi}","wb")
        fp.write(ff.content)
        fp.close()
    else:
        return False


threads = []
link = [
    'https://66.media.tumblr.com/ab577aacbce8fc33b13723faf48796b3/3b3a82872c0ea211-9d/s640x960/1bfd7601d25322df893c96e0ff9bb881c3930d02.jpg',
    'https://i.pinimg.com/564x/0f/34/9b/0f349b62865a7223104ecceff3a92de7.jpg',
    'https://i.pinimg.com/564x/04/b4/e8/04b4e8f964a7f886a0eaf3f219040d0d.jpg'
]
for i in range(3):
    t = threading.Thread(target=download_gambar,args=(link[i],))
    threads.append(t)
    
for thr in threads:
    thr.start()