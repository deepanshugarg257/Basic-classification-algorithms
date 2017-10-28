#!/usr/bin/env python

import sys
import os
import numpy as np

"""Feel free to add any extra classes/functions etc as and when needed.
This code is provided purely as a starting point to give you a fair idea
of how to go about implementing machine learning algorithms in general as
a part of the first assignment. Understand the code well"""

classes = ['galsworthy/','galsworthy_2/','mill/','shelley/','thackerey/','thackerey_2/','wordsmith_prose/','cia/','johnfranklinjameson/','diplomaticcorr/']

class FeatureVector(object):
	def __init__(self,vocabsize,numdata):
		self.vocabsize = vocabsize
		self.X =  np.zeros((numdata,self.vocabsize), dtype=np.int)
		self.Y =  np.zeros((numdata,), dtype=np.int)

	def make_featurevector(self, input, classid):
		pass

class KNN(object):
	def __init__(self,trainVec,testVec):
		self.X_train = trainVec.X
		self.Y_train = trainVec.Y
		self.X_test = testVec.X
		self.Y_test = testVec.Y
		self.metric = Metrics('accuracy')

	def classify(self, nn=1):
		for i in range(self.Y_test.shape[0]):
			Y_pred = classes[np.random.randint(0,10)]
			print(Y_pred.strip('/'))

class Metrics(object):
	def __init__(self,metric):
		self.metric = metric

	def score(self):
		if self.metric == 'accuracy':
			return self.accuracy()
		elif self.metric == 'f1':
			return self.f1_score()

	def get_confmatrix(self,y_pred,y_test):
		"""
		Implements a confusion matrix
		"""

	def accuracy(self):
		"""
		Implements the accuracy function
		"""

	def f1_score(self):
		"""
		Implements the f1-score function
		"""

if __name__ == '__main__':
	traindir = sys.argv[1]
	testdir = sys.argv[2]
	inputdir = [traindir,testdir]

	vocab = 30000 #Random Value
	trainsz = 1000 #Random Value
	testsz = 500 #Random Value

	# print('Making the feature vectors.')
	trainVec = FeatureVector(vocab,trainsz)
	testVec = FeatureVector(vocab,testsz)

	for idir in inputdir:
		classid = 1
		for c in classes:
			listing = os.listdir(idir+c)
			for filename in listing:
				f = open(idir+c+filename,'r')
				inputs = "Test"
				classid = 0
				#Insert code here
				if idir == traindir:
					trainVec.make_featurevector(inputs,classid)
				else:
					testVec.make_featurevector(inputs,classid)
			classid += 1

	# print('Finished making features.')
	# print('Statistics ->')
	# print(trainVec.X.shape,trainVec.Y.shape,testVec.X.shape,testVec.Y.shape)

	knn = KNN(trainVec,testVec)
	knn.classify()
