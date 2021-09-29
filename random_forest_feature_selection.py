#!/usr/bin/python
# only work for python/3.6.4-anaconda
import os,sys
import argparse
import matplotlib
matplotlib.use('agg')
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectFromModel
from sklearn.metrics import accuracy_score

def argParser():
	'''Parse argument.'''
	p=argparse.ArgumentParser(description="cluster correlation heatmap")
	p._optionals.title="Options"
	p.add_argument("-i", dest="infile",metavar="input matrix with full genelist", required=True,help="input matrix with full genelist")
	p.add_argument("-g", dest="gene",metavar="feature gene list", required=True,help="feature gene list with gene in very line")
	p.add_argument("-c", dest="clusters",metavar="merged clusters for cells", required=True,help="merged clusters for cells")
	if len(sys.argv)==1:
		sys.exit(p.print_help())
	args=p.parse_args()
	return args

if __name__=='__main__':
	args=argParser()
	data = pd.read_csv(args.infile, sep=" ", header=None)
	genes = [line. rstrip('\n') for line in open(args.gene)]
	labels= np.array([line. rstrip('\n') for line in open(args.clusters)])
	clf = RandomForestClassifier(n_estimators=10000, random_state=0, n_jobs=-1)
	clf.fit(data, labels)
	for feature in zip(genes, clf.feature_importances_):
    		print (feature)
	

	
