from fpdf import FPDF

class Shirtificate(FPDF):
    def header(self):
        self.set_font("Arial", style="", size =12)
        self.cell(0, 10, "CS50 Shirtificate", 0, 1, "C")

    def generate(self, name):
        self.add_page()
        self.set_font("Arial", style="", size=24)
        width, height = self.w, self.h
        name_width = self.get_string_width(name)
        self.set_xy((width - name_width) / 2, height / 2)
        self.set_text_color(255, 255, 255)
        self.cell(0, 10, name, 0, 1, "C")

        self.image("shirtificate.png", (width - 100) / 2, (height - 100) / 2, 100)

name = input("Name: ")


pdf = Shirtificate(format="A4", orientation="P")
pdf.generate(name)
pdf.output("shirtificate.pdf")
