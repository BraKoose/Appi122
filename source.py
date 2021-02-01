import mysql.connector
from difflib import get_close_matches

con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)
def translate(w):
    if results:
        for result in results:
            print(result[0])
    elif w.lower():
        if w in results:
            return result[w]
    elif w.title() in results:
        return result[w.upper()]
    elif len(get_close_matches(w, results.keys())) > 0:
        yn=input('Did you mean %s instead? Enter Y if yes, or N if No!')
        if yn.upper() == 'Y':
            return results[get.get_close_matches(w, query.keys())[0]]
        elif yn.upper() == 'N':
            return 'MisMatch, Word Dont Exist'
        else:
            return 'Word Dont Exist, Please Double check!'

    else:
        print("No word found!")

word=input("Enter the word: ")
cursor = con.cursor()
query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word)
results = cursor.fetchall()






output = translate(word)
if type(output)==list:
    for results in output:
        print (results)
else:
    print(output)
