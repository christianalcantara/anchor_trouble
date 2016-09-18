# -*- coding: utf-8 -*-
# Autor: christian


class GasStation(object):
    """Gast Station"""

    def __init__(self, matrix):
        self.matrix = matrix  # string array
        self.data = []  # list of lines of formatted string array
        self._format_data()

    def __str__(self):
        """ String representation of an object """
        return '<class: GasStation>'

    def _format_data(self):
        nline = 1  # line number

        for line in self.matrix.split('\n'):
            line = line.replace('"', '').replace(' ', '')
            itens = line.split(',')
            dict_data = {}

            if len(itens) < 3:
                raise Exception("Invalid data")

            gas_station = itens[0]  # gas station number
            #
            # check if gas station number is digit
            #
            if not gas_station.isdigit() or not gas_station:
                raise Exception("Invalid number \"{0}\" for gas station in line {1}.".format(gas_station, nline))
            gas_station = int(gas_station)  # convert gas station to int
            #
            # check if number of gas station is less than 2
            #
            if gas_station < 2:
                raise Exception(
                    "Number of gas stations '{0}' must be greater than 1 in line {1}.".format(gas_station, nline)
                )
            dict_data['gas_station'] = int(gas_station)

            # validate stop station
            stop_stations = []
            for stop in map(lambda x: x.split(':'), itens[1:]):
                if not len(stop) == 2:
                    raise Exception(
                        "Invalid size \"{0}\" for stop station in line {1}. Size should be 2 <n:n>".format(
                            len(stop), nline
                        )
                    )
                try:
                    stop_stations.append(tuple(map(lambda x: int(x), stop)))
                except ValueError as e:
                    raise Exception("invalid literal for int() with base 10 in line {0}: '<{1}:{2}>'".format(
                        nline, stop[0], stop[1])
                    )
            dict_data['stop_stations'] = stop_stations
            #
            # check if number of gas station is equal amount of total stops
            #
            amount_stop_stations = len(stop_stations)
            if gas_station != amount_stop_stations:
                raise Exception(
                    "Number of gas stations '{0}' different of amount of total stops '{1}' in line {2}.".format(
                        gas_station, amount_stop_stations, nline
                    )
                )

            dict_data['is_possible'] = self.is_possible(stop_stations)
            self.data.append(dict_data)
            nline += 1  # increment line number

    @staticmethod
    def check_gas_cons(gas_cons_list):
        total = 0
        for x in gas_cons_list:
            total += x
            if total < 0:
                return False
        return True

    def is_possible(self, stations_list):
        circular_stations = (stations_list[i:] + stations_list[:i] for i in range(len(stations_list)))
        inc = 1
        for stations in circular_stations:
            gas_cons = map(lambda x: x[0] - x[1], stations)  # calculate fuel consumption for gas station
            if self.check_gas_cons(gas_cons):
                return inc
            inc += 1
        return False

if __name__ == '__main__':
    matrix = '''"4","3:1","2:2","1:2","0:1"
    "5","5:1","0:2","0:2","1:1","3:2"
    "3","0:1","2:2","3: 1"
    "2","0:1","1:2"'''


    g = GasStation(matrix)

    for x in g.data:
        print '>', x.get('is_possible'), x.get('gas_station'), x.get('stop_stations')

