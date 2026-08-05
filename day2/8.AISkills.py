# Input
# Delibrately not using dictionaries

python = float(input("Enter Python Rating: "))
sql = float(input("Enter sql Rating: "))
machine_learning = float(input("Enter machine learning Rating: "))
deep_learning = float(input("Enter Deep Learning Rating: "))
llm = float(input("Enter LLMs Rating: "))

#processing

average_rating = (python + sql + machine_learning + deep_learning + llm)/5

if 0 <= python <=10 and 0 <= sql <= 10 and 0 <= machine_learning <= 10 and 0 <= deep_learning <= 10 and 0 <= llm <= 10:
        
    highest_skill_rating = max(python,sql,machine_learning,deep_learning,llm)

    # Highest Skill

    if highest_skill_rating == llm:
        highest_skill = "LLM"

    elif highest_skill_rating == deep_learning:
        highest_skill ="Deep Learning" 

    elif highest_skill_rating == machine_learning:
        highest_skill ="Machine Learning" 

    elif highest_skill_rating == python:
        highest_skill ="Python"

    elif highest_skill_rating == sql:
        highest_skill = "SQL"

    

    lowest_skill_rating = min(python,sql,machine_learning,deep_learning,llm)

    # Lowest Skill
    if lowest_skill_rating == llm:
        lowest_skill = "LLM"

    elif lowest_skill_rating == deep_learning:
        lowest_skill ="Deep Learning" 

    elif lowest_skill_rating == machine_learning:
        lowest_skill ="Machine Learning" 

    elif lowest_skill_rating == python:
        lowest_skill ="Python" 

    elif lowest_skill_rating == sql:
        lowest_skill = "SQL"

    #Skill classification
    if average_rating >= 8:
        skill_level = "Advanced"
    elif average_rating >= 5:
        skill_level = "Intermediate"
    else:
        skill_level = "Basic"

    line = 50*'='
    print(line)
    print("SKILL REPORT")
    print(line)
    print(f"Average Skill Rating : {average_rating}")
    print(f"Highest Skill  : {highest_skill}")
    print(f"Lowest Skill  : {lowest_skill}")
    print(f"Skill Level: {skill_level}")

    #Improvement skill
    if skill_level == "Basic":
        print(f"Improve {lowest_skill} fundamentals before moving into AI Engineering.")
        
    print(line)
else:
    print("Invalid input")




