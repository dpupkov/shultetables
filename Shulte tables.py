import random
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm

def generate_schulte_table(size=5):
    numbers = list(range(1, size * size + 1))
    random.shuffle(numbers)
    table = [numbers[i * size:(i + 1) * size] for i in range(size)]
    return table

def draw_table(c, table, x_start, y_start, cell_size):
    for row_idx, row in enumerate(table):
        for col_idx, num in enumerate(row):
            x = x_start + col_idx * cell_size
            y = y_start - row_idx * cell_size
            c.rect(x, y, cell_size, cell_size, stroke=1, fill=0)
            c.drawString(x + cell_size / 4, y + cell_size / 4, str(num))

def create_pdf(file_name):
    c = canvas.Canvas(file_name, pagesize=A4)
    width, height = A4

    # Set font
    c.setFont("Helvetica", 12)

    def draw_two_tables(y_start):
        # Generate and draw first table
        table1 = generate_schulte_table()
        x_start1 = 4 * cm
        cell_size1 = 2 * cm
        draw_table(c, table1, x_start1, y_start, cell_size1)

        # Generate and draw second table
        table2 = generate_schulte_table()
        x_start2 = 4 * cm
        y_start2 = y_start - (6 * cell_size1)  # Adjust position for second table
        draw_table(c, table2, x_start2, y_start2, cell_size1)

    # Draw tables on first page
    draw_two_tables(height - 4 * cm)
    
    # Add a new page
    c.showPage()

    # Draw tables on second page
    draw_two_tables(height - 4 * cm)

    c.save()

create_pdf("schulte_tables.pdf")

