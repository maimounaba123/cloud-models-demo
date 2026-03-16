import os
from flask import Flask, render_template, jsonify

app = Flask(__name__)

CLOUD_MODELS = {
    "iaas": {
        "name": "IaaS",
        "full": "Infrastructure as a Service",
        "color": "#e74c3c",
        "description": "Le fournisseur gere l infrastructure physique. Le client controle tout le reste.",
        "fournisseur": ["Serveurs physiques", "Stockage", "Reseau", "Virtualisation"],
        "client": ["Systeme exploitation", "Runtime", "Middleware", "Applications", "Donnees"],
        "exemples": [
            {"nom": "AWS EC2", "usage": "Louer des serveurs virtuels a la demande"},
            {"nom": "Google Compute Engine", "usage": "VMs dans le reseau mondial Google"},
            {"nom": "Azure Virtual Machines", "usage": "Integration Microsoft Office 365"},
        ],
        "pour_qui": "Grandes entreprises, equipes DevOps, jeux video",
        "analogie": "Terrain vide - tu construis tout toi-meme",
        "avantages": ["Controle total", "Flexibilite maximale", "Pay-as-you-go"],
        "inconvenients": ["Complexe a gerer", "Necessite des experts", "Temps de config long"],
    },
    "paas": {
        "name": "PaaS",
        "full": "Platform as a Service",
        "color": "#8e44ad",
        "description": "Le fournisseur gere l infrastructure ET la plateforme. Le client se concentre sur son code.",
        "fournisseur": ["Serveurs physiques", "Stockage", "Reseau", "Virtualisation", "Systeme exploitation", "Runtime", "Middleware"],
        "client": ["Applications", "Donnees"],
        "exemples": [
            {"nom": "Heroku", "usage": "Deployer une app en 1 commande git push"},
            {"nom": "Google App Engine", "usage": "Scale automatique de 0 a 1M users"},
            {"nom": "Azure App Service", "usage": "Apps web connectees a Microsoft"},
        ],
        "pour_qui": "Developpeurs, startups, equipes agiles",
        "analogie": "Maison a finir - fondations pretes, tu decores",
        "avantages": ["Deploiement rapide", "Pas de gestion serveur", "Scale automatique"],
        "inconvenients": ["Moins de controle", "Vendor lock-in possible", "Cout plus eleve"],
    },
    "saas": {
        "name": "SaaS",
        "full": "Software as a Service",
        "color": "#27ae60",
        "description": "Le fournisseur gere TOUT. Le client utilise simplement l application via un navigateur.",
        "fournisseur": ["Serveurs physiques", "Stockage", "Reseau", "Virtualisation", "Systeme exploitation", "Runtime", "Middleware", "Applications"],
        "client": ["Donnees uniquement"],
        "exemples": [
            {"nom": "Gmail", "usage": "Messagerie sans rien installer"},
            {"nom": "Salesforce", "usage": "CRM complet accessible depuis le browser"},
            {"nom": "Notion", "usage": "Collaboration en temps reel, 0 configuration"},
        ],
        "pour_qui": "Tout le monde - entreprises, particuliers, PME",
        "analogie": "Maison meublee - tu n as plus qu a vivre dedans",
        "avantages": ["Zero installation", "Accessible partout", "Mises a jour automatiques"],
        "inconvenients": ["Aucun controle technique", "Dependance fournisseur", "Donnees chez un tiers"],
    }
}

@app.route("/")
def index():
    return render_template("index.html", models=CLOUD_MODELS)

@app.route("/api/model/<model_id>")
def get_model(model_id):
    if model_id in CLOUD_MODELS:
        return jsonify(CLOUD_MODELS[model_id])
    return jsonify({"error": "Modele non trouve"}), 404

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
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
