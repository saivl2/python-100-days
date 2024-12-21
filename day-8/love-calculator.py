def calculate_love_score(n1, n2):
    word1 = 'TRUE'.lower()
    word2 = 'LOVE'.lower()
    name = (n1 + n2).lower()
    true_count = 0
    love_count = 0
    for i in word1:
        true_count+= name.count(i)
    for i in word2:
        love_count += name.count(i)
    total_score  = str(true_count) + str(love_count)

    print(f"{total_score}")

calculate_love_score("Angela Yu", "Jack Bauer")

        
        
    
    
            
    
        
        