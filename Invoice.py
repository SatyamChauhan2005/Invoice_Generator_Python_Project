import pandas as pd 

    # Read the orders Excel file
df = pd.read_excel(r"C:\Users\HP\Downloads\Orders.xlsx")
grouped = df.groupby("Invoice No")
from fpdf import FPDF
import os

    # Create output directory
os.makedirs("invoices", exist_ok=True)

    # Loop through each invoice
for invoice_no, data in grouped:
        pdf = FPDF()
        pdf.add_page()
        
        # Title
        pdf.set_font("Arial", "B", 16)
        pdf.cell(0, 10, f"Invoice #{invoice_no}", ln=True)
        
        client_name = data["Client Name"].values[0]
        pdf.set_font("Arial", "", 12)
        pdf.cell(0, 10, f"Client: {client_name}", ln=True)
        
        pdf.ln(10)
        
        # Table header
        pdf.set_font("Arial", "B", 12)
        pdf.cell(50, 10, "Product", border=1)
        pdf.cell(30, 10, "Qty", border=1)
        pdf.cell(30, 10, "Unit Price", border=1)
        pdf.cell(30, 10, "Total", border=1, ln=True)

        total_amount = 0
        
        # Table rows
        pdf.set_font("Arial", "", 12)
        for _, row in data.iterrows():
            total = row["Quantity"] * row["Unit Price"]
            total_amount += total
            
            pdf.cell(50, 10, row["Product"], border=1)
            pdf.cell(30, 10, str(row["Quantity"]), border=1)
            pdf.cell(30, 10, f"${row['Unit Price']:.2f}", border=1)
            pdf.cell(30, 10, f"${total:.2f}", border=1, ln=True)
        
        pdf.ln(10)
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, f"Total Amount: ${total_amount:.2f}", ln=True)
        
        # Save PDF
        pdf.output(f"invoices/{invoice_no}.pdf")


