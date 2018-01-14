"""Web crawler for extracting questions and answers data from https://www.grileonline.ro/teste/biologie/complement-simplu.html."""

__author__ = 'Robert-Mihail UNGUREANU'

import re
import json
import requests
import unidecode

# The number of questions found. Just hardcoding this >.>
TOTAL_NUMBER_OF_QUESTIONS = 250

# URLs used for the crawling.
MAIN_PAGE_URL = r'https://www.grileonline.ro/teste/biologie/complement-simplu.html?intrebare={}'

QUESTION_PATTERNS = [
    r'<blockquote class="with-borders intrebare"><p><strong>(?P<question>[^<]+)</strong>',
    r'<blockquote class="with-borders intrebare"><p><b>(?P<question>[^<]+)</b>'
]
ANSWERS_PATTERN = '<input type="checkbox" id="[^"]+" data-corect="(?P<correct>\d)">\s*?<label for="[^"]+">.\)</label>\s*?</div>\s*?<span class="raspuns">(?P<answer>[^<]+?)</span>'

# Basic headers used in the requests
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
}

def retrieve_page(page):
    return requests.get(page, headers=HEADERS).text


def retrieve_result_page(page, data):
    return requests.post(page, headers=HEADERS, data=data).text


if __name__ == '__main__':
    result = list()

    for i in range(1, TOTAL_NUMBER_OF_QUESTIONS + 1):
        first_page_data = retrieve_page(MAIN_PAGE_URL.format(i))

        print(i)
        for pattern in QUESTION_PATTERNS:
            res = re.search(pattern, first_page_data)
            if res:
                question = res.group(1)
                break
        temp_answers = re.findall(ANSWERS_PATTERN, first_page_data)
        answers = list()

        for answer in temp_answers:
            if answer[0] == '1':
                correct_answer = answer[1].replace('\r\n', ' ')
                correct_answer = unidecode.unidecode(correct_answer)
            answers.append(unidecode.unidecode(answer[1]).replace('\r\n', ' '))

        result.append(
            {
                'question': question,
                'answers': answers,
                'correct_answer': correct_answer,
                'topic': 'Unknown'
            }
        )

    with open('questions_with_topics_2.json', 'w', encoding='utf8') as handle:
        handle.write(
            json.dumps(result, indent=4, ensure_ascii=False)
        )
    print('Extracted', len(result), 'questions.')
