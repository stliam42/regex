import re

input = ["С227НА777",
        "КУ22777",
        "Т223ВВ777",
        "М227К19У9",
        " С227НА777",
        "М333КУ27"]

applied_letters = 'авекмнорстух'

private_regex = r'^[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}\s*'
taxi_regex = r'^[АВЕКМНОРСТУХ]{2}\d{4,5}'


for number in input:
    if re.fullmatch(private_regex, number, flags=re.IGNORECASE):
        print('Private')

    elif re.fullmatch(taxi_regex, number, flags=re.IGNORECASE):
        print('Taxi')

    else:
        print('Fail')