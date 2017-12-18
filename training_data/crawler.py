"""Web crawler for extracting questions and answers data from http://www.tests.ha-ha.ro."""

__author__ = 'Robert-Mihail UNGUREANU'

import re
import json
import requests

# URLs used for the crawling.
MAIN_PAGE_URL = r'http://www.teste.ha-ha.ro/'
START_PAGE_URL = r'http://www.teste.ha-ha.ro/anatomie.php'
INDEXED_PAGE_URL = r'http://www.teste.ha-ha.ro/anatomie.php?pagina={index}'
RESULT_PAGE_URL = r'http://teste.ha-ha.ro/rezultat.php'

# Basic headers used in the requests
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
}

# Patterns used for parsing data.
TEST_BUTTON_PATTERN = r"<a class='btn_teste btn_teste-4 btn_teste-4b fa-check' href='([^']+)'> Start test</a>"
LAST_PAGE_PATTERN = r"<a href='[^?]+\?pagina=(\d+)'><b>&#187;</b></a></div>"
QUESTIONS_AND_ANSWERS_PATTERN = r"<h2 class='toc-backref'>(?P<question>.+?)</h2>[\s\S]+?<ul class='wrapping-list'>(?P<answers_body>[\s\S]+?)</ul>"
ANSWERS_PATTERN = r"<input type='radio'.*?value='(?P<value>[^']+)'/>\s*<label for='[^']+'>(?P<answer>.+?)</label>"
CORRECT_ANSWER_PATTERN = r"<i class='fa fa-lg fa-check verde'></i> &nbsp;(.+?)</label>"


def retrieve_page(page):
    return requests.get(page, headers=HEADERS).text


def retrieve_result_page(page, data):
    return requests.post(page, headers=HEADERS, data=data).text


if __name__ == '__main__':
    first_page_data = retrieve_page(START_PAGE_URL)

    last_page_index = int(re.search(LAST_PAGE_PATTERN, first_page_data).group(1))

    result = list()

    for i in range(1, last_page_index + 1):
        # Retrieving indexed pages
        indexed_page = retrieve_page(
            INDEXED_PAGE_URL.format(index=i)
        )

        # For each page retrieve it's links towards the tests.
        for test_button_uri in re.findall(TEST_BUTTON_PATTERN, indexed_page):
            questions = []

            # For each test retrieve the token required for the POST request.
            token = re.search('test=(.+)$', test_button_uri).group(1)

            # Build the url for the test's page and retrieve its content.
            test_page = retrieve_page(MAIN_PAGE_URL + test_button_uri)

            # Retrieve the hash required for the POST request.
            hash_text = re.search('<input type="hidden" name="hash_test" value="([^"]+)" />', test_page).group(1)

            # Retrieve all the questions and answers on this page.
            for match in re.finditer(QUESTIONS_AND_ANSWERS_PATTERN, test_page):
                question = {
                    'question': match.group('question').strip(),
                    'answers': []
                }

                for item in re.finditer(ANSWERS_PATTERN, match.group('answers_body')):
                    question['answers'].append(item.group('answer').strip())

                questions.append(question)

            # Build the form data required for sending the POST request in order to obtain the test's result.
            data = {
                'hash_test': hash_text,
                'token': token
            }

            # There are 20 questions in each test (hopefully).
            for idx in range(1, 21):
                # Just assign a random answer to each question.
                data['intrebare_nr_{}'.format(idx)] = 'A'

            # Send the POST request, retrieve the data
            result_page = retrieve_result_page(RESULT_PAGE_URL, data)

            # Parse it in order to retrieve the correct answers.
            # The n-th answer corresponds to the n-th question.
            correct_answers = [correct_answer for correct_answer in re.findall(CORRECT_ANSWER_PATTERN, result_page)]

            for idx, correct_answer in enumerate(correct_answers):
                questions[idx]['correct_answer'] = correct_answer.strip()

            # Extend the final result using the questions determined in this test.
            result.extend(questions)

    with open('questions.json', 'w') as handle:
        handle.write(
            json.dumps(result, indent=4)
        )
    print('Extracted', len(result), 'questions.')
