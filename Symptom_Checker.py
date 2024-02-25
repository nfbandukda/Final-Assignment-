class Symptom:
    def __init__(self, name, conditions, actions, medicines):
        self.name = name
        self.conditions = conditions
        self.actions = actions
        self.medicines = medicines

class SymptomChecker:
    def __init__(self):
        self.symptoms = [
            Symptom("cough", ["Common Cold", "Flu", "Bronchitis"], ["Stay hydrated", "Rest", "Over-the-counter cough syrup"], ["Acetaminophen", "Ibuprofen"]),
            Symptom("fever", ["Flu", "COVID-19", "Pneumonia"], ["Rest", "Stay hydrated", "Take fever-reducing medication"], ["Acetaminophen", "Aspirin"]),
            Symptom("hepatitis", ["Hepatitis A", "Hepatitis B", "Hepatitis C"], ["Rest", "Maintain hydration", "Consult a doctor"], ["Antiviral medication", "Vaccination"]),
            Symptom("tb", ["Tuberculosis"], ["Complete antibiotic course", "Rest", "Isolation during contagious period"], ["Antibiotics"]),
            Symptom("corona", ["COVID-19"], ["Isolate", "Seek medical attention", "Follow health guidelines"], ["Antiviral medication", "Vaccination (if available)"]),
            Symptom("toothache", ["Tooth decay", "Gum disease", "Tooth abscess"], ["Rinse with warm saltwater", "Use pain relievers", "See a dentist"], ["Pain relievers", "Antibiotics (if infection)"]),
            Symptom("headache", ["Tension headache", "Migraine", "Cluster headache"], ["Rest in a dark, quiet room", "Hydrate", "Over-the-counter pain relievers"], ["Prescription medications"]),
            Symptom("migraine", ["Migraine"], ["Rest in a dark, quiet room", "Stay hydrated", "Use cold or warm compress"], ["Prescription migraine medications"]),
            Symptom("low blood pressure", ["Hypotension"], ["Increase salt intake", "Stay hydrated", "Eat smaller, more frequent meals"], ["No specific medication (unless severe)"]),
            Symptom("high blood pressure", ["Hypertension"], ["Adopt a healthy diet", "Exercise regularly", "Reduce sodium intake"], ["Antihypertensive medications"]),
            Symptom("heat stroke", ["Heat exhaustion", "Dehydration", "Heat cramps", "Rhabdomyolysis", "Hyponatremia", "Cardiac events related to heat", "Renal failure related to heat"], ["Move to a cooler place", "Cool the body with cold compresses", "Rehydrate with water or electrolyte drinks"], ["Emergency medical attention"]),
        ]

    def check_symptoms(self, user_symptoms):
        symptom_results = {}

        for user_symptom in user_symptoms:
            matched_symptoms = [symptom for symptom in self.symptoms if
                                user_symptom.lower() == symptom.name.lower() or user_symptom.lower() in
                                map(str.lower, symptom.conditions)]
            if matched_symptoms:
                for symptom in matched_symptoms:
                    symptom_results[symptom.name] = {
                        "conditions": symptom.conditions,
                        "actions": symptom.actions,
                        "medicines": symptom.medicines
                    }

        return symptom_results

while True:
    symptom_checker = SymptomChecker()
    user_symptoms = input("Welcome to the symptom checker!"'\n' "To provide you with accurate information, please be specific about your symptoms."'\n' "Remember, this tool is not a substitute for professional medical advice."'\n' "If you have a medical emergency, call your local emergency number immediately"'\n\n'"Enter your symptoms (comma-separated): ").lower().split(',')

    symptom_results = symptom_checker.check_symptoms(user_symptoms)

    if symptom_results:
        print("\nSymptom Checker Results:")
        for symptom, info in symptom_results.items():
            print("\nFor " + symptom + ":")
            print("Possible Conditions:")
            for condition in info["conditions"]:
                print("- " + condition)
            print("Recommended Actions:")
            for action in info["actions"]:
                print("- " + action)
            print("Prescribed Medicine:")
            for medicine in info["medicines"]:
                print("- " + medicine)
    else:
        print("\nNo matching conditions found for the provided symptoms.")

    another_input = input("Do you want to check symptoms again? (yes/no): ").lower()
    if another_input != 'yes':
        break
