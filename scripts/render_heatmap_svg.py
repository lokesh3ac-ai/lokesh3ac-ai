import json

PALETTE = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353", "#69f0a0"]

def render(json_path="data/contributions.json", output_path="contrib-heatmap.svg"):
    with open(json_path, "r") as f:
        days = json.load(f)
        
    weeks = [days[i:i + 7] for i in range(0, len(days), 7)]
    if len(weeks) > 53:
        weeks = weeks[-53:]
        
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 140" width="860" height="140">
  <style>
    .box { rx: 2px; ry: 2px; }
    .term-title { font-family: monospace; font-size: 12px; fill: #8b949e; }
  </style>
  <rect width="100%" height="100%" fill="#0d1117" rx="8" stroke="#30363d" stroke-width="1"/>
  <text x="20" y="24" class="term-title">Contributions Calendar (Past 53 Weeks)</text>
  <g transform="translate(20, 38)">
'''
    for col, week in enumerate(weeks):
        for row, day in enumerate(week):
            lvl = min(day.get("level", 0), len(PALETTE) - 1)
            color = PALETTE[lvl]
            x = col * 15
            y = row * 12
            svg += f'    <rect class="box" x="{x}" y="{y}" width="11" height="9" fill="{color}"/>\n'
            
    svg += '''  </g>
</svg>'''
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Rendered {output_path}")

if __name__ == "__main__":
    render()