from pypdf import PdfMerger

merger = PdfMerger()
# Add the files in the order you want
merger.append("file1.pdf")
merger.append("file2.pdf")

# Write out the combined PDF
merger.write("merged.pdf")
merger.close()
