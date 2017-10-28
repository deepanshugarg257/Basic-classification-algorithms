#!/usr/bin/env python

import sys
import os
import numpy as np
import random

if __name__ == '__main__':

	train_X = np.genfromtxt(sys.argv[1], delimiter = ',', dtype = int)
	train_Y = np.array(train_X[:, 0])
	train_X[:, 0] = 1
	# print train_X[0, :]
	for i in xrange(0, len(train_X)):
		train_X[i] *= (2*train_Y[i]-1)

	test_X = np.genfromtxt(sys.argv[2], delimiter = ',', dtype = int)
	test_X = np.append(np.ones((len(test_X), 1), int), test_X, 1)
	test_X[:, 0] = 1

	# print test_X[0]
	# exit()
	###################### PART-A ##########################
	# print "part A"
	W = np.zeros(len(train_X[0]), int)
	for T in xrange(1, 500):
		fl = 0
		for i in xrange(0, len(train_Y)):
			x = train_X[i]
			s = np.dot(x, W)
			if s <= 0:
				W = np.add(W, x)
				fl = 1
		if fl == 0:
			break

	for i in xrange(0, len(test_X)):
		x = test_X[i]
		s = np.dot(x, W)
		if s < 0:
			print 0
		elif s > 0:
			print 1
		else:
			print random.randint(0,1)

	###################### PART-B #########################
	# print "part B"
	W = np.zeros(len(train_X[0]), int)
	b = 1000000000
	for T in xrange(1, 500):
		fl = 0
		# print("epoch: ", T)
		for i in xrange(0, len(train_Y)):
			x = train_X[i]
			s = np.dot(x, W)
			if s <= b:
				fl = 1
				Wn = np.add(W, x)
				W = Wn
		if fl == 0:
			break

	# print "predicting"
	for i in xrange(0, len(test_X)):
		x = test_X[i]
		s = np.dot(x, W)
		if s < 0:
			print 0
		elif s > 0:
			print 1
		else:
			print random.randint(0,1)

	###################### PART-C ##########################
	# print "part C"
	W = np.zeros(len(train_X[0]), int)
	fl = 0
	for T in xrange(1, 500):
		fl = 0
		Wn = np.zeros(len(train_X[0]), int)
		for i in xrange(0, len(train_Y)):
			x = train_X[i]
			s = np.dot(x, W)
			if s <= 0:
				fl = 1
				Wn = np.add(Wn, x)
		W = np.add(W, Wn)
		if fl == 0:
			break

	# print "predicting"
	for i in xrange(0, len(test_X)):
		x = test_X[i]
		s = np.dot(x, W)
		if s < 0:
			print 0
		elif s > 0:
			print 1
		else:
			print random.randint(0,1)

	###################### PART-D ##########################
	# print "part D"
	W = np.zeros(len(train_X[0]), int)
	fl = 0
	b = 10000000
	for T in xrange(1, 500):
		fl = 0
		Wn = np.zeros(len(train_X[0]), int)
		for i in xrange(0, len(train_Y)):
			x = train_X[i]
			s = np.dot(x, W)
			if s <= b:
				fl = 1
				Wn = np.add(Wn, x)
		W = np.add(W, Wn)
		if fl == 0:
			break

	# print "predicting"
	for i in xrange(0, len(test_X)):
		x = test_X[i]
		s = np.dot(x, W)
		if s < 0:
			print 0
		elif s > 0:
			print 1
		else:
			print random.randint(0,1)