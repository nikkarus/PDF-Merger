from PyPDF2 import PdfFileMerger

pdfs = ['1.pdf', '2.pdf', '3.pdf'] #enter in list of pdfs to merge with directory

merger = PdfFileMerger() #run class

for pdf in pdfs: #loop through all pdfs to be merged
    merger.append(pdf) #append to the final

merger.write("result.pdf") #file name of output