from collections import defaultdict

USER_PROFILES = {
    "user123": {
        "usual_country": "US",
        "avg_transaction": 500.0,
        "account_age_days": 90,
        "known_devices": ["iphone_12", "macbook_pro_2020"],
        "active_hours": (9, 17)
    },
    "user456": {
        "usual_country": "CA",
        "avg_transaction": 1200.0,
        "account_age_days": 365,
        "known_devices": ["samsung_galaxy_s21", "ipad_pro"],
        "active_hours": (8, 16) 
    },
    "user789": {
        "usual_country": "GB",
        "avg_transaction": 200.0,
        "account_age_days": 3,
        "known_devices": ["unknown_device"],
        "active_hours": (0, 23)
    },
    "user_highroller": {
        "usual_country": "AE",
        "avg_transaction": 25000.0,
        "account_age_days": 180,
        "known_devices": ["iphone_14_pro", "windows_pc"],
        "active_hours": (20, 2)
    },
    "user_nomad": {
        "usual_country": "FR",
        "avg_transaction": 800.0,
        "account_age_days": 60,
        "known_devices": ["google_pixel_7"],
        "active_hours": (10, 18)
    },
    "user_risky1": {
        "usual_country": "DE",
        "avg_transaction": 150.0,
        "account_age_days": 5,
        "known_devices": ["burner_phone"],
        "active_hours": (3, 5)
    },
    "user_risky2": {
        "usual_country": "AU",
        "avg_transaction": 300.0,
        "account_age_days": 30,
        "known_devices": ["hacked_device"],
        "active_hours": (12, 14)
    }
}

TRANSACTION_COUNTS = defaultdict(int)

HIGH_RISK_RECIPIENTS = ["acct_hacker1", 
                        "acct_fraudster2",
                        "acct_darkweb123", 
                        "acct_moneylaunder", 
                        "acct_phishing_scam",
                        "acct_ransomware"]
