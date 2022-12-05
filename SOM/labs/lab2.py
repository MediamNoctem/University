import math
import numpy as np


def div_to_def_lead_row(i, j):
    if np.sign(i) != np.sign(j):
        return math.inf
    else:
        return i / j


def find_max_exclude(list_items, list_exclude_ind):
    ind_max = None
    max_item = None
    n = len(list_items)
    for i in range(n):
        if i not in list_exclude_ind:
            ind_max = i
            max_item = list_items[i]
            break
    for i in range(n):
        if i not in list_exclude_ind:
            if list_items[i] > max_item:
                ind_max = i
                max_item = list_items[i]
    return ind_max


def to_fixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


def print_number(number):
    if np.sign(number) >= 0:
        return "  " + to_fixed(number, 2) + " "
    else:
        return " " + to_fixed(number, 2) + " "


class SimplexTable:
    def __init__(self, basic_variables, free_values, free_variables):
        self.basic_variables = basic_variables
        self.free_values = free_values
        self.free_variables = free_variables
        self.coefficients = None
        self.leading_column = None
        self.leading_row = None

    def define_leading_column_and_row(self, check_for_identical_list_variables, flag):
        potential_columns = []
        exclusion = []
        n = len(self.free_variables)
        list_variables = [0 for i in range(n)]

        for i in range(len(self.free_variables)):
            potential_columns.append(abs(self.free_variables[i][1][-1]))

        while True:
            # flag1 = 1
            self.leading_column = find_max_exclude(potential_columns, exclusion)
            self.define_leading_row()
            print("leading_column: " + str(self.leading_column))
            print("leading_row: " + str(self.leading_row))
            # j = self.free_variables[self.leading_column][1]
            # for i in range(len(self.free_variables[self.leading_column][1])):
            #     if j[i] == 0.00 or j[i] == -0.00:
            #         exclusion.append(self.leading_column)
            #         flag1 = 0
            # if flag1:
            if flag != 1:
                for i in range(n):
                    list_variables[i] = self.free_variables[i][0][0]
                list_variables[self.leading_column] = self.basic_variables[self.leading_row]

                if check_for_identical_list_variables(set(list_variables)) or self.free_variables[self.leading_column][1][self.leading_row] == 0:
                    exclusion.append(self.leading_column)
                else:
                    break
            else:
                break

    def define_leading_row(self):
        t = []
        for i in range(len(self.free_values) - 1):
            t.append(div_to_def_lead_row(self.free_values[i], self.free_variables[self.leading_column][1][i]))
        self.leading_row = t.index(min(t))

    def update_basic_variables(self, prev_table):
        self.basic_variables.append(prev_table.free_variables[prev_table.leading_column][0][0])
        for i in range(len(prev_table.basic_variables)):
            if i != prev_table.leading_row:
                self.basic_variables.append(prev_table.basic_variables[i])

    def update_free_variables(self, prev_table):
        for i in range(len(prev_table.free_variables)):
            if i != prev_table.leading_column:
                self.free_variables.append([[prev_table.free_variables[i][0][0]], []])
            else:
                self.free_variables.append([[prev_table.basic_variables[prev_table.leading_row]], []])

    def calc_coefficients(self, prev_table):
        self.coefficients = []
        for i in range(len(prev_table.free_variables[prev_table.leading_column][1])):
            if i != prev_table.leading_row:
                self.coefficients.append(-1 * prev_table.free_variables[prev_table.leading_column][1][i])

    def calc_first_row_table(self, prev_table):
        self.free_values.append(prev_table.free_values[prev_table.leading_row] / prev_table.free_variables[prev_table.leading_column][1][prev_table.leading_row])
        self.free_variables[prev_table.leading_column][1].append(1 / prev_table.free_variables[prev_table.leading_column][1][prev_table.leading_row])

        for item in range(len(prev_table.free_variables)):
            if item != prev_table.leading_column:
                self.free_variables[item][1].append(prev_table.free_variables[item][1][prev_table.leading_row] / prev_table.free_variables[prev_table.leading_column][1][prev_table.leading_row])

    def calc_table_rows(self, prev_table):
        for i in range(1, len(prev_table.basic_variables)):
            self.free_values.append(self.free_values[0] * self.coefficients[i - 1] + prev_table.free_values[prev_table.basic_variables.index(self.basic_variables[i])])
            for j in range(len(prev_table.free_variables)):
                tmp = self.free_variables[j][1][0] * self.coefficients[i - 1]
                if self.free_variables[j][0][0] != prev_table.basic_variables[prev_table.leading_row]:
                    tmp += prev_table.free_variables[j][1][prev_table.basic_variables.index(self.basic_variables[i])]
                self.free_variables[j][1].append(tmp)

    def print_table(self):
        # "    x1    ", "    x2    ", "    x3    ", "    x4    ", "    x5    ", "    x6    ", "    F     "
        # "   x1  ", "   x2  ", "   x3  ", "   x4  ", "   x5  ", "   x6  ", "   F   "

        # "    x1    ", "    x2    ", "    l     ", "    v1    ", "    v2    ", "    z1    ", "    z2    ", "    w     ", "    F     "
        # "   x1  ", "   x2  ", "   l   ", "   v1  ", "   v2  ", "   z1  ", "   z2  ", "   w   ", "   F   "

        # "    x1    ", "    x2    ", "    l1    ", "    l2    ", "    v1    ", "    v2    ", "    z1    ", "    z2    ", "    w1    ", "    w2    ", "    F     "
        # "   x1  ", "   x2  ", "   l1  ", "   l2  ", "   v1  ", "   v2  ", "   z1  ", "   z2  ", "   w1  ", "   w2  ", "   F   "
        var = ["    x1    ", "    x2    ", "    l     ", "    v1    ", "    v2    ", "    z1    ", "    z2    ", "    w     ", "    F     "]
        var_ = ["   x1  ", "   x2  ", "   l   ", "   v1  ", "   v2  ", "   z1  ", "   z2  ", "   w   ", "   F   "]
        variables = ""
        coeff = None
        if self.coefficients is None:
            coeff = " "

        for x in self.free_variables:
            variables += var_[x[0][0]] + "|"

        # -------------------------------------------------
        # "basic     | free   | free_variables| coefficients"

        # "-------------------------------------------------------------------------"
        # "basic     | free   |             free_variables            | coefficients"

        # "---------------------------------------------------------------------------------"
        # "basic     | free   |                 free_variables                | coefficients"
        print("-------------------------------------------------------------------------")
        print("basic     | free   |             free_variables            | coefficients")
        print("variables | values |" + variables)
        print("-------------------------------------------------------------------------")
        fv = ""
        for j in self.free_variables:
            fv += print_number(j[1][0]) + "|"
        print(var[self.basic_variables[0]] + "|" + print_number(self.free_values[0]) + " |" + fv + " ")
        for i in range(1, len(self.basic_variables)):
            fv = ""
            for j in self.free_variables:
                fv += print_number(j[1][i]) + "|"
            if self.coefficients is not None:
                coeff = print_number(self.coefficients[i - 1])
            print(var[self.basic_variables[i]] + "|" + print_number(self.free_values[i]) + " |" + fv + coeff)
        print("-------------------------------------------------------------------------")


class SimplexMethod:
    def __init__(self, list_variables_of_free_variables):
        self.list_variables_of_free_variables = list_variables_of_free_variables
        self.cur_table = None
        self.prev_table = None
        # self.f = f

    def check_for_identical_list_variables(self, list_variables):
        for i in self.list_variables_of_free_variables:
            if set(i) == list_variables:
                return True
        return False

    def update_list_variables_of_free_variables(self, table):
        tmp = []
        for i in range(len(self.list_variables_of_free_variables[-1])):
            tmp.append(self.list_variables_of_free_variables[-1][i])
        tmp[table.leading_column] = table.basic_variables[table.leading_row]
        self.list_variables_of_free_variables.append(tmp)
        print("list_variables_of_free_variables: " + str(self.list_variables_of_free_variables))

    def is_end(self):
        # for i in self.cur_table.free_variables:
        #     if i[1][-1] < 0:
        #         return False
        for i in self.cur_table.free_variables:
            if i[0][0] != 5 and i[0][0] != 6 and i[1][-1] < 0:
                return False
            # if i[0][0] != 6 and i[0][0] != 7 and i[1][-1] < 0:
        if self.cur_table.free_values[-1] >= 0:
            return True
        return False

    def simplex_method(self, basic_variables, free_values, free_variables):
        self.prev_table = SimplexTable(basic_variables, free_values, free_variables)
        self.prev_table.print_table()
        self.prev_table.define_leading_column_and_row(self.check_for_identical_list_variables, 1)
        print("list_variables_of_free_variables: " + str(self.list_variables_of_free_variables))

        while True:
            self.cur_table = SimplexTable([], [], [])
            self.cur_table.update_basic_variables(self.prev_table)
            self.cur_table.update_free_variables(self.prev_table)
            self.cur_table.calc_coefficients(self.prev_table)
            self.cur_table.calc_first_row_table(self.prev_table)
            self.cur_table.calc_table_rows(self.prev_table)

            self.cur_table.print_table()

            print("is_end = " + str(self.is_end()))
            if self.is_end():
                break

            self.cur_table.define_leading_column_and_row(self.check_for_identical_list_variables, 0)
            self.update_list_variables_of_free_variables(self.prev_table)

            self.prev_table.basic_variables = self.cur_table.basic_variables
            self.prev_table.free_values = self.cur_table.free_values
            self.prev_table.free_variables = self.cur_table.free_variables
            self.prev_table.coefficients = self.cur_table.coefficients
            self.prev_table.leading_column = self.cur_table.leading_column
            self.prev_table.leading_row = self.cur_table.leading_row

            input("Press key >>> ")

        res = [self.cur_table.free_values[self.cur_table.basic_variables.index(0)],
               self.cur_table.free_values[self.cur_table.basic_variables.index(1)]]
        # for i in range(len(self.cur_table.basic_variables) - 1):
        #     res.append(self.cur_table.free_values[i])
        return res
# [[0, 1]]
# [2, 3, 4, 5, 6], [-2, -4, 2, 6, 0], [[[0], [1, -1, 1, 0, -1]], [[1], [-2, -1, -1, 1, -2]]]

# [[0, 1, 2, 3, 4]]
# [5, 6, 7, 8], [4, 6, 2, 10], [[[0], [4, 2, 1, 6]], [[1], [2, 4, 2, 6]], [[2], [1, 2, 0, 3]], [[3], [-1, 0, 0, -1]], [[4], [0, -1, 0, -1]]]

# [[0, 1, 2, 3, 4, 5]]
# [6, 7, 8, 9, 10], [6, 3, 1, 4, 9], [[[0], [4, 4, 1, 2, 8]], [[1], [4, 6, 1, 3, 10]], [[2], [1, 1, 0, 0, 2]], [[3], [2, 3, 0, 0, 5]], [[4], [-1, 0, 0, 0, -1]], [[5], [0, -1, 0, 0, -1]]]

# s = SimplexMethod([[0, 1, 2, 3, 4]], Function())
# print(s.simplex_method([5, 6, 7, 8], [4, 6, 2, 10], [[[0], [4, 2, 1, 6]], [[1], [2, 4, 2, 6]], [[2], [1, 2, 0, 3]], [[3], [-1, 0, 0, -1]], [[4], [0, -1, 0, -1]]]))
