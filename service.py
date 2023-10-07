import random


sport = {
    'Плавание': 'Вид спорта',
    'Бассейн': 'Место, где люди тренируются в воде',
    'Соревнования': 'Участники борятся между собой в погоне за победой',
}
def random_word():
    random_q = random.choice(list(sport.items()))
    return random_q

