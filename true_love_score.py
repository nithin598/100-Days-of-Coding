def calculate_love_score(name1,name2):
    combined_name = (name1+name2).upper()
    true_list = ["T","R","U","E"]
    love_list = ["L", "O", "V", "E"]
    true_total=0
    love_total = 0
    for letter in true_list:
        j = 0
        j=combined_name.count(letter)
        print(f"{letter} Occurred {j} times")
        true_total +=j
    print(f"Total = {true_total}")
    for letter in love_list:
        l = 0
        l=combined_name.count(letter)
        print(f"{letter} Occurred {l} times")
        love_total +=l
    print(f"Total = {love_total}")
    love_score = str(true_total)+str(love_total)
    print(f"Tue Love Score = {love_score}")


calculate_love_score("Kanye West", "Kim Kardashian")