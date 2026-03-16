from flask import Flask, render_template, jsonify

app = Flask(__name__)

# ── Données des 3 modèles cloud ──
CLOUD_MODELS = {
    "iaas": {
        "name": "IaaS",
        "full": "Infrastructure as a Service",
        "color": "#e74c3c",
        "emoji": "🏗️",
        "description": "Le fournisseur gère l'infrastructure physique. Le client contrôle tout le reste.",
        "fournisseur": ["Serveurs physiques", "Stockage", "Réseau", "Virtualisation"],
        "client": ["Système d'exploitation", "Runtime", "Middleware", "Applications", "Données"],
        "exemples": [
            {"nom": "AWS EC2", "usage": "Louer des serveurs virtuels à la demande"},
            {"nom": "Google Compute Engine", "usage": "VMs dans le réseau mondial Google"},
            {"nom": "Azure Virtual Machines", "usage": "Intégration Microsoft Office 365"},
        ],
        "pour_qui": "Grandes entreprises, équipes DevOps, jeux vidéo",
        "analogie": "🏚️ Terrain vide — tu construis tout toi-même",
        "avantages": ["Contrôle total", "Flexibilité maximale", "Pay-as-you-go"],
        "inconvenients": ["Complexe à gérer", "Nécessite des experts", "Temps de config long"],
    },
    "paas": {
        "name": "PaaS",
        "full": "Platform as a Service",
        "color": "#8e44ad",
        "emoji": "🏗️",
        "description": "Le fournisseur gère l'infrastructure ET la plateforme. Le client se concentre sur son code.",
        "fournisseur": ["Serveurs physiques", "Stockage", "Réseau", "Virtualisation",
                        "Système d'exploitation", "Runtime", "Middleware"],
        "client": ["Applications", "Données"],
        "exemples": [
            {"nom": "Heroku", "usage": "Déployer une app en 1 commande git push"},
            {"nom": "Google App Engine", "usage": "Scale automatique de 0 à 1M users"},
            {"nom": "Azure App Service", "usage": "Apps web connectées à l'écosystème Microsoft"},
        ],
        "pour_qui": "Développeurs, startups, équipes agiles",
        "analogie": "🏗️ Maison à finir — fondations prêtes, tu décores",
        "avantages": ["Déploiement rapide", "Pas de gestion serveur", "Scale automatique"],
        "inconvenients": ["Moins de contrôle", "Vendor lock-in possible", "Coût plus élevé"],
    },
    "saas": {
        "name": "SaaS",
        "full": "Software as a Service",
        "color": "#27ae60",
        "emoji": "🏠",
        "description": "Le fournisseur gère TOUT. Le client utilise simplement l'application via un navigateur.",
        "fournisseur": ["Serveurs physiques", "Stockage", "Réseau", "Virtualisation",
                        "Système d'exploitation", "Runtime", "Middleware", "Applications"],
        "client": ["Données uniquement"],
        "exemples": [
            {"nom": "Gmail", "usage": "Messagerie sans rien installer"},
            {"nom": "Salesforce", "usage": "CRM complet accessible depuis le browser"},
            {"nom": "Notion", "usage": "Collaboration en temps réel, 0 configuration"},
        ],
        "pour_qui": "Tout le monde — entreprises, particuliers, PME",
        "analogie": "🏠 Maison meublée — tu n'as plus qu'à vivre dedans",
        "avantages": ["Zéro installation", "Accessible partout", "Mises à jour automatiques"],
        "inconvenients": ["Aucun contrôle technique", "Dépendance au fournisseur", "Données chez un tiers"],
    }
}

@app.route("/")
def index():
    return render_template("index.html", models=CLOUD_MODELS)

@app.route("/api/model/<model_id>")
def get_model(model_id):
    if model_id in CLOUD_MODELS:
        return jsonify(CLOUD_MODELS[model_id])
    return jsonify({"error": "Modèle non trouvé"}), 404

@app.route("/api/compare")
def compare():
    comparison = {}
    for key, model in CLOUD_MODELS.items():
        comparison[key] = {
            "name": model["name"],
            "color": model["color"],
            "client_gere": len(model["client"]),
            "fournisseur_gere": len(model["fournisseur"]),
            "pour_qui": model["pour_qui"],
        }
    return jsonify(comparison)

if __name__ == "__main__":
    app.run(debug=True)
```

---

### Fichier 2 : `requirements.txt`
```
flask==3.0.0
gunicorn==21.2.0
