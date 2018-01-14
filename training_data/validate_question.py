import os
import json
import random

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QUESTIONS_FILE_PATH = os.path.join(BASE_PATH, 'training_data', 'all_questions.json')

def retrieve_questions(limit=1):
    with open(QUESTIONS_FILE_PATH, 'r', encoding = "ISO-8859-1") as handle:
        data = handle.read()

    questions = json.loads(data)

    return random.sample(questions, limit)


if __name__ == '__main__':
    for item in retrieve_questions(3):
        print(item)
