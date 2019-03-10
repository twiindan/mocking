import json
import random
import requests
from requests import Timeout
from src.configuration import URL


class TindevQA():

    users = ['Sara', 'Alexandra', 'Leia']

    # users = ['Sara', 'Alexandra', 'Bryan', 'Luke', 'Leia', 'Daniel', 'Noa', 'Noah', 'Martina', 'Jorge',
    # 'Carla', 'Blas', 'Epi', 'Elmo', 'Lidia', 'Paula', 'Torcuato', 'Celestino', 'Gaspara', 'Paco' ]

    def get_next_person(self, user):
        person = self.get_random_user()
        while person in user['people_seen']:
            person = self.get_random_user()
        return person

    def get_random_user(self):
        return random.choice(self.users)

    def evaluate(self, person1, person2):
        if person1 in person2['likes']:
            self.send_email(person1)
            self.send_email(person2)

        elif person1 in person2['dislikes']:
            self.let_down_gently(person1)

        elif person1 not in person2['likes'] and person1 not in person2['dislikes']:
            self.give_it_time(person1)

    def let_down_gently(self, person1):
        print('Podemos ser amigos')

    def send_email(self, person1):
        print('Eres mi media naranja!')

    def give_it_time(self, person1):
        print('Dale tiempo, algún día no pasaras desapercibido')

    def get_information_from_file(self, filename):
        try:
            return json.loads(open(filename).read())
        except (IOError, ValueError):
            return "ERROR"

    def send_sms(self, user, text, to=34677722314):

        try:
            body = {'from': user, 'text': text, 'to': to,
                    'api_key': 'fa93366b', 'api_secret': 't6WYC4aIry8JNM9T'}
            r = requests.post(url=URL, data=body)
            return r
        except Timeout:
            return "ERROR"
