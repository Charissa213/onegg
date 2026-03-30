import os

base = '/Users/charissavandelden/Source/onegg/src/main/resources'

# ── styles.scss ─────────────────────────────────────────────────────────────
styles_scss = """\
// ── Variables ─────────────────────────────────────────────
$bg:           #000000;
$brand:        #ff2020;
$font-display: 'Arial Black', 'Arial Bold', Impact, sans-serif;
$font-ui:      'Arial', Helvetica, sans-serif;

// ── Reset ─────────────────────────────────────────────────
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

body {
    background: $bg;
    color: $brand;
    font-family: $font-ui;
    height: 100vh;
    overflow: hidden;
}

a { color: inherit; text-decoration: none; transition: opacity 0.25s ease; cursor: pointer; }
a:hover { opacity: 0.55; }

// ── Layout: 3 fixed columns ───────────────────────────────
.layout {
    position: fixed;
    inset: 0;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
}

.col-left {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 2rem 1.5rem;
    flex-shrink: 0;
}

.col-right {
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    padding: 2rem 1.5rem;
    flex-shrink: 0;
}

// ── Corner logo (top-right) ────────────────────────────────
.logo-corner {
    position: fixed;
    top: 1.5rem;
    right: 1.5rem;
    z-index: 20;
}

.logo-corner img {
    width: clamp(50px, 7vw, 110px);
    height: auto;
    filter: drop-shadow(0 0 8px rgba($brand, 0.5));
}

.logo-corner__placeholder {
    width: clamp(50px, 7vw, 100px);
    height: clamp(50px, 7vw, 100px);
    border: 3px solid $brand;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: $font-display;
    font-size: clamp(0.9rem, 1.8vw, 1.4rem);
    font-weight: 900;
    color: $brand;
    text-shadow: 0 0 12px rgba($brand, 0.6);
}

// ── Vertical brand name ────────────────────────────────────
.brand-vertical {
    font-family: $font-display;
    font-size: clamp(3rem, 11vh, 9rem);
    font-weight: 900;
    color: $brand;
    writing-mode: vertical-lr;
    text-orientation: upright;
    letter-spacing: 0.02em;
    line-height: 1;
    text-transform: uppercase;
    user-select: none;
    text-shadow: 0 0 20px rgba($brand, 0.35), 0 0 70px rgba($brand, 0.12);
}

// ── Social icons ───────────────────────────────────────────
.social-icons {
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 1.1rem;
}

.social-icons a {
    display: flex;
    align-items: center;
    font-size: 1.2rem;
    line-height: 1;
    width: 24px;
    height: 24px;
    justify-content: center;
}

.social-icons svg {
    width: 20px;
    height: 20px;
    fill: currentColor;
}

// ── Main navigation (right side, vertical text) ────────────
.main-nav {
    display: flex;
    flex-direction: column;
    gap: 0;
}

.main-nav__item {
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    padding: 0.3rem 0;
}

// Vertical | line left of each nav item
.main-nav__item::before {
    content: '';
    display: block;
    width: 2px;
    height: clamp(3rem, 5vh, 5rem);
    background: $brand;
    flex-shrink: 0;
    margin-right: 0.7rem;
}

// Vertical text label
.main-nav__item a {
    font-family: $font-display;
    font-size: clamp(0.6rem, 0.9vw, 0.85rem);
    font-weight: 700;
    letter-spacing: 0.25em;
    text-transform: uppercase;
    color: $brand;
    // Rotate text to read bottom-to-top
    writing-mode: vertical-rl;
    transform: rotate(180deg);
    white-space: nowrap;
    display: block;
}

// ── Bottom CTA ─────────────────────────────────────────────
.cta {
    position: fixed;
    bottom: 2rem;
    left: 50%;
    transform: translateX(-50%);
    z-index: 10;
    text-align: center;
}

.cta a {
    display: block;
    color: #ffffff;
    text-decoration: underline;
    text-decoration-thickness: 1px;
    font-family: $font-display;
    font-size: clamp(0.65rem, 1vw, 0.85rem);
    font-weight: 700;
    letter-spacing: 0.25em;
    text-transform: uppercase;
    line-height: 2.2;
}
"""

# ── placeholder.scss ────────────────────────────────────────────────────────
placeholder_scss = """\
// ── Variables ─────────────────────────────────────────────
$bg-color:    #0a0a0f;
$font-family: 'Georgia', serif;
$glitter: linear-gradient(90deg, #ff0080, #ff8c00, #ffe600, #00ff9f, #00cfff, #cc00ff, #ff0080, #ff8c00, #ffe600);
$subtitle-grad: linear-gradient(90deg, #ffd700, #fff8b0, #ffd700);

// ── Reset ─────────────────────────────────────────────────
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

body {
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    background: $bg-color;
    overflow: hidden;
    font-family: $font-family;
}

// ── Keyframes ─────────────────────────────────────────────
@keyframes twinkle {
    0%, 100% { opacity: 0; transform: scale(0.5); }
    50%       { opacity: 0.9; transform: scale(1); }
}

@keyframes shimmer {
    0%   { background-position: 0% 50%; }
    100% { background-position: 300% 50%; }
}

@keyframes pop {
    0%   { opacity: 0;   transform: scale(0)   translateY(0); }
    30%  { opacity: 1;   transform: scale(1)   translateY(-10px); }
    70%  { opacity: 0.8; transform: scale(0.8) translateY(-20px); }
    100% { opacity: 0;   transform: scale(0)   translateY(-35px); }
}

// ── Stars ─────────────────────────────────────────────────
.stars { position: fixed; inset: 0; pointer-events: none; z-index: 0; }
.star {
    position: absolute;
    border-radius: 50%;
    background: white;
    animation: twinkle var(--dur, 3s) ease-in-out infinite var(--delay, 0s);
    opacity: 0;
}

// ── Center wrapper ────────────────────────────────────────
.center { position: relative; z-index: 1; text-align: center; user-select: none; }

// ── Glitter title ─────────────────────────────────────────
.glitter {
    font-size: clamp(3rem, 15vw, 11rem);
    font-weight: 900;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    background: $glitter;
    background-size: 300% 100%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: shimmer 4s linear infinite;
    filter:
        drop-shadow(0 0  8px rgba(255, 220,  50, 0.7))
        drop-shadow(0 0 20px rgba(255, 100, 200, 0.5))
        drop-shadow(0 0 40px rgba(100, 200, 255, 0.4));
}

// ── Sparkles ──────────────────────────────────────────────
.sparkles { position: absolute; inset: -60px; pointer-events: none; }

.sparkle {
    position: absolute;
    width: var(--size, 8px);
    height: var(--size, 8px);
    opacity: 0;
    animation: pop var(--dur, 1.5s) ease-in-out infinite var(--delay, 0s);
}

.sparkle::before,
.sparkle::after {
    content: '';
    position: absolute;
    inset: 0;
    background: var(--color, #ffe600);
    border-radius: 1px;
    clip-path: polygon(50% 0%, 60% 40%, 100% 50%, 60% 60%, 50% 100%, 40% 60%, 0% 50%, 40% 40%);
}

.sparkle::after { transform: rotate(45deg) scale(0.5); opacity: 0.6; }

// ── Subtitle ──────────────────────────────────────────────
.subtitle {
    margin-top: 1.2rem;
    font-size: clamp(1rem, 3vw, 1.6rem);
    letter-spacing: 0.3em;
    text-transform: uppercase;
    color: transparent;
    background: $subtitle-grad;
    background-size: 200% 100%;
    -webkit-background-clip: text;
    background-clip: text;
    animation: shimmer 3s linear infinite;
    opacity: 0.85;
}

// ── Back link ─────────────────────────────────────────────
.back-link {
    position: fixed;
    top: 2rem;
    left: 2rem;
    z-index: 10;
    color: rgba(255, 255, 255, 0.55);
    text-decoration: none;
    font-size: 0.85rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    transition: color 0.2s;
}

.back-link:hover { color: white; }
"""

# ── index.html ──────────────────────────────────────────────────────────────
index_html = """\
<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Onegg</title>
    <link rel="icon" type="image/png" href="assets/logos/onegg_wit.png" />
    <link rel="stylesheet" href="styles.css" />
</head>
<body>

<!-- Top-right: logo -->
<div class="logo-corner">
    <!-- <img src="/assets/logos/onegg-logo.png" alt="Onegg" /> -->
    <div class="logo-corner__placeholder">OG</div>
</div>

<!-- Main layout -->
<div class="layout">

    <!-- LEFT: Verticale naam + social icons -->
    <div class="col-left">
        <span class="brand-vertical">Onegg</span>

        <ul class="social-icons" aria-label="Social media">
            <li><a href="#" aria-label="Instagram">
                <svg viewBox="0 0 24 24"><path d="M12 2.2c3.2 0 3.6.01 4.85.07 3.25.15 4.77 1.69 4.92 4.92.06 1.27.07 1.65.07 4.85s-.01 3.59-.07 4.85c-.15 3.23-1.66 4.77-4.92 4.92-1.25.06-1.64.07-4.85.07s-3.59-.01-4.85-.07C3.67 21.57 2.15 20.03 2 16.8c-.06-1.26-.07-1.64-.07-4.85s.01-3.59.07-4.85C2.15 3.87 3.67 2.33 6.85 2.2 8.12 2.14 8.8 2.2 12 2.2zm0-2.2C8.74 0 8.33.01 7.05.07 2.7.27.27 2.7.07 7.05.01 8.33 0 8.74 0 12c0 3.26.01 3.67.07 4.95.2 4.36 2.62 6.78 6.98 6.98C8.33 23.99 8.74 24 12 24s3.67-.01 4.95-.07c4.35-.2 6.78-2.62 6.98-6.98.06-1.28.07-1.69.07-4.95s-.01-3.67-.07-4.95c-.2-4.35-2.62-6.78-6.98-6.98C15.67.01 15.26 0 12 0zm0 5.84a6.16 6.16 0 100 12.32A6.16 6.16 0 0012 5.84zm0 10.16a4 4 0 110-8 4 4 0 010 8zm6.4-11.85a1.44 1.44 0 100 2.88 1.44 1.44 0 000-2.88z"/></svg>
            </a></li>
            <li><a href="#" aria-label="Facebook">
                <svg viewBox="0 0 24 24"><path d="M24 12.07C24 5.41 18.63 0 12 0S0 5.41 0 12.07C0 18.1 4.39 23.1 10.13 24v-8.44H7.08v-3.49h3.04V9.41c0-3.02 1.8-4.7 4.54-4.7 1.31 0 2.68.24 2.68.24v2.97h-1.5c-1.5 0-1.96.93-1.96 1.89v2.26h3.32l-.53 3.5h-2.8V24C19.62 23.1 24 18.1 24 12.07z"/></svg>
            </a></li>
            <li><a href="#" aria-label="TikTok">
                <svg viewBox="0 0 24 24"><path d="M19.59 6.69a4.83 4.83 0 01-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 01-2.88 2.5 2.89 2.89 0 01-2.89-2.89 2.89 2.89 0 012.89-2.89c.28 0 .54.04.79.1V9.01a6.3 6.3 0 00-.79-.05 6.34 6.34 0 00-6.34 6.34 6.34 6.34 0 006.34 6.34 6.34 6.34 0 006.33-6.34V8.69a8.18 8.18 0 004.78 1.52V6.76a4.85 4.85 0 01-1.01-.07z"/></svg>
            </a></li>
            <li><a href="#" aria-label="Spotify">
                <svg viewBox="0 0 24 24"><path d="M12 0C5.37 0 0 5.37 0 12s5.37 12 12 12 12-5.37 12-12S18.63 0 12 0zm5.52 17.3a.75.75 0 01-1.03.25c-2.82-1.72-6.37-2.11-10.55-1.16a.75.75 0 01-.34-1.46c4.57-1.04 8.49-.59 11.66 1.34.36.22.47.68.26 1.03zm1.47-3.27a.94.94 0 01-1.29.31c-3.23-1.98-8.15-2.56-11.97-1.4a.94.94 0 01-.55-1.8c4.36-1.33 9.78-.68 13.5 1.6.44.27.58.84.31 1.29zm.13-3.41C15.24 8.39 8.8 8.17 5.14 9.27a1.12 1.12 0 01-.67-2.14c4.18-1.31 11.13-1.06 15.52 1.57a1.12 1.12 0 01-1.07 1.92h-.4z"/></svg>
            </a></li>
            <li><a href="#" aria-label="YouTube">
                <svg viewBox="0 0 24 24"><path d="M23.5 6.19a3.02 3.02 0 00-2.12-2.14C19.54 3.6 12 3.6 12 3.6s-7.54 0-9.38.45A3.02 3.02 0 00.5 6.19 31.6 31.6 0 000 12a31.6 31.6 0 00.5 5.81 3.02 3.02 0 002.12 2.14C4.46 20.4 12 20.4 12 20.4s7.54 0 9.38-.45a3.02 3.02 0 002.12-2.14C24 16.08 24 12 24 12a31.6 31.6 0 00-.5-5.81zM9.6 15.6V8.4l6.27 3.6-6.27 3.6z"/></svg>
            </a></li>
            <li><a href="#" aria-label="Apple Music">
                <svg viewBox="0 0 24 24"><path d="M18.71 19.5c-.83 1.24-1.71 2.45-3.05 2.47-1.34.03-1.77-.79-3.29-.79-1.53 0-2 .77-3.27.82-1.31.05-2.3-1.32-3.14-2.53C4.25 17 2.94 12.45 4.7 9.39c.87-1.52 2.43-2.48 4.12-2.51 1.28-.02 2.5.87 3.29.87.78 0 2.26-1.07 3.8-.91.65.03 2.47.26 3.64 1.98-.09.06-2.17 1.28-2.15 3.81.03 3.02 2.65 4.03 2.68 4.04-.03.07-.42 1.44-1.38 2.83M13 3.5c.73-.83 1.94-1.46 2.94-1.5.13 1.17-.34 2.35-1.04 3.19-.69.85-1.83 1.51-2.95 1.42-.15-1.15.41-2.35 1.05-3.11z"/></svg>
            </a></li>
        </ul>
    </div>

    <!-- CENTER: leeg -->
    <div class="col-center"></div>

    <!-- RIGHT: Navigatie -->
    <div class="col-right">
        <nav class="main-nav" aria-label="Navigatie">
            <div class="main-nav__item"><a href="tour.html">Tour</a></div>
            <div class="main-nav__item"><a href="music.html">Music</a></div>
            <div class="main-nav__item"><a href="signup.html">Sign Up</a></div>
            <div class="main-nav__item"><a href="store.html">Store</a></div>
        </nav>
    </div>

</div>

<!-- Onderkant CTA -->
<div class="cta">
    <a href="#">Watch</a>
    <a href="#">Full Video</a>
</div>

</body>
</html>
"""

# ── glitter.js (gedeeld voor alle placeholder paginas) ─────────────────────
glitter_js = """\
(function () {
    /* twinkling stars */
    var stars = document.getElementById('stars');
    if (stars) {
        for (var i = 0; i < 160; i++) {
            var s = document.createElement('div');
            s.className = 'star';
            var size = Math.random() * 2.5 + 0.5;
            s.style.cssText =
                'width:' + size + 'px;height:' + size + 'px;' +
                'top:' + Math.random() * 100 + '%;' +
                'left:' + Math.random() * 100 + '%;' +
                '--dur:' + (Math.random() * 4 + 2).toFixed(2) + 's;' +
                '--delay:-' + (Math.random() * 6).toFixed(2) + 's';
            stars.appendChild(s);
        }
    }

    /* sparkle particles */
    var sp = document.getElementById('sparkles');
    var colors = ['#ffe600','#ff80c0','#80dfff','#c0ff80','#ffb347','#ee82ee'];
    if (sp) {
        for (var j = 0; j < 28; j++) {
            var el = document.createElement('div');
            el.className = 'sparkle';
            var sz = Math.random() * 14 + 6;
            el.style.cssText =
                '--size:' + sz + 'px;' +
                '--color:' + colors[Math.floor(Math.random() * colors.length)] + ';' +
                '--dur:' + (Math.random() * 1.8 + 0.8).toFixed(2) + 's;' +
                '--delay:-' + (Math.random() * 3).toFixed(2) + 's;' +
                'top:' + Math.random() * 100 + '%;' +
                'left:' + Math.random() * 100 + '%';
            sp.appendChild(el);
        }
    }
})();
"""

# ── placeholder template builder ──────────────────────────────────────────
def placeholder_html(title, subtitle='coming soon'):
    return """\
<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Onegg \xe2\x80\x93 """ + title + """</title>
    <link rel="icon" type="image/png" href="assets/logos/onegg_wit.png" />
    <link rel="stylesheet" href="placeholder.css" />
</head>
<body>

<a class="back-link" href="index.html">Back</a>

<div class="stars" id="stars"></div>

<div class="center">
    <div class="sparkles" id="sparkles"></div>
    <div class="glitter">""" + title + """</div>
    <div class="subtitle">""" + subtitle + """</div>
</div>

<script src="glitter.js"></script>
</body>
</html>
"""

# ── Write all files ────────────────────────────────────────────────────────
files = {
    'styles.scss':      styles_scss,
    'placeholder.scss': placeholder_scss,
    'index.html':       index_html,
    'glitter.js':       glitter_js,
    'tour.html':        placeholder_html('Tour'),
    'music.html':       placeholder_html('Music'),
    'signup.html':      placeholder_html('Sign Up'),
    'store.html':       placeholder_html('Store'),
}

for name, content in files.items():
    path = os.path.join(base, name)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'  wrote {name}')

print('Done!')

