from flask import Flask, render_template, request, json
from collections import Counter

app = Flask(__name__)

@app.route("/nav")
def navigation():
    return render_template('nav.html')


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route("/footer")
def footer():
    return render_template('footer.html')


@app.route('/wordmaker', methods=['GET', 'POST'])

def wordMaker():
        
    if request.method == 'POST':
        letterinput = request.form.get('letterinput')

        userInputSet = set(Counter(letterinput.lower()))
        emp = []
        for k in letterinput:
            emp.append(k)
            print(Counter(emp))

        data = json.load(open('./english-words.json'))

        wordsMatch = []

        # words_array = ["apple", "banana", "cherry", "elderberry", "tea", "eat", "ate", "date", "add"]
        
        for i in data:
            if set(i).issubset(userInputSet):
                wordsMatch.append(i)

        return render_template('wordMaker.html', wordsMatch=wordsMatch)

# use the collections.Counter class to count characters in an element
# To check for duplicate characters in the user input and identify them, you can use the collections.Counter class from the Python standard library. 
# This class can count the occurrences in a list, making it easy to identify duplicates
    
# output is showing duplicate letters aswell which arent in the user input

    return render_template('wordMaker.html')



if  __name__ == "__main__":
    app.run(debug=True)

