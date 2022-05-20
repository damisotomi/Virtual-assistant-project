# A PYTHON DIGITAL ASSISTANT THAT TAKES IN ANY QUESTION AND RETURNS AN ANSWER AFTER SEARCHING THE INTERNET
# We can also do maths
# and also make it talk 
#we will install a package called wikipedia and wolframalpha
#we will also install wxpython to give us the dialog box 

import wikipedia
import wolframalpha

while True:
    try:
        # Combing through wolframalpha
        question=input('Ask a question or search for anything!! ')
        app_id="34HXQ6-UQ5KKEH664"
        client=wolframalpha.Client(app_id)  #creating our client to make the api calls using the api id

        res =client.query(question) 
        answer=next(res.results).text #to ensure wolframalpha returns a text
        print(answer)
    except:
        #combing through wikipedia
        try:
            print(wikipedia.summary(question,sentences=2, auto_suggest=False)) #plain text summary of page
        except (wikipedia.exceptions.DisambiguationError, wikipedia.exceptions.PageError): #searches if no page is found or too many suggestions of the query
            result=wikipedia.search(question,results=10,suggestion=False)
            if len(result)==0: #if no search result
                print (f"No result found for '{question}'. Please check spelling and try again")
            else: print(result)

   