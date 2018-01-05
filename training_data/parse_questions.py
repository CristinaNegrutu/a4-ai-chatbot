import re
import json
import codecs

# Link: http://simulare-admitere.ssmi.ro/subiecte-si-bareme-sesiune-1-11-03-2017/ 
if __name__ == '__main__':
    f = codecs.open('data.txt', encoding='utf-8')
    content = f.read()

    final_data = []
    data = re.split('\n+', content)
    print(len(data))

    for i in range(0, len(data), 7):
        q = {
            "correct_answer": "",
            "answers": [],
            "question": "",
        }
        question_data = data[i:i + 7]
        q['question'] = question_data[1].strip()
        for j in range(2, 7):
            match = re.search('(?<=[a-z][).] ).*', question_data[j].strip())

            try:
                q['answers'].append(match.group())
            except Exception as err:
                print(err, question_data[j].strip())
        final_data.append(q)

    with open('results.json', 'w', encoding='utf8') as handle:
        json.dump(final_data, handle, indent=4, ensure_ascii=False)

    for index, i in enumerate(final_data):
        print(index, i)
