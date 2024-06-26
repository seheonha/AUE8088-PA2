import numpy as np
from sklearn.model_selection import train_test_split
# 데이터를 불러옵니다.
ang = 0
ang1 = 0
ang2 = 0 
with open('validation_0.2.txt', 'r') as f:
    datas = f.readlines()

with open('kaist_ano_test.txt', 'w') as fk:
    fk.write("\"images\": [\n")
    for data in datas:
        data = data.strip()
        data = data[36:53]
        eng1 = data[:5]
        eng2 = data[6:10]
        eng3 = data[11:]
        #print("{\n\"id\": "+str(ang)+",\n\"im_name\": \""+data+"\",\n\"height\": 512,\n"+"\"width\": 640\n},")
        fk.write("{\n    \"id\": "+str(ang)+",\n    \"im_name\": \""+eng1+"/"+eng2+"/"+eng3+"\",\n    \"height\": 512,\n"+"    \"width\": 640\n},\n")
        ang = ang + 1
    fk.write("],\n\"annotations\": [")
    for data in datas:
        data = data.strip()
        data = data[36:53]
        with open('./datasets/kaist-rgbt/train/labels/'+data+'.txt', 'r') as f:
            ongs = f.readlines()
            for ong in ongs:
                if ong == "[]":
                    pass
                else:
                    ong = ong.strip()
                    #print(ong)
                    list_ong = ong.split(" ")
                    #print(list_ong[0])
                    print("{\n    \"id\": "+str(ang2)+",\n    \"image_id\": "+str(ang1)+",\n    \"category_id\": "+list_ong[0]+",\n"+"    \"bbox\": [\n        "+str(float(list_ong[1])*640)[:-2]+",\n        "+str(float(list_ong[2])*512)[:-2]+",\n        "+str(float(list_ong[3])*640)[:-2]+",\n        "+str(float(list_ong[4])*512)[:-2]+"\n    ],\n    \"height\": "+str(float(list_ong[4])*512)[:-2]+",\n    \"occlusion\": "+list_ong[5]+",\n    \"ignore\": 0\n},")
                    #fk.write("{\n    \"id\": "+str(ang2)+",\n    \"image_id\": "+str(ang1)+",\n    \"category_id\": "+list_ong[0]+",\n"+"    \"bbox\": [\n        "+str(int(float(list_ong[1])*640))+",\n        "+str(int(float(list_ong[2])*512))+",\n        "+str(int(float(list_ong[3])*640))+",\n        "+str(int(float(list_ong[4])*512))+"\n    ],\n    \"height\": "+str(int(float(list_ong[4])*512))+",\n    \"occlusion\": "+list_ong[5]+",\n    \"ignore\": 0\n},\n")
                    fk.write("{\n    \"id\": "+str(ang2)+",\n    \"image_id\": "+str(ang1)+",\n    \"category_id\": "+list_ong[5]+",\n"+"    \"bbox\": [\n        "+str(int(float(list_ong[1])*640))+",\n        "+str(int(float(list_ong[2])*512))+",\n        "+str(int(float(list_ong[3])*640))+",\n        "+str(int(float(list_ong[4])*512))+"\n    ],\n    \"height\": "+str(int(float(list_ong[4])*512))+",\n    \"occlusion\": "+list_ong[0]+",\n    \"ignore\": 0\n},\n")
                    ang2 = ang2 + 1
        ang1 = ang1 + 1

'''
with open('kaist_ano1.txt', 'r') as f:
    for item in datas:
        data1 = data1.strip()
        f.write("{\n" % item)

with open('kaist_ano2.txt', 'r') as f:
    for item in datas:
        f.write("%s" % item)
#data
'''