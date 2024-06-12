import pandas as pd

# Lees de data uit het Excel-bestand
file_path = 'Split_KennisNetwerk_Projects_version4.xlsx'
df = pd.read_excel(file_path)

# Begin van de HTML inhoud
html_content = """
<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kennisnetwerk Water</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Kennisnetwerk Water</h1>
    <div class="focusgebieden">
"""

# Voeg de projectinformatie toe aan de HTML
for index, row in df.iterrows():
    html_content += f"""
    <div class="project">
        <h2>{row['Projectnaam']}</h2>
        <p><strong>Hoofduitvoerder:</strong> {row['Hoofduitvoerder']}</p>
        <p><strong>Samenvatting:</strong> {row['Samenvatting']}</p>
        <p><strong>Bereik:</strong> {row['Bereik']}</p>
        <p><strong>Financieringsbron:</strong> {row['Financieringsbron']}</p>
        <p><strong>Organisatietype:</strong> {row['Organisatietype']}</p>
        <p><strong>Samenwerkingspartners:</strong> {row['Samenwerkingspartners']}</p>
        <p><strong>Gebruiker:</strong> {row['Gebruiker']}</p>
        <p><a href="{row['Website']}">Meer informatie</a></p>
    </div>
    """

# Einde van de HTML inhoud
html_content += """
    </div>
</body>
</html>
"""

# Sla de HTML op in een bestand
with open('index.html', 'w', encoding='utf-8') as file:
    file.write(html_content)
