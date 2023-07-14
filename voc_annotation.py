import xml.etree.ElementTree as ET
from os import getcwd

xmlfilepath=r'D:/Carla-Object-Detection-Dataset/labels/test'
saveBasePath=r"D:/Carla-Object-Detection-Dataset/image_sets/testing"

sets_test=[('2007', 'test')]
sets_train=[('2007', 'train')]


wd = getcwd()
classes = ["aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]

def convert_annotation(image_id, list_file):
    in_file = open('D:/Carla-Object-Detection-Dataset/labels/train/%s.xml'%(image_id))
    tree=ET.parse(in_file)
    root = tree.getroot()
    list_file.write('D:/Carla-Object-Detection-Dataset/images/train/%s.jpg'%(image_id))
    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult)==1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text), int(xmlbox.find('ymax').text))
        list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))

    list_file.write('\n')

for year, image_set in sets_train:
    image_ids = open('D:/Carla-Object-Detection-Dataset/image_sets/training/%s.txt'%(image_set)).read().strip().split()
    list_file = open('%s_%s.txt'%(year, image_set), 'w')
    for image_id in image_ids:
        convert_annotation(image_id, list_file)
    list_file.close()
