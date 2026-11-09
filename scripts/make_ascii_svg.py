import cv2
import numpy as np

RAMP = " .`:-=+*cs#%@"

def generate_ascii_svg(image_path="source-prepped.png", output_svg="portrait-ascii.svg", width=55):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f"Error: {image_path} nahi mila!")
        return

    h, w = img.shape
    aspect = h / w
    height = int(width * aspect * 0.52)
    resized = cv2.resize(img, (width, height))

    rows = []
    for r in range(height):
        row_str = ""
        for c in range(width):
            val = resized[r, c]
            idx = int((val / 255.0) * (len(RAMP) - 1))
            row_str += RAMP[idx]
        rows.append(row_str)

    font_size = 7.5
    line_height = 8.5
    svg_w = 370
    svg_h = height * line_height + 25

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_w} {svg_h}" width="{svg_w}" height="{svg_h}">
  <style>
    .bg {{ fill: #0d1117; stroke: #30363d; stroke-width: 1px; rx: 8px; }}
    .ascii {{
      font-family: 'Courier New', Courier, monospace;
      font-size: {font_size}px;
      font-weight: bold;
      fill: #8b949e;
      white-space: pre;
    }}
  </style>
  <rect width="100%" height="100%" class="bg" />
'''

    # Har row ko horizontal wipe clip dekar typewriter effect create karte hain
    for i, row in enumerate(rows):
        y_pos = 20 + (i * line_height)
        delay = i * 0.035
        escaped_row = row.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

        svg += f'''  <clipPath id="clip-{i}">
    <rect x="15" y="{y_pos - line_height + 2}" width="0" height="{line_height + 2}">
      <animate attributeName="width" from="0" to="{svg_w - 30}" dur="0.12s" begin="{delay:.3f}s" fill="freeze" />
    </rect>
  </clipPath>
  <text class="ascii" x="15" y="{y_pos}" clip-path="url(#clip-{i})" xml:space="preserve">{escaped_row}</text>
'''

    svg += '</svg>'

    with open(output_svg, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated animated SVG: {output_svg}")

if __name__ == "__main__":
    generate_ascii_svg()