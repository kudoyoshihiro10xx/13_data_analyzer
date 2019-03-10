from calculation import calculation_total

if __name__ == '__main__':
    # ユーザーからの入力を受け取る
    input_data = input("データを入力して下さい(スペース区切り) > ")

    # print(input_data)
    # 文字列のリストに変換
    numbers_as_str = input_data.split(" ")
    # print(numbers_as_str)

    # 整数のリストに変換
    numbers = []  # リストを初期化

    for number_as_str in numbers_as_str:
        int_num = int(number_as_str)  # 整数に変換

        numbers.append(int_num)  # numbersというリストに要素を追加

    #print(numbers)

    # 各統計量を計算する(合計，平均，)
    total = calculation_total(numbers)




    # ユーザーに見やすいようにフォーマットする
    # 出力する
    print(f"合計: {total}")
