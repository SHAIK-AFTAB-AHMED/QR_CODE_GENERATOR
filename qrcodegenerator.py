import qrcode
from PIL import Image, ImageDraw, ImageFont

# ---------------------------
# QR Code
# ---------------------------
url = "https://leetcode.com/u/SHAIK_AFTAB_AHMED/"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

qr.add_data(url)
qr.make(fit=True)

qr_img = qr.make_image(
    fill_color="orange",
    back_color="white"
).convert("RGB")

# ---------------------------
# Create card background
# ---------------------------
card_width = 800
card_height = 1000

card = Image.new("RGB", (card_width, card_height), "white")
draw = ImageDraw.Draw(card)

# ---------------------------
# Fonts
# ---------------------------
try:
    title_font = ImageFont.truetype("arial.ttf", 50)
    subtitle_font = ImageFont.truetype("arial.ttf", 30)
except:
    title_font = ImageFont.load_default()
    subtitle_font = ImageFont.load_default()

# ---------------------------
# Add Name
# ---------------------------
name = "SHAIK AFTAB AHMED"
title_bbox = draw.textbbox((0, 0), name, font=title_font)
title_width = title_bbox[2] - title_bbox[0]

draw.text(
    ((card_width - title_width)//2, 60),
    name,
    fill="black",
    font=title_font
)

# ---------------------------
# Add Subtitle
# ---------------------------
subtitle = "LeetCode Profile"

sub_bbox = draw.textbbox((0, 0), subtitle, font=subtitle_font)
sub_width = sub_bbox[2] - sub_bbox[0]

draw.text(
    ((card_width - sub_width)//2, 140),
    subtitle,
    fill="gray",
    font=subtitle_font
)

# ---------------------------
# Paste QR Code
# ---------------------------
qr_size = 500
qr_img = qr_img.resize((qr_size, qr_size))

qr_x = (card_width - qr_size)//2
qr_y = 250

card.paste(qr_img, (qr_x, qr_y))

# ---------------------------
# Bottom Text
# ---------------------------
bottom_text = "Scan to view my LeetCode Profile"

bottom_bbox = draw.textbbox((0, 0), bottom_text, font=subtitle_font)
bottom_width = bottom_bbox[2] - bottom_bbox[0]

draw.text(
    ((card_width - bottom_width)//2, 800),
    bottom_text,
    fill="black",
    font=subtitle_font
)

# ---------------------------
# Save
# ---------------------------
card.save("leetcodeprofileqr.png")

print("Saved Successfully!")