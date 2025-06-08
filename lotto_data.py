import datetime
import random

# 최근 5주간 회차별 당첨 번호 샘플 데이터 (수동으로 입력하거나 자동화 가능)
RECENT_WINNING_NUMBERS = {
    1115: [7, 9, 14, 18, 28, 33],
    1114: [1, 6, 9, 15, 19, 42],
    1113: [11, 17, 19, 21, 27, 36],
    1112: [2, 13, 20, 31, 35, 43],
    1111: [3, 7, 11, 22, 25, 40]
}

def get_recent_numbers():
    """최근 회차 번호를 단일 리스트로 통합"""
    all_numbers = []
    for nums in RECENT_WINNING_NUMBERS.values():
        all_numbers.extend(nums)
    return all_numbers

def get_number_frequencies():
    """최근 번호들의 등장 빈도 계산"""
    freq = {}
    for nums in RECENT_WINNING_NUMBERS.values():
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
    return freq
