#!/usr/bin/env python

import sys
import os
import random
import numpy as np

class FeatureVector(object):
	def __init__(self,vocabsize,numdata):
		self.vocabsize = vocabsize
		self.X =  np.zeros((numdata,self.vocabsize), dtype=float)
		self.Y =  np.zeros((numdata,), dtype=int)

	def make_featurevector(self, inputdir, vocab, classes):
		x = 0
		nocl = len(classes)
		classid = 0
		for c in classes:
			listing = os.listdir(inputdir+c)
			for filename in listing:
				f = open(inputdir+c+filename,'r')
				lines = f.readlines()
				tot = 0
				for line in lines :
					line = line.strip("\n")
					line = line.replace("<s>", "")
					line = line.replace("<\s>", "")
					line = line.split()
					tot += len(line)
					for word in line:
						if word in vocab:
							self.X[x][vocab[word]] += 1.0
				if tot > 0:
					self.X[x] = (1000.0*self.X[x])/float(tot)
				self.Y[x] = classid
				x += 1
			classid += 1

def shift_list(lis, i):
	for x in xrange(len(lis)-1, i, -1):
		lis[x] = lis[x-1]

def find_dis(a, b):
	return np.sum(abs(np.array(a) - np.array(b)))

class KNN(object):
	def __init__(self,trainVec,testVec):
		self.X_train = trainVec.X
		self.Y_train = trainVec.Y
		self.X_test = testVec.X
		self.Y_test = np.zeros((len(testVec.Y),), dtype = np.int)
		self.asli = testVec.Y

	def classify(self, k=1):
		a = [[100000000000.0, -1] for blah in xrange(0, k)]
		for x in xrange(0, len(self.X_test)):
			a = [[100000000000.0, -1] for blah in xrange(0,k)]
			for xt in xrange(0, len(self.X_train)):
				dis = find_dis(self.X_test[x], self.X_train[xt])
				for i in xrange(0, len(a)):
					if (dis <= a[i][0]):
						shift_list(a, i)
						a[i] = [dis, self.Y_train[xt]]
						break
			maxc = 0
			coun = dict()
			cl = -1
			for i in xrange(0, k) :
				if a[i][1] in coun:
					coun[a[i][1]] += 1
				else:
					coun[a[i][1]] = 1
				if (coun[a[i][1]] > maxc):
					maxc = coun[a[i][1]]
					cl = a[i][1]
			print classes[cl].strip("/")
			self.Y_test[x] = cl

if __name__ == '__main__':
	classes = ['galsworthy/','galsworthy_2/','mill/','shelley/','thackerey/','thackerey_2/','wordsmith_prose/','cia/','johnfranklinjameson/','diplomaticcorr/']

	vocab = dict()
	trainsz = 0
	testsz = 0

	inpsi = 0

	traindir = sys.argv[1]
	testdir = sys.argv[2]
	classid = 1
	for c in classes:
		listing = os.listdir(traindir+c)
		for filename in listing:
			f = open(traindir+c+filename,'r')
			lines = f.readlines()
			trainsz+=1
			for line in lines :
				line = line.strip("\n")
				line = line.replace("<s>", "")
				line = line.replace("<\s>", "")
				line = line.split()
				for word in line:
					if word not in vocab:
						vocab[word] = len(vocab)
	trainVec = FeatureVector(len(vocab), trainsz)
	trainVec.make_featurevector(traindir, vocab, classes)

	for c in classes:
		listing = os.listdir(testdir+c)
		testsz += len(listing)

	testVec = FeatureVector(len(vocab), testsz)
	testVec.make_featurevector(testdir, vocab, classes)

	knn = KNN(trainVec,testVec)
	knn.classify(4)