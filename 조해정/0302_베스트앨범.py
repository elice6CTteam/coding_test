def solution(genres, plays):
    """
    genre_plays : 장르별 총 재생 수
    genre_plays = { "classic": 1450, "pop": 3100 }
    playlist : 장르별 곡 정보(재생수, 고유번호) 리스트
    playlist = { "classic": [(500, 0),(150, 2),(800, 3)], "pop": [(600, 1),(2500, 4)] }
    """
    genre_list = set(genres)
    genre_plays = {genre: 0 for genre in genre_list}
    playlist = {genre: [] for genre in genre_list}

    for i in range(len(genres)):
        genre, play = genres[i], plays[i]
        genre_plays[genre] += play
        playlist[genre].append((play, i))

    answer = []
    # 장르별 총 재생 수로 장르 내림차순 정렬
    for genre, _ in sorted(genre_plays.items(), key=lambda x: -x[1]):
        # 장르별: 곡 재생 수 내림차순 정렬(우선), 고유번호 오름차순 정렬
        sorted_playlist = sorted(playlist[genre], key=lambda x: (-x[0], x[1]))
        # 최대 2곡 선정
        for (_, i) in sorted_playlist[:2]:
            answer.append(i)

    return answer
