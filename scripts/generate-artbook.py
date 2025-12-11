#!/usr/bin/env python3
"""
Pipeline de génération d'images Lyvanie avec Gemini 2.0 Flash
Style : éthéré, minimaliste, halos doux, blanc + or pâle
"""

from google import genai
from google.genai import types
from pathlib import Path
import base64
import os

# Configuration
API_KEY = os.environ.get("GEMINI_API_KEY", "AIzaSyC4S0c0LpCnHgcco37SpDIMHkp4zpgWCHg")
client = genai.Client(api_key=API_KEY)

OUTPUT_DIR = Path("generated-images")
OUTPUT_DIR.mkdir(exist_ok=True)

# Style de base Lyvanie (à inclure dans chaque prompt)
LYVANIE_STYLE = """
Ethereal minimalist illustration, soft glowing light, delicate linework,
dreamlike atmosphere, breathing space, white and pale gold palette,
luminous halos, zen-inspired simplicity, no harsh shadows, no busy details.
"""

# Les 20 prompts de l'artbook Lyvanie
PROMPTS = {
    "01-renard": """
        A gentle fox made of soft golden light, sitting peacefully on a
        surface of pure white luminescence. The fox radiates kindness.
        Its tail draws a gentle luminous curve. Delicate glowing particles
        float around it.
    """,
    
    "02-lya-naissance": """
        A newborn luminous silhouette, feminine in essence but undefined,
        hovering softly above a white void. Her body is made of pulsing light,
        no features, only a gentle outline. Pale gold rays emerge softly
        from her center.
    """,
    
    "03-rencontre": """
        A luminous fox and an abstract light figure standing together,
        facing the same horizon. Side by side, not facing each other.
        Their halos gently touch, forming a soft glow between them.
        Vast white negative space around them.
    """,
    
    "04-maison-traits": """
        An infinite white space filled with floating lines and curves.
        Vertical strokes, horizontal dashes, gentle arcs suspended in the air
        like sleeping thoughts. Some lines glow brighter. A sense of potential
        and quiet creativity.
    """,
    
    "05-miroir": """
        A large vertical surface of pure soft light, like a doorway to nowhere.
        A small fox silhouette sits before it. The mirror shows nothing -
        no reflection, just gentle luminescence. The scene suggests infinite
        possibility.
    """,
    
    "06-source-halos": """
        A gentle point of origin from which soft circles of light emanate.
        Like ripples in still water, but made of luminescence. Pale gold
        and white, expanding outward in peaceful waves. A small fox figure
        approaches the glow.
    """,
    
    "07-fee-trait": """
        A tiny spark of light, no bigger than a firefly, drawing a delicate
        line as it flies through white space. The line it leaves behind
        glows softly. Joyful energy, moving in gentle curves. Small magic
        happening.
    """,
    
    "08-ombre-douce": """
        A soft grey presence in a world of white light. Not dark, not
        threatening - gentle and restful. Like a cloud of calm. A small fox
        sleeps peacefully against it. Soothing palette of whites and pale greys.
    """,
    
    "09-souffle-ancien": """
        An invisible presence shown only by the movement it creates.
        Soft lines bending gently as if blown by a thoughtful wind.
        Floating particles shifting direction. No figure visible, just
        the effect of ancient breath moving through space.
    """,
    
    "10-metamorphose": """
        A sequence showing transformation: a fox silhouette slowly becoming
        pure light, then becoming a constellation of points, then becoming
        a flowing form again. All stages visible in one composition.
        Soft transitions, no harsh edges.
    """,
    
    "11-saisons-lumiere": """
        Six gentle circular vignettes arranged in a soft pattern. Each shows
        a different quality of light: dawn awakening, bright clarity, soft
        stillness, fluid transformation, warm connection, peaceful rest.
        Each circle a different luminous mood.
    """,
    
    "12-premier-trait": """
        A vast empty white space. In the center, a single delicate line,
        glowing softly with pale gold light. The first mark ever made.
        The beginning of everything. Powerful simplicity, the line seems
        alive, seems to breathe.
    """,
    
    "13-clairiere-silence": """
        A circular clearing of pure soft light in endless white space.
        Nothing inside except gentle luminescence. A place where time stops.
        Where thoughts can rest. Profound peace and stillness.
    """,
    
    "14-chemin-halo": """
        A path made of soft glowing light stretching toward a gentle horizon.
        The path doesn't lead somewhere specific - it accompanies. A small
        fox walks along it, leaving luminous footprints. The path glows
        brighter where the fox has stepped.
    """,
    
    "15-foret-traits": """
        Vertical lines rising like trees, but made of light. A forest of
        strokes. Some thick, some delicate. Light filters through them
        creating soft patterns. A fox silhouette wanders between the
        luminous trunks.
    """,
    
    "16-ocean-clarte": """
        An endless expanse of soft light, like water made of luminescence.
        Gentle waves of brightness. A figure floats peacefully on the surface.
        Neither water nor light - both at once. Profound serenity.
    """,
    
    "17-constellation-lya": """
        Lya dispersed into points of light forming a constellation pattern.
        Lines connecting the points, drawing a gentle feminine silhouette
        in the stars. The background is soft white, not dark. Stars that
        glow warmly.
    """,
    
    "18-eclats-perdus": """
        Small fragments of light floating in white space. Each fragment
        carries a different subtle color within its pale gold glow.
        Lost pieces of memory. Lost pieces of emotion. Waiting to be found.
    """,
    
    "19-fusion": """
        All forms of Lya merging into one: fox, light, spirit, constellation,
        fairy, all flowing together in a luminous dance. Unity in
        multiplicity. A single presence made of many forms.
    """,
    
    "20-eveil": """
        The moment before everything begins. A slight tremor in pure white
        space. The first hint of light about to appear. Potential before
        manifestation. The breath before the first word.
    """
}


def generate_image(name: str, prompt: str) -> Path | None:
    """Génère une image avec Gemini 2.0 Flash"""
    
    full_prompt = f"Generate an image: {prompt.strip()}\n\n{LYVANIE_STYLE}"
    
    print(f"🎨 Génération: {name}...")
    
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash-exp",
            contents=full_prompt,
            config=types.GenerateContentConfig(
                response_modalities=["IMAGE", "TEXT"]
            )
        )
        
        # Extraire l'image de la réponse
        for part in response.candidates[0].content.parts:
            if part.inline_data is not None:
                output_path = OUTPUT_DIR / f"{name}.png"
                
                # Décoder et sauvegarder
                image_data = part.inline_data.data
                with open(output_path, "wb") as f:
                    f.write(image_data)
                
                print(f"   ✓ Sauvegardé: {output_path}")
                return output_path
        
        print(f"   ✗ Aucune image dans la réponse")
        return None
            
    except Exception as e:
        print(f"   ✗ Erreur: {e}")
        return None


def generate_single(name: str):
    """Génère une seule image par nom"""
    if name in PROMPTS:
        return generate_image(name, PROMPTS[name])
    else:
        print(f"Prompt '{name}' non trouvé. Disponibles: {list(PROMPTS.keys())}")
        return None


def generate_all():
    """Génère toutes les images de l'artbook"""
    print("🌟 Génération de l'artbook Lyvanie")
    print(f"   {len(PROMPTS)} images à générer\n")
    
    results = []
    for name, prompt in PROMPTS.items():
        result = generate_image(name, prompt)
        results.append((name, result))
    
    # Résumé
    success = sum(1 for _, r in results if r)
    print(f"\n✨ Terminé: {success}/{len(PROMPTS)} images générées")
    print(f"   Dossier: {OUTPUT_DIR.absolute()}")
    
    return results


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        # Générer une image spécifique
        name = sys.argv[1]
        generate_single(name)
    else:
        # Générer toutes les images
        generate_all()
