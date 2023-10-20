from tkinter import *

# Функция для шифрования текста шифром Цезаря
def encrypt_text():
    text = input_text.get()
    shift = int(shift_value.get())

    encrypted_text = ""

    for char in text:
        if char.isalpha():
            char_code = ord(char)
            if char.isupper():
                encrypted_text += chr((char_code - 65 + shift) % 26 + 65)
            else:
                encrypted_text += chr((char_code - 97 + shift) % 26 + 97)
        else:
            encrypted_text += char

    output_text.set(encrypted_text)

# Функция для расшифровки текста шифром Цезаря
def decrypt_text():
    text = input_text.get()
    shift = int(shift_value.get())

    decrypted_text = ""

    for char in text:
        if char.isalpha():
            char_code = ord(char)
            if char.isupper():
                decrypted_text += chr((char_code - 65 - shift) % 26 + 65)
            else:
                decrypted_text += chr((char_code - 97 - shift) % 26 + 97)
        else:
            decrypted_text += char

    output_text.set(decrypted_text)


# Создание графического интерфейса
window = Tk()
window.title("Шифр Цезаря")
window.geometry("400x300")

# Метка для ввода текста
input_label = Label(window, text="Введите текст используя латиницу и знаки припинания:")
input_label.pack()

# Поле ввода текста
input_text = Entry(window)
input_text.pack()

# Метка для выбора шага сдвига
shift_label = Label(window, text="Шаг сдвига (число):")
shift_label.pack()

# Поле ввода шага сдвига
shift_value = Entry(window)
shift_value.pack()

# Кнопка для шифрования текста
encrypt_button = Button(window, text="Зашифровать", command=encrypt_text)
encrypt_button.pack()

# Кнопка для расшифровки текста
decrypt_button = Button(window, text="Расшифровать", command=decrypt_text)
decrypt_button.pack()

# Метка для отображения результата
output_label = Label(window, text="Результат:")
output_label.pack()

# Поле вывода результата
output_text = StringVar()
output_text.set("")
result = Label(window, textvariable=output_text)
result.pack()

# Запуск цикла обработки событий
window.mainloop()

