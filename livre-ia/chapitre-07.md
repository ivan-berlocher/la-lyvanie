# Chapitre 7
## Le modèle économique (suivez l'argent)

---

Pour comprendre l'IA, suivez l'argent.

Qui paie ? Qui gagne ? Pourquoi ChatGPT est-il "gratuit" ? Ces questions révèlent les vraies motivations des géants de la tech — et ce que vous leur donnez sans le savoir.

---

### 7.1 Pourquoi ChatGPT est "gratuit" (spoiler : vous êtes le produit)

Ouvrez un compte ChatGPT. Posez des questions pendant des heures. Ne payez rien.

Comment est-ce possible ?

**Le modèle freemium**

ChatGPT offre une version gratuite pour une raison simple : vous attirer, vous habituer, vous rendre dépendant. Ensuite, vous passerez (peut-être) à la version payante (20€/mois) pour avoir accès aux fonctionnalités premium.

**Mais ce n'est pas tout.**

Même si vous ne payez jamais, vous êtes rentable. Voici comment :

**1. Vos données améliorent le produit**

Chaque conversation que vous avez avec ChatGPT peut être utilisée pour améliorer les futurs modèles. Vos questions, vos reformulations, vos corrections — tout cela est de l'or pour l'entraînement.

**2. Vous générez des effets de réseau**

Plus de gens utilisent ChatGPT, plus ça crée du buzz, plus d'autres gens veulent l'essayer. Vous êtes le marketing.

**3. Vous validez le produit**

Vos usages montrent ce qui marche et ce qui ne marche pas. Vous êtes le département qualité gratuit.

**La vraie économie**

Si un service est gratuit, vous n'êtes pas le client. Vous êtes le produit.

C'était vrai pour Google, Facebook, et les réseaux sociaux. C'est vrai pour l'IA.

---

### 7.2 Le coût réel d'entraîner un LLM

Créer un modèle comme GPT-4 coûte une fortune.

**L'entraînement**

- Des dizaines de milliers de GPU (cartes graphiques spécialisées à ~30 000€ pièce)
- Des mois de calcul continu
- Une consommation électrique colossale

Estimation pour GPT-4 : **entre 50 et 100 millions de dollars** rien que pour l'entraînement.

**L'inférence**

Ensuite, chaque fois que vous posez une question, le modèle doit "tourner" sur des serveurs. C'est l'inférence.

À l'échelle de 100 millions d'utilisateurs, ça représente des millions de dollars par jour en coûts de serveurs.

**Le paradoxe économique**

OpenAI perd de l'argent sur chaque utilisateur gratuit. L'entreprise brûle des milliards en espérant :
- Convertir des utilisateurs en payants
- Vendre des API aux entreprises
- Prendre une position dominante avant que les coûts baissent

C'est un pari massif. Qui marche tant que les investisseurs y croient.

---

### 7.3 L'API : comment les entreprises paient

Le vrai business d'OpenAI n'est pas vous. C'est les entreprises.

**L'API**

Une API (Application Programming Interface) permet à une entreprise d'intégrer ChatGPT dans ses propres produits. Votre banque, votre assurance, votre service client — beaucoup utilisent déjà l'API d'OpenAI en coulisses.

**Le prix**

Vous payez par "token" (environ 0,75 mot). Quelques centimes pour une réponse simple. Mais à l'échelle, ça chiffre vite :

- Une entreprise qui traite 1 million de requêtes par jour → des dizaines de milliers d'euros par mois
- Un usage intensif → des millions par an

**Le verrouillage**

Une fois qu'une entreprise a intégré l'API d'OpenAI dans ses systèmes, il est coûteux de changer. C'est le "lock-in" — le verrouillage.

C'est pourquoi la conquête de parts de marché est si agressive. Chaque entreprise convertie est une source de revenus récurrents pour des années.

---

### 7.4 La course aux données : votre texte vaut de l'or

Pour entraîner un LLM, il faut du texte. Beaucoup de texte.

**D'où viennent les données ?**

- Wikipédia (gratuit, mais limité)
- Livres numérisés (parfois sans l'accord des auteurs)
- Le web entier (aspiré par des "crawlers")
- Les réseaux sociaux (Reddit, Twitter...)
- Et... vos conversations avec l'IA

**Le problème du consentement**

Beaucoup de ces données ont été collectées sans demander l'avis des auteurs originaux. Des procès sont en cours aux États-Unis et en Europe.

**La valeur de vos données**

Quand vous corrigez ChatGPT ("Non, ce n'est pas ça, voici la bonne réponse"), vous faites du travail d'annotation gratuit. Ce travail vaut normalement plusieurs dollars de l'heure quand il est fait par des professionnels.

Multipliez par 100 millions d'utilisateurs : c'est une main-d'œuvre gratuite colossale.

---

### 7.5 Le cloud comme dépendance stratégique

Le dernier élément du puzzle économique : le cloud.

**Où tourne l'IA ?**

Pas sur votre ordinateur. Sur des serveurs distants, dans des datacenters géants.

**Qui possède ces datacenters ?**

- Amazon (AWS) : ~32% du marché mondial
- Microsoft (Azure) : ~23%
- Google (GCP) : ~10%
- Alibaba, autres : le reste

**Presque aucun datacenter européen de cette échelle.**

**La dépendance**

Utiliser l'IA, c'est envoyer vos données vers des serveurs américains, gérés par des entreprises américaines, soumises au droit américain.

Le Cloud Act de 2018 permet au gouvernement américain d'exiger l'accès aux données stockées par des entreprises américaines, même si les serveurs sont physiquement en Europe.

**Le coût de la dépendance**

- Pas de contrôle sur vos données
- Pas de levier en cas de conflit
- Des milliards d'euros qui partent aux États-Unis

---

### Ce que vous pouvez faire

1. **Comprenez le deal.** Quand c'est gratuit, vous payez autrement — en données, en attention, en habitudes.

2. **Lisez les conditions.** Oui, c'est long. Cherchez au moins les sections sur les données.

3. **Désactivez le partage quand possible.** ChatGPT a une option pour ne pas utiliser vos conversations pour l'entraînement. Activez-la.

4. **Préférez les modèles locaux.** Des alternatives comme Llama peuvent tourner sur votre ordinateur, sans envoyer de données.

5. **Soutenez les alternatives européennes.** Même si elles sont imparfaites, elles offrent une diversité nécessaire.

---

*Chapitre suivant : Vos données, leur trésor*
