def time_to_text(temps):
    heures = temps // 60
    minutes = temps % 60
    print(f"{heures} heure et {minutes} minutes")
    
time_to_text(67)
time_to_text(123)