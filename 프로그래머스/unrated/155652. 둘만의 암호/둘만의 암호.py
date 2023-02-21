def solution(s, skip, index):
    answer = ''
    st = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j' ,'k', 'l', 'm', 'n', 'o', 'p' ,'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for c in skip:
        st.remove(c)
    for c in s:
        answer += st[(st.index(c) + index)%len(st)]
    return answer