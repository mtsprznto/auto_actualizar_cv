from fpdf import FPDF

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.utils import limpiar_texto


class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, limpiar_texto("Matías Pérez Nauto – Desarrollador de Software"), ln=True, align="C")
        self.ln(10)

    def section_title(self, title):
        self.set_font("Arial", "B", 12)
        self.set_fill_color(230, 230, 230)
        self.cell(0, 8, limpiar_texto(title), ln=True, fill=True)
        self.ln(1)

    def multi_section(self, items):
        self.set_font("Arial", "", 10)
        for line in items:
            self.multi_cell(0, 6, limpiar_texto(f"- {line}"))
        self.ln(2)

    def paragraph(self, text):
        self.set_font("Arial", "", 10)
        self.multi_cell(0, 6, limpiar_texto(text))
        self.ln(2)

    def proyectos_dinamicos(self, repos: list, max_items=5):
        self.section_title("Proyectos Relevantes (Automáticos)")
        self.set_font("Arial", "", 10)

        for i, repo in enumerate(repos[:max_items]):
            texto = formatear_proyecto(repo)
            self.multi_cell(0, 6, limpiar_texto(texto))
            self.ln(1)


