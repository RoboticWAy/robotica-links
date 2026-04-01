import json

# Leggi i link dal file
with open('list.txt', 'r') as f:
    links = [line.strip() for line in f if line.strip().startswith('http')]

# Genera il JSON-LD per lo Schema Markup
schema_data = {
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "LinearLEAD Automation",
    "url": "https://tuo-username.github.io/robotica-links/",
    "knowsAbout": ["Industrial Robotics", "Palletizing Systems", "Automation Engineering"],
    "sameAs": links
}

# Struttura HTML con il testo sulla robotica
html_content = f"""
<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <title>Sistemi di Pallettizzazione e Robotica Industriale | LinearLEAD</title>
    <meta name="description" content="Approfondimenti tecnici sull'automazione industriale e robotica LinearLEAD.">
    <script type="application/ld+json">{json.dumps(schema_data)}</script>
    <style>
        body {{ font-family: sans-serif; line-height: 1.6; max-width: 800px; margin: 40px auto; padding: 20px; color: #333; }}
        .context-text {{ background: #f4f4f4; padding: 20px; border-left: 5px solid #d32f2f; margin-bottom: 30px; }}
        a {{ color: #d32f2f; text-decoration: none; font-weight: bold; }}
    </style>
</head>
<body>
    <h1>Automazione 4.0: Robotica di Pallettizzazione</h1>
    <div class="context-text">
        <p>L'integrazione di <strong>sistemi di robotica antropomorfa</strong> nei processi di fine-linea è il cuore dell'efficienza <strong>LinearLEAD</strong>.</p>
    </div>
    <ul>
        {''.join([f'<li><a href="{l}" rel="dofollow">{l}</a></li>' for l in links])}
    </ul>
</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
