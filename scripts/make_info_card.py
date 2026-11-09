def make_card(output_path="info-card.svg"):
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 490 280" width="490" height="280">
  <style>
    .term { font-family: 'Courier New', monospace; font-size: 13px; fill: #c9d1d9; }
    .green { fill: #3fb950; font-weight: bold; }
    .cyan { fill: #58a6ff; font-weight: bold; }
    .purple { fill: #bc8cff; font-weight: bold; }
    .yellow { fill: #d29922; font-weight: bold; }
    .gray { fill: #8b949e; }
    .fade { animation: fadeIn 0.4s ease forwards; opacity: 0; }
    @keyframes fadeIn { to { opacity: 1; } }
  </style>
  <rect width="100%" height="100%" fill="#0d1117" rx="8" stroke="#30363d" stroke-width="1"/>
  
  <!-- Terminal Header -->
  <circle cx="20" cy="18" r="5" fill="#ff5f56"/>
  <circle cx="36" cy="18" r="5" fill="#ffbd2e"/>
  <circle cx="52" cy="18" r="5" fill="#27c93f"/>
  <text x="75" y="22" class="term gray" font-size="11">lokesh@developer-rig ~ neofetch</text>
  <line x1="0" y1="34" x2="490" y2="34" stroke="#30363d" stroke-width="1"/>

  <text class="term" x="25" y="65">
    <tspan class="green fade" style="animation-delay: 0.1s;">lokesh</tspan><tspan class="gray">@</tspan><tspan class="green fade" style="animation-delay: 0.1s;">github</tspan>
    <tspan x="25" dy="14" class="gray fade" style="animation-delay: 0.2s;">------------------------------------</tspan>
    <tspan x="25" dy="22" class="cyan fade" style="animation-delay: 0.3s;">OS       :</tspan><tspan class="fade" style="animation-delay: 0.3s;"> Arch Linux / Windows 11</tspan>
    <tspan x="25" dy="20" class="cyan fade" style="animation-delay: 0.4s;">Focus    :</tspan><tspan class="fade" style="animation-delay: 0.4s;"> AI / ML &amp; Full-Stack Systems</tspan>
    <tspan x="25" dy="20" class="cyan fade" style="animation-delay: 0.5s;">Stack    :</tspan><tspan class="fade" style="animation-delay: 0.5s;"> Python, Flask, PyTorch, C++, JS</tspan>
    <tspan x="25" dy="20" class="cyan fade" style="animation-delay: 0.6s;">Projects :</tspan><tspan class="fade" style="animation-delay: 0.6s;"> Defect Monitoring, Sentiment AI</tspan>
    <tspan x="25" dy="20" class="cyan fade" style="animation-delay: 0.7s;">Editor   :</tspan><tspan class="fade" style="animation-delay: 0.7s;"> VS Code &amp; Terminal</tspan>
    <tspan x="25" dy="24" class="purple fade" style="animation-delay: 0.8s;">Status   :</tspan><tspan class="fade" style="animation-delay: 0.8s;"> Shipping intelligent systems</tspan>
    
    <!-- Color Palette Blocks -->
    <tspan x="25" dy="30" class="fade" style="animation-delay: 0.9s;">
      <tspan fill="#ff7b72">███ </tspan>
      <tspan fill="#7ee787">███ </tspan>
      <tspan fill="#d29922">███ </tspan>
      <tspan fill="#79c0ff">███ </tspan>
      <tspan fill="#d2a8ff">███ </tspan>
      <tspan fill="#f0883e">███ </tspan>
    </tspan>
  </text>
</svg>'''
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    make_card()