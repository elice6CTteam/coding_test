def solution(genres, plays):
    answer = []

    # 장르별로 분류하는 딕셔너리 생성
    # key : 장르명
    # value : (play횟수, 인덱스)의 형태인 튜플을 갖는 리스트형태
    genre_dict = {}
    for i in range(len(genres)):
        g = genres[i]
        if g not in genre_dict:
            genre_dict[g] = [(plays[i], i)]
        else:
            genre_dict[g].append((plays[i], i))

    # 장르별 인기곡을 찾기 위한 for문 작성
    # 장르별 총 play수를 구하고 (장르명, 장르별 총 play횟수)형태의 튜플을 갖는 most_popular리스트 생성
    most_popular = []
    for i in genre_dict:
        tmp = sum([a for (a, _) in genre_dict[i]])
        most_popular.append((i, tmp))
    most_popular.sort(reverse=True, key=(lambda x: x[1]))


    # answer를 작성하기 위한 코드 작성
    # most_popular에 저장된 장르명 순서대로 for문을 돌면서 정답을 이어나가는 과정.
    for i in most_popular:
        # 해정님의 도움으로 알게된 것.
        # key에서 튜플형태로 여러 함수를 넣게되면 순서대로 진행해가며 sorting이 진행됨
        # -(마이너스)를 붙여 reverse=True 없이도 내림차순 정렬이 가능함
        sorted_list = sorted(genre_dict[i[0]], key=lambda x: (-x[0], x[1]))[0:2]
        tmp = [x[1] for x in sorted_list]
        answer += tmp

    return answer