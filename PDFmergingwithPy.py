import PYPDF2 #this PYPDF2 is used while handling the PDF's

import sys  # To get the args

inputs = sys.argv[1:]
'''
  [1:]
  Here my pdf files are from 2 & first file is PYTHON file
'''
def pdfCombiner(pdf_list):
  merger = PyPDF2.PdfFileMerger()
  for pdf in pdf_list:
    merger.append(pdf)
  merger.write('mergedFile.pdf')
  
pdfCombiner(inputs)      
