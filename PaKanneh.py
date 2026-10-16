
from datetime import date


class VaccinationRecord:
    """Store information about a patient's vaccination."""

    def __init__(self, vaccine_name, vaccination_date, dose_number):
        if not vaccine_name.strip():
            raise ValueError("Vaccine name cannot be empty.")

        try:
            date.fromisoformat(vaccination_date)
        except ValueError:
            raise ValueError("Date must use YYYY-MM-DD format.")

        if not isinstance(dose_number, int) or dose_number < 1:
            raise ValueError("Dose number must be a positive integer.")

        self.vaccine_name = vaccine_name.strip()
        self.vaccination_date = vaccination_date
        self.dose_number = dose_number

    def display_record(self):
        """Display one vaccination record."""
        print(f"Vaccine: {self.vaccine_name}")
        print(f"Date: {self.vaccination_date}")
        print(f"Dose number: {self.dose_number}")


class Patient:
    """Represent one patient and their vaccination history."""

    def __init__(self, patient_id, name, age, contact):
        if not patient_id.strip():
            raise ValueError("Patient ID cannot be empty.")

        if not name.strip():
            raise ValueError("Patient name cannot be empty.")

        if not isinstance(age, int) or isinstance(age, bool):
            raise ValueError("Age must be a whole number.")

        if not 0 <= age <= 130:
            raise ValueError("Age must be between 0 and 130.")

        self.patient_id = patient_id.strip()
        self.name = name.strip()
        self.age = age
        self.contact = contact.strip()
        self.vaccinations = []

    def add_vaccination(self, vaccination):
        """Add a vaccination object to this patient's history."""
        if not isinstance(vaccination, VaccinationRecord):
            raise TypeError("A valid VaccinationRecord is required.")

        self.vaccinations.append(vaccination)
        return True

    def update_contact(self, new_contact):
        """Update the patient's contact information."""
        self.contact = new_contact.strip()

    def display_record(self):
        """Display patient details and vaccination history."""
        print("\n" + "=" * 40)
        print("PATIENT RECORD")
        print("=" * 40)
        print(f"Patient ID: {self.patient_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Contact: {self.contact}")

        if not self.vaccinations:
            print("Vaccination history: No records available.")
        else:
            print("\nVaccination History:")
            for number, vaccination in enumerate(
                self.vaccinations, start=1
            ):
                print(f"\nVaccination {number}")
                vaccination.display_record()

        print("=" * 40)

    @classmethod
    def from_dictionary(cls, data):
        """Create a patient object from dictionary data."""
        return cls(
            data["patient_id"],
            data["name"],
            data["age"],
            data.get("contact", "")
        )


class PatientManagementSystem:
    """Manage patient records using a dictionary."""

    def __init__(self):
        self.patients = {}

    def add_patient(self, patient):
        """Add a patient if the patient ID is unique."""
        if not isinstance(patient, Patient):
            raise TypeError("A valid Patient object is required.")

        if patient.patient_id in self.patients:
            print("Error: This patient ID already exists.")
            return False

        self.patients[patient.patient_id] = patient
        print("Patient added successfully.")
        return True

    def find_patient(self, patient_id):
        """Search for a patient using their ID."""
        return self.patients.get(patient_id.strip())

    def display_all_patients(self):
        """Display every stored patient record."""
        if not self.patients:
            print("No patient records are available.")
            return

        for patient in self.patients.values():
            patient.display_record()

    def display_patient(self, patient_id):
        """Display one patient's record."""
        patient = self.find_patient(patient_id)

        if patient is None:
            print("Patient not found.")
            return

        patient.display_record()


def main():
    system = PatientManagementSystem()

    # Demonstrate the @classmethod.
    patient_data = {
        "patient_id": "P001",
        "name": "Amandus Benjamin Coker",
        "age": 31,
        "contact": "amandus.bcoker01@limkokwing.edu.sl"
    }

    patient = Patient.from_dictionary(patient_data)
    system.add_patient(patient)

    # Demonstrate object interaction.
    vaccination = VaccinationRecord(
        "Example Vaccine",
        "2026-10-10",
        1
    )
    patient.add_vaccination(vaccination)

    # Add a second patient using the normal constructor.
    second_patient = Patient(
        "P002",
        "Prince Kanneh",
        26,
        "princekanneh01@gmail.com"
    )
    system.add_patient(second_patient)

    # Display the records.
    system.display_all_patients()

    # Demonstrate searching.
    print("\nSEARCH RESULT")
    result = system.find_patient("P001")

    if result:
        print(f"Found patient: {result.name}")
    else:
        print("Patient not found.")

    # Demonstrate updating.
    second_patient.update_contact("new@email.com")
    print("Updated contact:", second_patient.contact)
    print("\nContact information updated.")


if __name__ == "__main__":
    main()
