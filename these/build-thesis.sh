#!/bin/bash
# Script de génération du PDF de la thèse AMI
# Usage: ./build-thesis.sh

set -e

THESIS_DIR="$(dirname "$0")"
OUTPUT="$THESIS_DIR/these-AMI.pdf"

echo "🔨 Construction de la thèse AMI..."

# Vérifier les dépendances
if ! command -v pandoc &> /dev/null; then
    echo "❌ Pandoc non trouvé. Installez avec: brew install pandoc"
    exit 1
fi

if ! command -v xelatex &> /dev/null; then
    echo "❌ XeLaTeX non trouvé. Installez avec: brew install --cask mactex"
    exit 1
fi

# Concaténer tous les chapitres
cd "$THESIS_DIR"

echo "📚 Assemblage des chapitres..."

# Créer un fichier temporaire avec tous les contenus
TEMP_FILE=$(mktemp)

# Header YAML + préambule
cat thesis.md > "$TEMP_FILE"

# Ajouter les chapitres (en retirant les éventuels headers YAML des chapitres)
for chapter in \
    01-introduction.md \
    02-etat-de-lart.md \
    03-cadre-theorique.md \
    04-architecture-ami.md; do
    echo "" >> "$TEMP_FILE"
    cat "$chapter" >> "$TEMP_FILE"
    echo "" >> "$TEMP_FILE"
done

# Partie II
echo "" >> "$TEMP_FILE"
echo "\\newpage" >> "$TEMP_FILE"
echo "" >> "$TEMP_FILE"
echo "# PARTIE II : SPHÈRES COGNITIVES" >> "$TEMP_FILE"
echo "" >> "$TEMP_FILE"
echo "\\newpage" >> "$TEMP_FILE"
echo "" >> "$TEMP_FILE"

for chapter in \
    05-harmonia-lot.md \
    06-lumeria-raisonnement.md \
    07-spheres-affectives.md \
    08-spheres-pratiques.md \
    09-lumenia-responsabilite.md \
    10-trustia-confiance.md; do
    echo "" >> "$TEMP_FILE"
    cat "$chapter" >> "$TEMP_FILE"
    echo "" >> "$TEMP_FILE"
done

# Partie III
echo "" >> "$TEMP_FILE"
echo "\\newpage" >> "$TEMP_FILE"
echo "" >> "$TEMP_FILE"
echo "# PARTIE III : RÉALISATION" >> "$TEMP_FILE"
echo "" >> "$TEMP_FILE"
echo "\\newpage" >> "$TEMP_FILE"
echo "" >> "$TEMP_FILE"

for chapter in \
    11-implementation.md \
    12-validation.md \
    13-discussion.md \
    14-conclusion.md; do
    echo "" >> "$TEMP_FILE"
    cat "$chapter" >> "$TEMP_FILE"
    echo "" >> "$TEMP_FILE"
done

echo "📄 Génération du PDF..."

pandoc "$TEMP_FILE" \
    -o "$OUTPUT" \
    --pdf-engine=xelatex \
    --number-sections \
    --toc \
    --toc-depth=3 \
    -V papersize=a4 \
    -V geometry:margin=3cm \
    -V fontsize=12pt \
    -V documentclass=report \
    -V lang=fr \
    --highlight-style=tango

# Nettoyer
rm "$TEMP_FILE"

echo "✅ Thèse générée : $OUTPUT"
echo "📖 $(ls -lh "$OUTPUT" | awk '{print $5}') générés"
