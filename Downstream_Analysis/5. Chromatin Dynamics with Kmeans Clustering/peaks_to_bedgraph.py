#!/usr/bin/env python

"""

This script generates a bedGraph file from each column of a tsv file containing
counts information. Genomic coordinates must be provided from a separate bed
annotation file.

"""

# Usage: peaks_to_bedgraph.py  normalized_peak_file.tsv annotation_peaks.bed

# Usage Example: 
#    $WD/peaks_to_bedgraph.py $WD/dynamic_peaks_x_stage.tsv $WD/dynamic_peaks.bed

# To move it to Margulis:
# scp MAYFLY/ATAC_SEQ/peaks_to_bedgraph.py jpallares@evodevo.bio.ub.edu:ATAC_SEQ/


# Imports #

import sys
import pandas as pd


# Definition #

def column_to_bedgraph(column_name, tsv, bed):
    """Converts a column from the tsv file into a 
       separated bedgraph file using information 
       from the bed file.
    """
    
    if column_name != 'peak_id':
        
        # Generate a column-specific Temporary DataFrame
        t_df = tsv[['peak_id', column_name]]
        
        # Add Peak coordinates information 
        t_df = pd.merge(t_df, bed, on=['peak_id'])
 
        # Adjust to Bedgraph format (Chr, Start, End, Value) 
        t_df.drop(["peak_id"], axis=1, inplace=True) 
        t_df = t_df.loc[:,['Chromosome','Start','End', column_name]]
        
        # Prepare Output
        l = arg[1].split("/")
        path = ''
        
        # Obtain the path without file name:
        for element in map(lambda x: x+"/", l[:-1]): # Maybe this is 
            path += element                          # unnecessarily complex
            
        path += column_name + '.bedgraph'
        
        return t_df.to_csv(path, sep='\t', header=False, index=False,
                           doublequote=False)


# Exectuion #

# Load Files
arg = sys.argv

tsv = arg[1]
tsv = pd.read_csv(tsv, sep='\t')

bed = arg[2]
bed = pd.read_csv(bed, sep='\t', 
                  names=['Chromosome', 'Start', 'End', 'peak_id'])

# Generate bedGraph from each column in TSV
for column in tsv.columns:
    column_to_bedgraph(column, tsv, bed)
    
