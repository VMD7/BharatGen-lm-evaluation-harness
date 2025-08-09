def doc_to_text(doc) -> str:
    """
    Question: <question>
    Choices:
    A. <option1>
    B. <option2>
    C. <option3>
    D. <option4>
    Answer:
    """
    choices = [doc["option1"], doc["option2"], doc["option3"], doc["option4"]]
    option_choices = {
        "A": choices[0],
        "B": choices[1],
        "C": choices[2],
        "D": choices[3],
    }

    prompt = "Question: " + doc["question"] + "\nChoices:\n"
    for choice, option in option_choices.items():
        prompt += f"{choice.upper()}. {option}\n"
    prompt += "Answer:"

    return prompt

def doc_to_target(doc) -> int:
    """
    Returns the index of the correct answer in the list of choices
    """
    answer_text = doc["answer"]
    options = [doc['option1'], doc['option2'], doc['option3'], doc['option4']]
    option_key = options.index(answer_text)
    return option_key
