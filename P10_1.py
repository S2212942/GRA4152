#Add a class NumericQuestion to the question hierarchy of Section 10.1.
#  If the response and the expected answer differ by no more than 0.01, 
# then accept the response as correct.

##
#  This module defines a class that models exam questions. 
#

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
   #
   def setAnswer(self, correctResponse) :
      self._answer = correctResponse

   ## Checks a given response for correctness.
   #  @param response the response to check
   #  @return True if the response was correct, False otherwise
   #
   def checkAnswer(self, response) :
      return response == self._answer

   ## Displays this question.
   #
   def display(self) :
      print(self._text)         
    
class NumericQuestion(Question) :
    # The subclass has its own constructor
    def __init__(self) :
        super().__init__()  

    # Check a given response for correctness
    # @param response the response to check
    # return True if the absolute difference between response and true result not more than 0.01, otherwise return False
    def checkAnswer(self, response):
        # absolute difference between response and true result 
        absDiff = abs(float(self._answer) - float(response))

        if float(absDiff) <= 0.01:
            return True
        else:
            return False
    # Set the answer for question
    #@param correctResponse the answer for the given question
    # the try block sets an exception when the answer is not a float.
    def setAnswer(self, correctResponse) :
        try:
            self._answer = float(correctResponse)
        except: 
            raise ValueError("The correct respond must be number.")

# display the question, ask for the response and check this response for correctness
def presentQuestion(question) :
    question.display()
    response = input("Your answer: ")
    print(question.checkAnswer(response))
    

# Test for Numeric question class

q1 = NumericQuestion()
q1.setText("What would be the result of 3.1 + 4.2")
q1.setAnswer(7.3)

presentQuestion(q1)
