import aspose.pdf.plugins as ap

input_pdf = "sample.pdf"
output_pdf = "convert_pdf_to_xlsx.xlsx"

plugin = ap.PdfExcel()
options = ap.PdfToExcelOptions()
options.add_input(ap.FileDataSource("sample.pdf"))
options.add_output(ap.FileDataSource("sample.xlsx"))

resultContainer = plugin.process(options)
result = resultContainer.result_collection[0].data

print(result)