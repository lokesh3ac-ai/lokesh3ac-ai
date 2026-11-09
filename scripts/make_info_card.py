import cv2
import numpy as np

RAMP = " .`:-=+*cs#%@"

def get_ascii_rows(image_path="source-prepped.png", width=62):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f"Error: {image_path} nahi mila!")
        return []
    h, w = img.shape
    aspect = h / w
    height = int(width * aspect * 0.50)
    resized = cv2.resize(img, (width, height))
    
    rows = []
    for r in range(height):
        row_str = ""
        for c in range(width):
            val = resized[r, c]
            idx = int((val / 255.0) * (len(RAMP) - 1))
            row_str += RAMP[idx]
        rows.append(row_str.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))
    return rows

def generate_unified_whoami(output_svg="whoami-card.svg"):
    rows = get_ascii_rows()
    
    card_w = 860
    card_h = 390
    
    font_size = 7
    line_height = 8.2
    
    # Activity bars data: (height, delay)
    bar_data = [
        (15, 0.1), (28, 0.3), (45, 0.2), (72, 0.5), (38, 0.4), 
        (85, 0.15), (60, 0.6), (75, 0.25), (50, 0.35), (95, 0.1), 
        (65, 0.45), (35, 0.2), (22, 0.5)
    ]
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {card_w} {card_h}" width="{card_w}" height="{card_h}">
  <style>
    .bg {{ fill: #0d1117; stroke: #21262d; stroke-width: 1.5px; rx: 12px; }}
    .ascii {{
      font-family: 'SFMono-Regular', Consolas, 'Courier New', monospace;
      font-size: {font_size}px;
      font-weight: 600;
      fill: #8b949e;
      white-space: pre;
    }}
    .name-text {{
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
      font-size: 17px;
      font-weight: 700;
      fill: #ffffff;
      letter-spacing: 0.8px;
    }}
    .stat-val {{
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
      font-size: 21px;
      font-weight: 700;
      fill: #e6edf3;
    }}
    .stat-label {{
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
      font-size: 11px;
      font-weight: 600;
      fill: #7d8590;
      text-transform: uppercase;
      letter-spacing: 0.6px;
    }}
    .bar {{
      fill: #39d353;
      transform-origin: bottom;
      animation: pulse 1.6s ease-in-out infinite alternate;
    }}
    @keyframes pulse {{
      0% {{ transform: scaleY(0.28); }}
      50% {{ transform: scaleY(1.0); }}
      100% {{ transform: scaleY(0.42); }}
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

  <!-- Left: Large Animated Typing ASCII Art -->
  <g transform="translate(25, 25)">
'''
    ascii_end_time = 0.0
    for i, r in enumerate(rows):
        y = i * line_height
        delay = i * 0.02
        ascii_end_time = delay + 0.10
        svg += f'''    <clipPath id="cp-{i}">
      <rect x="0" y="{y - line_height + 2}" width="0" height="{line_height + 2}">
        <animate attributeName="width" from="0" to="400" dur="0.10s" begin="{delay:.3f}s" fill="freeze" />
      </rect>
    </clipPath>
    <text class="ascii" x="0" y="{y}" clip-path="url(#cp-{i})" xml:space="preserve">{r}</text>\n'''

    # Photo ke theek neeche typing animated "Lokesh Maurya" with terminal cursor
    name_y = len(rows) * line_height + 18
    name_reveal_delay = ascii_end_time + 0.15

    svg += f'''
    <!-- Animated Name Below Photo -->
    <clipPath id="cp-name">
      <rect x="0" y="{name_y - 20}" width="0" height="26">
        <animate attributeName="width" from="0" to="240" dur="0.8s" begin="{name_reveal_delay:.2f}s" fill="freeze" />
      </rect>
    </clipPath>
    <text class="name-text" x="0" y="{name_y}" clip-path="url(#cp-name)">Lokesh Maurya</text>
    <rect class="cursor" x="135" y="{name_y - 15}" width="8" height="17" rx="1">
      <animate attributeName="x" from="0" to="135" dur="0.8s" begin="{name_reveal_delay:.2f}s" fill="freeze" />
    </rect>
  </g>

  <!-- Vertical Divider Line -->
  <line x1="435" y1="25" x2="435" y2="365" stroke="#21262d" stroke-width="1.2" />

  <!-- Right: Metrics Grid (2x3) -->
  <g transform="translate(480, 52)">
    <!-- Row 1 -->
    <text class="stat-val" x="0" y="0">149</text>
    <text class="stat-label" x="0" y="16">REPOSITORIES</text>

    <text class="stat-val" x="175" y="0">149</text>
    <text class="stat-label" x="175" y="16">CONTRIBUTIONS</text>

    <!-- Row 2 -->
    <text class="stat-val" x="0" y="70">8,504</text>
    <text class="stat-label" x="0" y="86">COMMITS</text>

    <text class="stat-val" x="175" y="70">362</text>
    <text class="stat-label" x="175" y="86">STARS</text>

    <!-- Row 3 -->
    <text class="stat-val" x="0" y="140">128</text>
    <text class="stat-label" x="0" y="156">FOLLOWERS</text>

    <text class="stat-val" x="175" y="140">23.5</text>
    <text class="stat-label" x="175" y="156">AVG/WEEK</text>
  </g>

  <!-- Bottom-Right: Activity Visualizer Bars -->
  <g transform="translate(480, 320)">
'''
    for idx, (height, delay) in enumerate(bar_data):
        x = idx * 24
        svg += f'    <rect class="bar" x="{x}" y="-{height}" width="13" height="{height}" rx="2" style="animation-delay: {delay}s;" />\n'

    svg += '''  </g>
</svg>'''

    with open(output_svg, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Regenerated unified whoami card: {output_svg}")

if __name__ == "__main__":
    generate_unified_whoami()