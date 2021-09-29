#!/usr/bin/python
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
	p.add_argument("-i", dest="infile",metavar="single cell expression matrix for reference sample", required=True,help="single cell expression matrix for reference sample")
	p.add_argument("-i2", dest="infile2",metavar="single cell expression matrix for query sample", required=True,help="single cell expression matrix for query sample")
	p.add_argument("-g", dest="gene",metavar="gene id of 1000 most important genes in reference sample", required=True,help="gene id of 1000 most important genes in reference sample")
	p.add_argument("-g2", dest="gene2",metavar="gene id of 1000 most important genes in query sample", required=True,help="gene id of 1000 most important genes in query sample")
	p.add_argument("-c", dest="clusters",metavar="clusters for cells in reference sample", required=True,help="clusters of cells in reference sample")
	if len(sys.argv)==1:
		sys.exit(p.print_help())
	args=p.parse_args()
	return args

if __name__=='__main__':
	args=argParser()
	data = pd.read_csv(args.infile, sep=" ", header=None)
	pre_data = pd.read_csv(args.infile2, sep=" ", header=None)
	full_pre_data=pre_data
	selected_gene_features = [line. rstrip('\n') for line in open(args.gene)]
	pre_gene_features = [line. rstrip('\n') for line in open(args.gene2)]
	data=data.take(selected_gene_features, axis=1)
	pre_data=pre_data.take(pre_gene_features, axis=1)
	labels= np.array([line. rstrip('\n') for line in open(args.clusters)])
	clf = RandomForestClassifier(n_estimators=1000, random_state=0, n_jobs=-1)
	clf.fit(data, labels)
	y_pred = clf.predict(pre_data)
	fhd=open("predicted_lables.txt","w")
	for i in y_pred:
		fhd.writelines("%s\n"%i)
	fhd.close()
	scores=clf.predict_proba(pre_data)
	MPP_score=scores[:,0]
	GMP_score=scores[:,1]
	Mono_score=scores[:,2]
	GN1_score=scores[:,3]
	GN2_score=scores[:,4]
	Meg_score=scores[:,5]
	Ly_score=scores[:,6]
	Er_pro_score=scores[:,7]
	Early_Er_score=scores[:,8]
	Late_Er_score=scores[:,9]
	columns = list(full_pre_data)
	MPP_gene_coeff=[]
	for i in columns:
		gene_score=np.array(full_pre_data[i])
		MPP_corr=np.corrcoef(MPP_score,gene_score)[1,0]
		MPP_gene_coeff.append(MPP_corr)
	fhd=open("Gene_correlation_with_MPP.txt","w")
	for i in MPP_gene_coeff:
		fhd.writelines("%s\n"%i)
	fhd.close()

