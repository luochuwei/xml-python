#-*- coding:utf-8 -*-
####################################################
#
#    Author: Chuwei Luo
#    Email: luochuwei@gmail.com
#    Date: 07/03/2016
#    Usage: movie_dic_xml
#
####################################################

import cPickle
from xml.etree import ElementTree as ET

per = ET.parse(r'E:\Learning\DATA\conversation_dataset\MovieDiC_V2\MovieDiC_V2\MovieDiC_V2.xml')
# per = ET.parse(r't2.xml')
p = per.findall('./movie/dialogue')

# f1 = open(r'post.txt', 'w')
# f2 = open(r'response.txt', 'w')



dialogue = {}

last_speaker = ""

for num, oneper in enumerate(p):
    speaker = []
    utterance = []
    for child in oneper.getchildren():
        # print child.tag,':',child.text
        if child.tag == "speaker":
            speaker.append(child.text)
        if child.tag == 'utterance':
            utterance.append(child.text)
    assert len(speaker) == len(utterance)

    d = []
    for s, u in zip(speaker, utterance):
        d.append([s,u])

    dialogue[num] = d


train_pair = {}
n = 0

for i in dialogue:
    p = []
    for j in dialogue[i]:
        if len(p) == 2:
            if j[0] != last_speaker:
                train_pair[n] = p
                p = []
                n+=1
        if j[0] != last_speaker:
            p.append(j[1])
            last_speaker = j[0]
        else:
            p[-1] += ' '
            p[-1] += j[1]

    if len(p) == 1:
        p = [train_pair[n-1][-1], p[0]]
        train_pair[n] = p
        n += 1
    last_speaker = ''
    assert len(p) == 2
    train_pair[n] = p
    n += 1


cPickle.dump(train_pair, open(r'movie_pair.pkl', 'wb'))