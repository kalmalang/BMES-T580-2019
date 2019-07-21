import wizard_code as wc
from random import choice

if __name__ == '__main__':
    #creature = wc.Creature('small animal', 1)
    creatures_to_fight = [wc.Creature('bear', 5),
                          wc.Creature('bird', 3),
                          wc.Creature('wolf', 8),
                          wc.Wizard('Evil Guy', 9)]
    possible_events = [wc.Event('Snowstorm', -2),
                       wc.Event('Thunder', 1),
                       wc.Event('Sunshine', 2),
                       wc.Event('Rain', -1)]
    me = wc.IceWizard('Joe', 10)

    while True:

        turn_creature = choice(creatures_to_fight)
        print('-------------------------------')
        print('From the forest emerges {}'.format(turn_creature.name))

        if turn_creature.level < me.level:
            print('Should be easy. Its only level {}'.format(turn_creature.level))

        else:
            print('Watch out! Its level {}'.format(turn_creature.level))

        turn_event = choice(possible_events)
        if turn_event.type == 'Snowstorm':
            print('There is a snowstorm coming, your level will be reduced by 2')
            me.level_down()
            me.level_down()
        elif turn_event.type == 'Thunder':
            print('A Thunderstorm comes through. The {} is scared and you feel empowered (+1 level)'.format(turn_creature.name))
            me.level_up()
        elif turn_event.type == 'Sunshine':
            print('The sun comes out and you feel in best fighting spirit. Your level is raised by 2')
            me.level_up()
            me.level_up()
        else:
            print('It is starting to rain. The grass becomes slippery and you lose a level')
            me.level_down()


        print('What do you want to do?')
        action = input('[A]ttack, [R]un, [Q]uit')

        if action == 'Q':
            print('Bye')
            raise SystemExit
        elif action == 'A':
            my_roll = me.attack_roll()
            creature_roll = turn_creature.defense_roll()
            print('You got: ', my_roll, 'and the creature got', creature_roll)
            if my_roll > creature_roll:

                me.level_up()
                print('Yay! You won! Your level is now %i' % me.level)

            else:
                me.level_down()
                print('You lost! Your level is now %i' % me.level)
                if me.level == 0:
                    print('Oop, you died')
                    raise SystemExit
        elif action == 'R':
            print('Coward! Your level remains %i' % me.level)

