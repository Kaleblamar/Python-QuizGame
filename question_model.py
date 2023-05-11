# step1: create a question model (class)

class Question:
    # use the __init__dunder method to indicate the function is a constructor
    # set 2 attributes for the question text and answer
    def __init__(self, q_text, q_answer):
        # Be sure to use self syntax to be able to refer back to the object to access the attributes later

        self.text = q_text
        self.answer = q_answer

# test make sure functioning properly
new_q = Question("Are you ready for this quiz?", "False")
print(new_q)