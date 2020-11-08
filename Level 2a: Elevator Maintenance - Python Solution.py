def solution(l):
    parsing = [e.split(".") for e in l]
    sorting = [map(int, e) for e in parsing]
    sorted_ints = sorted(sorting)
    sorted_join=[('.'.join(str(ee) for ee in e)) for e in sorted_ints]
    return sorted_join
