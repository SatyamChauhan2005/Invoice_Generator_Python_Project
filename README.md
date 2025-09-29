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
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Invoice Data</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            padding: 30px;
        }
        h2 {
            color: #333;
        }
        table {
            border-collapse: collapse;
            width: 70%;
            margin-top: 20px;
        }
        th, td {
            border: 1px solid #888;
            padding: 10px 15px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
        }
        caption {
            caption-side: top;
            font-weight: bold;
            margin-bottom: 10px;
        }
    </style>
</head>
<body>

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

</body>
</html>



