from dateutil import parser


def optionalNumeric(s):
    try:
        return float(s)
    except ValueError:
        return s

def standardizeDate(s):
    d = parser.parse(s)
    return d.isoformat()

if __name__ == "__main__":
        print(standardizeDate('Aug 12, 2020'))
        print(standardizeDate('05/03/18'))
        print(standardizeDate('12 Aug 2020'))
        print(standardizeDate('01.07.2019 07:00'))
        print(standardizeDate('07:00'))
        print(standardizeDate('03/05/18'))
        print(standardizeDate('31/12/18'))
        print(standardizeDate('31/03/18'))



