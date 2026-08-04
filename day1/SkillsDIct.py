#Input 
skills = {}
print(50*"=")
print("Rate yourself on below skills, 1-5, 5 being the best")
skills["Python"] = float(input("Python: "))
skills["SQL"] = float(input("SQL: "))
skills["Machine Learning"] = float(input("Machine Learning: "))
skills["Deep Learning"] = float(input("Deep Learning: "))
skills["LLMs"] = float(input("LLMs: "))
print(skills)


print(50*"=")
#Average
overall_average = sum(skills.values())/len(skills)

print(f"Overall Average: {overall_average}")

#Highest Skill

best_skill = max(skills, key=skills.get)

print(f"Best Skill: {best_skill} (Rating: {skills[best_skill]})")

#lowest Skill

worst_skill = min(skills, key=skills.get)

print(f"Lowest Skill: {worst_skill} (Rating: {skills[worst_skill]})")

print(50*"=")