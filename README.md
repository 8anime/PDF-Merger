# Receipt PDF Merger

This Python project allows you to merge multiple PDF receipt files from a specified folder into a single PDF file which will contain all the merged receipts from individual PDF files. The merged receipts are saved in the output PDF file you specify.

## Table of Contents
- [Prerequisites](#prerequisites)
- [How to Run](#how-to-run)
- [Example](#example)

### Prerequisites
Before using this project, make sure you have the following:

- Python installed on your system.
- The required Python libraries: `PyPDF2`. You can install it using `pip`:

    ```
    pip install PyPDF2==1.26.0
    ```

### How to Run

1. Clone or download this repository to your local machine.

2. Place the PDF files you want to merge in the `data folder` which is located in the root directory. The application will merge theses files in a single PDF file.

3. Navigate to the `main.py` script in the root directory.

4. Run the script using the following command:

    ```
    python main.py
    ```

    - `pdf_folder`: The path to the folder containing the PDF files you want to merge.
    - `output_pdf`: The name of the output PDF file where the merged receipts will be saved.

5. The application will merge the PDF receipt files and save the resulting PDF as `combined_receipts.pdf` which will be located in the root directory.

### Example

Suppose you have the following PDF files in the folder `data folder`:

- document1.pdf
- document2.pdf
- document3.pdf

To merge them into a single PDF document named `combined_receipts.pdf` located in the root directory, run the `main.py` script with the following command:

```terminal
python main.py
