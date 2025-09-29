#✅ Project Title:<br>
<b>🧾 Invoice Generator with PDF Export using Python</b><br>
<b>#🧠 What You’ll Learn</b>
<ol>
<li>File handling in Python</li>
<li>Data from Excel (using pandas)</li>
<li>PDF generation (using fpdf or reportlab)</li>
<li>Basic automation</li>
<li>Modular, clean code structure</li></ol><br>
<br>
<ul><b>🔧 Tools & Libraries</b>

<li>pandas (for reading Excel/CSV)</li>
<li>fpdf or reportlab (for generating PDFs)</li>
<li>os (to manage folders/files)</li>
<li>datetime (to add invoice date)</li></ul>

<b>📝 Sample Excel Format</b><br>
<h2>Sample Invoice Data</h2>

<table>
    <caption>Orders.xlsx Sample Data</caption>
    <thead>
        <tr>
            <th>Invoice No</th>
            <th>Client Name</th>
            <th>Product</th>
            <th>Quantity</th>
            <th>Unit Price</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>INV001</td>
            <td>Shivam</td>
            <td>Pen</td>
            <td>10</td>
            <td>4</td>
        </tr>
        <tr>
            <td>INV002</td>
            <td>Rahul</td>
            <td>Notebook</td>
            <td>5</td>
            <td>3</td>
        </tr>
        <tr>
            <td>INV003</td>
            <td>Ashish</td>
            <td>Pencil</td>
            <td>20</td>
            <td>1</td>
        </tr>
        <tr>
            <td>INV004</td>
            <td>Rajinder</td>
            <td>Pencil</td>
            <td>10</td>
            <td>2</td>
        </tr>
        <tr>
            <td>INV005</td>
            <td>Satish</td>
            <td>Marker</td>
            <td>12</td>
            <td>5</td>
        </tr>
    </tbody>
</table>

<b>PYTHON</b>
<details>
<summary><b></b>📄✅ Click to view Python code ✅📄</summary> </b></summary>
import pandas as pd 
'''
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


</details>
🚀 Just finished building an **Invoice Generator with Python** that reads Excel files and exports PDFs automatically!

📄 Check out the full Python code here 👉 [Invoice Generator Python Code](https://gist.github.com/chatgpt-helper/8d5b6f7f17b08ef75a8f6b21f4e6ec4e)

#Python #Automation #PDFGeneration #Excel #fpdf #pandas #OpenSource #GitHub




