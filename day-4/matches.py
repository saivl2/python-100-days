series = "N-02"
# Match is used to compare the value of 'series' against multiple cases
# If vs Match -- Match is more readable and cleaner for multiple conditions

match series:
    case "N-01":
        print('Samsung')
    case "N-02":
        print('Nokia')
    case "N-03":
        print('Motorola')
    case _:
        print('Unknown Series')

client = {
    'name': 'Feddie',
    'age': 30,
    'occupation': 'Engineer'
}

movie = {
    'title': 'Inception',
    'credits':{
        'main_star': 'Leonardo DiCaprio',
        'director': 'Christopher Nolan'
    }
}

items = [client, movie, 'book'] 
for item in items:
    match item:
        case {'name': name, 'age': age, 'occupation': occupation}:
            print(f'Client Name: {name}, Age: {age}, Occupation: {occupation}')
        case {'title': title, 'credits': {'main_star': main_star, 'director': director}}:
            print(f'Movie Title: {title}, Main Star: {main_star}, Director: {director}')
        case _:
            print('Unknown Item')