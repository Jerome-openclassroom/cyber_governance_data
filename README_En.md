# 🔐 Cyber Governance Data – n8n Workflow

AI-powered n8n workflow for data governance and cybersecurity.  
Monitors script integrity with SHA256, triggers alerts, and uses Human-in-the-Loop validation for secure rollback.  
Integrates RAG for contact lookup, Gmail for alerts, and Google Sheets for reference scripts.

---

## ⚙️ Key Features
- **Integrity check**: SHA256 comparison between active script and reference version.  
- **Automatic alert**: email notification when an altered script is detected.  
- **Workflow chaining**: the main workflow automatically triggers the restoration workflow.  
- **Human-in-the-Loop (HITL)**: password validation before restoring.  
- **Automated rollback**: reinserts the reference script upon validation.  
- **RAG-based contact lookup**: retrieves the responsible security contact from a knowledge base.  

---

## 💾 Project Structure

```
cyber_governance_data/
├── README.md                # Main documentation (French)
├── README_En.md             # English translated documentation
├── code/                    # Workflows and scripts
│   ├── cyber_gouvernance_data.json  # Main workflow blueprint
│   ├── Restauration_HITL.json       # Restoration workflow blueprint (triggered by the main workflow)
│   ├── hashcompare.py               # Python script for hash comparison
│   └── passwords_compare.py         # Python script for password validation
├── screenshots/             # Illustrative screenshots
│   ├── alert_mail.png              # Example of received alert email
│   ├── password_check.png          # Password validation form (HITL)
│   ├── cyber_gouvernance_data.png  # Main workflow overview
│   └── Restauration_HITL.png       # Restoration workflow overview
├── data_RAG/                # RAG support data
│   ├── Agent_Prompt.txt            # System prompt used by the AI agent
│   └── contacts.txt                # Fictitious contacts list (including test address "Jérôme")
```

---

## 📌 Workflow Example

1. **Integrity check**: the workflow computes SHA256 hash of the active script and compares it to the reference.  
2. **If altered**: an alert email is sent and the restoration workflow is triggered.  
3. **HITL – Password validation**: the user is prompted to enter a password.  
4. **If correct**: the reference script is automatically restored.  
5. **Confirmation**: the user receives a final confirmation email.  

---

## 🛠️ Requirements

- [n8n.cloud](https://n8n.io) account or local installation.  
- OpenAI API access (GPT-5).  
- Google account (Gmail + Google Sheets).  
- Python 3.9+ to run utility scripts.  

---

## 🚀 Installation

1. Clone the repository:  
```bash
git clone https://github.com/Jerome-openclassroom/cyber_governance_data.git
```
2. Import `code/cyber_gouvernance_data.json` and `code/Restauration_HITL.json` into n8n.  
3. Configure your credentials (OpenAI, Gmail, Google Sheets).  
4. Launch the main workflow.  

---

## 📸 Screenshots

- **Alert mail**: detection of an altered script.  
- **Password check (HITL)**: validation step before rollback.  

### Workflow overviews

![Main workflow](https://github.com/Jerome-openclassroom/cyber_governance_data/blob/main/screenshots/cyber_gouvernance_data.png)

![Restoration workflow](https://github.com/Jerome-openclassroom/cyber_governance_data/blob/main/screenshots/Restauration_HITL.png)


---

## 📜 License

MIT License.  
