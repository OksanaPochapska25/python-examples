import asposepdfcloud
import os
            
pdf_api_client = asposepdfcloud.api_client.ApiClient(
                    app_key=str("your-key"),
                    app_sid=str("your-sid"))

pdf_api = asposepdfcloud.PdfApi(pdf_api_client)

local_pdf_file="sample.pdf"
storage_pdf_file = "sample.pdf"
local_xlsx_file = "sample_cloud.xlsx"

pdf_api.upload_file(local_pdf_file, storage_pdf_file)

response = pdf_api.get_pdf_in_storage_to_xlsx(storage_pdf_file,)

print(response)

os.rename(response, "/home/aspose/aspose-pdf-python/sample-cloud.xlsx")
