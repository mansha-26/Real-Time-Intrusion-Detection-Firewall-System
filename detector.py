SUSPICIOUS_KEYWORDS = ["intrusion", "attack", "malware", "unauthorized"]

class Detector:
    def __init__(self, threshold):
        self.threshold = threshold

    def detect_intrusion(self, data):
        return any(keyword in data.lower() for keyword in SUSPICIOUS_KEYWORDS)