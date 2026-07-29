from fpdf import FPDF
# Youtube Coding Shiksha - Python 3 FPDF Library Script to Add Text & Images to PDF Document & Save it as Output
def createPDF():
    pdf = FPDF()
    pdf.add_page()
    pdf.image("shirtificate.png", w=210)
    pdf.set_font("Helvetica", style="B", size=25)
    pdf.set_text_color(255, 255, 255)
    inp = input("Name: ")
    wording = inp + " took CS50"
    pdf.cell(210, 10, wording)
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    createPDF()
