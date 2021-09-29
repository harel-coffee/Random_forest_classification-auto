# Random_forest_classification
These scripts are used to calculate the correlation of genes to MPP prediction score. 

We applied random forest algorithm in single-cell RNA-seq data to identify cell-type-specific genes by treating cells as samples, genes as features, and different cell types as different classes. We used RandomForestClassifier package from scikit-learn v0.20.2 to build random forest classifier and classified single cells into different cell types annotated in WT HSPCs. To train random forest classifier, feature selection was first performed by training a random forest classifier on all expressed genes.

# step1 
selected the 1,000 most informative genes based on overall gene importance in the classifier to train random forest classifier
```
python random_forest_feature_selection.py -i reference_single_cell_expression_matrix.txt -g genelist.txt -c cluster_labels.txt > 
feature_importance.txt
```
-i single cell expression matrix with rows as cells and columns as genes 

-g gene list with each gene in a row. Gene order is the same as the column order in single cell expression matrix

-c cell clusters lable represented by numbers with each number in a row. The order is the same as row order in single cell expression matrix. 

The output file feature_importance.txt contains two columns. The first column is gene name and the second column is importance score.  1,000 most informative genes based on overall gene importance were selected for the next step.

# step2
To identify MPP-specific genes in query samples, we predicted the probabilities of each cell in MPP using the trained random forest classifier. We then calculated the correlation for each gene with MPP probabilities. Genes with high correlation to MPP prediction score were identified as MPP preferentially expressed genes.   

```
python Genes_correalted_with_MPP.py -i reference_single_cell_expression_matrix.txt -i2 qurey_sample_single_cell_gene_expression_matrix.txt -g reference_sample_gene_id.txt -g2 query_sample_gene_id.txt -c cluster_labels.txt 
```
-i single cell expression matrix for reference sample with rows as cells and columns as genes 

-i2 single cell expression matrix for query sample with rows as cells and columns as genes 

-g gene index of 1000 most important genes in reference sample with each index in a row

-g2 gene index of 1000 most important genes in query sample with each index in a row

-c clusters for cells in reference sample (same as the input in step1)

Output will be stored in the file of "Gene_correlation_with_MPP.txt" with each row as correlation cofficiency of each gene with MPP prediction score.  

