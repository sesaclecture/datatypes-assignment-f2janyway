# ==========================
# assignment_drama_template.py (학생용 템플릿)
# 조건: 함수/조건문/반복문 금지. 변수 선언과 input(), print()만 사용.
# ==========================

drama1 = {
    "제목": "눈물의 여왕",
    "장르": "로맨스, 코미디",
    "주제": "재벌 3세와 평범한 남자의 결혼 생활",
    "방영기간": "2024-03-09 ~ 2024-04-28",
    "배우": ["김수현", "김지원"],
    "명대사": "\"사랑은 때론 기적처럼 찾아와.\""
}

drama2 = {
    "제목": "선재 업고 튀어",            
    "장르": "타임슬립, 로맨스",            
    "주제": "톱스타의 죽음을 막기 위한 타임슬립",            
    "방영기간": "2024-04-08 ~ 2024-05-28",         
    "배우": ["변우석", "김혜윤"],            
    "명대사": "\"널 사랑해, 내가 널 지킬게.\""           
}


new_title = input("새 드라마 제목: ")  

new_genre = input("새 드라마 장르: ")
new_theme =  input("새 드라마 주제: ")
new_period = input("새 드라마 방영기간(예: 2024-01-01 ~ 2024-02-01): ")
new_actors_input = input("새 드라마 배우들(쉼표로 구분): ")
new_quote_raw = input("인상 깊었던 대사(따옴표 없이 입력): ")

new_actors = new_actors_input.split(",")
new_quote = f"\"{new_quote_raw}\""

drama3 = {
    "제목": new_title,
    "장르": new_genre,
    "주제": new_theme,
    "방영기간": new_period,
    "배우": new_actors,
    "명대사": new_quote
}


upd_title = input("수정(덮어쓰기)할 제목(대상: ): ")  
upd_genre =  input("수정할 장르: ")
upd_theme = input("수정할 주제: ")
upd_period =input("수정할 방영기간: ")
upd_actors_input = input("수정할 배우들(쉼표로 구분): ")
upd_quote_raw =   input("수정할 명대사(따옴표 없이 입력): ")

upd_actors = upd_actors_input.split(",")
upd_quote = f"\"{upd_quote_raw}\""

drama2["제목"] = upd_title
drama2["장르"] = upd_genre
drama2["주제"] = upd_theme
drama2["방영기간"] = upd_period
drama2["배우"] = upd_actors
drama2["명대사"] = upd_quote

print("\n[드라마 1]")
print(f"제목: {drama1['제목']}")
print(f"장르: {drama1['장르']}")
print(f"주제: {drama1['주제']}")
print(f"방영기간: {drama1['방영기간']}")
print(f"배우: {drama1['배우']}")
print(f"명대사: {drama1['명대사']}")

print("\n[드라마 2]  # 수정 후")
print(f"제목: {drama2['제목']}")
print(f"장르: {drama2['장르']}")
print(f"주제: {drama2['주제']}")
print(f"방영기간: {drama2['방영기간']}")
print(f"배우: {drama2['배우']}")
print(f"명대사: {drama2['명대사']}")

print("\n[드라마 3]  # 새로 추가")
print(f"제목: {drama3['제목']}")
print(f"장르: {drama3['장르']}")
print(f"주제: {drama3['주제']}")
print(f"방영기간: {drama3['방영기간']}")
print(f"배우: {drama3['배우']}")
print(f"명대사: {drama3['명대사']}")
