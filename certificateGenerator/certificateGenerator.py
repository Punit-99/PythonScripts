import os
from PIL import Image, ImageDraw, ImageFont
import pandas as pd

def generate_certificate_from_excel():
    try:
        # EXCEL PATH
        excel_path = input("Enter the path to the Excel file containing names: ").strip('\"')

        # TEMPLATE PATH
        template_path = input("Enter the path to the certificate template image: ").strip('\"')

        # FONT PATH
        font_path = input("Enter the path to the font file: ").strip('\"')

        # FONT SIZE
        font_size_input = input("Enter font size (default is 45): ")
        font_size = int(font_size_input) if font_size_input.strip() else 45

        # COLOUR 
        color_input = input("Enter text color in hex, press Enter for default (black): ")
        text_color = color_input if color_input.strip() else "#000000"

        # COLUMN NAME CONTAINING NAMES
        column_name = input("Enter the name of the column containing names in the Excel file: ")

    #     X&Y OFFSET
        x_offset = 0
        y_offset = 0

        names_df = pd.read_excel(excel_path)
        font = ImageFont.truetype(font_path, font_size)
        template = Image.open(template_path)
        image_width, image_height = template.size

        output_dir = os.getcwd()

        folder_name = "Certificates"
        folder_path = os.path.join(output_dir, folder_name)
        os.makedirs(folder_path, exist_ok=True)

        for index, row in names_df.iterrows():
            name = row[column_name]

            certificate = template.copy()

            draw = ImageDraw.Draw(certificate)

            center_x = image_width // 2
            center_y = image_height // 2

            x = center_x + x_offset
            y = center_y + y_offset
            vertical_gap = font_size + 10

            text_width = font.getlength(name)

            text_height = font_size * name.count('\n')

            text_x = x - text_width // 2
            text_y = y - text_height // 2

            draw.text((text_x, text_y), name, fill=text_color, font=font)

            certificate_name = f"{name}_certificate.png"
            output_path = os.path.join(folder_path, certificate_name)
            certificate.save(output_path)

            print(f"Certificate for '{name}' generated successfully and saved as '{output_path}'.")

    except Exception as e:
        print("Error: Certificate generation failed. {}".format(e))

generate_certificate_from_excel()
