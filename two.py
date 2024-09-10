trip_expenses = {
    "여행지": "영국 런던",
    "여행 기간": "12박 14일",
    "총 여행 비용": 4850000,
    "세부 내역": {
        "비행기 값 (왕복)": 1000000,
        "식비": 1500000,
        "호텔": 1000000,
        "교통비": 300000,
        "관광비": 1000000,
        "기타 비용 (핸드폰 유심칩 등)": 50000
    }
}

for key, value in trip_expenses.items():
    if isinstance(value, dict):
        print(f"{key}:")
        for sub_key, sub_value in value.items():
            print(f"  {sub_key}: {sub_value}원")
    else:
        print(f"{key}: {value}")