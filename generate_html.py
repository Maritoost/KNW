import pandas as pd
import requests

# URL van de gepubliceerde Google Spreadsheet CSV-export
google_sheet_url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSYIGb-aEpKn2dUjunFaE-E4zNQAyRyCAhFDggR5FCS1Pow01nEObLPw_zSgNr137ucmQIb_bfFFwUA/pub?gid=1369086145&single=true&output=csv'

# Download de CSV-gegevens
response = requests.get(google_sheet_url)
with open('spreadsheet.csv', 'wb') as file:
    file.write(response.content)

# Lees de data uit het CSV-bestand
df = pd.read_csv('spreadsheet.csv')

# Begin van de HTML inhoud met inline CSS
html_content = """
<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kennisnetwerk Water</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 20px; background-color: #f4f4f4; }
        .focusgebieden { display: flex; flex-wrap: wrap; }
        .project { background: white; padding: 15px; margin: 10px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); flex: 1; min-width: 300px; }
        .project h2 { margin-top: 0; }
        .project p { margin: 5px 0; }
    </style>
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

html_content += """
    </div>
</body>
</html>
"""

# Sla de HTML op in een bestand
with open('index.html', 'w', encoding='utf-8') as file:
    file.write(html_content)
