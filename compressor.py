import fitz  # PyMuPDF
from PIL import Image
import io

# Input and output file paths
input_file = "doc2.pdf"
output_file = "doc2_compressed.pdf"

# Open the original PDF
doc = fitz.open(input_file)
compressed_doc = fitz.open()

# Loop through each page and compress
for page in doc:
    pix = page.get_pixmap(dpi=50)  # Reduce resolution
    img = Image.open(io.BytesIO(pix.tobytes("ppm"))).convert("RGB")

    # Save the image as JPEG in memory with high compression
    img_bytes = io.BytesIO()
    img.save(img_bytes, format="JPEG", quality=10, optimize=True)  # Adjust quality if needed
    img_bytes.seek(0)

    # Create a new PDF page and insert the compressed image
    img_pdf = fitz.open()
    rect = fitz.Rect(0, 0, pix.width, pix.height)
    page_pdf = img_pdf.new_page(width=rect.width, height=rect.height)
    page_pdf.insert_image(rect, stream=img_bytes.read())
    compressed_doc.insert_pdf(img_pdf)

# Save the final compressed PDF
compressed_doc.save(output_file)
compressed_doc.close()
doc.close()

print(f"✅ Compressed PDF saved as: {output_file}")

