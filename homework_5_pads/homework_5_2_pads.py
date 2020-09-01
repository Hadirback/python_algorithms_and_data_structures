'''
2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется
как массив, элементы которого — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем счисления,
задача решается в несколько строк. Для прокачки алгоритмического мышления такой вариант не подходит.
Поэтому использование встроенных функций для перевода из одной системы счисления в другую в данной задаче под запретом.
'''
from collections import deque


class HexOperation:
    def get_hex_values_list(self, title: str):
        while True:
            try:
                l = list(input(f"Введите {title} шестнадцатеричное число: ").lower())
                if not self.validate_hex(l):
                    continue
                return l
            except:
                print("Введено не корректное число! Введите заново!")

    def get_values(self):
        return self.get_hex_values_list("первое"), self.get_hex_values_list("второе")

    def validate_hex(self, list_hex : list) -> bool:
        check_list = ['a', 'b', 'c', 'd', 'e', 'f']
        for item in list_hex:
            if not item.isdigit() and (item.lower() not in check_list):
                return False
        return True

    def addition_operation_hex(self, first: list, second: list) -> list:

        a = deque(first)
        b = deque(second)

        result = deque()

        residual_amount = 0
        while a or b:
            tmp_1 = self.replace_hex_to_dec(a.pop()) if a else 0
            tmp_2 = self.replace_hex_to_dec(b.pop()) if b else 0
            curr_value = self.replace_dec_to_hex((tmp_1 + tmp_2 + residual_amount) % 16)
            residual_amount = (tmp_1 + tmp_2 + residual_amount) // 16
            result.appendleft(curr_value)

        if residual_amount != 0:
            result.appendleft(self.replace_dec_to_hex(residual_amount))

        return list(result)

    def multiplication_operation_hex(self, first, second) -> list:
        a = deque(second) if len(first) > len(second) else deque(first)
        b = deque(first) if len(first) > len(second) else deque(second)

        result = []
        count = 0

        while a:
            tmp_1 = self.replace_hex_to_dec(a.pop()) if a else 1

            residual_multiplication = 0
            tmp_decue = deque()
            b_tmp = b.copy()
            while b_tmp:
                tmp_2 = self.replace_hex_to_dec(b_tmp.pop()) if b_tmp else 1
                mltp = tmp_1 * tmp_2
                current_value = self.replace_dec_to_hex((mltp + residual_multiplication) % 16)
                tmp_decue.appendleft(current_value)
                residual_multiplication = mltp // 16

            tmp_decue.appendleft(self.replace_dec_to_hex(residual_multiplication))

            tmp_count = count
            while tmp_count != 0:
                tmp_decue.append(0)
                tmp_count = tmp_count - 1

            result.append(tmp_decue)
            count = count + 1

        return self.sum_all_components(result)

    def sum_all_components(self, list_comp : list):
        sum = [0]
        for item in list_comp:
            sum = self.addition_operation_hex(list(item), sum)

        return sum

    def replace_hex_to_dec(self, elem) -> int:
        if elem == 'a':
            return 10
        elif elem == 'b':
            return 11
        elif elem == 'c':
            return 12
        elif elem == 'd':
            return  13
        elif elem == 'e':
            return  14
        elif elem == 'f':
            return 15
        else:
            return elem

    def replace_dec_to_hex(self, elem):
        if elem == 10:
            return 'a'
        elif elem == 11:
            return  'b'
        elif elem == 12:
            return 'c'
        elif elem == 13:
            return 'd'
        elif elem == 14:
            return 'e'
        elif elem == 15:
            return  'f'
        else:
            return elem


if __name__ == "__main__":
    service = HexOperation()
    first_value, second_value = service.get_values()

    print(service.addition_operation_hex(first_value, second_value))
    print(service.multiplication_operation_hex(first_value, second_value))
