# Gene Regulatory Dynamics During the Development of _Cloeon dipterum_

This repository contains the code and analysis pipeline associated with the paper "Gene regulatory dynamics during the development of a paleopteran insect, the mayfly _Cloeon dipterum_." The repository is structured into two main sections: ATAC Pipeline and Downstream Analysis.

## ATAC Pipeline

The ATAC pipeline processes ATAC-seq data to identify consensus peaks and associates these peaks with genomic zones.

### ATAC-seq Mapping and Peak Calling

The `ATAC_pipe.pl` script is used for mapping reads using Bowtie2. Peak calling is conducted with the `idr_ATAC_script.sh`, which employs MACS2 for peak detection and IDR analysis. For more detail, see [here](https://github.com/alexgilgal/Thesis_methods/tree/main/ATAC-seq%20analysis).

### Peak Classification and Gene Assignment

Peaks are classified and linked to genes based on proximity to Transcription Start Sites (TSS). The `cisreg_map.py` script maps these peaks to genes. For more detail, see [here](https://github.com/m-rossello/GeneRegLocator).

## Downstream Analysis

This section encompasses various analyses related to chromatin accessibility during different embryonic stages of _C. dipterum_:

1. **Genomic Peaks Analysis & Comparative Distribution**
2. **Differential Chromatin Accessibility Analysis**
3. **Chromatin Changes in Relation to WGCNA Modules**
4. **Chromatin Dynamics with Mfuzz Clustering**
5. **Chromatin Dynamics with Kmeans Clustering**
6. **Integrative Analysis of RNA-seq and ATAC-seq Data**

## Contact

For further inquiries, please contact:

- Maria Rossello: [mariarossello@ub.edu](mailto:mariarossello@ub.edu)
- Isabel Almudi: [ialudi@ub.edu](mailto:ialudi@ub.edu)
