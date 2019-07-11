import datetime


def print_header():
    print('---------------------------')
    print('   JOHANNES PREGNANCY WHEEL')
    print('---------------------------')
    print()


def get_lmp_from_patient():
    print("When was your LMP? ")

    date_str = input('Format: [dd/mm/yyyy]? ')
    # '05/06/2018'

    parts = date_str.split('/')
    if len(parts) != 3:
        print('Bad date found', date_str)
        return get_lmp_from_patient()

    year = int(parts[2])
    month = int(parts[1])
    day = int(parts[0])

    LMP = datetime.date(year, month, day)
    print(LMP)
    return LMP


def compute_days_between_dates(original_date, target_date):
    this_year = datetime.date(target_date.year, original_date.month, original_date.day)

    dt = this_year - target_date
    return dt.days


def print_due_date_information(min_due_date, max_due_date, exp_due_date):

    print('Your expected due date is', exp_due_date.strftime('%A %B %d %Y'))
    print('But it may be as early as', min_due_date.strftime('%A %B %d %Y'))
    print('Or as late as', max_due_date.strftime('%A %B %d %Y'))



    #if days < 0:
     #   print("You had your birthday {} days ago this year.".format(-days))
    #elif days > 0:
    #    print("Your birthday is in {} days!".format(days))
    #else:
    #    print("Happy birthday!!!")


def main():
    print_header()
    LMP = get_lmp_from_patient()
    gest_length = datetime.timedelta(days=281)
    gest_std = datetime.timedelta(days = 13)

    exp_due_date = LMP + gest_length
    min_due_date = exp_due_date - gest_std
    max_due_date = exp_due_date + gest_std


    #today = datetime.date.today()
    #number_of_days = compute_days_between_dates(LMP, today)
    print_due_date_information(min_due_date, max_due_date, exp_due_date)


main()