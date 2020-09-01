'''
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для
каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно
вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
'''
from collections import defaultdict


class EnterpriseService:
    def __init__(self):
        self.count = self.get_count_enterprize()

    def get_count_enterprize(self) -> int:
        while True:
            try:
                return int(input('Введите количество предприятий для заполнения: '))
            except:
                print("Введены не корректные данные!")

    def get_profit_quater(self, quater_name) -> int:
        while True:
            try:
                return int(input(f'Введите прибыль за {quater_name} квартал: '))
            except:
                print('Некорректно введены данные прибыли!')

    def fill_main_dict(self) -> defaultdict:
        main_dict = defaultdict(list)
        while self.count > 0:
            name = input('Введите имя предприятия: ')
            try:
                quater_1 = self.get_profit_quater("первый")
                quater_2 = self.get_profit_quater("второй")
                quater_3 = self.get_profit_quater("третий")
                quater_4 = self.get_profit_quater("четвертый")

                list_quater = [quater_1,
                               quater_2,
                               quater_3,
                               quater_4]

                main_dict[name].append(list_quater)
                self.count -= 1
            except Exception as ex:
                print(f'Ошибка {ex}! Введите данные заново')
        return main_dict

    def get_average_profit_for_the_year(self, main_dict: defaultdict) -> defaultdict:
        avrg_profit = defaultdict(float)
        for key, item in main_dict.items():
            avrg_profit[key] = sum(item[0]) / len(item[0])
        return avrg_profit

    def show_average_profit_enterprizes(self, main_dict: defaultdict):
        for key, item in main_dict.items():
            print(f"У предприятия {key} средняя прибыль за год равна - {item}")

    def get_average_profit_by_all_enterprize(self, main_dict: defaultdict) -> float:
        avrg_sum = 0
        for key, item in main_dict.items():
            avrg_sum = avrg_sum + item
        return avrg_sum / len(main_dict.items())

    def get_statistics_info(self, main_dict: defaultdict) -> defaultdict:
        average_by_all = self.get_average_profit_by_all_enterprize(main_dict)
        statistic_dict = defaultdict(list)
        for key, item in main_dict.items():
            if item <= average_by_all:
                statistic_dict["less_than_average"].append(key)
            else:
                statistic_dict["more_than_average"].append(key)

        return statistic_dict

    def show_statistics_info(self, main_dict):
        print(f"Предприятие(я) у которого(ых) прибыль меньше среднего значения {main_dict['less_than_average']}")
        print(f"Предприятиe(я) у которого(ых) прибыль больше среднего значения {main_dict['more_than_average']}")


if __name__ == "__main__":
    service = EnterpriseService()
    enterprize_dict = service.fill_main_dict()
    avrg_dict = service.get_average_profit_for_the_year(enterprize_dict)
    service.show_average_profit_enterprizes(avrg_dict)
    stat_dict = service.get_statistics_info(avrg_dict)
    service.show_statistics_info(stat_dict)

