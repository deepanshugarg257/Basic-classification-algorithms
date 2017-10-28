#!/usr/bin/env python
import sys
import os
import random
import numpy as np

if __name__ == '__main__':
	train_X = np.genfromtxt(sys.argv[1], delimiter = ',', dtype = int)
	train_X[:, 0] = 1
	train_Y = train_X[:, -1]
	train_X = np.delete(train_X, -1, 1)
	for i in xrange(0, len(train_X)):
		train_X[i] *= (train_Y[i]-3)
	train_Y = train_Y-3
	b = 10
	W = np.zeros(len(train_X[0]), dtype=float)
	for T in xrange(1, 1000):
		# print "epoch: ", T
		for i in xrange(0, len(train_X)):
			x = train_X[i]
			s = np.dot(x, W)
			if s <= b:
				W = np.subtract(W, 0.01*x*(s-b)/np.dot(x, x) ) 

	test_X = np.genfromtxt(sys.argv[2], delimiter = ',', dtype = int)
	test_X[:, 0] = 1
	# train_X = np.delete(train_X, -1, 1)
	for i in xrange(0, len(test_X)):
		x = np.array(test_X[i]).reshape((1, len(test_X[i])))
		s = np.dot(x, W)
		if s<0 :
			print 2
		elif s > 0 :
			print 4
		else:
			print 2*random.randint(1,2)

	eta = 1.00
	trainl = len(train_X)
	b = 100
	W = np.zeros(len(train_X[0]), int)
	for T in xrange(1, 500):
		for i in xrange(0, len(train_X)):
			s = np.dot(train_X[i], W)
			if s <= b:
				W = np.add(W, eta*train_X[i])
		w = 0
		for i in xrange(1, trainl):
			s = np.dot(train_X[i], W)
			if s<=0:
				w+=1
		eta = eta*(float(w)/trainl)

	for i in xrange(0, len(test_X)):
		x = np.array(test_X[i]).reshape((1, len(test_X[i])))
		s = np.dot(x, W)
		if s<0 :
			print 2
		elif s > 0 :
			print 4
		else:
			print 2*random.randint(1,2)