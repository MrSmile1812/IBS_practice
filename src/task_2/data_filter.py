def find_in_different_registers(words: list[str]) -> list:
    """Логика алгоритма - ищем повторящиееся слова в одинаковом регистре
    и выносим их в отдельный список. Приводим все слова в нижний регистр и
    удаляем повторы. В итоге убираем дубли с помощью списка повторений"""
    repeat = []
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if words[i] == words[j]:
                repeat.append(words[i].lower())

    for i in range(len(words)):
        words[i] = words[i].lower()

    words = list(set(words))
    repeat = list(set(repeat))

    for word in repeat:
        words.remove(word)

    return words


words = ["Мама", "МАМА", "Мама", "папа", "ПАПА", "Мама", "ДЯдя",
         "брАт", "Дядя", "Дядя", "Дядя"]
words_2 = ["МАМА", "Мама", "БРАТ", "папа", "ПАПА", "ДЯдя", "брАт",
           "Дядя", "Дядя", "Дядя"]

if __name__ == "__main__":
    find_in_different_registers(words)
    find_in_different_registers(words_2)
