from flask import Flask, request, render_template
from stories import Story, story

app = Flask(__name__)
print("does this run every time?")
currentStory = story
storyPresets = [story,
Story(["person","verb","adverb","object"],"""{person} usually enjoys {verb}. One day, {person} failed perfrom it {adverb}, so he was given the name {object}."""),
Story(["number", "adjective", "person"],"""{person} is {number} years old gramma, who loves her {adjective} dolls."""),
Story(['person', 'person2', 'person3'],"""{person} is {person2} and {person3}'s hidden best friends.""")]

@app.route('/home/<int:storyId>')
def homePage(storyId):
    currentStory = storyPresets[storyId]
    print(currentStory.prompts)
    return render_template('form.html',words = currentStory.prompts, storyCount=range(len(storyPresets)), storyIndex=storyId)
@app.route('/home')
def homePageDefault():
    return render_template('form.html',words = currentStory.prompts, storyCount=range(len(storyPresets)), storyIndex=0)

@app.route('/story/<int:storyId>')
def storyPage(storyId):
    answers = dict(request.args)
    currentStory = storyPresets[storyId]
    print(answers)
    print(currentStory.prompts)
    print(currentStory.template)
    return render_template('story.html',text = currentStory.generate(answers),storyCount=range(len(storyPresets)),storyIndex=storyId)

@app.route('/customStory')
def customStory():
    return render_template('newStory.html')
