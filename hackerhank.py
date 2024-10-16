if __name__ == '__main__':
    dict_name_score: dict = {}
    for _ in range(3):
        name = input()
        score = float(input())
        dict_name_score.update({f'{name}': f'{score}'})
        
    print(dict_name_score)