import PyPDF2
import sys


def combine(*args):
    # Usage: pdf.py combine filename(s) 
    merger = PyPDF2.PdfFileMerger()
    for pdf in [*args]:
        merger.append(pdf)
    merger.write('combined.pdf')


def watermark(*args):
    # Usage: pdf.py watermark file2 file3
    # [2] - file to be watermarked
    # [3] - watermark
    file_list = [*args]
    output = PyPDF2.PdfFileWriter()
    file = PyPDF2.PdfFileReader(open(file_list[0], 'rb'))
    watermark = PyPDF2.PdfFileReader(open(file_list[1], 'rb'))
    
    for i in range(file.getNumPages()):
        page = file.getPage(i)
        page.mergePage(watermark.getPage(0))
        output.addPage(page)

    with open('watermarked.pdf', 'wb') as file:
        output.write(file)


def rotate(*args):
    # Usage: pdf.py rotate filename
    # rb mode - we need to convert file to binary, so reader can read it.
    with open(*args, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        page = reader.getPage(0)
        page.rotateCounterClockwise(90)
        writer = PyPDF2.PdfFileWriter()
        writer.addPage(page)
        with open('tilt.pdf', 'wb') as new_file:
            writer.write(new_file)


if __name__ == '__main__':
    args = sys.argv
    # [0] - current file
    # [1] - function name
    # [2] - function arguments
    globals()[args[1]](*args[2:])