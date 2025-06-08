import random
from lotto_data import get_number_frequencies

def generate_weighted_numbers(game_count):
    freq = get_number_frequencies()
    
    # 번호별 가중치 리스트 생성 (번호를 가중치 수만큼 반복)
    weighted_pool = []
    for number, count in freq.items():
        weighted_pool.extend([number] * count)

    # 번호가 없는 경우 대비: 모든 번호로 구성
    if not weighted_pool:
        weighted_pool = list(range(1, 46))

    results = []
    for _ in range(game_count):
        selected = set()
        while len(selected) < 6:
            picked = random.choice(weighted_pool)
            selected.add(picked)
        results.append(sorted(selected))

    return results

