import cv2
import numpy as np

RAMP = " .`:-=+*cs#%@"

def generate_ascii_svg(image_path="source-prepped.png", output_svg="portrait-ascii.svg", width=65):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f"Error: Could not read {image_path}")
        return

    h, w = img.shape
    aspect = h / w
    height = int(width * aspect * 0.55)
    resized = cv2.resize(img, (width, height))
    
    rows = []
    for r in range(height):
        line = ""
        for c in range(width):
            val = resized[r, c]
            idx = int((val / 255.0) * (len(RAMP) - 1))
            line += RAMP[idx]
        # XML-safe escaping
        escaped_line = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        rows.append(escaped_line)

    font_size = 7
    line_height = 8.5
    svg_w = 370
    svg_h = height * line_height + 30

    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_w} {svg_h}" width="{svg_w}" height="{svg_h}">
  <style>
    .ascii {{
      font-family: 'Courier New', monospace;
      font-size: {font_size}px;
      fill: #8b949e;
      white-space: pre;
    }}
    @keyframes lineFadeIn {{
      from {{ opacity: 0; }}
      to {{ opacity: 1; }}
    }}
    .line {{
      opacity: 0;
      animation: lineFadeIn 0.05s ease forwards;
    }}
  </style>
  <rect width="100%" height="100%" fill="#0d1117" rx="8" stroke="#30363d" stroke-width="1"/>
  <text class="ascii" x="15" y="20" xml:space="preserve">
'''
    for i, row in enumerate(rows):
        y_pos = 20 + i * line_height
        delay = i * 0.03
        svg_content += f'    <tspan class="line" x="15" y="{y_pos}" style="animation-delay: {delay:.2f}s;">{row}</tspan>\n'

    svg_content += '''  </text>
</svg>'''

    with open(output_svg, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Regenerated valid {output_svg}")

if __name__ == "__main__":
    generate_ascii_svg()