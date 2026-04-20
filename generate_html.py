import base64

def generate_html():
    logo_path = '/home/ubuntu/upload/ChatGPTImage18.Apr.2026,12_27_15.png'
    with open(logo_path, 'rb') as f:
        logo_b64 = base64.b64encode(f.read()).decode()

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>POVGram - Experience life through others</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@700;800;900&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-gradient: linear-gradient(135deg, #87CEEB 0%, #87CEEB 100%);
            --text-color: #333;
            --btn-bg: #fff;
            --btn-text: #333;
            --btn-hover: #f0f0f0;
            --active-color: #ff7e5f;
        }}
        body {{
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            background: var(--bg-gradient);
            color: var(--text-color);
            scroll-behavior: smooth;
        }}
        header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px 5%;
        }}
        .logo {{
            display: flex;
            align-items: center;
        }}
        .logo img {{
            height: 120px;
            filter: drop-shadow(0 8px 16px rgba(0, 0, 0, 0.15));
            transition: transform 0.3s ease;
        }}
        .logo img:hover {{
            transform: scale(1.05);
        }}
        .header-links a {{
            text-decoration: none;
            color: var(--text-color);
            margin-left: 20px;
            font-weight: 600;
        }}
        .hero {{
            text-align: center;
            padding: 80px 20px;
        }}
        .hero h1 {{
            font-family: 'Poppins', sans-serif;
            font-size: 4.5rem;
            margin-bottom: 10px;
            font-weight: 900;
            background: linear-gradient(135deg, #ff6b6b 0%, #ff7e5f 50%, #ffa500 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            letter-spacing: -2px;
        }}
        .hero p {{
            font-size: 1.4rem;
            margin-bottom: 30px;
            opacity: 0.9;
        }}
        .btn {{
            display: inline-block;
            padding: 14px 28px;
            background: var(--btn-bg);
            color: var(--btn-text);
            text-decoration: none;
            border-radius: 50px;
            font-weight: bold;
            margin: 10px;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }}
        .btn:hover {{
            background: var(--btn-hover);
            transform: translateY(-3px);
            box-shadow: 0 6px 20px rgba(0,0,0,0.15);
        }}
        .btn-primary {{
            background: var(--active-color);
            color: white;
        }}
        .btn-primary:hover {{
            background: #e06c50;
        }}
        .section-title {{
            text-align: center;
            font-size: 2.5rem;
            margin: 60px 0 30px;
            font-weight: 700;
        }}
        .pov-of-the-day {{
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 40px 20px;
        }}
        .video-container {{
            position: relative;
            width: 100%;
            max-width: 900px;
            aspect-ratio: 16 / 9;
            border-radius: 20px;
            overflow: hidden;
            box-shadow: 0 20px 40px rgba(0,0,0,0.2);
        }}
        .video-container iframe {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            border: none;
        }}
        .filter-bar {{
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 15px;
            padding: 25px;
            position: sticky;
            top: 0;
            background: rgba(255, 255, 255, 0.7);
            backdrop-filter: blur(15px);
            z-index: 1000;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        }}
        .filter-btn {{
            padding: 10px 25px;
            background: white;
            border: none;
            border-radius: 50px;
            cursor: pointer;
            font-weight: 600;
            transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        }}
        .filter-btn:hover {{
            transform: scale(1.1);
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }}
        .filter-btn.active {{
            background: var(--active-color);
            color: white;
        }}
        .category-section {{
            padding: 60px 5%;
        }}
        .video-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
            gap: 30px;
        }}
        .video-card {{
            background: white;
            border-radius: 20px;
            overflow: hidden;
            box-shadow: 0 10px 25px rgba(0,0,0,0.08);
            transition: all 0.3s ease;
        }}
        .video-card:hover {{
            transform: translateY(-10px);
            box-shadow: 0 15px 35px rgba(0,0,0,0.12);
        }}
        .video-card .video-wrapper {{
            position: relative;
            padding-bottom: 56.25%; /* 16:9 */
            height: 0;
        }}
        .video-card iframe {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            border: none;
        }}
        .video-card h3 {{
            padding: 20px;
            margin: 0;
            font-size: 1.2rem;
            font-weight: 600;
        }}
        .submit-section {{
            text-align: center;
            padding: 100px 20px;
            background: rgba(255,255,255,0.2);
            margin-top: 40px;
        }}
        .submit-section h2 {{
            font-size: 2.5rem;
            margin-bottom: 20px;
        }}
        footer {{
            text-align: center;
            padding: 40px;
            font-size: 1rem;
            opacity: 0.6;
            font-weight: 500;
        }}
        @media (max-width: 768px) {{
            .hero h1 {{ font-size: 2.5rem; }}
            .hero p {{ font-size: 1.1rem; }}
            .video-grid {{ grid-template-columns: 1fr; }}
            .filter-bar {{ padding: 15px; gap: 10px; }}
            .filter-btn {{ padding: 8px 18px; font-size: 0.9rem; }}
            .logo img {{ height: 80px; }}
        }}
    </style>
</head>
<body>

    <header>
        <div class="logo">
            <img src="data:image/png;base64,{logo_b64}" alt="POVGram Logo">
        </div>
        <div class="header-links">
            <a href="#explore">Explore</a>
            <a href="#submit">Submit</a>
        </div>
    </header>

    <section class="hero">
        <h1>Experience life through others' eyes</h1>
        <p>Discover real-world POV experiences from around the world</p>
        <a href="#explore" class="btn">Explore Experiences</a>
        <a href="#submit" class="btn btn-primary">Submit a POV</a>
    </section>

    <section class="pov-of-the-day">
        <h2 class="section-title">🌍 POV of the Day</h2>
        <div class="video-container" id="potd-container">
            <!-- Video will be injected here -->
        </div>
    </section>

    <div class="filter-bar" id="explore">
        <button class="filter-btn active" onclick="scrollToSection('travel', this)">Travel</button>
        <button class="filter-btn" onclick="scrollToSection('nightlife', this)">Night Life</button>
        <button class="filter-btn" onclick="scrollToSection('jobs', this)">Jobs</button>
        <button class="filter-btn" onclick="scrollToSection('relaxing', this)">Relaxing</button>
        <button class="filter-btn" onclick="scrollToSection('adrenaline', this)">Adrenaline</button>
        <button class="filter-btn" onclick="scrollToSection('lifeexperiences', this)">Life Experiences</button>
    </div>

    <section id="travel" class="category-section">
        <h2 class="section-title">🌴 Travel Experiences</h2>
        <div class="video-grid" id="grid-travel"></div>
    </section>

    <section id="nightlife" class="category-section">
        <h2 class="section-title">🌃 Night Life</h2>
        <div class="video-grid" id="grid-nightlife"></div>
    </section>

    <section id="jobs" class="category-section">
        <h2 class="section-title">💼 Jobs</h2>
        <div class="video-grid" id="grid-jobs"></div>
    </section>

    <section id="relaxing" class="category-section">
        <h2 class="section-title">🧘 Relaxing</h2>
        <div class="video-grid" id="grid-relaxing"></div>
    </section>

    <section id="adrenaline" class="category-section">
        <h2 class="section-title">⚡ Adrenaline</h2>
        <div class="video-grid" id="grid-adrenaline"></div>
    </section>

    <section id="lifeexperiences" class="category-section">
        <h2 class="section-title">❤️ Life Experiences</h2>
        <div class="video-grid" id="grid-lifeexperiences"></div>
    </section>

    <section id="submit" class="submit-section">
        <h2>Want to share your POV experience?</h2>
        <p>YouTube Link (required) • Title (optional) • Category (optional)</p>
        <a href="https://docs.google.com/spreadsheets/d/1oVCh8CD_njc5IDf-8xZlTvWVyD4YVroDJDROTv2qWwQ/edit?usp=sharing" target="_blank" class="btn btn-primary">Submit Your POV</a>
    </section>

    <footer>
        POVGram — Experience life through others
    </footer>

    <script>
        const videos = {{
            travel: [
                {{ id: '1-6wILcqil4', title: 'POV: Walking in Tokyo at Night' }},
                {{ id: '8mBJUQ5O_3w', title: 'POV: Exploring Swiss Alps' }},
                {{ id: 'oJ1CDeGkXb8', title: 'POV: Venice Canal Boat Ride' }},
                {{ id: 'm6_8_0-o6-s', title: 'POV: Walking in Paris' }}
            ],
            nightlife: [
                {{ id: '3O1_3zBUKM8', title: 'POV: Clubbing in Berlin' }},
                {{ id: '9aO2E9hX2vA', title: 'POV: Seoul Night Market' }},
                {{ id: '0n_6v-0-0-0', title: 'POV: New York Times Square at Night' }}
            ],
            jobs: [
                {{ id: 'v=dQw4w9WgXcQ', title: 'POV: Barista Morning Rush' }},
                {{ id: 'v=dQw4w9WgXcQ', title: 'POV: Pilot Landing Plane' }},
                {{ id: 'v=dQw4w9WgXcQ', title: 'POV: Chef in a Busy Kitchen' }}
            ],
            relaxing: [
                {{ id: 'v=dQw4w9WgXcQ', title: 'POV: Reading by the Fireplace' }},
                {{ id: 'v=dQw4w9WgXcQ', title: 'POV: Rain on a Tin Roof' }},
                {{ id: 'v=dQw4w9WgXcQ', title: 'POV: Forest Walk in Autumn' }}
            ],
            adrenaline: [
                {{ id: 'v=dQw4w9WgXcQ', title: 'POV: Skydiving over Dubai' }},
                {{ id: 'v=dQw4w9WgXcQ', title: 'POV: Downhill Mountain Biking' }},
                {{ id: 'v=dQw4w9WgXcQ', title: 'POV: Formula 1 Cockpit' }}
            ],
            lifeexperiences: [
                {{ id: 'v=dQw4w9WgXcQ', title: 'POV: Playing with Child' }},
                {{ id: 'v=dQw4w9WgXcQ', title: 'POV: Birthday Celebration' }},
                {{ id: 'v=dQw4w9WgXcQ', title: 'POV: Family Dinner' }}
            ]
        }};

        // All videos for POTD
        const allVideos = Object.values(videos).flat();

        // Set POV of the Day
        function setPOTD() {{
            const randomVideo = allVideos[Math.floor(Math.random() * allVideos.length)];
            const container = document.getElementById('potd-container');
            container.innerHTML = `<iframe src="https://www.youtube.com/embed/${{randomVideo.id}}" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>`;
        }}

        // Populate Grids
        function populateGrids() {{
            for (const category in videos) {{
                const grid = document.getElementById(`grid-${{category}}`);
                if (grid) {{
                    videos[category].forEach(video => {{
                        grid.innerHTML += `
                            <div class="video-card">
                                <div class="video-wrapper">
                                    <iframe src="https://www.youtube.com/embed/${{video.id}}" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                                </div>
                                <h3>${{video.title}}</h3>
                            </div>
                        `;
                    }});
                }}
            }}
        }}

        // Smooth Scroll and Active Button
        function scrollToSection(id, btn) {{
            const section = document.getElementById(id);
            if (section) {{
                const yOffset = -100; 
                const y = section.getBoundingClientRect().top + window.pageYOffset + yOffset;
                window.scrollTo({{top: y, behavior: 'smooth'}});
            }}
            
            // Update active button
            document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
        }}

        // Initialize
        window.onload = () => {{
            setPOTD();
            populateGrids();
        }};
    </script>
</body>
</html>"""

    with open('/home/ubuntu/index.html', 'w') as f:
        f.write(html_content)

if __name__ == "__main__":
    generate_html()
