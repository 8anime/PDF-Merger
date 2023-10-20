
import os
import PyPDF2
import logging

# Configure the logging module
logging.basicConfig(filename='pdf_merge.log', level=logging.INFO)


def mergePdfDocuments(pdf_folder, ouput_pdf):
    """
    Merge multiple PDF files from a specified folder into a single PDF.

    Args:
        pdf_folder (str): The path to the folder containing the PDF files to be merged.
        output_pdf (str): The name of the output PDF file where the merged content will be saved.

    This method searches for PDF files in the specified folder, sorts them in case-insensitive alphabetical order,
    and then merges them into a single PDF file. The resulting PDF is saved with the provided output file name.

    Example:
        mergePdfDocuments("pdf_folder_path", "output_merged.pdf")

    Returns:
        None: This method has no return value. It either successfully merges the PDFs or raises an exception in case of an error.
    """
    try:
        pdfFiles = []                                # Store all PDF file paths in a list
        for filename in os.listdir(pdf_folder):      # Search for PDF files in the 'data folder' in the root directory
            if filename.endswith('.pdf'):            # Search for files ending with '.pdf' extension located in the 'data folder'
                pdfFiles.append(os.path.join(pdf_folder, filename))  # Add files with '.pdf' extension to the 'pdfFiles list'
    
        # Sort the filenames to lowercase and make them case-insensitive alphabetic order
        pdfFiles.sort(key=str.lower)
    
        blankDocument = PyPDF2.PdfFileWriter()  # Create a Blank PDF document
    
        # Loop through all the PDF filepaths in the list
        for path in pdfFiles:
            readPDF = open(path, 'rb')               # Open PDF files identified by their paths in the list
            reader = PyPDF2.PdfFileReader(readPDF)   # Create a reader object to read the PDF file(s)
            
            # Loop through all the pages and add them to the blank document
            for pageNum in range(reader.numPages):    # Look for every page in a PDF file
                page = reader.getPage(pageNum)        # Get the pages from the PDF file
                blankDocument.addPage(page)           # Add each page found to the blank PDF document
    
        # Save the resulting PDF to a file
        with open(ouput_pdf, 'wb') as outputPDF:  # Open a new PDF file to write the results in
            blankDocument.write(outputPDF)        # Write the pages in the blank document to a new PDF file
    
        print('PDF merge was successful')         # Display message to user if the process was successful
        logging.info('PDF merge was successful')

    except Exception as e:     # Handle any errors that might have occurred during processing of the file
        print(e)               # Print the error message
        logging.error(f'An error occurred: {str(e)}')