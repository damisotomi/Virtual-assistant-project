import wikipedia
while True:

    question=input('Ask a question or search for anything!! ')
    try:
        print(wikipedia.summary(question,sentences=2, auto_suggest=False)) #plain text summary of page
    except (wikipedia.exceptions.DisambiguationError, wikipedia.exceptions.PageError): #searches if no page is found or too many suggestions of the query
        result=wikipedia.search(question,results=10,suggestion=False)
        if len(result)==0: #if no search result
            print (f"No result found for '{question}'. Please check spelling and try again")

        else: print(result)


    