def process_list(input_list):
    assert len(input_list) >= 3, "Список повинен містити принаймні 3 елементи"
    print(f"Список містить {len(input_list)} елементів")

process_list([3, 6])