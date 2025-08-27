import json
from difflib import get_close_matches


def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data


def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)


def find_best_match(user_question: str, questions: list[str]) -> str | None:
    matches: list = get_close_matches(user_question,
                                      questions,
                                      n=1,
                                      cutoff=0.7)
    return matches[0] if matches else None


def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]
    return None


def chat_bot():
    knowledge_base: dict = load_knowledge_base('knowledge_base.json')

    while True:
        user_input: str = input('You: ')

        if user_input.lower() == 'math':
            import os
            os.system('python SimpleCalc.py')
          #Use this format to run a seperate file

        if user_input.lower() == 'test':
            import os
            os.system('python testbody.py')

        if user_input.lower() == 'speak':
            import os
            os.system('python Speaking.py')
#not working yet
        if user_input.lower() == 'web':
            import os
            os.system('python WebTest.py')
           #Get the AI to webscrape specific websites

        if user_input.lower() == "define":
            import os
            os.system(' python Define.py')
        #making a dictionary

        if user_input.lower() == 'roll d20':
            import os
            os.system('python D20.py')

        if user_input.lower() == 'roll d12':
            import os
            os.system('python D12.py')

        if user_input.lower() == 'roll d10':
            import os
            os.system('python D10.py')

        if user_input.lower() == 'roll d8':
            import os
            os.system('python D8.py')

        if user_input.lower() == 'roll d6':
            import os
            os.system('python D6.py')

        if user_input.lower() == 'roll d4':
            import os
            os.system('python D4.py')

        if user_input.lower() == 'roll d100':
            import os
            os.system('python D100.py')

        if user_input.lower() == 'roll d1000':
            import os
            os.system('python d1000.py')

        if user_input.lower() == 'look around':
            import os
            os.system('python Sight.py')
#not working yet
        if user_input.lower() == 'talk':
            import os
            os.system('python Speaking.py')
        #not working yet

        if user_input.lower() == 'time':
            import os
            os.system('python Clock2.py')

        if user_input.lower() == 'translate':
            import os
            os.system('python Translate.py')

        if user_input.lower() == 'decide':
            import os
            os.system('python choice.py')
        
        if user_input.lower() == 'quit':
            break

        best_match: str | None = find_best_match(
            user_input, [q["question"] for q in knowledge_base["questions"]])

        if best_match:
            answer: str = get_answer_for_question(best_match, knowledge_base)
            print(f'Prio: {answer}')
        else:
            print('Prio: I don\'t know that. Can you teach me?')
            new_answer: str = input('Answer to teach or say "skip" to skip: ')

            if new_answer.lower() != 'skip':
                knowledge_base["questions"].append({
                    "question": user_input,
                    "answer": new_answer
                })
                save_knowledge_base('knowledge_base.json', knowledge_base)
                print('Prio: Thanks! Data learned!')


if __name__ == '__main__':
    chat_bot()
