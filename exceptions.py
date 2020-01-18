"""Module for implementing exceptions """


class GameOver(Exception):
    """In my case that is just useless that do nothing."""
    pass

    @staticmethod
    def save_result(name, score):
        with open('scores.txt', 'a') as file:
            file.write(name + ' - ' + str(score) + '\n')



class EnemyDown(Exception):
    """One more almost useless exception."""
    pass
