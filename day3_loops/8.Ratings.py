# Input
total = 0
cust_num=20
max_rating=0
min_rating=6
num_ratings_gt4=0

for i in range(cust_num):
    rating = -1
    while rating < 0 or rating > 5:
        rating = float(input(f"Enter rating between 1-5 for customer {i+1}: "))
        if rating < 0 or rating > 5:
            print("Enter valid rating")
    total+=rating
    if rating > max_rating:
        max_rating = rating
    if rating < min_rating:
        min_rating = rating

    if rating>=4:
        num_ratings_gt4+=1

line = 50 * "="


print(line)

print(f"Total Number of customers: {cust_num}") 

print(f"Average rating: {total/cust_num :.2f}")

print(f"Maximum rating: {max_rating}")

print(f"Minimum rating: {min_rating}")

print(f"Number of customers with rating >=4: {num_ratings_gt4}")

print(line)

        
    