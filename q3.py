#!/usr/bin/env python

from __future__ import division
import sys
import os
import numpy as np

def check_qual(lefc, lefo, rigc, rigo):
	qual = 0.00
	lefo = float(lefo)
	lefc = float(lefc)
	rigc = float(rigc)
	rigo = float(rigo)

	if lefc <= 0.5 or rigc <= 0.5:
		return 10000.0
	if lefo >= 0.5 and lefc-lefo >= 0.5:
			qual+= -1 * (lefc/(lefc+rigc)) * (((lefo/lefc)*np.log2(lefo/lefc)) + (((lefc-lefo)/lefc)*np.log2((lefc-lefo)/lefc)) )

	if rigo >= 0.5 and rigc-rigo >= 0.5:
			qual+= -1 * (rigc/(lefc+rigc)) * (((rigo/rigc)*np.log2(rigo/rigc)) + (((rigc-rigo)/rigc)*np.log2((rigc-rigo)/rigc)) )
	return qual

disc = [0 for x in xrange(0,9)]
count = 0

class node:
	def __init__(self, pos_val, data_set, Y, prev_qual):
		self.feat = -1
		self.left = None
		self.right = None
		self.mid = -1.0
		self.isLeaf = 0
		self.label = -1
		self.split(pos_val, data_set, Y, prev_qual)

	def split(self, pos_val, data_set, Y, prev_qual):
		global count
		global disc
		count += 1
		lefc = rigc = lefo = rigo = 0
		mi = 10000
		
		for f in xrange(0,9):
			lefc = rigc = 0
			if float(pos_val[f][1] - pos_val[f][0]) < 0.00001:
				continue
			x = pos_val[f][0]
			while x < pos_val[f][1]:
				lefc = rigc = lefo = rigo = 0
				for i in xrange(0, len(data_set)):
					if data_set[i][f] <= x:
						lefc += 1
						if Y[i] == 1:
							lefo += 1
					else:
						rigc += 1
						if Y[i] == 1:
							rigo += 1

				qual = 100000
				if lefc>0 and rigc>0:
					qual = check_qual(lefc, lefo, rigc, rigo)
				if qual < mi:
					mi = qual
					self.feat = f
					self.mid = x

				if disc[f] == 0:
					x += float((pos_val[f][1] - pos_val[f][0])/100)
				else:
					x += 1

		lef_ds = []
		rig_ds = []
		lef_Y = []
		rig_Y = []

		if self.feat<0 or lefc == 0 or rigc == 0 or len(data_set) <= 5:
			self.isLeaf = 1
			oc = 0
			zc = 0
			for i in xrange(0, len(Y)):
				if Y[i] == 0:
					zc+=1
				else:
					oc+=1
			if zc > oc:
				self.label = 0
			else:
				self.label = 1
		else :
			for i in xrange(0, len(data_set)):
				if data_set[i][self.feat] <= self.mid:
					lef_ds.append(data_set[i])
					lef_Y.append(Y[i])
				else:
					rig_ds.append(data_set[i])
					rig_Y.append(Y[i])
			lef_pos_val = []
			rig_pos_val = []
			for i in xrange(0,9):
				if i != self.feat:
					lef_pos_val.append(pos_val[i])
					rig_pos_val.append(pos_val[i])
				else :
					lef_pos_val.append([pos_val[i][0], self.mid])
					if disc[i] == 1:
						rig_pos_val.append([self.mid + 1, pos_val[i][1]])
					else:
						rig_pos_val.append([self.mid + ( (pos_val[i][1] - pos_val[i][0]) / 100.0), pos_val[i][1]])
			self.left = node(lef_pos_val, lef_ds, lef_Y, mi)
			self.right = node(rig_pos_val, rig_ds, rig_Y, mi)

	def pred(self, data_point):
		if self.isLeaf == 1:
			return self.label

		if data_point[self.feat] <= self.mid:
			return self.left.pred(data_point)
		else:
			return self.right.pred(data_point)


def main():
	f = open(sys.argv[1],'r')
	al = f.readlines()
	alwn = []

	for i in xrange(1, len(al)):
		alwn.append(al[i].strip("\n").strip("\r").split(','))

	dept = dict()
	sal = dict()
	for i in xrange(0, len(alwn)):
		if alwn[i][8] not in dept:
			dept[alwn[i][8]] = len(dept)
		if alwn[i][9] not in sal:
			sal[alwn[i][9]] = len(sal)

	X = []
	Y = []
	pos_val = []
	for x in xrange(0, 9):
		pos_val.append([1000000.0, -1000000.0])
	for i in xrange(0, len(alwn)):
		X.append([])
		for j in xrange(0, 5):
			X[i].append(float(alwn[i][j]))
			if X[i][j] < pos_val[j][0]:
				pos_val[j][0] = float(alwn[i][j])
			if X[i][j] > pos_val[j][1]:
				pos_val[j][1] = float(alwn[i][j])
		X[i].append(int(alwn[i][5]))
		Y.append(int(alwn[i][6]))
		X[i].append(int(alwn[i][7]))
		X[i].append(int(dept[alwn[i][8]]))
		X[i].append(int(sal[alwn[i][9]]))

	pos_val[5] = [0, 1]
	pos_val[6] = [0, 1]
	pos_val[7] = [0, len(dept)-1]
	pos_val[8] = [0, len(sal)-1]
	disc[5] = disc[6] = disc[7] = disc[8] = 1

	train_X = X
	train_Y = Y
	tree = node(pos_val, train_X, train_Y, 10000)


	f = open(sys.argv[2],'r')
	al = f.readlines()
	alwn = []

	for i in xrange(1, len(al)):
		alwn.append(al[i].strip("\n").strip("\r").split(','))
	X = []
	for i in xrange(0, len(alwn)):
		X.append([])
		for j in xrange(0, 5):
			X[i].append(float(alwn[i][j]))
		for j in xrange(5, 7):
			X[i].append(int(alwn[i][j]))
		X[i].append(int(dept[alwn[i][7]]))
		X[i].append(int(sal[alwn[i][8]]))

	test_X = X
	for i in xrange(0, len(test_X)):
		y = tree.pred(test_X[i])
		print y
if __name__ == "__main__":
    main()