import pypdf

pdfFiles = ["file1.pdf", "file2.pdf"]
merger = pypdf.PdfMerger()
for filename in pdfFiles:
    pdfFiles = open(filename, 'rb')
    pdfReader = pypdf.PdfReader(pdfFiles)
    merger.append(pdfReader)
pdfFiles.close()
merger.write('merged.pdf')
