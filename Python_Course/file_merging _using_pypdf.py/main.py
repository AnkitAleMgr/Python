from pypdf import PdfMerger

merger = PdfMerger()

# Add PDF files
merger.append("file1.pdf")
merger.append("file2.pdf")

# Write to a new PDF
merger.write("merged_output.pdf")
merger.close()
