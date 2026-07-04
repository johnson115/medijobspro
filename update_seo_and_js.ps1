$dir = "c:\Users\ASUS\Desktop\johnsnow\italy project\ahmed agency\pre final desing choosed"
$htmlFiles = Get-ChildItem -Path $dir -Filter "*.html"

foreach ($file in $htmlFiles) {
    $content = Get-Content $file.FullName -Raw

    # 1. Remove inline JS for lang toggles to prevent conflict with lang.js
    $content = $content -replace '(?s)const langToggleBtn = document\.getElementById\(''lang-toggle-btn''\);.*?}\s*}\s*', ''
    $content = $content -replace '(?s)const mobileLangBtn = document\.getElementById\(''mobile-lang-toggle-btn''\);.*?}\s*}\s*', ''

    # 2. Add SEO / OpenGraph
    $title = ""
    $desc = ""

    if ($file.Name -eq "index.html") {
        $title = "Medijobs Pro — Recrutement Médical en Allemagne"
        $desc = "Agence spécialisée dans le recrutement et l'accompagnement des professionnels de santé vers l'Allemagne. Infirmiers, techniciens, accompagnement complet."
    } elseif ($file.Name -eq "about.html") {
        $title = "À propos de Medijobs Pro | Recrutement Médical"
        $desc = "Découvrez l'histoire, la mission et l'équipe derrière Medijobs Pro, votre partenaire de confiance pour travailler en Allemagne."
    } elseif ($file.Name -eq "candidates.html") {
        $title = "Candidats | Postulez pour travailler en Allemagne"
        $desc = "Démarrez votre carrière médicale en Allemagne. Découvrez notre processus d'accompagnement et postulez en ligne dès aujourd'hui."
    } elseif ($file.Name -eq "entreprise.html") {
        $title = "Entreprises & Hôpitaux | Recrutez du personnel qualifié"
        $desc = "Partenaires de santé en Allemagne : trouvez le personnel infirmier qualifié dont vous avez besoin avec Medijobs Pro."
    } elseif ($file.Name -eq "contact.html") {
        $title = "Contact | Medijobs Pro"
        $desc = "Contactez Medijobs Pro pour toute question concernant le recrutement médical en Allemagne. Nous sommes là pour vous aider."
    }

    $seoTags = @"
<meta name="description" content="$desc"/>
<meta property="og:title" content="$title" />
<meta property="og:description" content="$desc" />
<meta property="og:type" content="website" />
<meta property="og:image" content="https://medijobspro.com/media/employer_hero.png" />
<meta property="og:site_name" content="Medijobs Pro" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="$title" />
<meta name="twitter:description" content="$desc" />
"@

    # Remove existing <title> and <meta name="description"> to avoid duplicates
    $content = $content -replace '(?i)<title>.*?</title>', ''
    $content = $content -replace '(?i)<meta name="description" content=".*?"\s*/?>', ''
    
    # Insert new <title> and SEO tags right after <meta content="width=device-width... />
    $insertPos = '<meta content="width=device-width, initial-scale=1.0" name="viewport"/>'
    $replacement = "$insertPos`n<title>$title</title>`n$seoTags"
    $content = $content -replace [regex]::Escape($insertPos), $replacement

    Set-Content -Path $file.FullName -Value $content -Encoding UTF8
    Write-Host "Processed $($file.Name)"
}
