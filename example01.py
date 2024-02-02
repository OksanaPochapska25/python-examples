import aspose.pdf as ap

input_pdf = "sample.pdf"
output_pdf = "convert_pdf_to_xlsx.xlsx"

# Open PDF document
document = ap.Document(input_pdf)

save_option = ap.ExcelSaveOptions()

# Save the file into MS Excel format
document.save(output_pdf, save_option)
