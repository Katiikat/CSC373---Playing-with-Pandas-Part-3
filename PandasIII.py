# This application will allow the user to classify different types of vehicles based on
# some basic information. This will help users differentiate between the vehicle types by having the ability
# to enter in information and have the application predict what the type most likely is.

import pandas as pd
from sklearn import tree


def intro():
    # Let the user know what our application is about.
    print("\n\nThis application will allow you to classify different types of used vehicles based on some basic "
          "information. Simply enter numbers for the asked vehicle features, and the program will give you the "
          "best prediction of the vehicle type.")

    # User input for interaction with user
    repeat = True
    while repeat:
        ans = input("\nReady to begin?  Type Y/N\n")

        if ans == "Y" or ans == "y":
            repeat = False
        elif ans == "N" or ans == "n":
            print("See you soon. Goodbye.")
            print("Program has ended.")
            exit()
        else:
            print("Please type \"Y\" or \"N\"")


def get_user_input(clf):
    # User input for new data to predict on
    repeat = True
    while repeat:
        ans = input("Would you like to enter data about a vehicle? Type Y/N\n")

        if ans == "Y" or ans == "y":
            repeat = False
            print("Please enter only numbered digits. Do not spell out numbers. Thank you.")
            doors = int(input("How many doors does the vehicle have?\n"))
            mileage = int(input("How many miles does the vehicle have?\n"))
            wheels = int(input("Is the vehicle 4 wheel drive (also known as All Wheel Drive) or 2 wheel drive?\n"))
            seating = int(input("How many people can be seated in the vehicle?\n"))

            prediction_generation(clf, doors, mileage, wheels, seating)
        elif ans == "N" or ans == "n":
            print("See you soon. Goodbye.")
            print("Program has ended.")
            exit()
        else:
            print("Please type \"Y\" or \"N\"")


def load(csv_name):
    # Loading in the data using Pandas
    dataset = pd.read_csv(csv_name)
    train(dataset)


def train(dataset):
    # Make sure our data is reading in correctly
    # print("\n______________________________")
    # print("\t\tTraining Data")
    # print("______________________________")
    # print(dataset)

    # Features are in this order: # of Doors, Mileage, 2W or 4W, Seating Capacity, Reference

    # removing the first and last columns that aren't important to the bot
    labels = list(dataset['Type of Vehicle'].values.tolist())
    features = dataset.drop(columns=['Type of Vehicle', 'References']).values.tolist()

    test(features, labels)


def test(features, labels):
    # Training
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(features, labels)
    # # Use our AI ML app to predict what type of vehicle it will be

    get_user_input(clf)


# this method will call get_user_input and take in the features given by the user in order to predict on the new data
def prediction_generation(clf, doors, mileage, wheels, seating):
    print("Your vehicle is most likely a: ", clf.predict([[doors, mileage, wheels, seating]]))

    repeat = True
    while repeat:
        ans = input("Predict another vehicle? Type Y/N\n")

        if ans == "Y" or ans == "y":
            repeat = False
            get_user_input(clf)
        elif ans == "N" or ans == "n":
            print("See you soon. Goodbye.")
            print("Program has ended.")
            exit()
        else:
            print("Please type \"Y\" or \"N\"")


def main():
    intro()
    load("Custom Data Set - Automotive Comparison.csv")


if __name__ == "__main__":
    main()





