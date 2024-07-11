
from .constants import BOT_WELCOME_MESSAGE, PYTHON_QUESTION_LIST


def generate_bot_responses(message, session):
    bot_responses = []

    current_question_id = session.get("current_question_id")
    if not current_question_id:
        bot_responses.append(BOT_WELCOME_MESSAGE)

    success, error = record_current_answer(message, current_question_id, session)

    if not success:
        return [error]

    next_question, next_question_id = get_next_question(current_question_id)

    if next_question:
        bot_responses.append(next_question)
    else:
        final_response = generate_final_response(session)
        bot_responses.append(final_response)

    session["current_question_id"] = next_question_id
    session.save()

    return bot_responses


def record_current_answer(answer, current_question_id, session):
    '''
    Validates and stores the answer for the current question to django session.
    '''
    return True, ""


def get_next_question(current_question_id):
    '''
    Fetches the next question from the PYTHON_QUESTION_LIST based on the current_question_id.
    '''
    if current_question_id is None:
        # If there is no current question, start with the first question
        next_question = PYTHON_QUESTION_LIST[0]
    else:
        # Find the index of the current question
        current_index = next(
            (index for (index, d) in enumerate(PYTHON_QUESTION_LIST) if d["id"] == current_question_id), 
            None
        )
        if current_index is None or current_index + 1 >= len(PYTHON_QUESTION_LIST):
            # If current question is not found or it's the last question, no next question
            return None, None
        next_question = PYTHON_QUESTION_LIST[current_index + 1]

    next_question_text = next_question["question_text"]
    next_question_id = next_question["id"]
    
    return next_question_text, next_question_id

    return "dummy question", -1


def generate_final_response(session):
    '''
    Creates a final result message including a score based on the answers
    by the user for questions in the PYTHON_QUESTION_LIST.
    '''user_answers = session.get('answers', {})
    correct_answers = CORRECT_ANSWERS
    score = 0

    for question_id, correct_answer in correct_answers.items():
        if user_answers.get(question_id) == correct_answer:
            score += 1

    total_questions = len(correct_answers)
    final_message = (
        f"Quiz Completed!\n"
        f"Your Score: {score} out of {total_questions}\n\n"
        f"Thank you for participating!"
    )

    

    return "dummy result"
