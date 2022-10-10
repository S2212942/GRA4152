#Add a class MultiChoiceQuestion to the question hierarchy of Section 10.1 that allows multiple correct choices. 
# The respondent should provide all correct choices, sepa- rated by spaces. 
# Provide instructions in the question text.

##
#  This module defines a class that models exam questions. 
#

## A question with a text and an answer.
#
from calendar import c


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
    
# Subclass ChoiceQuestion
class ChoiceQuestion(Question) :
        # The subclass has its own constructor.
        def __init__(self):
           super().__init__()
           self._choices = []
        
        # addChoice method is added to the subclass
        def addChoice(self, choice, correct):
            self._choices.append(choice)
            if correct:
                # the answer is the length of the list
                lengthList = str(len(self._choices))
                self.setAnswer(lengthList)
        
        # The display method is  overridden its method from the superclass:
        def display(self):
            # display the question text
            super().display()
            # display the answer choices
            for i in range(len(self._choices)):
                choiceNumber = 1+ i
                print(f"{choiceNumber}. {self._choices[i]}")
# Subclass MultiChoice Question
class MultiChoiceQuestion(ChoiceQuestion) :
    # the subclass has its own constructor:
    def __init__(self):
        super().__init__()

    # Set the answer for question
    def setAnswer(self, correctResponse):
        self._answer = self._answer + " " + correctResponse

    # Checks a given response for correctness.
    def checkAnswer(self, response):
        # Slit the _answer and response into lists to compare 
        respondList = response.split()
        answerList =self._answer.split()

        # Sort and check if two lists are equal:
        return sorted(respondList) == sorted(answerList)

    # The display method is overridden in MultiChoiceQuestion class:
    def display(self):
        return super().display()
        # add instruction 
    

def presentQuestion(question):
    question.display()
    print("This question may have more than one answer, print all answers you think that is correct.")
    response = input("Your answer: ")
    print(question.checkAnswer(response))

## Test
q1 = MultiChoiceQuestion()
q1.setText("Which countries are in Europe?")
q1.addChoice( "Canada", False)
q1.addChoice( "Netherland", True)
q1.addChoice( "US", False)
q1.addChoice( "Norway", True)
presentQuestion(q1)