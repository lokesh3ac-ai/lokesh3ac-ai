import cv2
import numpy as np

RAMP = " .`:-=+*cs#%@"

def get_ascii_rows(image_path="source-prepped.png", width=64):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f"Error: {image_path} not found!")
        return []

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
        # Strict XML character escaping
        escaped = row_str.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")
        rows.append(escaped)
    return rows

def generate_unified_whoami(output_svg="whoami-card.svg"):
    rows = get_ascii_rows(width=64)
    
    font_size = 8
    line_height = 9.2
    
    # Dynamic height calculation taaki koi clipping na ho
    card_w = 860
    card_h = max(390, int(len(rows) * line_height + 60))
    
    # Pulse animation bars
    bar_data = [
        (14, 0.1), (22, 0.3), (35, 0.2), (58, 0.5), (30, 0.4), 
        (78, 0.15), (92, 0.6), (65, 0.25), (80, 0.35), (98, 0.1), 
        (70, 0.45), (42, 0.2), (28, 0.5), (18, 0.3)
    ]
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {card_w} {card_h}" width="{card_w}" height="{card_h}">
  <style>
    .bg {{ fill: #0d1117; stroke: #21262d; stroke-width: 1.5px; rx: 12px; }}
    .ascii {{
      font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace;
      font-size: {font_size}px;
      font-weight: 700;
      fill: #8b949e;
      white-space: pre;
    }}
    .name-text {{
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
      font-size: 18px;
      font-weight: 700;
      fill: #ffffff;
      letter-spacing: 0.8px;
    }}
    .stat-val {{
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
      font-size: 24px;
      font-weight: 700;
      fill: #e6edf3;
    }}
    .stat-label {{
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
      font-size: 11px;
      font-weight: 600;
      fill: #7d8590;
      text-transform: uppercase;
      letter-spacing: 0.7px;
    }}
    .bar {{
      fill: #39d353;
      transform-origin: bottom;
      animation: pulse 1.6s ease-in-out infinite alternate;
    }}
    @keyframes pulse {{
      0% {{ transform: scaleY(0.30); }}
      50% {{ transform: scaleY(1.0); }}
      100% {{ transform: scaleY(0.40); }}
    }}
    @keyframes blink {{
      0%, 100% {{ opacity: 1; }}
      50% {{ opacity: 0; }}
    }}
    .cursor {{
      animation: blink 0.9s infinite;
      fill: #58a6ff;
    }}
  </style>

  <!-- Container Box -->
  <rect width="100%" height="100%" class="bg" />

  <!-- Left: Large ASCII Portrait -->
  <g transform="translate(30, 28)">
'''
    ascii_end_time = 0.0
    for i, r in enumerate(rows):
        y = (i + 1) * line_height
        delay = i * 0.015
        ascii_end_time = delay + 0.08
        svg += f'''    <clipPath id="cp-{i}">
      <rect x="0" y="{y - line_height}" width="0" height="{line_height + 2}">
        <animate attributeName="width" from="0" to="420" dur="0.10s" begin="{delay:.3f}s" fill="freeze" />
      </rect>
    </clipPath>
    <text class="ascii" x="0" y="{y}" clip-path="url(#cp-{i})" xml:space="preserve">{r}</text>\n'''

    # Name right below the photo
    name_y = (len(rows) + 2) * line_height
    name_reveal_delay = ascii_end_time + 0.10

    svg += f'''
    <!-- Animated Name Below Photo -->
    <clipPath id="cp-name">
      <rect x="0" y="{name_y - 20}" width="0" height="26">
        <animate attributeName="width" from="0" to="260" dur="0.75s" begin="{name_reveal_delay:.2f}s" fill="freeze" />
      </rect>
    </clipPath>
    <text class="name-text" x="0" y="{name_y}" clip-path="url(#cp-name)">Lokesh Maurya</text>
    <rect class="cursor" x="145" y="{name_y - 16}" width="8" height="18" rx="1">
      <animate attributeName="x" from="0" to="145" dur="0.75s" begin="{name_reveal_delay:.2f}s" fill="freeze" />
    </rect>
  </g>

  <!-- Vertical Divider -->
  <line x1="445" y1="20" x2="445" y2="{card_h - 20}" stroke="#21262d" stroke-width="1.2" />

  <!-- Right: Real GitHub Stats (2x3 Grid) -->
  <g transform="translate(485, 52)">
    <!-- Row 1 -->
    <text class="stat-val" x="0" y="0">5</text>
    <text class="stat-label" x="0" y="16">REPOSITORIES</text>

    <text class="stat-val" x="180" y="0">61</text>
    <text class="stat-label" x="180" y="16">CONTRIBUTIONS</text>

    <!-- Row 2 -->
    <text class="stat-val" x="0" y="72">48</text>
    <text class="stat-label" x="0" y="88">COMMITS</text>

    <text class="stat-val" x="180" y="72">0</text>
    <text class="stat-label" x="180" y="88">STARS</text>

    <!-- Row 3 -->
    <text class="stat-val" x="0" y="144">0</text>
    <text class="stat-label" x="0" y="160">FOLLOWERS</text>

    <text class="stat-val" x="180" y="144">1.2</text>
    <text class="stat-label" x="180" y="160">AVG/WEEK</text>
  </g>

  <!-- Bottom-Right: Activity Visualizer Bars -->
  <g transform="translate(485, {card_h - 45})">
'''
    for idx, (height, delay) in enumerate(bar_data):
        x = idx * 22
        svg += f'    <rect class="bar" x="{x}" y="-{height}" width="13" height="{height}" rx="2" style="animation-delay: {delay}s;" />\n'

    svg += '''  </g>
</svg>'''

    with open(output_svg, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated clean valid SVG: {output_svg}")

if __name__ == "__main__":
    generate_unified_whoami()