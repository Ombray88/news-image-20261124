import os
from PIL import Image, ImageDraw, ImageFont

def create_entry():
    os.makedirs("/output", exist_ok=True)
    width, height = 1600, 1735
    img = Image.new("RGB", (width, height), "#F8F6F0")
    draw = ImageDraw.Draw(img)

    # Fonts
    font_path_regular = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    font_path_bold = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    
    font_title = ImageFont.truetype(font_path_bold, 56)
    font_kicker = ImageFont.truetype(font_path_bold, 20)
    font_subtitle = ImageFont.truetype(font_path_regular, 22)
    font_section = ImageFont.truetype(font_path_bold, 28)
    font_hero_h = ImageFont.truetype(font_path_bold, 26)
    font_hero_deck = ImageFont.truetype(font_path_regular, 16)
    font_badge = ImageFont.truetype(font_path_bold, 18)
    font_grid_h = ImageFont.truetype(font_path_bold, 18)
    font_grid_deck = ImageFont.truetype(font_path_regular, 14)
    font_tag = ImageFont.truetype(font_path_bold, 12)
    font_body = ImageFont.truetype(font_path_regular, 14)
    font_footer = ImageFont.truetype(font_path_regular, 13)

    # Colors
    c_bg = "#F8F6F0"
    c_card = "#FFFFFF"
    c_border = "#D3CFC9"
    c_text_dark = "#1A1A1A"
    c_text_muted = "#555555"
    
    # Continent colors
    continents = {
        "Europe": "#2B547E",
        "Asia": "#B22222",
        "Africa": "#2E8B57",
        "North America": "#D35400",
        "South America": "#8E44AD",
        "Oceania": "#16A085"
    }

    # 1. Masthead
    draw.rectangle([40, 30, width - 40, 160], fill="#1A1A24")
    draw.text((60, 45), "THE DAY IN WORLD NEWS", fill="#E67E22", font=font_kicker)
    draw.text((60, 72), "TUESDAY 24 NOVEMBER 2026", fill="#FFFFFF", font=font_title)
    draw.text((60, 132), "35 stories · 6 continents", fill="#CCCCCC", font=font_subtitle)

    # Continent Legend on Masthead right
    legend_x = 950
    legend_y = 50
    for name, col in continents.items():
        draw.rectangle([legend_x, legend_y, legend_x + 14, legend_y + 14], fill=col)
        draw.text((legend_x + 20, legend_y - 2), name, fill="#FFFFFF", font=ImageFont.truetype(font_path_regular, 14))
        legend_x += 115
        if legend_x > 1450:
            legend_x = 950
            legend_y += 24

    # 2. Hero Panels (Stories 1-3)
    hero_y = 185
    hero_w = (width - 80 - 40) // 3  # 460 each
    hero_h = 240
    
    heroes = [
        ("1. LIBYA", "WARSHIP SUNK OFF BENGHAZI", "Ukraine says its sea drones sank the Russian corvette Merkury and disabled MV Angara off Benghazi.", "7 SEA DRONES", "Africa", continents["Africa"]),
        ("2. NVIDIA", "HUANG IS BACK", "Jensen Huang reinstated as Nvidia CEO after Trump intervenes; Nvidia shares surge 31% at open.", "+31%", "North America", continents["North America"]),
        ("3. INDONESIA", "24 DEAD IN FACTORY FIRE", "Fire rips through a candy factory in Indonesia, killing 24 workers and injuring dozens.", "24 DEAD", "Asia", continents["Asia"])
    ]

    for i, (num_title, head, deck, badge, cont, c_col) in enumerate(heroes):
        hx = 40 + i * (hero_w + 20)
        # Card background
        draw.rectangle([hx, hero_y, hx + hero_w, hero_y + hero_h], fill=c_card, outline=c_border, width=2)
        # Top color accent bar
        draw.rectangle([hx, hero_y, hx + hero_w, hero_y + 6], fill=c_col)
        
        draw.text((hx + 15, hero_y + 18), num_title, fill=c_col, font=font_kicker)
        draw.text((hx + 15, hero_y + 45), head, fill=c_text_dark, font=font_hero_h)
        
        # Deck wrapping
        words = deck.split()
        lines = []
        curr_line = ""
        for w in words:
            test_line = curr_line + " " + w if curr_line else w
            if draw.textlength(test_line, font=font_hero_deck) < hero_w - 30:
                curr_line = test_line
            else:
                lines.append(curr_line)
                curr_line = w
        if curr_line:
            lines.append(curr_line)
        
        ly = hero_y + 82
        for line in lines[:3]:
            draw.text((hx + 15, ly), line, fill=c_text_muted, font=font_hero_deck)
            ly += 22

        # Data Badge
        bw = draw.textlength(badge, font=font_badge) + 24
        bx = hx + hero_w - bw - 15
        by = hero_y + hero_h - 45
        draw.rectangle([bx, by, bx + bw, by + 30], fill=c_col)
        draw.text((bx + 12, by + 6), badge, fill="#FFFFFF", font=font_badge)

    # 3. Numbered Grid Stories 4-15 (3 columns x 4 rows)
    grid_start_y = 445
    draw.text((40, grid_start_y), "MAJOR STORIES (4–15)", fill=c_text_dark, font=font_section)
    
    grid_y = grid_start_y + 40
    gw = (width - 80 - 40) // 3 # 460
    gh = 110
    
    grid_stories = [
        (4, "GAZA", "ISRAELI STRIKES KILL 3 IN GAZA", "Al Jazeera: Strikes kill 3 including UNRWA worker.", "CONFLICT", continents["Asia"]),
        (5, "IRAN", "TRUMP WARNS IRAN: 'VERY TRAUMATIC'", "Warns of traumatic outcome if nuclear deal fails.", "DIPLOMACY", continents["Asia"]),
        (6, "CLIMATE", "COP31 FAILURE SPARKS OUTRAGE", "Talks in Türkiye end without cover decision; Australia reacts.", "CLIMATE", continents["Oceania"]),
        (7, "UKRAINE", "STRIKE ON ZAPORIZHZHIA KILLS 2", "Russian strike on Zaporizhzhia kills two and injures dozens.", "CONFLICT", continents["Europe"]),
        (8, "INDIA", "INDIA 3RD IN ASIA POWER INDEX", "Ranks 3rd in Lowy Index 2026, overtaking Russia.", "POWER", continents["Asia"]),
        (9, "TRADE", "TRUMP ANNOUNCES JAPAN DEAL", "Trade deal agreed; Tokyo's Nikkei leads Asian rally.", "TRADE", continents["Asia"]),
        (10, "HORMUZ", "RECORD IRANIAN ATTACKS IN HORMUZ", "UK logs record attacks on shipping amid rising tensions.", "SECURITY", continents["Asia"]),
        (11, "SUDAN", "UN CONDEMNS KHARTOUM STRIKES", "Denounces drone strikes on Khartoum including UN building.", "CONFLICT", continents["Africa"]),
        (12, "CONGO", "FIGHTING TRAPS EBOLA TEAMS", "Heavy fighting in Ituri traps Ebola responders for 24h.", "HEALTH", continents["Africa"]),
        (13, "TECH", "STATES SUE SPACEX OVER IMAGES", "Oregon & Virginia sue over Grok child abuse images.", "TECH", continents["North America"]),
        (14, "TENNIS", "ALCARAZ WINS FIRST ATP FINALS", "Beats Alexander Zverev in straight sets in Turin.", "SPORT", continents["Europe"]),
        (15, "FOOTBALL", "BRENTFORD BEAT EVERTON", "Lewis-Potter scores twice; Brentford climb to sixth.", "SPORT", continents["Europe"])
    ]

    for idx, (num, cat, head, deck, tag, c_col) in enumerate(grid_stories):
        col_i = idx % 3
        row_i = idx // 3
        gx = 40 + col_i * (gw + 20)
        gy = grid_y + row_i * (gh + 12)
        
        draw.rectangle([gx, gy, gx + gw, gy + gh], fill=c_card, outline=c_border, width=1)
        draw.rectangle([gx, gy, gx + 4, gy + gh], fill=c_col)
        
        # Number & Category tag
        draw.text((gx + 15, gy + 10), f"{num}. {cat}", fill=c_col, font=font_tag)
        
        # Headline
        draw.text((gx + 15, gy + 28), head, fill=c_text_dark, font=font_grid_h)
        
        # Deck
        draw.text((gx + 15, gy + 56), deck, fill=c_text_muted, font=font_grid_deck)

    # 4. Bottom Section: World Map (Left) & ALSO ON 24 NOVEMBER (Right)
    bot_y = grid_y + 4 * (gh + 12) + 20
    draw.line([40, bot_y, width - 40, bot_y], fill=c_border, width=2)
    bot_y += 20

    # Left: World Map "WHERE IT HAPPENED"
    map_w = 750
    map_h = 650
    draw.rectangle([40, bot_y, 40 + map_w, bot_y + map_h], fill="#111827", outline=c_border, width=2)
    draw.text((60, bot_y + 15), "WHERE IT HAPPENED · STORIES (1–15)", fill="#FFFFFF", font=font_section)

    # Draw simplified stylized world map continents
    # North America
    draw.rounded_rectangle([90, bot_y + 90, 320, bot_y + 280], radius=15, fill="#1E293B", outline="#334155")
    draw.text((110, bot_y + 105), "NORTH AMERICA", fill="#64748B", font=font_tag)
    # South America
    draw.rounded_rectangle([220, bot_y + 300, 360, bot_y + 500], radius=15, fill="#1E293B", outline="#334155")
    draw.text((235, bot_y + 315), "SOUTH AMERICA", fill="#64748B", font=font_tag)
    # Europe
    draw.rounded_rectangle([390, bot_y + 80, 520, bot_y + 200], radius=15, fill="#1E293B", outline="#334155")
    draw.text((405, bot_y + 95), "EUROPE", fill="#64748B", font=font_tag)
    # Africa
    draw.rounded_rectangle([400, bot_y + 220, 550, bot_y + 450], radius=15, fill="#1E293B", outline="#334155")
    draw.text((415, bot_y + 235), "AFRICA", fill="#64748B", font=font_tag)
    # Asia
    draw.rounded_rectangle([540, bot_y + 70, 740, bot_y + 330], radius=15, fill="#1E293B", outline="#334155")
    draw.text((555, bot_y + 85), "ASIA", fill="#64748B", font=font_tag)
    # Oceania
    draw.rounded_rectangle([630, bot_y + 360, 750, bot_y + 500], radius=15, fill="#1E293B", outline="#334155")
    draw.text((645, bot_y + 375), "OCEANIA", fill="#64748B", font=font_tag)

    # Plot pins for 1-15 on map
    pin_coords = {
        1: (460, bot_y + 160),  # Libya (Africa)
        2: (180, bot_y + 180),  # Nvidia / USA (NA)
        3: (670, bot_y + 270),  # Indonesia (Asia)
        4: (520, bot_y + 210),  # Gaza (Asia)
        5: (580, bot_y + 190),  # Iran (Asia)
        6: (690, bot_y + 420),  # Australia / COP31 (Oceania)
        7: (440, bot_y + 130),  # Ukraine (Europe)
        8: (640, bot_y + 220),  # India (Asia)
        9: (710, bot_y + 180),  # Japan (Asia)
        10: (600, bot_y + 215), # Hormuz (Asia)
        11: (470, bot_y + 270), # Sudan (Africa)
        12: (490, bot_y + 310), # Congo (Africa)
        13: (140, bot_y + 140), # SpaceX / USA (NA)
        14: (430, bot_y + 140), # Alcaraz / Italy (Europe)
        15: (410, bot_y + 120), # Brentford / UK (Europe)
    }

    for num, (px, py) in pin_coords.items():
        draw.ellipse([px - 10, py - 10, px + 10, py + 10], fill="#E67E22", outline="#FFFFFF", width=2)
        text_w = draw.textlength(str(num), font=font_tag)
        draw.text((px - text_w / 2, py - 6), str(num), fill="#FFFFFF", font=font_tag)

    # Briefs 16-35 small dots on map
    brief_coords = [
        (450, bot_y + 110), # 16 EU
        (425, bot_y + 125), # 17 Poland
        (465, bot_y + 135), # 18 Putin/Zelensky
        (445, bot_y + 145), # 19 Germany
        (435, bot_y + 155), # 20 Greece
        (415, bot_y + 115), # 21 Estonia
        (720, bot_y + 150), # 22 South Korea
        (650, bot_y + 200), # 23 Bangladesh
        (660, bot_y + 210), # 24 India flood
        (680, bot_y + 250), # 25 Thai-Cambodia
        (700, bot_y + 160), # 26 SoftBank
        (690, bot_y + 175), # 27 SK hynix
        (560, bot_y + 230), # 28 Houthis Yemen
        (480, bot_y + 380), # 29 Somalia/Uganda
        (160, bot_y + 220), # 30 Mexico
        (280, bot_y + 350), # 31 Colombia
        (300, bot_y + 400), # 32 Brazil
        (190, bot_y + 160), # 33 Pennsylvania
        (710, bot_y + 450), # 34 Qantas Australia
        (650, bot_y + 430), # 35 NZ/India
    ]
    for bx, by in brief_coords:
        draw.ellipse([bx - 4, by - 4, bx + 4, by + 4], fill="#38BDF8")

    # Right: "ALSO ON 24 NOVEMBER" (Stories 16-35)
    also_x = 810
    also_w = width - 40 - also_x # 750
    draw.rectangle([also_x, bot_y, also_x + also_w, bot_y + map_h], fill=c_card, outline=c_border, width=2)
    draw.text((also_x + 20, bot_y + 15), "ALSO ON 24 NOVEMBER (16–35)", fill=c_text_dark, font=font_section)

    also_stories = [
        "16. EU unveils its 22nd sanctions package against Russia. (Europe)",
        "17. Poland summons Russia's envoy after three Kh-101 missiles enter NATO airspace. (Europe)",
        "18. Putin lets Europe join the next Ukraine peace talks; Zelensky welcomes it. (Europe)",
        "19. Ukraine and Germany reach a preliminary deal on interceptor missiles. (Europe)",
        "20. Greece builds a Ukraine-Alexandroupolis freight route for grain. (Europe)",
        "21. Russia warns Estonia's moves are 'on the verge of triggering open war'. (Europe)",
        "22. South Korea scrambles jets after Russian aircraft approach its islands. (Asia)",
        "23. Bangladesh begins vaccinating 50 million children against typhoid. (Asia)",
        "24. Indian Army searches for scores missing after a deadly Himalayan flood. (Asia)",
        "25. Thai-Cambodia border fighting on hold following a truce. (Asia)",
        "26. SoftBank to invest $2 billion in Intel. (Asia)",
        "27. SK hynix shares jump 20% after Huang's return to Nvidia. (Asia)",
        "28. Houthis claim a Saudi airstrike kills 17 in Hodeida, Yemen. (Asia)",
        "29. Somalia and Uganda intensify operations against Al-Shabaab. (Africa)",
        "30. Mexico to try 'El Chapo Isidro' despite a US extradition request. (North America)",
        "31. Car bomb strikes the governor's office in Meta, Colombia. (South America)",
        "32. Thousands displaced after a deadly storm hits a town in Brazil. (South America)",
        "33. Pennsylvania reports a ninth measles death in its outbreak. (North America)",
        "34. Qantas cuts 850 jobs; Australia's unemployment rises to 4.9%. (Oceania)",
        "35. India-New Zealand first Test drawn in Wellington; Gill urges ICC to rethink saliva ban. (Oceania/Asia)"
    ]

    ay = bot_y + 60
    for s in also_stories:
        draw.text((also_x + 20, ay), s, fill=c_text_dark, font=font_body)
        ay += 28

    # 5. Footer
    footer_y = bot_y + map_h + 20
    draw.line([40, footer_y, width - 40, footer_y], fill=c_border, width=1)
    footer_text = "Every story happened or was first reported on Tuesday 24 November 2026. Disputed claims are attributed. Sources: AP · Reuters · AFP · BBC · Al Jazeera · CNN · NYT · France 24 · UN News · Original drawings."
    draw.text((40, footer_y + 10), footer_text, fill=c_text_muted, font=font_footer)

    # Save output
    os.makedirs("/output", exist_ok=True)
    out_path = "/output/entry.png"
    img.save(out_path, "PNG", optimize=True)
    print(f"Successfully generated {out_path} ({os.path.getsize(out_path) / 1024:.1f} KB)")

if __name__ == "__main__":
    create_entry()
