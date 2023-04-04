#! /usr/bin/env python3
import pandas as pd
from Bio import Entrez
from Bio import SeqIO

# NCBI need an email to inform you when you were blocked
Entrez.email = 'fg_dean@163.com'

accession = pd.read_table('accessionID.txt', header=None)
ids = ','.join(accession.iloc[:, 0])
handle = Entrez.efetch(db='nucleotide', id=ids, rettype='fasta', retmode='text')
records = SeqIO.parse(handle, 'fasta')
output = 'test.fa'
SeqIO.write(records, output, 'fasta')
