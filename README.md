# 🔐 Cyber Gouvernance Data – Workflow n8n

Ce projet illustre un cas d’usage concret de **cybersécurité et gouvernance des données** en utilisant **n8n** et des agents IA.  
Il démontre comment automatiser :  
- la **surveillance d’intégrité** d’un script,  
- l’**alerte automatique** en cas d’anomalie,  
- la **supervision humaine (HITL)**,  
- et le **rollback sécurisé** d’un script de référence.  

---

## ⚙️ Fonctionnalités principales
- **Vérification d’intégrité** : comparaison SHA256 entre un script actif et une version de référence.  
- **Alerte automatique** : envoi d’un mail dès qu’un script est altéré.  
- **Appel de workflow** : le workflow principal déclenche automatiquement le workflow de restauration.  
- **Supervision humaine (HITL)** : validation par mot de passe avant toute restauration.  
- **Rollback automatisé** : insertion du script de référence si la validation est correcte.  
- **Base de contacts (RAG)** : identification du responsable sécurité à partir d’une liste.  

---

## 💾 Arborescence

```
cyber_gouvernance_data/
├── README.md                # Documentation principale (Français)
├── README_En.md             # Documentation traduite en anglais
├── code/                    # Workflows et scripts
│   ├── cyber_gouvernance_data.json  # Blueprint du workflow principal
│   ├── Restauration_HITL.json       # Blueprint du workflow de restauration (appelé par le principal)
│   ├── hashcompare.py               # Script Python de comparaison des condensats
│   └── passwords_compare.py         # Script Python de comparaison des mots de passe
├── screenshots/             # Captures d’écran illustratives
│   ├── alert_mail.png              # Exemple du mail d’alerte reçu
│   ├── password_check.png          # Interface de saisie du mot de passe (HITL)
│   ├── cyber_gouvernance_data.png  # Vue d’ensemble du workflow principal
│   └── Restauration_HITL.png       # Vue d’ensemble du workflow de restauration
├── data_RAG/                # Données de support RAG
│   ├── Agent_Prompt.txt            # Prompt système utilisé par l’agent IA
│   └── contacts.txt                # Liste de contacts fictifs (incluant l’adresse de test « Jérôme »)
```

---

## 📌 Exemple de fonctionnement

1. **Contrôle d’intégrité** : le workflow calcule le condensat SHA256 du script actif et le compare à la valeur de référence.  
2. **Si altération détectée** : un mail d’alerte est envoyé et un workflow de restauration est déclenché.  
3. **HITL – Validation par mot de passe** : l’utilisateur reçoit un formulaire et doit entrer un mot de passe.  
4. **Si mot de passe correct** : le script de référence est restauré automatiquement.  
5. **Confirmation** : l’utilisateur reçoit un message final confirmant la restauration.  

---

## 🛠️ Prérequis

- Compte [n8n.cloud](https://n8n.io) ou installation locale.  
- Accès à l’API OpenAI (GPT-5).  
- Compte Google (Gmail + Google Sheets).  
- Python 3.9+ pour exécuter les scripts utilitaires.  

---

## 🚀 Installation

1. Cloner le dépôt :  
```bash
git clone https://github.com/Jerome-openclassroom/cyber_gouvernance_data.git
```
2. Importer `code/cyber_gouvernance_data.json` et `code/Restauration_HITL.json` dans n8n.  
3. Configurer vos credentials (OpenAI, Gmail, Google Sheets).  
4. Lancer le workflow principal.  

---

## 📸 Captures

- **Mail d’alerte** : détection d’un script altéré.  
- **Password check (HITL)** : validation par mot de passe.  

### Vue d’ensemble des workflows

![Workflow principal](https://github.com/Jerome-openclassroom/cyber_governance_data/blob/main/screenshots/cyber_gouvernance_data.png)

![Workflow de restauration](https://github.com/Jerome-openclassroom/cyber_governance_data/blob/main/screenshots/Restauration_HITL.png)


---

## 📜 Licence

Projet sous licence MIT.  
