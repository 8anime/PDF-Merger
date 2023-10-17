
import os

from src.combinePDFs import mergePdfDocuments

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # Path to the directory this script belongs to

PDF_FOLDER = os.path.join(ROOT_DIR, 'data') # Folder containing PDF files you want to merge   
OUTPUT_FILE = os.path.join(ROOT_DIR, 'combined_receipts.pdf')  # PDF document containing the merged PDF files

if __name__ == '__main__':
    mergePdfDocuments(PDF_FOLDER, OUTPUT_FILE)



