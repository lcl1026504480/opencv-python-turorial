# -*- coding: utf-8 -*-
# @Author: lenovouser
# @Date:   2019-06-11 16:14:45
# @Last Modified by:   lenovouser
# @Last Modified time: 2019-06-11 16:14:45
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the data, converters convert the letter to a number
data= np.loadtxt('letter.data', dtype= 'float32', delimiter = ',',
                    converters= {0: lambda ch: ord(ch)})

#split the data to two, 10000 each for train and test
train, test = np.vsplit(data,2)

# split trainData and testData to features and responses
responses, trainData = np.hsplit(train,[1])
labels, testData = np.hsplit(test,[1])

# Initiate the kNN, classify, measure accuracy.
knn = cv2.ml.KNearest_create()
knn.train(trainData, cv2.ml.ROW_SAMPLE,responses)
ret, result, neighbours, dist = knn.findNearest(testData, k=5)

correct = np.count_nonzero(result == labels)
accuracy = correct*100.0/10000
print (accuracy)