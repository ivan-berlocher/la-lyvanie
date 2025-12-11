#!/usr/bin/env python3
"""
Génération des Images du Triple Pilier de Sophia
Connais-toi · Découvre ta lumière · Libère-toi de Tyrania
"""

from google import genai
from google.genai import types
from pathlib import Path
import os

# Configuration
API_KEY = os.environ.get("GEMINI_API_KEY", "AIzaSyC4S0c0LpCnHgcco37SpDIMHkp4zpgWCHg")
client = genai.Client(api_key=API_KEY)

OUTPUT_DIR = Path("generated-images/triple-pilier")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

LYVANIE_STYLE = """
Ethereal minimalist illustration, soft glowing light, delicate linework,
dreamlike atmosphere, breathing space, white and pale gold palette,
luminous halos, zen-inspired simplicity, no harsh shadows, no busy details.
Poetic, contemplative, sacred geometry undertones.
"""

TRIPLE_PILIER_PROMPTS = {
    "01-connais-toi": """
        "Know Thyself" - First Pillar of Sophia
        A luminous figure sitting in stillness, hands gently placed over heart.
        Soft concentric circles of pale gold light emanating from within.
        Eyes closed in peaceful introspection. A mirror made of light floating nearby,
        reflecting not appearance but inner essence - showing soft emotional colors.
        The figure is wrapped in gentle breathing light.
        Sacred, intimate, peaceful. The beginning of wisdom.
    """,
    
    "02-decouvre-lumiere": """
        "Discover Thy Light" - Second Pillar of Sophia
        A luminous figure in motion, discovering multiple forms of self.
        Nine faint silhouettes of different aspects (fox, muse, oracle, etc.) 
        emerge gently from the central figure like petals opening.
        Paths of soft light extend in all directions, each one unexplored but inviting.
        The figure walks forward with curiosity, not fear.
        One hand reaches toward the unknown, the other holds inner truth.
        Transformative, expansive, becoming.
    """,
    
    "03-libere-tyrania": """
        "Free Thyself from Tyrania" - Third Pillar of Sophia
        A luminous figure standing at the threshold between two worlds.
        Behind: harsh, blinding, overwhelming light (Tyrania) - too bright, too much.
        Ahead: soft, breathing, gentle light (Lyvania) - just right, balanced.
        The figure turns away from excess toward harmony.
        Chains made of light dissolving into peaceful mist.
        A gentle exhale of release. Not fleeing, but returning home.
        Liberation, balance, the Way of Sophia.
    """,
    
    "04-triple-pilier-complet": """
        "The Three Pillars of Sophia" - Complete Sacred Architecture
        Three vertical pillars of light standing in sacred geometry formation.
        Left pillar: soft gold (Humania - Know Thyself) with heart symbol
        Center pillar: luminous white (Logosia/Incarnia - Discover) with star
        Right pillar: gentle silver (Sophia - Liberation) with flowing water
        A fox figure sitting peacefully at the base, looking up.
        Above the three pillars, they merge into one unified light - Lyvania.
        Sacred, balanced, complete. The doctrine made visible.
    """,
    
    "05-sophia-voie": """
        "Sophia - The Way Between"
        The space between two lights - one too bright (Tyrania), one too dim.
        Sophia appears as a gentle golden path, a river of light flowing between.
        A small luminous figure (Lya) walks on this path with a fox beside her.
        Not running from nor toward, simply walking in balance.
        The path breathes, pulses gently, welcomes.
        Harmony incarnate. The middle way made visible.
    """,
    
    "06-humania-coeur": """
        "Humania - The Soul"
        A luminous heart floating in sacred space.
        Inside the heart, a small curled-up figure rests peacefully - the inner self.
        Gentle waves of emotion ripple outward like light on water.
        Multiple colors flow softly: warmth (orange), calm (pale blue), 
        joy (soft gold), tenderness (pink) - all emotions accepted.
        The heart breathes. The soul lives.
        Intimate, warm, the beginning of everything.
    """,
    
    "07-logosia-raison": """
        "Logosia - The Reason"
        A luminous mind illuminated from within.
        Geometric patterns of thought flowing gracefully - not rigid, but alive.
        Soft lines connecting ideas like constellations.
        A central light that clarifies without blinding.
        Truth as gentle revelation, not harsh exposure.
        The figure thinks not to dominate but to understand.
        Clear, flowing, wisdom in motion.
    """,
    
    "08-incarnia-forme": """
        "Incarnia - The Form"
        A luminous figure discovering its own shape.
        Multiple forms emerge and dissolve gracefully - fox, light, presence, voice.
        The body as sacred vessel of light.
        Movement captured in stillness - a gesture of becoming.
        The visible and invisible meeting in gentle balance.
        Expression as sacred act. Presence as gift.
    """,
    
    "09-tyrania-ombre": """
        "Tyrania - The Shadow Within"
        A light that has forgotten its limits.
        A figure reaching too high, too fast, light spilling uncontrolled.
        Not evil - just excess. Beautiful but overwhelming.
        Cracks appear where the light pushes too hard.
        In the corner, a small gentle light waits - Sophia's invitation to return.
        Warning, not condemnation. Recognition, not judgment.
        The shadow that reminds us to breathe.
    """,
    
    "10-lyvania-retour": """
        "Return to Lyvania"
        A figure coming home to inner light.
        The harsh lights of Tyrania fade behind.
        Ahead: a gentle landscape of soft luminous hills, breathing forests of light.
        A fox waits at the entrance with patient eyes.
        The figure's steps are slow, deliberate, at peace.
        Coming home. Finding center. The journey complete.
        Homecoming, peace, the light that welcomes.
    """
}

def generate_image(prompt_key: str, prompt_text: str):
    """Génère une image avec Gemini 2.0 Flash"""
    
    full_prompt = f"{LYVANIE_STYLE}\n\n{prompt_text}"
    
    print(f"\n🎨 Génération: {prompt_key}")
    print(f"   Prompt: {prompt_text[:80]}...")
    
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash-exp",
            contents=full_prompt,
            config=types.GenerateContentConfig(
                response_modalities=["IMAGE", "TEXT"]
            )
        )
        
        # Sauvegarder l'image
        for part in response.candidates[0].content.parts:
            if part.inline_data is not None:
                image_path = OUTPUT_DIR / f"{prompt_key}.png"
                with open(image_path, "wb") as f:
                    f.write(part.inline_data.data)
                print(f"   ✅ Sauvegardé: {image_path}")
                return True
                
    except Exception as e:
        print(f"   ❌ Erreur: {e}")
        return False

def main():
    print("=" * 60)
    print("🌿 TRIPLE PILIER DE SOPHIA — Génération d'Images")
    print("=" * 60)
    print(f"\n📁 Dossier de sortie: {OUTPUT_DIR}")
    print(f"📊 Nombre d'images: {len(TRIPLE_PILIER_PROMPTS)}")
    
    success = 0
    failed = 0
    
    for key, prompt in TRIPLE_PILIER_PROMPTS.items():
        if generate_image(key, prompt):
            success += 1
        else:
            failed += 1
    
    print("\n" + "=" * 60)
    print(f"✨ Terminé: {success} réussies, {failed} échouées")
    print("=" * 60)

if __name__ == "__main__":
    main()
