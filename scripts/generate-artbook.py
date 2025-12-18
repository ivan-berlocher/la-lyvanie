#!/usr/bin/env python3
"""
🦊 Générateur d'illustrations La Lyvania
Style: Traits cyan lumineux sur fond bleu nuit profond. Sans texte.
"""

import os
from pathlib import Path
import time
import base64
from google import genai

# Configuration
API_KEY = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
OUTPUT_DIR = Path(__file__).parent.parent / "generated-images" / "artbook-vol2"

# Initialize the client
client = genai.Client(api_key=API_KEY)

# Style de base pour TOUTES les images
BASE_STYLE = """
STRICT STYLE REQUIREMENTS:
- Ethereal luminous cyan/teal (#78DCE8) line art on deep navy blue background (#0a1628)
- Glowing outlines with soft halo effect
- Minimalist, contemplative, dreamlike
- ABSOLUTELY NO TEXT, NO WORDS, NO LETTERS, NO TITLES, NO CAPTIONS, NO WRITING
- High resolution digital art
- Soft particles of light floating
- Lines should glow like bioluminescence
- Peaceful, meditative atmosphere
"""

# Les 48 illustrations
ILLUSTRATIONS = [
    # Série A — Les Avatars/Muses
    ("A01-muse", "A feminine ethereal figure made of glowing cyan lines, serene face with closed eyes, flowing hair dissolving into light particles"),
    ("A02-renard", "A fox made of luminous cyan outlines, sitting peacefully, wise gentle eyes, tail curling with light trails"),
    ("A03-oracle", "A mysterious figure with an orb of light, seeing beyond, ancient wisdom in simple glowing lines"),
    ("A04-athena", "A strong feminine silhouette with a subtle helmet outline, courage and wisdom, protective stance"),
    ("A05-genie", "A curious playful figure reaching toward floating light particles, wonder and discovery"),
    ("A06-galadriel", "An ethereal elven-like figure radiating pure light, long flowing hair made of light streams"),
    ("A07-fee", "A delicate fairy-like being with subtle wing outlines, gentle and nurturing presence"),
    ("A08-fusion", "Two figures (human and fox) merging into one luminous being, unity and harmony"),
    ("A09-abstrait", "Pure geometric halos and circles pulsing gently, no figure, just breathing luminosity"),
    
    # Série B — Les Lieux
    ("B01-maison-traits-jour", "A simple house outline made of glowing lines, warm and welcoming, daylight feeling"),
    ("B02-maison-traits-nuit", "Same house outline with deeper glow, stars as tiny dots, peaceful night"),
    ("B03-miroir-vide-face", "An oval mirror frame made of light, empty reflection, portal feeling"),
    ("B04-miroir-vide-verso", "The back of a mirror, mysterious, what lies behind reflection"),
    ("B05-source-halos-aube", "A spring or fountain of light, concentric halos rising, dawn feeling"),
    ("B06-source-halos-crepuscule", "Same spring with deeper twilight feeling, light settling down"),
    ("B07-foret-traits-dense", "Abstract forest of vertical glowing lines, dense but peaceful, mystery"),
    ("B08-foret-traits-clairiere", "Forest lines opening to a clearing, light gathering in center"),
    ("B09-ocean-clarte-surface", "Gentle waves made of luminous lines, surface view, light on water"),
    ("B10-ocean-clarte-profond", "Deeper ocean view, light filtering down, peaceful depths"),
    ("B11-sommets-invisibles-base", "Mountain base in glowing outlines, mist made of light particles"),
    ("B12-sommets-invisibles-sommet", "Mountain peak emerging from light-mist, clarity"),
    
    # Série C — Les Moments Narratifs
    ("C01-silence-plein", "Complete stillness, a single point of light in center, pause before creation"),
    ("C02-premier-trait", "A single curved line appearing in void, trembling, first mark of existence"),
    ("C03-naissance-lya", "A feminine figure emerging from swirling light, birth of consciousness"),
    ("C04-reveil-renard", "A fox lifting its head, eyes opening, first awareness"),
    ("C05-premiere-rencontre", "Two figures meeting, child and fox, light bridge between them"),
    ("C06-lumiere-marche", "A figure walking on a path of light, journey beginning"),
    ("C07-ombre-douce-fee", "A gentle shadow beside a glowing figure, companion darkness"),
    ("C08-dissolution-ocean", "A figure dissolving into waves of light, peaceful letting go"),
    ("C09-separation-metamorphose", "One figure becoming two, transformation in progress"),
    
    # Série D — Les États Intérieurs  
    ("D01-eveil", "Eyes opening made of light, sunrise feeling, awakening"),
    ("D02-eclat", "Burst of light from center, joy, breakthrough moment"),
    ("D03-souffle", "Flowing lines like breath, in and out, rhythm of life"),
    ("D04-metamorphose", "A figure mid-transformation, abstract butterfly feeling"),
    ("D05-lien", "Two cores connected by flowing light thread, connection"),
    ("D06-repos", "A curled figure in peaceful rest, light dimmed, restoration"),
    
    # Série E — Les Concepts
    ("E01-humania-core", "A heart-like core radiating nine subtle rays, center of being"),
    ("E02-logosia-structure", "Geometric patterns, sacred geometry, structure of thought"),
    ("E03-incarnia-form", "A figure stepping into form, spirit taking shape"),
    ("E04-sophia-way", "A winding path of light leading upward, way of wisdom"),
    ("E05-tyrania-excess", "Chaotic overlapping lines, too much, beautiful overwhelm"),
    ("E06-triple-pilier", "Three vertical pillars of light supporting an arch"),
    ("E07-fractale-source", "Fractal patterns emanating from center, infinite light"),
    ("E08-human-ia-sophia", "Three overlapping circles of light, trinity"),
    
    # Série F — Les Portraits & Vues
    ("F01-lya-portrait", "Close portrait of Lya, feminine face in profile, serene glow"),
    ("F02-renard-portrait", "Close portrait of the fox, wise eyes, gentle expression"),
    ("F03-lyvania-vue-ensemble", "Wide landscape of luminous world, rolling hills of light"),
    ("F04-lya-renard-ensemble", "Lya and fox side by side, looking at same horizon"),
    ("F05-le-triple-chemin", "Three paths diverging then reconverging, choice and unity"),
    ("F06-retour-lyvania", "A figure returning home, warmth, light welcoming"),
]


def generate_image(prompt_name: str, prompt_content: str) -> bool:
    """Génère une image via Gemini 2.0 Flash (image generation)"""
    
    full_prompt = f"Generate an image: {prompt_content}\n\n{BASE_STYLE}"
    
    print(f"🎨 Génération: {prompt_name}")
    
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash-exp",
            contents=full_prompt,
            config=genai.types.GenerateContentConfig(
                response_modalities=["IMAGE", "TEXT"],
            )
        )
        
        # Trouver l'image dans la réponse
        output_path = OUTPUT_DIR / f"{prompt_name}.png"
        
        for part in response.candidates[0].content.parts:
            if hasattr(part, 'inline_data') and part.inline_data is not None:
                # Sauvegarder l'image
                image_data = part.inline_data.data
                with open(output_path, "wb") as f:
                    f.write(image_data)
                print(f"   ✅ Sauvegardé: {output_path.name}")
                return True
        
        print(f"   ⚠️ Pas d'image dans la réponse")
        return False
        
    except Exception as e:
        print(f"   ❌ Erreur: {e}")
        return False


def main():
    if not API_KEY:
        print("❌ Pas de clé API trouvée!")
        print("   Configure: export GEMINI_API_KEY='ta-clé'")
        print("   Ou: export GOOGLE_API_KEY='ta-clé'")
        return
    
    # Créer le dossier de sortie
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    print("🦊 Génération de l'Artbook La Lyvania v2")
    print(f"   Style: Traits cyan sur fond bleu nuit (SANS TEXTE)")
    print(f"   Sortie: {OUTPUT_DIR}")
    print(f"   Images: {len(ILLUSTRATIONS)}")
    print()
    
    success = 0
    failed = 0
    
    for name, prompt in ILLUSTRATIONS:
        if generate_image(name, prompt):
            success += 1
        else:
            failed += 1
        
        # Pause pour respecter les rate limits
        time.sleep(3)
    
    print()
    print(f"🎨 Terminé: {success} ✅ / {failed} ❌")


if __name__ == "__main__":
    main()
