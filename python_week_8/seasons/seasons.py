from datetime import date
import sys
import inflect

def main():
   birthdate = get_birthdate_from_input()
   age_in_minutes = calculate_age_in_minutes(birthdate)
   age_in_words = format_minutes_in_words(age_in_minutes)
   print(f"{age_in_words} minutes")


def calculate_age_in_minutes(birthdate: date):
    today = date.today()
    delta = today - birthdate
    age_in_minutes = delta.days * 24 * 60
    return age_in_minutes


def get_birthdate_from_input():
        try:
            birthdate_str = input("Date of Birth: ")
            birthdate = date.fromisoformat(birthdate_str)
            return birthdate
        except ValueError:
            print("Invalid date format")
            sys.exit(1)


def format_minutes_in_words(minutes):
    inflect_engine = inflect.engine()
    return inflect_engine.number_to_words(minutes, andword="").capitalize()



if __name__ == "__main__":
    main()
