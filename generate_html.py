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
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 20px; background-color: #f4f4f4; }
        .bubble { width: 200px; height: 200px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; color: white; font-size: 20px; font-weight: bold; cursor: pointer; margin: 10px; }
        #droogte { background-color: #ff6347; }
        #waterkwaliteit { background-color: #6ab150; }
        #wateroverlast { background-color: #4682b4; }
        .hidden { display: none; }
        footer { font-style: italic; font-size: 12px; text-align: center; margin-top: 20px; }
        .project { margin: 10px 0; }
        .details { display: none; margin-left: 20px; font-size: 1em; }
        .project-name { font-size: 1em; font-style: italic; cursor: pointer; color: black; text-decoration: underline; }
    </style>
    <script>
        let lastOpen = null;
        function toggleDetails(projectId) {
            const details = document.querySelectorAll(`[id^='details-' + projectId]`);
            details.forEach(detail => {
                if (lastOpen && lastOpen !== detail) {
                    lastOpen.style.display = 'none';
                }
                detail.style.display = detail.style.display === 'none' ? 'block' : 'none';
                lastOpen = detail.style.display === 'none' ? null : detail;
            });
        }
        let lastVisible = null;
        function toggleVisibility(focusArea) {
            const element = document.getElementById(focusArea + "-projects");
            if (lastVisible && lastVisible !== element) {
                lastVisible.classList.add('hidden');
            }
            element.classList.toggle('hidden');
            lastVisible = element.classList.contains('hidden') ? null : element;
        }
    </script>
</head>
<body>
    <h1>Kennisnetwerk Water</h1>
    <p style="font-size: 24px; font-weight: bold;">Focusgebieden:</p>
    <div class="bubble" id="droogte" onclick="toggleVisibility('droogte')">Droogte</div>
    <div class="bubble" id="waterkwaliteit" onclick="toggleVisibility('waterkwaliteit')">Waterkwaliteit</div>
    <div class="bubble" id="wateroverlast" onclick="toggleVisibility('wateroverlast')">Wateroverlast</div>

    <div id='droogte-projects' class='hidden'><ul>
"""

# Voeg de projectinformatie toe aan de HTML
for index, row in df.iterrows():
    if row['Categorie'] == 'Droogte':
        html_content += f"""
        <li><span class='project-name' onclick="toggleDetails('{index}')">{row['Projectnaam']}</span>
            <div id="details-{index}" class="details">
                <p><strong>Hoofduitvoerder:</strong> {row['Hoofduitvoerder']}</p>
                <p><strong>Samenvatting:</strong> {row['Samenvatting']}</p>
                <p><strong>Bereik:</strong> {row['Bereik']}</p>
                <p><strong>Financieringsbron:</strong> {row['Financieringsbron']}</p>
                <p><strong>Organisatietype:</strong> {row['Organisatietype']}</p>
                <p><strong>Samenwerkingspartners:</strong> {row['Samenwerkingspartners']}</p>
                <p><strong>Gebruiker:</strong> {row['Gebruiker']}</p>
                <p><strong>Website:</strong> <a href="{row['Website']}" target="_blank">{row['Website']}</a></p>
            </div>
        </li>
        """

html_content += """
    </ul></div>
    <div id='waterkwaliteit-projects' class='hidden'><ul>
"""

for index, row in df.iterrows():
    if row['Categorie'] == 'Waterkwaliteit':
        html_content += f"""
        <li><span class='project-name' onclick="toggleDetails('{index}')">{row['Projectnaam']}</span>
            <div id="details-{index}" class="details">
                <p><strong>Hoofduitvoerder:</strong> {row['Hoofduitvoerder']}</p>
                <p><strong>Samenvatting:</strong> {row['Samenvatting']}</p>
                <p><strong>Bereik:</strong> {row['Bereik']}</p>
                <p><strong>Financieringsbron:</strong> {row['Financieringsbron']}</p>
                <p><strong>Organisatietype:</strong> {row['Organisatietype']}</p>
                <p><strong>Samenwerkingspartners:</strong> {row['Samenwerkingspartners']}</p>
                <p><strong>Gebruiker:</strong> {row['Gebruiker']}</p>
                <p><strong>Website:</strong> <a href="{row['Website']}" target="_blank">{row['Website']}</a></p>
            </div>
        </li>
        """

html_content += """
    </ul></div>
    <div id='wateroverlast-projects' class='hidden'><ul>
"""

for index, row in df.iterrows():
    if row['Categorie'] == 'Wateroverlast':
        html_content += f"""
        <li><span class='project-name' onclick="toggleDetails('{index}')">{row['Projectnaam']}</span>
            <div id="details-{index}" class="details">
                <p><strong>Hoofduitvoerder:</strong> {row['Hoofduitvoerder']}</p>
                <p><strong>Samenvatting:</strong> {row['Samenvatting']}</p>
                <p><strong>Bereik:</strong> {row['Bereik']}</p>
                <p><strong>Financieringsbron:</strong> {row['Financieringsbron']}</p>
                <p><strong>Organisatietype:</strong> {row['Organisatietype']}</p>
                <p><strong>Samenwerkingspartners:</strong> {row['Samenwerkingspartners']}</p>
                <p><strong>Gebruiker:</strong> {row['Gebruiker']}</p>
                <p><strong>Website:</strong> <a href="{row['Website']}" target="_blank">{row['Website']}</a></p>
            </div>
        </li>
        """

html_content += """
    </ul></div>
</body>
</html>
"""

# Sla de HTML op in een bestand
with open('index.html', 'w', encoding='utf-8') as file:
    file.write(html_content)
