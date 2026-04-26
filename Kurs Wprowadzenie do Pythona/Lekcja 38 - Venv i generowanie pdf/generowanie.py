from fpdf import FPDF

A4W= 210
A4H= 297

pdf = FPDF()

pdf.add_page()
pdf.set_text_color(255,0,0)
pdf.set_font('helvetica', size=12)

# pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf')
# pdf.set_font('DejaVu', size=12)

pdf.text(x=30, y=20, text="Oferta biura podrozy")

pdf.image(
    "logo.png",
    x = A4W*0.25,
    y = A4W*0.25,
    w = A4W*0.5,
    h = A4W*0.5
)

pdf.set_text_color(0,0,0)
pdf.text(x=40, y=A4W*0.75+20, text="Wycieczka po Polsce")

pdf.text(x=10, y=A4H-20, text="Oferta powstala przy uzyciu pythona i sztucznej inteligencji")

pdf.output("Oferta_biura.pdf")





# crtl+shft+P
# Python: Select Interpreter