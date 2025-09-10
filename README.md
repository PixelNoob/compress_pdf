# PDF Compressor

A simple Python script to compress scanned PDF files by converting each page to a low-resolution JPEG image and rebuilding the PDF. Useful for reducing file sizes of scanned documents (e.g., CamScanner exports) to meet upload or email size limits.

## Features

- Converts each page to JPEG with configurable DPI and quality.
- Suitable for scanned/image-based PDFs.
- Simple and fast – works locally without sending data to external servers.

## Requirements

- Python 3.7+
- [`PyMuPDF`](https://pymupdf.readthedocs.io/en/latest/)
- [`Pillow`](https://pillow.readthedocs.io/en/stable/)

Install dependencies:

```bash
pip install -r requirements.txt
