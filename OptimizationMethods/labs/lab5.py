import pybee
import beeexamples


def bee_algorithm(scoutbeecount, bestsitescount, bestbeecount, selectedbeecount, selsitescount, maxiteration):
    # Класс пчел, который будет использоваться в алгоритме
    # beetype = beeexamples.spherebee
    # beetype = beeexamples.rosenbrockbee
    beetype = beeexamples.Rastriginbee
    # beetype = beeexamples.Himmelblaybee

    # Количество пчел-разведчиков
    _scoutbeecount = scoutbeecount

    # Количество пчел, отправляемых на выбранные, но не лучшие участки
    _selectedbeecount = selectedbeecount

    # Количество пчел, отправляемые на лучшие участки
    _bestbeecount = bestbeecount

    # Количество выбранных, но не лучших, участков
    _selsitescount = selsitescount

    # Количество лучших участков
    _bestsitescount = bestsitescount

    # Максимальное количество итераций
    _maxiteration = maxiteration

    # Через такое количество итераций без нахождения лучшего решения уменьшим область поиска
    max_func_counter = 10

    # Во столько раз будем уменьшать область поиска
    koeff = beetype.getrangekoeff()

    ###################################################

    currhive = pybee.hive(_scoutbeecount, _selectedbeecount, _bestbeecount, _selsitescount, _bestsitescount,
                          beetype.getstartrange(), beetype)

    # Начальное значение целевой функции
    best_func = -1.0e9

    # Количество итераций без улучшения целевой функции
    func_counter = 0

    for n in range(_maxiteration):
        currhive.nextstep()
        if currhive.bestfitness != best_func:
            # Найдено место, где целевая функция лучше
            best_func = currhive.bestfitness
            func_counter = 0
        else:
            func_counter += 1
            if func_counter == max_func_counter:
                # Уменьшим размеры участков
                currhive.range = [currhive.range[m] * koeff[m] for m in range(len(currhive.range))]
                func_counter = 0
    return currhive.bestposition

# bee_algorithm(300, 5, 30, 10, 15, 2000)