import random

def get_recent_numbers():
    # 예시로 넣은 최근 자주 출현한 번호 리스트
    return [1, 3, 7, 11, 15, 20, 22, 27, 30, 34, 38, 40, 43]

def generate_hybrid_numbers(game_count):
    recent = get_recent_numbers()
    numbers = []

    for _ in range(game_count):
        hybrid_game = []

        # 최근 번호에서 2~3개 포함시키기
        while len(hybrid_game) < 3:
            n = random.choice(recent)
            if n not in hybrid_game:
                hybrid_game.append(n)

        # 나머지 번호는 랜덤으로 추가 (1~45 중복 없이)
        while len(hybrid_game) < 6:
            n = random.randint(1, 45)
            if n not in hybrid_game:
                hybrid_game.append(n)

        hybrid_game.sort()
        numbers.append(hybrid_game)

    return numbers




