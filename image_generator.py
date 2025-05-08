from PIL import Image, ImageDraw, ImageFont
import os
import uuid

def create_branded_image(keywords, output_dir):
    # Create a simple background image (blue gradient)
    width, height = 800, 400
    image = Image.new("RGB", (width, height), color=(0, 100, 200))
    
    # Add text overlay
    draw = ImageDraw.Draw(image)
    try:
        font = ImageFont.truetype("arial.ttf", 40)  # Use default font
    except:
        font = ImageFont.load_default()  # Fallback if font not found

    # Center the keywords text
    text = keywords.upper()
    # Use textbbox to get text dimensions
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    text_position = ((width - text_width) // 2, (height - text_height) // 2)
    draw.text(text_position, text, fill=(255, 255, 255), font=font)

    # Save image with unique filename
    filename = f"branded_image_{uuid.uuid4()}.png"
    output_path = os.path.join(output_dir, filename)
    image.save(output_path)

    return output_path