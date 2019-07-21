import csv
import os

def main():

    print_header()

    filename = get_filename()

    age_min, age_max = get_age_cutoff()

    infection_inp = get_infection_cutoff()

    therapy = get_therapy()

    sex = get_sex()

    coin_inp = get_coinfection()

    out_filename = filename + '.valid.csv'

    num_pats = 0

# Open file and start reader
    with open(filename, mode = 'r') as handle:
        reader = csv.DictReader(handle)

        with open(out_filename, mode = 'w') as out_handle:

            fields = ['PAT_NUM', 'SEX', 'AGE', 'INFECTION_LENGTH','ON_THERAPY','COINFECTION']
            writer = csv.DictWriter(out_handle, fields)

            writer.writeheader()


            for row in reader:
                pat_age = int(row['AGE'])
                infection_len = int(row['INFECTION_LENGTH'])
                therapy_status = str(row['ON_THERAPY'])
                pat_sex = str(row['SEX'])
                pat_coinfection = str(row['COINFECTION'])


                match_age = (pat_age > age_min) and (pat_age < age_max)
                match_infection = (infection_len > infection_inp)
                match_therapy = (therapy_status == therapy)
                match_sex = (pat_sex == sex)
                match_coinfection = (pat_coinfection == coin_inp)

                if match_age and match_infection and match_therapy and match_sex and match_coinfection:
                    num_pats += 1
                    writer.writerow(row)

        print('Based on the following criteria: ')
        print(' - Age: [%i. %i]' % (age_min, age_max))
        print(' - Infection Length: %i' % infection_inp)
        print(' - On Therapy? %s' % therapy)
        print(' - Sex: %s' % sex)
        print(' - Coinfection: %s' % coin_inp)
        print('There are %i eligible patients' % num_pats)

def print_header():
    print('----------------------------')
    print('-------    Process     -----')
    print('-------  Demographics  -----')
    print('----------------------------')

def get_filename():

    filename = None
    while filename is None:

        filename = input('What is the /path/to/the/file?')

        if not os.path.exists(filename):
            print('That file could not be found. Try again.')
            filename = None

    return filename

def get_age_cutoff():

    age_min, age_max = None, None
    while age_min is None:
        age_inp = input('What is the youngest patient you are looking for? ')
        try:
            age_min = int(age_inp)
        except ValueError:
            print(age_inp + ' is not a number. Try again!')
            continue

        if age_min < 18:
            print('Ethics boards require special permission for youth cohort. Try again with an older age!')
            age_min = None

    while age_max is None:
        age_inp = input('What is the oldest age for the study? ')
        try:
            age_max = int(age_inp)
        except ValueError:
            print(age_inp + ' is not a number. Try once more.')
            continue

    return age_min, age_max

def get_infection_cutoff():

    infection_inp = None
    while infection_inp is None:
        inf_inp = input('What is the infection length in days you are looking for? ')
        try:
            infection_inp = int(inf_inp)
        except ValueError:
            print(inf_inp + ' is not a number. Try again!')
            continue
    return infection_inp

def get_therapy():

    therapy_inp = None
    while therapy_inp is None:
        thinp = input('Is the patient on therapy? [Y]es or [N]o')
        thinp = thinp.lower().strip()

        if thinp == 'y':
            therapy_inp = 'Yes'
        elif thinp == 'n':
            therapy_inp = 'No'

        else:
            print('Your input is not correct. Try again!')
            continue
    return therapy_inp

def get_sex():
    sex_inp = None
    while sex_inp is None:
        sinp = input('What is the patients sex you are looking for? [F]emale or [M]ale')
        sinp = sinp.lower().strip()

        if sinp == 'f':
            sex_inp = 'Female'
        elif sinp == 'm':
            sex_inp = 'Male'

        else:
            print('Your input is not correct. Try again!')
            continue
    return sex_inp

def get_coinfection():
    coin_inp = None
    while coin_inp is None:
        coinp = input('Do you consider coinfection? [Y]es or [N]o')
        coinp = coinp.lower().strip()

        if coinp == 'y':
            coin_inp = 'Yes'
        elif coinp == 'n':
            coin_inp = 'No'
        else:
            print('Bad input. Try again!')
            continue
    return coin_inp

if __name__ == '__main__':
    main()
