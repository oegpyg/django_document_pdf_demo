from django_document_pdf.document_wrapper import DocumentPDF
from demo.models import PurchaseInvoice


def run():
    record = PurchaseInvoice.objects.get(pk=1)
    doc = DocumentPDF(document_spec_code='Invoice_Test',
                      filename='file.pdf',
                      record=record)

    doc.generatePDF()
