
# Project 3: Rule-Based Expert System
# Student Career Recommendation System

def career_expert_system():
    print("=" * 45)
    print(" STUDENT CAREER EXPERT SYSTEM ")
    print("=" * 45)

    print("\nAnswer using yes or no.\n")

    python_skill = input("Do you enjoy Python programming? ").strip().lower()
    maths_interest = input("Do you enjoy mathematics? ").strip().lower()
    web_interest = input("Do you enjoy HTML, CSS, and JavaScript? ").strip().lower()
    sql_interest = input("Do you enjoy SQL and analyzing data? ").strip().lower()
    problem_solving = input("Do you enjoy solving logical problems? ").strip().lower()

    # Knowledge base and rules
    if python_skill == "yes" and maths_interest == "yes":
        career = "AI / Machine Learning Engineer"
        reason = "You enjoy Python and mathematics."

    elif web_interest == "yes":
        career = "Web Developer"
        reason = "You enjoy building websites."

    elif sql_interest == "yes":
        career = "Data Analyst"
        reason = "You enjoy SQL and analyzing data."

    elif problem_solving == "yes":
        career = "Software Developer"
        reason = "You enjoy logical problem-solving."

    else:
        career = "Explore Different Technology Fields"
        reason = "More exploration can help identify your interests."

    # Display result
    print("\n" + "=" * 45)
    print(" EXPERT SYSTEM RESULT ")
    print("=" * 45)
    print("Recommended career:", career)
    print("Reason:", reason)
    print("=" * 45)


if __name__ == "__main__":
    career_expert_system()
