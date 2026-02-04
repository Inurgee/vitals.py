from dkce.integration.dkce_engine import DKCEEngine

def main():
    engine = DKCEEngine()

    vitals_sim = [
        {"glucose": 100, "temp": 38.0, "threat": 0.1},
        {"glucose": 80,  "temp": 40.0, "threat": 0.9},
        {"glucose": 50,  "temp": 90.0, "threat": 0.2},
        {"glucose": 15,  "temp": 37.0, "threat": 0.1},
        {"glucose": 100, "temp": 38.0, "threat": 0.0},
    ]

    engine.run_pulses(vitals_sim)

if __name__ == "__main__":
    main()
