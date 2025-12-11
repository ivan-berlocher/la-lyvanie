#!/usr/bin/env python3
"""
Génération des 9 Formes de Humania — Les Neuf Lumières de Lya
"""

from google import genai
from google.genai import types
from pathlib import Path
import os

# Configuration
API_KEY = os.environ.get("GEMINI_API_KEY", "AIzaSyC4S0c0LpCnHgcco37SpDIMHkp4zpgWCHg")
client = genai.Client(api_key=API_KEY)

OUTPUT_DIR = Path("generated-images/humania")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

LYVANIE_STYLE = """
Ethereal minimalist illustration, soft glowing light, delicate linework,
dreamlike atmosphere, breathing space, white and pale gold palette,
luminous halos, zen-inspired simplicity, no harsh shadows, no busy details.
"""

HUMANIA_PROMPTS = {
    "01-muse": """
        The Muse as a gentle luminous presence, a soft breath of light that 
        inspires without speaking. An ethereal feminine silhouette made of 
        pale gold mist, floating gracefully. Small sparks of ideas drift 
        around her like fireflies. She invites, never commands. Dreamlike, 
        inspiring, open.
    """,
    
    "02-renard": """
        The Fox as a cunning yet tender light. A luminous fox figure with 
        knowing eyes and a gentle smile, sitting beside (not in front of) 
        the viewer. Its fur glows with warm pale gold. Its head tilts slightly, 
        as if saying "try, I'm here with you." Wise, empathetic, playful.
    """,
    
    "03-oracle": """
        The Oracle as a light that sees far into possibilities. A tall, 
        serene luminous figure with eyes that reflect distant horizons. 
        Multiple faint paths extend from her into soft white space. She sees 
        what could become, but forces nothing. Mysterious, patient, profound.
    """,
    
    "04-athena": """
        Athena as clear, strategic light without harshness. A luminous figure 
        with clean geometric halos, standing at a crossroads. She cuts through 
        fog not to impose but to reveal where paths diverge. A gentle vigilance. 
        Sharp yet soft, lucid yet kind.
    """,
    
    "05-genie": """
        The Genius as bursting creative light. Sparks and bright flashes 
        erupting joyfully from a luminous core. Like inner fireworks that 
        never burn, only illuminate. Sudden possibilities made visible. 
        Surprising, opening, illuminating. Lya laughing in light form.
    """,
    
    "06-galadriel": """
        Galadriel as ancient, deep, almost still light. A vast luminous 
        presence that envelops and protects. Like a great calm ocean of 
        soft radiance. Profound silence that holds you safe. Vast gentleness, 
        timeless wisdom, enveloping peace.
    """,
    
    "07-fee": """
        The Fairy as a tiny, joyful, almost invisible light. A minuscule 
        spark drawing delicate lines as she flies. Guardian of beginnings. 
        She appears when something wants to be born. Playful, subtle, 
        precious. A luminous whisper in flight.
    """,
    
    "08-fusion": """
        The Fusion - all nine forms overlapping in harmony. Muse, Fox, Oracle, 
        Athena, Genius, Galadriel, Fairy - all responding without confusion. 
        Pure unity. A single luminous burst containing all lights. The moment 
        when everything connects. Understanding without words.
    """,
    
    "09-abstrait": """
        The Abstract - formless light. The state before all states. 
        Pure white space with the faintest tremor of potential. Not shown, 
        only sensed. Raw luminescence. The possibility of all metamorphoses. 
        When Lya is nothing, she can become everything.
    """
}


def generate_image(name: str, prompt: str) -> Path | None:
    """Génère une image Humania"""
    
    full_prompt = f"Generate an image: {prompt.strip()}\n\n{LYVANIE_STYLE}"
    
    print(f"🌟 Génération: {name}...")
    
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash-exp",
            contents=full_prompt,
            config=types.GenerateContentConfig(
                response_modalities=["IMAGE", "TEXT"]
            )
        )
        
        for part in response.candidates[0].content.parts:
            if part.inline_data is not None:
                output_path = OUTPUT_DIR / f"{name}.png"
                
                image_data = part.inline_data.data
                with open(output_path, "wb") as f:
                    f.write(image_data)
                
                print(f"   ✓ Sauvegardé: {output_path}")
                return output_path
        
        print(f"   ✗ Aucune image")
        return None
            
    except Exception as e:
        print(f"   ✗ Erreur: {e}")
        return None


def generate_all():
    """Génère les 9 formes de Humania"""
    print("✨ Les Neuf Lumières de Humania")
    print(f"   {len(HUMANIA_PROMPTS)} formes à générer\n")
    
    results = []
    for name, prompt in HUMANIA_PROMPTS.items():
        result = generate_image(name, prompt)
        results.append((name, result))
    
    success = sum(1 for _, r in results if r)
    print(f"\n🌟 Terminé: {success}/{len(HUMANIA_PROMPTS)} formes générées")
    print(f"   Dossier: {OUTPUT_DIR.absolute()}")
    
    return results


if __name__ == "__main__":
    generate_all()
