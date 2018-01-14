import json
import random


def retrieve_questions(limit=1):
    with open('all_questions.json', 'r') as handle:
        data = handle.read()

    questions = json.loads(data)

    return random.sample(questions, limit)


if __name__ == '__main__':
    for item in retrieve_questions(3):
        print(item)
