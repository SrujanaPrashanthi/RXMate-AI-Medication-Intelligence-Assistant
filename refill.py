# refill.py

refill_data = {

    "abhi@gmail.com": {
        "medicine": "Metformin 500mg",
        "last_refill": "2025-07-01",
        "next_refill_due": "2025-08-01",
        "status": "Upcoming"
    },
    "sathvika@gmail.com": {
        "medicine": "Amlodipine 5mg",
        "last_refill": "2025-07-15",
        "next_refill_due": "2025-08-15",
        "status": "Upcoming"
    }
}

def check_refill_status(username):
    username = username.strip().lower()

    for key in refill_data:
        if key == username or username in key:
            return refill_data[key]
    return None