# Modify the checkAnswer method of the Question class so that 
# it does not take into account different spaces or upper/lowercase characters. 
# For example, the response "GUIDO van Rossum" should match an answer of "Guido van Rossum".

## A question with a text and an answer.
#
class Question :
   ## Constructs a question with empty question and answer strings.
   #
   def __init__(self) :
      self._text = ""
      self._answer = ""
      
   ##  Sets the question text.
   #   @param questionText the text of this question
   #
   def setText(self, questionText) :   
      self._text = questionText

   ## Sets the answer for this question.
   #  @param correctResponse the answer
   # the answer then transfer to lowercase and no space between texts.
   def setAnswer(self, correctResponse) :
      self._answer = correctResponse.lower().replace(" ", "")

   ## Checks a given response for correctness.
   #  @param response the response to check
   #  @return True if the response was correct, False otherwise
   #
   def checkAnswer(self, response) :
    # compare the no spacing and lower-case response with corresponding edited answer.
      return response.lower().replace(" ", "") == self._answer

   ## Displays this question.
   #
   def display(self) :
      print(self._text) 

    # Test the class
    
    # Create the question and expected answer.
q = Question()
q.setText("Who is the inventor of Python?")
q.setAnswer("Guido van Rossum")      

# Display the question and obtain user's response.
q.display()
response = input("your answer: ") # "GUIDO van Rossum"
print(q.checkAnswer(response))
print('expected: True')

