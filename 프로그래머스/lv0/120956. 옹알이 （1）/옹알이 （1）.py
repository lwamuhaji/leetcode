def solution(babbling):
    answer = 0
    for word in babbling:
        while word:
            if word.startswith("aya"):
                word = word[3:]
            elif word.startswith("ye"):
                word = word[2:]
            elif word.startswith("woo"):
                word = word[3:]
            elif word.startswith("ma"):
                word = word[2:]
            else:
                break
        if word == "":
            answer += 1
    return answer