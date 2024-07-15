def get_binary_input(question):
    while True:
        answer = input(question + " (0 = No, 1 = Yes): ").strip()
        if answer in ['0', '1']:
            return int(answer)
        print("Invalid input. Please enter 0 or 1.")

def get_numeric_input(question, min_val, max_val):
    while True:
        try:
            answer = int(input(question + f" ({min_val}-{max_val}): "))
            if min_val <= answer <= max_val:
                return answer
            print(f"Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_age_category():
    age_categories = [
        "1. 18-24",
        "2. 25-29",
        "3. 30-34",
        "4. 35-39",
        "5. 40-44",
        "6. 45-49",
        "7. 50-54",
        "8. 55-59",
        "9. 60-64",
        "10. 65-69",
        "11. 70-74",
        "12. 75-79",
        "13. 80 or older"
    ]
    
    print("\nWhat is your age category?")
    for category in age_categories:
        print(category)
    
    return get_numeric_input("Enter the number corresponding to your age category", 1, 13)

def get_income_level():
    income_levels = [
        "1. Less than $10,000",
        "2. $10,000 to less than $15,000",
        "3. $15,000 to less than $20,000",
        "4. $20,000 to less than $25,000",
        "5. $25,000 to less than $35,000",
        "6. $35,000 to less than $50,000",
        "7. $50,000 to less than $75,000",
        "8. $75,000 or more"
    ]
    
    print("\nWhat is your income level?")
    for level in income_levels:
        print(level)
    
    return get_numeric_input("Enter the number corresponding to your income level", 1, 8)

def main():
    responses = []

    # Questions 1-3, 5-13, 17-18
    binary_questions = [
        "Do you have high blood pressure?",
        "Do you have high cholesterol?",
        "Have you had a cholesterol check in the past 5 years?",
        "Have you smoked at least 100 cigarettes in your entire life?",
        "Have you ever been told you had a stroke?",
        "Have you ever had coronary heart disease (CHD) or myocardial infarction (MI)?",
        "Have you engaged in physical activity in the past 30 days, not including job?",
        "Do you consume fruit 1 or more times per day?",
        "Do you consume vegetables 1 or more times per day?",
        "Are you a heavy drinker? (Adult men >14 drinks/week, adult women >7 drinks/week)",
        "Do you have any kind of health care coverage?",
        "Was there a time in the past 12 months when you needed to see a doctor but could not because of cost?",
        "Do you have serious difficulty walking or climbing stairs?",
        "What is your sex? (0 = female, 1 = male)"
    ]

    for question in binary_questions:
        responses.append(get_binary_input(question))

    # Question 4: BMI
    responses.append(get_numeric_input("What is your Body Mass Index?", 1, 100))

    # Questions 14-16
    responses.append(get_numeric_input("In general, how would you say your health is? (1 = excellent, 5 = poor)", 1, 5))
    responses.append(get_numeric_input("For how many days during the past 30 days was your mental health not good?", 0, 30))
    responses.append(get_numeric_input("For how many days during the past 30 days was your physical health not good?", 0, 30))

    # Question 19: Age
    responses.append(get_age_category())

    # Question 20: Income
    responses.append(get_income_level())

    # Questions 21-26: Education
    print("\nWhat is your highest level of education?")
    print("1. College 1 year to 3 years (Some college or technical school)")
    print("2. College 4 years or more (College graduate)")
    print("3. Grade 12 or GED (High school graduate)")
    print("4. Grades 1 through 8 (Elementary)")
    print("5. Grades 9 through 11 (Some high school)")
    print("6. Never attended school or only kindergarten")
    
    education_choice = get_numeric_input("Enter the number corresponding to your education level", 1, 6)
    education_responses = [0] * 6
    education_responses[education_choice - 1] = 1
    responses.extend(education_responses)

    print("\nSurvey complete. Responses:", responses)
    return responses

if __name__ == "__main__":
    main()