from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_invoice_pdf(invoice_data, filename):
    # Create a canvas
    c = canvas.Canvas(filename, pagesize=letter)

    # Set up some coordinates for data placement
    x_offset = 50
    y_offset = 750
    line_height = 15

    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(300, y_offset, "INVOICE")
    y_offset -= 30

    # Draw a line under the title
    c.line(x_offset, y_offset, 550, y_offset)
    y_offset -= 10

    # Invoice details
    c.setFont("Helvetica", 10)
    for key, value in invoice_data['invoice_details'].items():
        c.drawString(x_offset, y_offset, f"{key}: {value}")
        y_offset -= line_height

    # Customer information
    c.setFont("Helvetica-Bold", 10)
    y_offset -= 20
    c.drawString(x_offset, y_offset, "Customer Information:")
    c.line(x_offset, y_offset - 5, 550, y_offset - 5)
    c.setFont("Helvetica", 10)
    y_offset -= 20
    for key, value in invoice_data['customer_info'].items():
        c.drawString(x_offset, y_offset, f"{key}: {value}")
        y_offset -= line_height

    # Draw a line after customer information
    c.line(x_offset, y_offset, 550, y_offset)

    # Draw table header
    c.setFont("Helvetica-Bold", 10)
    y_offset -= 20
    c.drawString(x_offset, y_offset, "Description")
    c.drawString(x_offset + 200, y_offset, "Quantity")
    c.drawString(x_offset + 350, y_offset, "Amount ($)")

    # Draw table content
    c.setFont("Helvetica", 10)
    y_offset -= 20
    for item in invoice_data['items']:
        c.drawString(x_offset, y_offset, item['description'])
        c.drawString(x_offset + 200, y_offset, str(item['quantity']))
        c.drawString(x_offset + 350, y_offset, str(item['amount']))
        y_offset -= line_height

    # Draw a line under the table
    c.line(x_offset, y_offset, 550, y_offset)

    # Total section
    c.setFont("Helvetica-Bold", 10)
    y_offset -= 30
    c.drawString(x_offset + 350, y_offset, "Total:")
    c.drawString(x_offset + 450, y_offset, str(invoice_data['total']))

    c.save()

# Example data
invoice_data = {
    'invoice_details': {'Invoice No': 'ABC123', 'Date': '2024-03-27'},
    'customer_info': {'Name': 'John Doe', 'Address': '123 Main St, City, Country', 'Email': 'johndoe@example.com'},
    'items': [{'description': 'Product 1', 'quantity': 2, 'amount': 20.00},
              {'description': 'Product 2', 'quantity': 1, 'amount': 15.00}],
    'total': 35.00,
}

# Generate PDF
generate_invoice_pdf(invoice_data, 'invoice.pdf')
