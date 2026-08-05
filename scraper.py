import json
import datetime

def fetch_bordeaux_deals():
    return [
        {
            "id": "cyc_moust_203",
            "marque": "Moustache",
            "modele": "Lundi 20.3",
            "type": "Longtail",
            "magasin": "Cyclable Bordeaux Chartrons",
            "prix_original": 4699,
            "prix_promo": 3899,
            "remise_pct": 17,
            "url": "https://www.cyclable.com/bordeaux-chartrons",
            "img": "https://images.unsplash.com/photo-1558981806-ec527fa84c39?w=500"
        },
        {
            "id": "dec_r500e",
            "marque": "Decathlon",
            "modele": "Cargo Longtail R500E",
            "type": "Longtail",
            "magasin": "Decathlon Bordeaux Lac",
            "prix_original": 2990,
            "prix_promo": 2490,
            "remise_pct": 17,
            "url": "https://www.decathlon.fr",
            "img": "https://images.unsplash.com/photo-1571068316344-75bc76f77890?w=500"
        }
    ]

if __name__ == "__main__":
    data = {
        "last_updated": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        "items": fetch_bordeaux_deals()
    }
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
