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

-c cell clusters lable by numbers with each number in a each row. The order is the same as row order in single cell expression matrix. 
```
| PCR_II_Forward_Primer_A | FZ_Sample1 | AATGATACGGCGACCACCGAGATCTACACTCTTTCCCTACACGACGCTCTTCCGATCTtAAGTAGAGtcttgtggaaaggacgaaacaccg | TAAGTAGAGTCTTGT|
| PCR_II_Forward_Primer_B | FZ_Sample2 | AATGATACGGCGACCACCGAGATCTACACTCTTTCCCTACACGACGCTCTTCCGATCTatACACGATCtcttgtggaaaggacgaaacaccg|ATACACGATCTCTTG|
| PCR_II_Forward_Primer_C | FZ_Sample3 | AATGATACGGCGACCACCGAGATCTACACTCTTTCCCTACACGACGCTCTTCCGATCTgatCGCGCGGTtcttgtggaaaggacgaaacaccg|GATCGCGCGGTTCTT
```
The output file demultiplexed fastq files, like FZ_Sample1_sgRNA.fastq,FZ_Sample2_sgRNA.fastq .....

There are some barcode or primer sequences in the original fastq files. So we first need to extract sgRNA fastq sequences using the following commands. We used multiprocessing to increase the processing speed. 
```
python Genes_correalted_with_MPP.py -i ../../T0_combine/Random_forest_classifier/T0_com
bine_normalized_matrix_full_gene.txt -i2 ../../D_34_Kit_G12D_E2KO_T2/34_G12D_E2KO_T2_normalized_matrix_full_gene.txt -g training
_gene_ix_for_927_important_features.txt -g2 predicting_gene_ix.txt -c ../../T0_combine/Random_forest_classifier/reannotation_fil
es/cluster_labels.txt
```
The library.txt contains sgRNA sequences. Here are a few lines of library.txt file:
```
sgRNA Sequence
AAATCCGGGGATGGATTGAG
CTGTGCGCTGGACCAGTGCG
GCAGAGTGCAGCTGGTACAC
AGTGCCGCTCAATCCATCCC
CCAGCGCACAGGATATAGCT
GGATTCTGGCTGGCTAGAGC
GTCCAATAGCAGAGTGCAG
```
The following command is used to generate raw and normalized counts of sgRNAs. 
```
python sgRNA_count.py -b annotation_table.txt -f sgRNA.fastq > sgRNA_count.txt
```
The are three columns in input annotation_table.txt file. The first colum is sgRNA sequence. The sescond column is description (you can put "NA" if no decription needed). And the third column is sgRNA id. Here are a few lines of the annotation table file:
```
| CAAGTTCCTGATTTTATCGA | NA | SPil_1 |
| GCCCCCTCCCTTGACATTGC | NA | SPil_1 |
| ACGGTCGTGGGTCAGACGCA | NA | SPil_1 |
```
There are four columns in the output sgRNA_count.txt file. The first colum is sgRNA sequence. The second column is sgRNA id. The third column is sgRNA raw counts. And the fourth column is normalized sgRNA counts (normalized by total counts). Here are a few lines of output count file.
```
| CAAGTTCCTGATTTTATCGA | SPil_1 | raw count | normalized count|
| GCCCCCTCCCTTGACATTGC | SPil_1 | raw count | normalized count|
| ACGGTCGTGGGTCAGACGCA | SPil_1 | raw count | normalized count|
```
