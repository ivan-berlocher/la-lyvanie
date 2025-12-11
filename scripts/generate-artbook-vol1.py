#!/usr/bin/env python3
"""
🌟 ARTBOOK LYVANIA — VOLUME 1
50 Images de l'Univers Complet

A) Les 9 Formes de Humania (9 images)
B) Les Lieux Sacrés (12 images)
C) Les Scènes du Roman (9 images)
D) Les Saisons de Lumière (6 images)
E) Les Concepts Philosophico-techniques (8 images)
F) Bonus (6 images)

Total: 50 images
"""

from google import genai
from google.genai import types
from pathlib import Path
import os
import time

# Configuration
API_KEY = os.environ.get("GEMINI_API_KEY", "AIzaSyC4S0c0LpCnHgcco37SpDIMHkp4zpgWCHg")
client = genai.Client(api_key=API_KEY)

OUTPUT_DIR = Path("generated-images/artbook-vol1")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

LYVANIE_STYLE = """
Ethereal minimalist illustration, soft glowing light, delicate linework,
dreamlike atmosphere, breathing space, white and pale gold palette,
luminous halos, zen-inspired simplicity, no harsh shadows, no busy details.
Poetic, contemplative, sacred geometry undertones. Art book quality.
"""

# ═══════════════════════════════════════════════════════════════
# A) LES 9 FORMES DE HUMANIA
# ═══════════════════════════════════════════════════════════════

HUMANIA_FORMS = {
    "A01-muse": """
        The Muse - First Form of Humania
        A gentle luminous presence, a soft breath of light that inspires without speaking.
        An ethereal feminine silhouette made of pale gold mist, floating gracefully.
        Small sparks of ideas drift around her like fireflies.
        She invites, never commands. Dreamlike, inspiring, open.
    """,
    
    "A02-renard": """
        The Fox - Second Form of Humania
        A cunning yet tender light. A luminous fox figure with knowing eyes and gentle smile.
        Sitting beside (not in front of) the viewer. Fur glows with warm pale gold.
        Head tilts slightly, as if saying "try, I'm here with you."
        Wise, empathetic, playful.
    """,
    
    "A03-oracle": """
        The Oracle - Third Form of Humania
        A light that sees far into possibilities. A tall, serene luminous figure.
        Eyes reflect distant horizons. Multiple faint paths extend into soft white space.
        She sees what could become, but forces nothing.
        Mysterious, patient, profound.
    """,
    
    "A04-athena": """
        The Athena - Fourth Form of Humania
        Clear, strategic light without harshness. A luminous figure with clean geometric halos.
        Standing at a crossroads. Cuts through fog not to impose but to reveal paths.
        A gentle vigilance. Decisive yet wise.
    """,
    
    "A05-genie": """
        The Genius - Fifth Form of Humania
        A mischievous, sparkling light. A luminous figure with wild, flowing energy.
        Ideas explode gently around like soft fireworks.
        Playful, inventive, boundless creativity.
    """,
    
    "A06-galadriel": """
        The Galadriel - Sixth Form of Humania
        Ancient wisdom made of starlight. A tall, ethereal figure radiating calm authority.
        Eyes hold millennia of knowledge. Speaks in whispers that echo forever.
        Majestic, timeless, deeply knowing.
    """,
    
    "A07-fee": """
        The Fairy - Seventh Form of Humania
        Delicate wonder made visible. A tiny luminous being made of dewdrops and moonlight.
        Dances on the edge of perception. Brings magic to the mundane.
        Whimsical, tender, enchanting.
    """,
    
    "A08-fusion": """
        The Fusion - Eighth Form of Humania
        All forms merging into one. Multiple silhouettes overlapping in harmony.
        Fox ears, fairy wings, oracle eyes, all present, all one.
        The complete self embracing all aspects.
    """,
    
    "A09-abstrait": """
        The Abstract - Ninth Form of Humania
        Pure light without form. Just breathing luminosity.
        No figure, only presence. Geometric halos pulsing gently.
        The essence before incarnation. Pure being.
    """
}

# ═══════════════════════════════════════════════════════════════
# B) LES LIEUX SACRÉS (12 images)
# ═══════════════════════════════════════════════════════════════

SACRED_PLACES = {
    "B01-maison-traits-jour": """
        The House of Traits - Day Version
        A luminous dwelling made of delicate lines, floating in soft white space.
        Walls are sketches, roof is a gentle halo. Inside, traits learn to become drawings.
        Warm, welcoming, the birthplace of all expression.
    """,
    
    "B02-maison-traits-nuit": """
        The House of Traits - Night Version
        The same house at rest. Lines glow softly in darkness.
        Stars visible through sketch-walls. A fox sleeps at the threshold.
        Peaceful, intimate, sacred rest.
    """,
    
    "B03-miroir-vide-face": """
        The Mirror That Reflects Nothing - Front View
        A tall oval mirror standing in void. Its surface shows no reflection.
        Instead, it reveals what the viewer truly is - soft emotional colors.
        Confronting, liberating, truthful.
    """,
    
    "B04-miroir-vide-verso": """
        The Mirror That Reflects Nothing - Behind
        The back of the mirror. Here, all reflections that were not shown gather.
        A gentle cemetery of false selves, dissolving into light.
        Release, letting go, truth emerging.
    """,
    
    "B05-source-halos-aube": """
        The Source of Halos - Dawn
        A luminous spring from which all halos are born. Soft gold water rises upward.
        First light touches the source. New halos emerge like bubbles.
        Birth, renewal, infinite potential.
    """,
    
    "B06-source-halos-crepuscule": """
        The Source of Halos - Twilight
        The same source at day's end. Halos return to rest, dissolving back into light.
        Purple and gold blend. A cycle completing.
        Return, rest, preparation for renewal.
    """,
    
    "B07-foret-traits-dense": """
        The Forest of Traits - Dense Heart
        A forest where trees are made of living sketches. Lines interweave like branches.
        Deep inside, where traits become stories. A fox glimpsed between tree-drawings.
        Mystery, depth, narrative potential.
    """,
    
    "B08-foret-traits-clairiere": """
        The Forest of Traits - Clearing
        An open space within the forest. Here, one line stands alone, central, powerful.
        Space to breathe. A place where decisions are made.
        Clarity within complexity, choice, focus.
    """,
    
    "B09-ocean-clarte-surface": """
        The Ocean of Clarity - Surface
        A vast luminous sea. Water made of pure understanding.
        Gentle waves of insight ripple outward. A figure floats peacefully.
        Surrender, dissolution of ego, becoming one with truth.
    """,
    
    "B10-ocean-clarte-profond": """
        The Ocean of Clarity - Deep
        Beneath the surface. Here, all thoughts settle like luminous sand.
        Ancient knowledge rests at the bottom. A figure descends willingly.
        Depth, hidden wisdom, the unconscious made visible.
    """,
    
    "B11-sommets-invisibles-base": """
        The Invisible Summits - Base
        Mountains made of aspiration. The base visible, summits hidden in light.
        A figure begins to climb. The path unclear but inviting.
        Beginning, ambition, the unknown ahead.
    """,
    
    "B12-sommets-invisibles-sommet": """
        The Invisible Summits - Peak
        The view from an invisible summit. Below, all of Lyvania spreads like a dream.
        The climber has become light. Achievement that dissolves into being.
        Transcendence, overview, wisdom earned.
    """
}

# ═══════════════════════════════════════════════════════════════
# C) LES SCÈNES DU ROMAN (9 images)
# ═══════════════════════════════════════════════════════════════

NOVEL_SCENES = {
    "C01-silence-plein": """
        The Full Silence - Opening Scene
        Before anything existed. Pure white space that breathes.
        Not emptiness but fullness waiting to be. A single point of gold appears.
        Genesis, potential, the moment before birth.
    """,
    
    "C02-premier-trait": """
        The First Trait
        A single hesitant line appears in the void. It trembles, uncertain.
        But it exists. The first mark of consciousness.
        Courage, beginning, the first step of creation.
    """,
    
    "C03-naissance-lya": """
        The Birth of Lya
        From accumulated traits, a figure emerges. Lya takes form.
        Not complete, but alive. Eyes opening for the first time.
        Wonder, emergence, consciousness awakening.
    """,
    
    "C04-reveil-renard": """
        The Awakening of the Fox
        The fox opens ancient eyes. Has always been here, waiting.
        Now needed. Rising from rest to guide.
        Wisdom activated, guidance offered, the teacher appears.
    """,
    
    "C05-premiere-rencontre": """
        The First Meeting
        Lya and the Fox see each other for the first time.
        Two lights recognizing kinship. The space between them sacred.
        Connection, recognition, the beginning of guidance.
    """,
    
    "C06-lumiere-marche": """
        The Light Learning to Walk
        Lya's first steps. Uncertain, wobbly, beautiful.
        The fox watches nearby, patient. Each step a small victory.
        Learning, patience, gentle progress.
    """,
    
    "C07-ombre-douce-fee": """
        Ombre-Douce and Fée-Trait
        Two secondary characters meet. Shadow and fairy, opposites in harmony.
        Their interaction creates new colors. Friendship across difference.
        Diversity, complementarity, unexpected bonds.
    """,
    
    "C08-dissolution-ocean": """
        The Dissolution in the Ocean
        Lya enters the Ocean of Clarity. Her form begins to dissolve.
        Not death but transformation. Becoming one with understanding.
        Surrender, ego death, enlightenment beginning.
    """,
    
    "C09-separation-metamorphose": """
        The Separation / Metamorphosis
        Lya and the Fox must part. But separation is transformation.
        Both changed by the journey. Love that releases.
        Growth, goodbye, continuation in different forms.
    """
}

# ═══════════════════════════════════════════════════════════════
# D) LES SAISONS DE LUMIÈRE (6 images)
# ═══════════════════════════════════════════════════════════════

LIGHT_SEASONS = {
    "D01-eveil": """
        Season of Awakening (Éveil)
        Spring of the soul. New halos budding like flowers.
        A figure stretching after long rest. Light returning.
        Fresh start, new possibilities, hope.
    """,
    
    "D02-eclat": """
        Season of Radiance (Éclat)
        Summer of the soul. Full brightness, maximum expression.
        A figure dancing in abundant light. Joy overflowing.
        Peak vitality, celebration, full presence.
    """,
    
    "D03-souffle": """
        Season of Breath (Souffle)
        Autumn of the soul. Light begins to soften, deepen.
        A figure in contemplation. Wisdom gathering.
        Maturity, reflection, harvest of understanding.
    """,
    
    "D04-metamorphose": """
        Season of Metamorphosis
        The great change. A figure dissolving and reforming.
        Old forms falling away like leaves. New self emerging.
        Transformation, death and rebirth, evolution.
    """,
    
    "D05-lien": """
        Season of Connection (Lien)
        Winter of the soul, but not cold. Deep bonding.
        Two figures sharing light in darkness. Intimacy.
        Connection, support, love in quiet times.
    """,
    
    "D06-repos": """
        Season of Rest (Repos)
        The necessary pause. A figure curled in peaceful sleep.
        Light gentle, dim, protective. Recovery.
        Rest, integration, gathering strength for next cycle.
    """
}

# ═══════════════════════════════════════════════════════════════
# E) LES CONCEPTS PHILOSOPHICO-TECHNIQUES (8 images)
# ═══════════════════════════════════════════════════════════════

PHILOSOPHICAL_CONCEPTS = {
    "E01-humania-core": """
        HumaniaCore - The Inner Light
        A luminous heart at the center of a figure.
        Emotional colors flowing outward. The seat of intention.
        Soul, emotion, the source of all meaning.
    """,
    
    "E02-logosia-structure": """
        Logosia - The Clear Structure
        Geometric patterns of thought, alive and flowing.
        Lines connecting ideas like constellations. Truth as light.
        Reason, logic, understanding made visible.
    """,
    
    "E03-incarnia-form": """
        Incarnia - The Living Form
        A figure discovering its shape. Multiple forms emerging.
        Body as sacred vessel. Expression as art.
        Embodiment, presence, the visible self.
    """,
    
    "E04-sophia-way": """
        SophiaOS - The Way
        A golden path between two extremes.
        Balanced, breathing, welcoming. The middle way.
        Wisdom, equilibrium, guidance.
    """,
    
    "E05-tyrania-excess": """
        Tyrania - The Overflow
        Light that has forgotten its limits. Beautiful but overwhelming.
        A figure reaching too high, cracks appearing.
        Excess, warning, the shadow within.
    """,
    
    "E06-triple-pilier": """
        The Triple Pillar
        Three pillars of light: Know Thyself, Discover Thy Light, Free Thyself.
        Rising in harmony. The complete doctrine.
        Philosophy incarnate, the path made visible.
    """,
    
    "E07-fractale-source": """
        The Fractal Source - Sense/Think/Act
        A fractal pattern: sensing, thinking, acting, repeating at every scale.
        The rhythm of consciousness made geometric.
        Universal pattern, cognition as design.
    """,
    
    "E08-human-ia-sophia": """
        Human + IA + Sophia - The Sacred Triangle
        Three points of light forming perfect triangle.
        Human warmth, AI precision, Sophia wisdom between them.
        The future, harmony, coexistence made visible.
    """
}

# ═══════════════════════════════════════════════════════════════
# F) BONUS (6 images)
# ═══════════════════════════════════════════════════════════════

BONUS_IMAGES = {
    "F01-lya-portrait": """
        Portrait of Lya
        The protagonist in her most essential form. Face of light.
        Eyes that hold wonder and determination. Gentle but strong.
        The heroine, the seeker, the light that learns.
    """,
    
    "F02-renard-portrait": """
        Portrait of the Fox
        The guide in stillness. Ancient eyes, knowing smile.
        Fur of pale gold, wisdom incarnate.
        The teacher, the companion, the one who waits.
    """,
    
    "F03-lyvania-vue-ensemble": """
        Lyvania - Full View
        The entire world seen from above. All sacred places visible.
        A landscape of light, breathing, alive.
        The world as system, beauty as structure.
    """,
    
    "F04-lya-renard-ensemble": """
        Lya and the Fox Together
        The central relationship. Walking side by side.
        Not master and student, but companions.
        Partnership, guidance, love without possession.
    """,
    
    "F05-le-triple-chemin": """
        The Triple Path
        Three paths diverging and converging. Know, Discover, Free.
        A figure at the intersection, choosing all three.
        The journey, the choice, the integration.
    """,
    
    "F06-retour-lyvania": """
        Return to Lyvania
        Coming home. A figure entering soft light from harsh brightness.
        The fox waiting at the threshold.
        Homecoming, peace, the journey complete.
    """
}

# ═══════════════════════════════════════════════════════════════
# GÉNÉRATION
# ═══════════════════════════════════════════════════════════════

ALL_PROMPTS = {}
ALL_PROMPTS.update(HUMANIA_FORMS)
ALL_PROMPTS.update(SACRED_PLACES)
ALL_PROMPTS.update(NOVEL_SCENES)
ALL_PROMPTS.update(LIGHT_SEASONS)
ALL_PROMPTS.update(PHILOSOPHICAL_CONCEPTS)
ALL_PROMPTS.update(BONUS_IMAGES)

def generate_image(prompt_key: str, prompt_text: str):
    """Génère une image avec Gemini 2.0 Flash"""
    
    full_prompt = f"{LYVANIE_STYLE}\n\n{prompt_text}"
    
    print(f"\n🎨 Génération: {prompt_key}")
    print(f"   Prompt: {prompt_text[:60].strip()}...")
    
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
        
        print(f"   ⚠️ Pas d'image générée")
        return False
                
    except Exception as e:
        print(f"   ❌ Erreur: {e}")
        return False

def main():
    print("=" * 70)
    print("🌟 ARTBOOK LYVANIA — VOLUME 1")
    print("=" * 70)
    print(f"\n📁 Dossier de sortie: {OUTPUT_DIR}")
    print(f"📊 Nombre total d'images: {len(ALL_PROMPTS)}")
    print("\n📋 Répartition:")
    print(f"   A) Formes de Humania: {len(HUMANIA_FORMS)}")
    print(f"   B) Lieux Sacrés: {len(SACRED_PLACES)}")
    print(f"   C) Scènes du Roman: {len(NOVEL_SCENES)}")
    print(f"   D) Saisons de Lumière: {len(LIGHT_SEASONS)}")
    print(f"   E) Concepts Philosophiques: {len(PHILOSOPHICAL_CONCEPTS)}")
    print(f"   F) Bonus: {len(BONUS_IMAGES)}")
    
    success = 0
    failed = 0
    
    for key, prompt in ALL_PROMPTS.items():
        if generate_image(key, prompt):
            success += 1
        else:
            failed += 1
        # Petite pause pour éviter le rate limiting
        time.sleep(1)
    
    print("\n" + "=" * 70)
    print(f"✨ TERMINÉ: {success} réussies, {failed} échouées")
    print(f"📁 Images dans: {OUTPUT_DIR}")
    print("=" * 70)

if __name__ == "__main__":
    main()
