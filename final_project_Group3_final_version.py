# Final Project Wandering in the Woods Game
# File Name: final_project_Group3_final_version.py
# Jose Montes De Oca Morfin, Paige Dyer
# PaigeDyer@lewisu.edu
# joseamontesdeocamo@lewisu.edu
# CPSC-44000-LT1
# Finished and Submitted: TBA


import PySimpleGUI as sg
from turtle import *
import turtle as tur


sc = tur.Screen()




font = ("Arial", 20)

intro_layout = [[sg.Text("Hello! Welcome to the wandering in the woods game. This game is designed for three sets of students.", font = font)],
          [sg.Text("The first is for students between the grades Kindergarden through Second grade. The second set is for", font = font)],
          [sg.Text("students between Third grade and Fifth grade, and the last set of students is for Sixth grade through", font = font)],
          [sg.Text("Eight grade. Each level of this game gets progressivley more complex the higher in grade level you go.", font = font )],
          [sg.Button("Get Started", size=(10,2))]]


questions_layout = [[sg.Text("Which grade level would you like to try?")],
                    [sg.Button("K - 2", key = "k_2")],
                    [sg.Button("3 - 5", key = "3_5")],
                    [sg.Button("6 - 8", key = "6_8")]]

kindergarden_second_layout_questions = [[sg.Text("How many rows and columns would you like the square to be.")],
                                        [sg.Input(size = (5, 1), enable_events=True, key= 'box_size'), sg.Button("Submit")]]


def draw_board(size):
    tur.setup(500, 500)
    pen = tur.Turtle()
    pen.speed(0)  
    
    for y in range(size):
        pen.penup()
        pen.goto(0, y * 20)
        pen.pendown()
        pen.goto((size - 1) * 20, y * 20)

        pen.penup()
        pen.goto(y * 20, 0)
        pen.pendown()
        pen.goto(y * 20, (size - 1) * 20)

    tur.done()



intro_window = sg.Window("Wandering in the Woods Game", intro_layout, element_justification='c')
questions_window = sg.Window("Select your grade year", questions_layout, element_justification= "c")
kindergarden_second_question_window = sg.Window("Select your grid size", kindergarden_second_layout_questions, element_justification="c")



while True:
    event, values = intro_window.read()
    if event == "Get Started" or event == sg.WIN_CLOSED:
        break
intro_window.close()


while True:
    event, values = questions_window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "k_2":
        event, values = kindergarden_second_question_window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Submit":
            size = int(values["box_size"])
            kindergarden_second_question_window.close()
            draw_board(size)
            
            
            
kindergarden_second_question_window.close()
questions_window.close()  