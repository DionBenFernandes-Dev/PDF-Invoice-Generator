# PDF Invoice Generator
The PDF Invoice Generator is a Python project that utilizes the ReportLab library to dynamically generate professional-looking invoices in PDF format.

The PDF Invoice Generator project leverages the ReportLab library, a powerful PDF generation tool in Python. ReportLab allows for the creation of complex PDF documents from simple scripts, providing precise control over the layout and design. The project also demonstrates best practices such as creating a virtual environment using tools like virtualenv, which helps manage dependencies and ensures a clean development environment.

To run the code, follow these steps:

1. **Setup Virtual Environment:** Create a virtual environment using virtualenv to isolate dependencies. Navigate to the project directory in your terminal and run:
    ```
    virtualenv venv
    ```

2. **Activate Virtual Environment:** Activate the virtual environment:
    - On Windows:
      ```
      venv\Scripts\activate
      ```
    - On macOS and Linux:
      ```
      source venv/bin/activate
      ```

3. **Install Dependencies:** Install required dependencies using pip:
    ```
    pip install reportlab
    ```

4. **Run the Code:** Execute the Python script `invoice_generator.py`:
    ```
    python invoice_generator.py
    ```

This will generate the PDF invoice based on the provided data and template design. The output PDF will be saved in the project directory with the name `invoice.pdf`.

**Output Images:**  
![Invoice](https://github.com/DionBenFernandes-Dev/PDF-Invoice-Generator/blob/main/Screenshot%202024-03-27%20124853.png)
