'''
Implement a function fill_up_missing_dates() that takes one argument as input:

dates — list of string dates in DD.MM.YYYY format
The function should return a list containing all the dates in the dates list, in ascending order, plus any missing dates in between.

Note 1: Let's look at the first test. The dates list contains the period from 11/01/2021 to 11/07/2021:

dates = ['11/01/2021', '11/07/2021', '11/04/2021', '11/03/2021']
which does not contain the dates 11/02/2021, 11/05/2021, 11/06/2021. Then the function call: fill_up_missing_dates(dates)
should return a list:

['11/01/2021', '11/02/2021', '11/03/2021', '11/04/2021', '11/05/2021', '11/06/2021', '11/07/2021']
'''

from datetime import datetime, timedelta


def fill_up_missing_dates(dates: list) -> list:
        """
        The function returns a list containing all dates from the dates list,
        arranged in ascending order, as well as all missing intermediate dates.
        Args:
            dates (list): a list of string dates in the format DD.MM.YYYY

        Returns:
            list: a list of dates in ascending order
        """
        my_dates = list(map(lambda x: datetime.strptime(x, '%d.%m.%Y'), dates))
        min_date = min(my_dates)
        max_date = max(my_dates)
        final = []
        while min_date != max_date:
                final.append(min_date.date().strftime('%d.%m.%Y'))
                min_date += timedelta(days=1)
        final.append(min_date.date().strftime('%d.%m.%Y'))
        return final

