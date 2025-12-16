# Chapitre 15
## Protéger ses données au quotidien

---

Vous ne pouvez pas échapper totalement à l'IA.
Elle est dans votre téléphone, vos emails, vos recherches, vos achats.

Mais vous pouvez réduire votre exposition.
Voici comment.

---

### 15.1 L'hygiène numérique de base

**Ces gestes simples font une grande différence :**

| Geste | Impact | Difficulté |
|-------|--------|------------|
| Utiliser un gestionnaire de mots de passe | Élevé | Facile |
| Activer l'authentification à deux facteurs | Élevé | Facile |
| Mettre à jour ses appareils | Élevé | Facile |
| Utiliser des emails différents (pro/perso/poubelle) | Moyen | Facile |
| Vérifier les autorisations des applications | Moyen | Facile |
| Désactiver la géolocalisation quand non nécessaire | Moyen | Facile |

**L'erreur classique :**

Beaucoup de gens ont un excellent mot de passe... qu'ils utilisent partout.
Un seul site piraté = tous vos comptes compromis.

---

### 15.2 Paramétrer ses outils IA

**ChatGPT (OpenAI)**

Allez dans Settings → Data Controls :
- ❌ Désactivez "Improve the model for everyone"
- ✅ Activez "Temporary Chat" pour les conversations sensibles
- Vérifiez régulièrement l'historique et supprimez le superflu

**Google (Gemini, Search)**

Allez dans Mon compte Google → Données et confidentialité :
- ❌ Désactivez "Activité sur le Web et les applications" (ou limitez)
- ❌ Désactivez "Personnalisation des annonces"
- Supprimez régulièrement l'historique

**Microsoft (Copilot)**

Allez dans Paramètres du compte Microsoft :
- Vérifiez les autorisations Copilot
- Gérez l'historique de recherche Bing
- Pour Copilot entreprise : demandez les paramètres à votre IT

**Claude (Anthropic)**

Allez dans Settings :
- Vérifiez les options de confidentialité
- Opt-out de l'entraînement si disponible

---

### 15.3 Les données que vous ne savez pas que vous donnez

**Au-delà de ce que vous tapez :**

- **Métadonnées** : Quand vous vous connectez, combien de temps, sur quel appareil
- **Habitudes** : Vos horaires, vos patterns de recherche
- **Inférences** : Ce que l'IA déduit de vos questions
- **Contexte** : Les fichiers que vous uploadez, les images, les documents

**Exemple :**

Vous demandez à ChatGPT : "Comment annoncer un divorce à mes enfants ?"

Vous venez de révéler :
- Que vous divorcez
- Que vous avez des enfants
- Votre niveau de détresse (peut-être)
- Votre style de communication

Ces informations, agrégées sur des milliers d'utilisateurs, ont de la valeur.

---

### 15.4 Le principe du "minimum nécessaire"

**Ne donnez que ce qui est strictement nécessaire.**

| Besoin | Mauvaise pratique | Bonne pratique |
|--------|-------------------|----------------|
| Résumer un article | Coller le texte intégral | Donner juste le lien ou les points clés |
| Rédiger un email pro | Donner tout le contexte interne | Formuler le besoin de manière générique |
| Analyser des données | Uploader le fichier complet | Anonymiser ou utiliser des données d'exemple |
| Aide au code | Coller tout le projet | Isoler la fonction problématique |

**La règle d'or :**

Avant de soumettre quelque chose à une IA, demandez-vous :
"Est-ce que j'accepterais que cette information soit publique ?"

---

### 15.5 Les outils de protection

**Navigateurs et extensions :**

- **Brave** : Navigateur avec protection intégrée contre le tracking
- **Firefox** + uBlock Origin : Bloque publicités et trackers
- **DuckDuckGo** : Moteur de recherche sans tracking

**Email :**

- **Proton Mail** : Email chiffré, basé en Suisse
- **SimpleLogin / AnonAddy** : Alias email pour ne pas donner votre vraie adresse

**VPN :**

- **Mullvad** : VPN axé confidentialité, pas de compte, paiement anonyme possible
- **ProtonVPN** : Du même fournisseur que ProtonMail

**Gestionnaire de mots de passe :**

- **Bitwarden** : Open source, gratuit, audité
- **1Password** : Payant mais excellent

**Note :**

Ces outils ne sont pas parfaits et ne vous rendent pas invisible.
Mais ils réduisent significativement votre exposition.

---

### 15.6 Les alternatives locales

**Faire tourner l'IA sur votre machine = vos données restent chez vous.**

**Pour le texte :**

- **Ollama** : Permet de faire tourner des LLM localement
- **LM Studio** : Interface graphique pour modèles locaux
- **GPT4All** : Solution simple pour débutants

**Pour les images :**

- **Stable Diffusion** (local) : Génération d'images sur votre PC
- **AUTOMATIC1111** : Interface populaire pour Stable Diffusion

**Pour la transcription :**

- **Whisper** (OpenAI, mais local) : Transcription audio de qualité

**Les limites :**

- Qualité souvent inférieure aux modèles cloud
- Nécessite un ordinateur puissant
- Plus complexe à configurer

Mais vos données restent chez vous. Ça a un prix.

---

### 15.7 Au travail : les bonnes pratiques

**Si votre entreprise utilise des outils IA :**

| Situation | Recommandation |
|-----------|----------------|
| Email avec Copilot | Ne pas écrire d'informations confidentielles dans les brouillons |
| Résumé de réunion | Demander le consentement des participants |
| Analyse de documents | Vérifier la classification des documents |
| Code avec Copilot | Attention aux secrets (API keys, mots de passe) |
| Questions RH sensibles | Utiliser des canaux non-surveillés |

**La règle générale :**

Tout ce que vous faites avec un outil d'entreprise peut potentiellement être vu par :
- L'outil IA lui-même
- Votre département IT
- Votre management

Comportez-vous en conséquence.

---

### 15.8 Les enfants et l'IA

**Les mineurs sont particulièrement vulnérables.**

**Ce qu'ils ne comprennent pas toujours :**

- Que leurs conversations sont stockées
- Que les images qu'ils génèrent peuvent révéler des choses sur eux
- Que les informations partagées peuvent les suivre des années

**Ce que vous pouvez faire :**

1. **Expliquez** le fonctionnement (vos données ont de la valeur)
2. **Supervisez** les premiers usages
3. **Définissez des règles** (pas d'infos personnelles, pas de photos de famille)
4. **Utilisez les contrôles parentaux** quand disponibles
5. **Montrez l'exemple** (vos propres pratiques)

**Les outils pour enfants :**

Certains outils IA ont des versions "enfants" avec plus de restrictions.
Mais la meilleure protection reste l'éducation.

---

### 15.9 Que faire si vos données ont fuité ?

**Les signes d'alerte :**

- Emails de phishing très personnalisés
- Connexions suspectes à vos comptes
- Publicités étrangement pertinentes
- Notifications "nouveau connexion" non reconnues

**Actions immédiates :**

1. **Changez les mots de passe** des comptes concernés
2. **Vérifiez les connexions actives** et déconnectez les suspectes
3. **Activez 2FA** partout si ce n'est pas déjà fait
4. **Surveillez vos comptes bancaires**
5. **Consultez haveibeenpwned.com** pour voir si votre email a fuité

**Pour le RGPD :**

Si vous pensez qu'une entreprise a mal protégé vos données :
1. Contactez leur DPO
2. Demandez des explications par écrit
3. Si pas de réponse satisfaisante, plainte CNIL

---

### Checklist quotidienne

| Habitude | Fréquence |
|----------|-----------|
| Vérifier les autorisations des nouvelles apps | À chaque installation |
| Supprimer l'historique des conversations IA | Hebdomadaire |
| Vérifier les connexions à vos comptes | Mensuel |
| Revoir les paramètres de confidentialité | Trimestriel |
| Supprimer les comptes inutilisés | Annuel |

---

### Ce que vous pouvez faire

1. **Commencez par UN changement.** Installer un gestionnaire de mots de passe, par exemple.

2. **Paramétrez vos outils IA.** 5 minutes dans les paramètres peuvent faire une grande différence.

3. **Adoptez le réflexe "minimum nécessaire".** Moins vous donnez, moins vous risquez.

4. **Explorez les alternatives locales.** Si vous avez un bon PC, essayez Ollama.

5. **Éduquez vos proches.** Les pratiques de protection sont contagieuses (dans le bon sens).

---

*Chapitre suivant : Utiliser l'IA sans se faire manipuler*
