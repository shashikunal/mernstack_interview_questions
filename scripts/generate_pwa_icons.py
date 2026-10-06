from PIL import Image, ImageDraw, ImageFont
import math

def create_icon(size, filename):
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # 1. Background Rounded Rect / Squircle
    margin = int(size * 0.04)
    r = int(size * 0.22)
    
    # Outer Glow / Border
    draw.rounded_rectangle(
        [margin, margin, size - margin, size - margin],
        radius=r,
        fill=(11, 15, 25, 255),
        outline=(56, 189, 248, 120),
        width=max(2, int(size * 0.015))
    )

    # Gradient circle accent
    cx, cy = size // 2, size // 2
    circ_r = int(size * 0.36)
    
    # Radial glow ring
    for i in range(10, 0, -1):
        alpha = int(12 * (1 - i / 10.0))
        draw.ellipse([cx - circ_r - i*2, cy - circ_r - i*2, cx + circ_r + i*2, cy + circ_r + i*2], 
                     outline=(139, 92, 246, alpha), width=3)

    # Core colored disc
    draw.ellipse([cx - circ_r, cy - circ_r, cx + circ_r, cy + circ_r],
                 fill=(26, 36, 59, 255), outline=(56, 189, 248, 200), width=max(2, int(size * 0.012)))

    # 2. Draw Lightning Bolt Polygon (⚡)
    scale = size / 512.0
    
    # Points relative to 512x512
    bolt_pts = [
        (280 * scale, 100 * scale),
        (170 * scale, 260 * scale),
        (250 * scale, 260 * scale),
        (220 * scale, 412 * scale),
        (350 * scale, 230 * scale),
        (270 * scale, 230 * scale),
    ]

    # Bolt glow shadow
    shadow_offset = int(4 * scale)
    shadow_pts = [(x, y + shadow_offset) for x, y in bolt_pts]
    draw.polygon(shadow_pts, fill=(2, 132, 199, 140))

    # Lightning bolt body (Vibrant Gold / Cyan Gradient look)
    draw.polygon(bolt_pts, fill=(250, 204, 21, 255), outline=(255, 255, 255, 220))

    # Inner highlight line
    hl_pts = [
        (275 * scale, 120 * scale),
        (190 * scale, 250 * scale),
        (260 * scale, 250 * scale)
    ]
    draw.line(hl_pts, fill=(255, 255, 255, 240), width=max(2, int(size * 0.01)))

    img.save(filename, 'PNG')
    print(f"Generated: {filename} ({size}x{size})")

if __name__ == '__main__':
    create_icon(192, 'icon-192.png')
    create_icon(512, 'icon-512.png')
    create_icon(192, 'netlify-deploy/icon-192.png')
    create_icon(512, 'netlify-deploy/icon-512.png')
