import matplotlib.pyplot as plt 

def find_mood():
    happy = 0
    sad = 0
    with open('recent_genres.txt', 'r') as file:
        for line in file:
            happy = 0
            sad = 1
            line = line.strip()
            if "hip hop" in line or "rap" in line:
                happy = happy + 1
            elif "rnb" in line:
                sad = sad + 1
    
    return happy, sad

# To create some sort of graph or any visual for that matter 
def produce_visual():
    mood_mapping = {"Uncertain": 3, "Happy": 1, "Sad": 2, "Error": 0}
    feeling = []
    days=['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

    with open('mood_tracker.txt', 'r') as file:
        for line in file:
            line = line.strip()
            mood_number = mood_mapping.get(line, 0)
            feeling.append(mood_number)

    if (len(feeling) != len(days)): 
        print("Not enough Information to produce Visual!")
    else:
        plt.plot(days, feeling)
        plt.xlabel('Days')
        plt.ylabel('Feelings')
        plt.title('How do I Feel Based On Listening History')
        plt.show()

# Problem here, code cant run all at once, but you can run it individually 
def main_run():
    subprocess.run(['python', 'main.py'])
             
def main():

    main_run()

    happy, sad = find_mood()

    mood = ""
    number = "0"

    if (happy-sad >= 0 and happy-sad <= 3):
        mood = "Uncertain"
        number = "3"
    elif (happy-sad > 3):
        mood = "Happy"
        number = "1"
    elif (happy-sad < 0):
        mood = "Sad"
        number = "2"
    else:
        mood = "Error"
        number = "0"

    with open("mood_tracker.txt", 'r') as file:
        first_char = file.read(1)
        file.seek(0)

        if not first_char:
            with open("mood_tracker.txt", 'a') as file:
                file.write(mood)

        else:
            with open("mood_tracker.txt", 'a') as file:
                file.write('\n' + mood)

    produce_visual()

main()

