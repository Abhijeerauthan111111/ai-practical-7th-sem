def career_expert_system():
    print("Welcome to the Career Advisory Expert System!")
    print("I'll help you find a suitable career path based on your interests.")
    print("Please answer the following questions with 'yes' or 'no'.\n")

    # Dictionary to store career recommendations based on responses
    recommendations = {
        "tech": "You might enjoy a career in Technology/IT. Consider roles like:\n- Software Developer\n- Data Scientist\n- System Administrator",
        "creative": "You might enjoy a creative career. Consider roles like:\n- Graphic Designer\n- Content Creator\n- UI/UX Designer",
        "business": "You might enjoy a business-oriented career. Consider roles like:\n- Business Analyst\n- Project Manager\n- Marketing Specialist",
        "science": "You might enjoy a career in Sciences. Consider roles like:\n- Research Scientist\n- Lab Technician\n- Environmental Analyst"
    }

    score = {"tech": 0, "creative": 0, "business": 0, "science": 0}

    # Questions for assessment
    questions = [
        ("Do you enjoy solving complex problems?", "tech", "science"),
        ("Do you like working with computers?", "tech", None),
        ("Do you enjoy expressing yourself artistically?", "creative", None),
        ("Are you interested in how businesses operate?", "business", None),
        ("Do you like conducting experiments?", "science", None),
        ("Do you enjoy creating visual content?", "creative", None),
        ("Are you interested in managing teams?", "business", None),
        ("Do you enjoy analyzing data?", "tech", "business")
    ]

    # Ask questions and collect responses
    for question, primary_field, secondary_field in questions:
        while True:
            response = input(f"{question} (yes/no): ").lower()
            if response in ['yes', 'no']:
                break
            print("Please answer with 'yes' or 'no'.")

        if response == 'yes':
            score[primary_field] += 1
            if secondary_field:
                score[secondary_field] += 0.5

    # Find the career field with highest score
    recommended_field = max(score.items(), key=lambda x: x[1])[0]

    print("\nBased on your responses:")
    print(recommendations[recommended_field])

if __name__ == "__main__":
    career_expert_system()