from fpdf import FPDF

class Shirt(FPDF):
    def header(self):
        self.image("./shirtificate.png", 15, 60, 185)
        self.set_font("helvetica", size=35)
        self.set_xy(0,25)
        self.cell(210, 20, "CS50 Shirtificate", align="C")

    def add_name(self, name):
        self.name = name
        self.add_page(orientation="portrait", format="A4")
        self.set_xy(70,85)
        self.set_font("helvetica", style="B", size=22)
        self.set_text_color(255, 255, 255)
        self.cell(80, 80, f"{self.name} took CS50", align="C")



def main():
    pdf = Shirt()
    name = input("Name: ")
    pdf.add_name(name)
    pdf.output("shirtificate.pdf")


if __name__ == "__main__" :
    main()

