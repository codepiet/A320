posx = 0
posy = 0
total = 0

# Farben für xTool Studio Layer:
COLOR_CUT      = "#ff0000"  # Rot    → Schneiden
COLOR_ENGRAVE  = "#0000ff"  # Blau   → Flächengravur

def advance_position():
    global posx,posy,total
    if posx >= 17 * 16:  # 17 Buttons pro Reihe
        posx = 0
        posy += 17
    else:
        posx += 17
    total+=1

def make_button(label_top, label_bottom, box_bottom=False,
                scale_top=1.0, scale_bottom=1.0, box_width=10):
    box = ""
    if box_bottom:
        box_x = (17 - box_width) / 2
        box = f'<rect x="{box_x}" y="9.5" width="{box_width}" height="5" fill="none" stroke="{COLOR_ENGRAVE}" stroke-width="0.5"/>'

    arrow = ""
    poly = ""
    if label_bottom == "CAPT":
        # Blockpfeil nach rechts →
        poly =  "4,3.5 10,3.5 10,2.0 13,4.5 10,7.0 10,5.5 4,5.5"
    elif label_bottom == "F/O":
        # Blockpfeil nach links ←
        poly = "13,3.5 7,3.5 7,2.0 4,4.5 7,7.0 7,5.5 13,5.5"
    arrow = f"""<polygon points="{poly}" fill="none" stroke="{COLOR_ENGRAVE}" stroke-width="0.5" stroke-linejoin="round"/>"""


    s = f"""
  <g transform="translate({posx}, {posy})">
    <rect x="0" y="0" width="17" height="17" rx="1" ry="1"
      stroke="{COLOR_CUT}" stroke-width="0.1" fill="none"/>
    <g transform="translate(8.5, 5.8) scale({scale_top}, 1)">
      <text x="0" y="0" font-family="'Arial Narrow'"
        font-size="4.2" font-weight="bold" fill="{COLOR_ENGRAVE}"
        text-anchor="middle" dominant-baseline="middle"
        letter-spacing="0.05">{label_top}</text>
    </g>
    {box}
    {arrow}
    <g transform="translate(8.5, 12.3) scale({scale_bottom}, 1)">
      <text x="0" y="0" font-family="'Arial Narrow'"
        font-size="4.2" font-weight="bold" fill="{COLOR_ENGRAVE}"
        text-anchor="middle" dominant-baseline="middle"
        letter-spacing="0.05">{label_bottom}</text>
    </g>
  </g>"""
    advance_position()
    return s

def make_button_wide(label_top, scale_top=1.0):
    button_w = 22
    button_h = 13

    s = f"""
  <g transform="translate({posx}, {posy})">
    <rect x="0" y="0" width="{button_w}" height="{button_h}" rx="1" ry="1"
      stroke="{COLOR_CUT}" stroke-width="0.1" fill="none"/>
    <g transform="translate({button_w / 2}, 7) scale({scale_top}, 1)">
      <text x="0" y="0" font-family="'Arial Narrow'"
        font-size="4.2" font-weight="bold" fill="{COLOR_ENGRAVE}"
        text-anchor="middle" dominant-baseline="middle"
        letter-spacing="0.05">{label_top}</text>
    </g>
  </g>"""
    advance_position()
    return s

content = ""

content += make_button("SYS ON", "", scale_top=0.8)
content += make_button("CALL","ON", box_bottom=True, scale_top=0.8)
content += make_button("EVAC", "ON", box_bottom=True, scale_top=0.8)
content += make_button("SMOKE","OFF", box_bottom=True, scale_top=0.8)
for i in range(3):
    content += make_button("FAULT", "", scale_top=0.8)
for i in range(38):
    content += make_button("FAULT", "OFF", box_bottom=True, scale_top=0.8)
for i in range(6):
    content += make_button("", "OFF", box_bottom=True)
content += make_button("", "OFF", scale_bottom=0.8)
for i in range(8):
    content += make_button("", "ON", box_bottom=True)
for i in range(5):
    content += make_button("FAULT", "ON", box_bottom=True, scale_top=0.8)
content += make_button("FAULT", "MAN", box_bottom=True, scale_top=0.8)
for i in range(2):
    content += make_button("AVAIL", "ON", box_bottom=True, scale_top=0.8)
content += make_button("FAULT", "ALTN", box_bottom=True, scale_top=0.8, box_width=12)
content += make_button("OPEN", "ON", box_bottom=True, scale_top=0.8)
for i in range(5):
    content += make_button("SQUIB", "DISCH", box_bottom=True, scale_top=0.8, box_width=12)
for i in range(2):
    content += make_button("SMOKE", "", scale_top=0.8)
content += make_button("DISCH", "AGENT 1", scale_top=0.8, scale_bottom=0.8)
content += make_button("DISCH", "AGENT 2", scale_top=0.8, scale_bottom=0.8)
content += make_button("DISCH 1", "DISCH 2", scale_top=0.8, scale_bottom=0.8)
for i in range(2): 
    content += make_button("FAULT", "OVRD", box_bottom=True, scale_top=0.8, box_width=12)

content += make_button("MASTER", "WARN")
content += make_button("MASTER", "WARN")
content += make_button("MASTER", "CAUT")
content += make_button("MASTER", "CAUT")
content += make_button("AUTO", "LAND")
content += make_button("AUTO", "LAND")
content += make_button("ATC", "MSG")
content += make_button("ATC", "MSG")
content += make_button("", "CAPT", box_bottom=True, box_width=12)
content += make_button("", "F/O", box_bottom=True, box_width=12)
for i in range(2): 
    content += make_button("OPEN", "FAULT", scale_top=0.8, scale_bottom=0.8)
content += make_button("DISCH 1", "DISCH 2", scale_top=0.8, scale_bottom=0.8)
for i in range(2): 
    content += make_button("FIRE", "FAULT", scale_top=0.8, scale_bottom=0.8)
for i in range(2): 
    content += make_button("PULL UP", "GPWS", scale_top=0.8, scale_bottom=0.8)
content +=make_button_wide("ON BAT", scale_top=1.2)

svg_width = 17 * 17  # 17mm pro Button, 17 Buttons pro Reihe
svg_height = posy + 17

svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="{svg_width}mm" height="{svg_height}mm" viewBox="0 0 {svg_width} {svg_height}">\n'
svg += content
svg += "\n</svg>"

with open("A320-korrys.svg", "w") as f:
    f.write(svg)

print("A320-korrys.svg wurde erstellt!")