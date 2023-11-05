import datetime

import pyttsx3
import speech_recognition as sr
from firebase import firebase
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.snackbar import Snackbar

# ----------------------------------------------------------------------------------------------------------------------

Window.size = (325, 670)

# ----------------------------------------------------------------------------------------------------------------------
engine = pyttsx3.init()


# ----------------------------------------------------------------------------------------------------------------------

class Command(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    font_name = "fonts/PoppinsEL.otf"
    font_size = 14


class Response(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    font_name = "fonts/PoppinsEL.otf"
    font_size = 14


class User_data(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    font_name = "fonts/PoppinsEL.otf"
    font_size = 13


class TCUAdvisor(MDApp):
    def build(self):

        global screen
        screen = ScreenManager(transition=SlideTransition(duration=.8))
        screen.add_widget(Builder.load_file("Introduction.kv"))
        screen.add_widget(Builder.load_file("Introduction1.kv"))
        screen.add_widget(Builder.load_file("Login.kv"))
        screen.add_widget(Builder.load_file("Register.kv"))
        screen.add_widget(Builder.load_file("Admin_login.kv"))
        screen.add_widget(Builder.load_file("Admin_Home-screen.kv"))
        screen.add_widget(Builder.load_file("Welcome-screen.kv"))
        screen.add_widget(Builder.load_file("Home-screen.kv"))
        screen.add_widget(Builder.load_file("Notification-screen.kv"))
        screen.add_widget(Builder.load_file("Profile-screen.kv"))
        screen.add_widget(Builder.load_file("About.kv"))

        screen.add_widget(Builder.load_file("Love_Command-screen.kv"))
        screen.add_widget(Builder.load_file("Love_message-screen.kv"))
        screen.add_widget(Builder.load_file("Academic_Command-screen.kv"))
        screen.add_widget(Builder.load_file("Academic_message-screen.kv"))
        screen.add_widget(Builder.load_file("Family_Command-screen.kv"))
        screen.add_widget(Builder.load_file("Family_message-screen.kv"))
        screen.add_widget(Builder.load_file("Financial_Command-screen.kv"))
        screen.add_widget(Builder.load_file("Financial_message-screen.kv"))

        return screen

    # AI Voices----------------------------------------------------------------------------------------------------------
    def speak_male(self, text):
        engine.setProperty('rate', 160)
        engine.setProperty('pitch', 100)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)

        engine.say(text)
        engine.runAndWait()

    def speak_female(self, text):
        engine.setProperty('rate', 160)
        engine.setProperty('pitch', 100)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)

        engine.say(text)
        engine.runAndWait()

    # Command & Responses -----------------------------------------------------------------------------------
    def response_love(self, *args):
        firebase_app = firebase.FirebaseApplication('https://test-e079c-default-rtdb.firebaseio.com/', None)
        Love_response = firebase_app.get('aidb-72811-default-rtdb/Category/Love_category', '')

        for x in Love_response.keys():
            if Love_response[x]['Command'] == command:
                response = Love_response[x]['Response']
                screen.get_screen('Love_message-screen').chat_list.add_widget(Response(text=response, size_hint_x=.75))
                self.speak_female(response)
                return

        for x in Love_response.keys():
            if Love_response[x]['Command'] != command:
                response = "Doesn't recognize or not in the category."
                screen.get_screen('Love_message-screen').chat_list.add_widget(Response(text=response, size_hint_x=.75))
                self.speak_female(response)
                return

    def response_academic(self, *args):
        firebase_app = firebase.FirebaseApplication('https://test-e079c-default-rtdb.firebaseio.com/', None)
        academic_response = firebase_app.get('aidb-72811-default-rtdb/Category/academic_category', '')

        for x in academic_response.keys():
            if academic_response[x]['Command'] == command:
                response = academic_response[x]['Response']
                screen.get_screen('Academic_message-screen').chat_list.add_widget(
                    Response(text=response, size_hint_x=.75))
                self.speak_female(response)
                return

        for x in academic_response.keys():
            if academic_response[x]['Command'] != command:
                response = "Doesn't recognize or not in the category."
                screen.get_screen('Academic_message-screen').chat_list.add_widget(
                    Response(text=response, size_hint_x=.75))
                self.speak_female(response)
                return

    def response_family(self, *args):
        firebase_app = firebase.FirebaseApplication('https://test-e079c-default-rtdb.firebaseio.com/', None)
        family_response = firebase_app.get('aidb-72811-default-rtdb/Category/family_category', '')

        for x in family_response.keys():
            if family_response[x]['Command'] == command:
                response = family_response[x]['Response']
                screen.get_screen('Family_message-screen').chat_list.add_widget(
                    Response(text=response, size_hint_x=.75))
                self.speak_female(response)
                return

        for x in family_response.keys():
            if family_response[x]['Command'] != command:
                response = "Doesn't recognize or not in the category."
                screen.get_screen('Family_message-screen').chat_list.add_widget(
                    Response(text=response, size_hint_x=.75))
                self.speak_female(response)
                return

    def response_financial(self, *args):
        firebase_app = firebase.FirebaseApplication('https://test-e079c-default-rtdb.firebaseio.com/', None)
        financial_response = firebase_app.get('aidb-72811-default-rtdb/Category/financial_category', '')

        for x in financial_response.keys():
            if financial_response[x]['Command'] == command:
                response = financial_response[x]['Response']
                screen.get_screen('Financial_message-screen').chat_list.add_widget(
                    Response(text=response, size_hint_x=.75))
                self.speak_female(response)
                return

        for x in financial_response.keys():
            if financial_response[x]['Command'] != command:
                response = "Doesn't recognize or not in the category."
                screen.get_screen('Financial_message-screen').chat_list.add_widget(
                    Response(text=response, size_hint_x=.75))
                self.speak_female(response)
                return

    def send_love(self):
        global size, halign, command
        if screen.get_screen('Love_message-screen').text_input != "":
            command = screen.get_screen('Love_message-screen').text_input.text
            if len(command) < 6:
                size = .22
                halign = "center"
            elif len(command) < 11:
                size = .32
                halign = "center"
            elif len(command) < 16:
                size = .45
                halign = "center"
            elif len(command) < 21:
                size = .58
                halign = "center"
            elif len(command) < 26:
                size = .71
                halign = "center"
            else:
                size = .77
                halign = "left"
            screen.get_screen('Love_message-screen').chat_list.add_widget(
                Command(text=command, size_hint_x=size, halign=halign))
            Clock.schedule_once(self.response_love, 0)
            screen.get_screen('Love_message-screen').text_input.text = ""

    def send_academic(self):
        global size, halign, command
        if screen.get_screen('Academic_message-screen').text_input != "":
            command = screen.get_screen('Academic_message-screen').text_input.text
            if len(command) < 6:
                size = .22
                halign = "center"
            elif len(command) < 11:
                size = .32
                halign = "center"
            elif len(command) < 16:
                size = .45
                halign = "center"
            elif len(command) < 21:
                size = .58
                halign = "center"
            elif len(command) < 26:
                size = .71
                halign = "center"
            else:
                size = .77
                halign = "left"
            screen.get_screen('Academic_message-screen').chat_list.add_widget(
                Command(text=command, size_hint_x=size, halign=halign))
            Clock.schedule_once(self.response_academic, 0)
            screen.get_screen('Academic_message-screen').text_input.text = ""

    def send_family(self):
        global size, halign, command
        if screen.get_screen('Family_message-screen').text_input != "":
            command = screen.get_screen('Family_message-screen').text_input.text
            if len(command) < 6:
                size = .22
                halign = "center"
            elif len(command) < 11:
                size = .32
                halign = "center"
            elif len(command) < 16:
                size = .45
                halign = "center"
            elif len(command) < 21:
                size = .58
                halign = "center"
            elif len(command) < 26:
                size = .71
                halign = "center"
            else:
                size = .77
                halign = "left"
            screen.get_screen('Family_message-screen').chat_list.add_widget(
                Command(text=command, size_hint_x=size, halign=halign))
            Clock.schedule_once(self.response_family, 0)
            screen.get_screen('Family_message-screen').text_input.text = ""

    def send_financial(self):
        global size, halign, command
        if screen.get_screen('Financial_message-screen').text_input != "":
            command = screen.get_screen('Financial_message-screen').text_input.text
            if len(command) < 6:
                size = .22
                halign = "center"
            elif len(command) < 11:
                size = .32
                halign = "center"
            elif len(command) < 16:
                size = .45
                halign = "center"
            elif len(command) < 21:
                size = .58
                halign = "center"
            elif len(command) < 26:
                size = .71
                halign = "center"
            else:
                size = .77
                halign = "left"
            screen.get_screen('Financial_message-screen').chat_list.add_widget(
                Command(text=command, size_hint_x=size, halign=halign))
            Clock.schedule_once(self.response_financial, 0)
            screen.get_screen('Financial_message-screen').text_input.text = ""

    def Love_take_command(self):

        global size, halign, command

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening . . .")
            r.pause_threshold = 1
            text = r.listen(source)
        try:
            print("Recognizing. . .")
            command = r.recognize_google(text, language='en-in')
            if len(command) < 6:
                size = .22
                halign = "center"
            elif len(command) < 11:
                size = .32
                halign = "center"
            elif len(command) < 16:
                size = .45
                halign = "center"
            elif len(command) < 21:
                size = .58
                halign = "center"
            elif len(command) < 26:
                size = .71
                halign = "center"
            else:
                size = .77
                halign = "left"
            screen.get_screen('Love_message-screen').chat_list.add_widget(
                Command(text=command, size_hint_x=size, halign=halign))
            Clock.schedule_once(self.response_love(), 1)
            screen.get_screen('Love_message-screen').text_input.text = ""

        except Exception as e:
            print(e)
            screen.get_screen('Love_message-screen').chat_list.add_widget(
                Response(text="Doesn't recognize or not in the category!", size_hint_x=size, halign=halign))
            return "None"
        return command

    def Academic_take_command(self):

        global size, halign, command

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening . . .")
            r.pause_threshold = 1
            text = r.listen(source)
        try:
            print("Recognizing. . .")
            command = r.recognize_google(text, language='en-in')
            if len(command) < 6:
                size = .22
                halign = "center"
            elif len(command) < 11:
                size = .32
                halign = "center"
            elif len(command) < 16:
                size = .45
                halign = "center"
            elif len(command) < 21:
                size = .58
                halign = "center"
            elif len(command) < 26:
                size = .71
                halign = "center"
            else:
                size = .77
                halign = "left"
            screen.get_screen('Academic_message-screen').chat_list.add_widget(
                Command(text=command, size_hint_x=size, halign=halign))
            Clock.schedule_once(self.response_academic(), 1)
            screen.get_screen('Academic_message-screen').text_input.text = ""

        except Exception as e:
            print(e)
            screen.get_screen('Academic_message-screen').chat_list.add_widget(
                Response(text="Doesn't recognize or not in the category!", size_hint_x=size, halign=halign))
            return "None"
        return command

    def Family_take_command(self):

        global size, halign, command

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening . . .")
            r.pause_threshold = 1
            text = r.listen(source)
        try:
            print("Recognizing. . .")
            command = r.recognize_google(text, language='en-in')
            if len(command) < 6:
                size = .22
                halign = "center"
            elif len(command) < 11:
                size = .32
                halign = "center"
            elif len(command) < 16:
                size = .45
                halign = "center"
            elif len(command) < 21:
                size = .58
                halign = "center"
            elif len(command) < 26:
                size = .71
                halign = "center"
            else:
                size = .77
                halign = "left"
            screen.get_screen('Family_message-screen').chat_list.add_widget(
                Command(text=command, size_hint_x=size, halign=halign))
            Clock.schedule_once(self.response_family(), 1)
            screen.get_screen('Family_message-screen').text_input.text = ""

        except Exception as e:
            print(e)
            screen.get_screen('Family_message-screen').chat_list.add_widget(
                Response(text="Doesn't recognize or not in the category!", size_hint_x=size, halign=halign))
            return "None"
        return command

    def Financial_take_command(self):

        global size, halign, command

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening . . .")
            r.pause_threshold = 1
            text = r.listen(source)
        try:
            print("Recognizing. . .")
            command = r.recognize_google(text, language='en-in')
            if len(command) < 6:
                size = .22
                halign = "center"
            elif len(command) < 11:
                size = .32
                halign = "center"
            elif len(command) < 16:
                size = .45
                halign = "center"
            elif len(command) < 21:
                size = .58
                halign = "center"
            elif len(command) < 26:
                size = .71
                halign = "center"
            else:
                size = .77
                halign = "left"
            screen.get_screen('Financial_message-screen').chat_list.add_widget(
                Command(text=command, size_hint_x=size, halign=halign))
            Clock.schedule_once(self.response_financial(), 1)
            screen.get_screen('Financial_message-screen').text_input.text = ""

        except Exception as e:
            print(e)
            screen.get_screen('Financial_message-screen').chat_list.add_widget(
                Response(text="Doesn't recognize or not in the category!", size_hint_x=size, halign=halign))
            return "None"
        return command

    def add_love_category_reponses(self, command, new_response):
        if any(field == "" for field in [command, new_response]):
            Snackbar(text="Please fill out all fields!",
                     snackbar_animation_dir="Top",
                     font_size='12sp',
                     snackbar_x=.1,
                     size_hint_x=.999,
                     size_hint_y=.07,
                     bg_color=(1, 0, 0, 1),
                     ).open()
        else:
            firebase_app = firebase.FirebaseApplication('https://test-e079c-default-rtdb.firebaseio.com/', None)
            data = {
                'Command': command,
                'Response': new_response
            }
            result = firebase_app.post('aidb-72811-default-rtdb/Category/Love_category', data)

            self.clear_admin_fields()

            Snackbar(text="Updated Successfully!",
                     font_size='12sp',
                     snackbar_x="10dp",
                     snackbar_y="10dp",
                     pos_hint={'center_x': 0.5, 'center_y': 0.9},
                     radius=[15, 15, 15, 15],
                     size_hint_x=(Window.width - (dp(75) * 2)) / Window.width,
                     bg_color=(0, 255, 0, 1),
                     ).open()

    def add_academic_category_reponses(self, command, new_response):
        if any(field == "" for field in [command, new_response]):
            Snackbar(text="Please fill out all fields!",
                     snackbar_animation_dir="Top",
                     font_size='12sp',
                     snackbar_x=.1,
                     size_hint_x=.999,
                     size_hint_y=.07,
                     bg_color=(1, 0, 0, 1),
                     ).open()
        else:
            firebase_app = firebase.FirebaseApplication('https://test-e079c-default-rtdb.firebaseio.com/', None)
            data = {
                'Command': command,
                'Response': new_response
            }
            result = firebase_app.post('aidb-72811-default-rtdb/Category/academic_category', data)

            self.clear_admin_fields()

            Snackbar(text="Updated Successfully!",
                     font_size='12sp',
                     snackbar_x="10dp",
                     snackbar_y="10dp",
                     pos_hint={'center_x': 0.5, 'center_y': 0.9},
                     radius=[15, 15, 15, 15],
                     size_hint_x=(Window.width - (dp(75) * 2)) / Window.width,
                     bg_color=(0, 255, 0, 1),
                     ).open()

    def add_family_category_reponses(self, command, new_response):
        if any(field == "" for field in [command, new_response]):
            Snackbar(text="Please fill out all fields!",
                     snackbar_animation_dir="Top",
                     font_size='12sp',
                     snackbar_x=.1,
                     size_hint_x=.999,
                     size_hint_y=.07,
                     bg_color=(1, 0, 0, 1),
                     ).open()
        else:
            firebase_app = firebase.FirebaseApplication('https://test-e079c-default-rtdb.firebaseio.com/', None)
            data = {
                'Command': command,
                'Response': new_response
            }
            result = firebase_app.post('aidb-72811-default-rtdb/Category/family_category', data)

            self.clear_admin_fields()

            Snackbar(text="Updated Successfully!",
                     font_size='12sp',
                     snackbar_x="10dp",
                     snackbar_y="10dp",
                     pos_hint={'center_x': 0.5, 'center_y': 0.9},
                     radius=[15, 15, 15, 15],
                     size_hint_x=(Window.width - (dp(75) * 2)) / Window.width,
                     bg_color=(0, 255, 0, 1),
                     ).open()

    def add_financial_category_reponses(self, command, new_response):
        if any(field == "" for field in [command, new_response]):
            Snackbar(text="Please fill out all fields!",
                     snackbar_animation_dir="Top",
                     font_size='12sp',
                     snackbar_x=.1,
                     size_hint_x=.999,
                     size_hint_y=.07,
                     bg_color=(1, 0, 0, 1),
                     ).open()
        else:
            firebase_app = firebase.FirebaseApplication('https://test-e079c-default-rtdb.firebaseio.com/', None)
            data = {
                'Command': command,
                'Response': new_response
            }
            result = firebase_app.post('aidb-72811-default-rtdb/Category/financial_category', data)

            self.clear_admin_fields()

            Snackbar(text="Updated Successfully!",
                     font_size='12sp',
                     snackbar_x="10dp",
                     snackbar_y="10dp",
                     pos_hint={'center_x': 0.5, 'center_y': 0.9},
                     radius=[15, 15, 15, 15],
                     size_hint_x=(Window.width - (dp(75) * 2)) / Window.width,
                     bg_color=(0, 255, 0, 1),
                     ).open()

    # User Registration----------------------------------------------------------------------------------------------------

    def register(self, name, stud_id, yr_course, section, password):

        firebase_app = firebase.FirebaseApplication('https://test-e079c-default-rtdb.firebaseio.com/', None)
        result = firebase_app.get('aidb-72811-default-rtdb/User', '')

        for i in result.keys():
            if result[i]['Student ID'] == stud_id:
                Snackbar(text="Student ID already Existed!",
                         snackbar_animation_dir="Top",
                         font_size='12sp',
                         snackbar_x=.1,
                         size_hint_x=.999,
                         size_hint_y=.07,
                         bg_color=(1, 0, 0, 1),
                         ).open()
                return

            elif any(field == "" for field in [name, stud_id, yr_course, section, password]):
                Snackbar(text="Please fill out all fields!",
                         snackbar_animation_dir="Top",
                         font_size='12sp',
                         snackbar_x=.1,
                         size_hint_x=.999,
                         size_hint_y=.07,
                         bg_color=(1, 0, 0, 1),
                         ).open()
                return

            else:
                firebase_app = firebase.FirebaseApplication('https://test-e079c-default-rtdb.firebaseio.com/', None)
                data = {
                    'Name': name,
                    'Student ID': stud_id,
                    'Year & Course': yr_course,
                    'Section': section,
                    'Password': password
                }

                result = firebase_app.post('aidb-72811-default-rtdb/User', data)

                self.clear_registration_fields()
                self.speak_male("Registered successfully!, please Log In your Account!")
                self.root.current = 'Login'

    # Admin & User Login----------------------------------------------------------------------------------------------------
    def user_login(self, stud_id, password):
        if not stud_id:
            self.speak_male("Please enter your Student ID!")
            return
        if not password:
            self.speak_male("Please enter your Password!")
            return

        firebase_app = firebase.FirebaseApplication('https://test-e079c-default-rtdb.firebaseio.com/', None)
        result = firebase_app.get('aidb-72811-default-rtdb/User', '')

        for i in result.keys():
            if result[i]['Student ID'] == stud_id:
                if result[i]['Password'] == password:
                    print("Logged In successfully!")
                    self.clear_user_login_fields()
                    self.root.current = 'Welcome-screen'

                    screen.get_screen('Profile-screen').add_widget(
                        User_data(text=result[i]['Name'], font_name="fonts/OpenSans-Semibold.ttf",
                                  pos_hint={"center_x": .73, "center_y": .60}))
                    screen.get_screen('Profile-screen').add_widget(
                        User_data(text=result[i]['Student ID'], font_name="fonts/OpenSans-Semibold.ttf",
                                  pos_hint={"center_x": .73, "center_y": .47}))
                    screen.get_screen('Profile-screen').add_widget(
                        User_data(text=result[i]['Year & Course'], font_name="fonts/OpenSans-Semibold.ttf",
                                  pos_hint={"center_x": .73, "center_y": .34}))
                    screen.get_screen('Profile-screen').add_widget(
                        User_data(text=result[i]['Section'], font_name="fonts/OpenSans-Semibold.ttf",
                                  pos_hint={"center_x": .73, "center_y": .21}))
                    return

        for i in result.keys():
            if result[i]['Student ID'] != stud_id:
                if result[i]['Password'] != password:
                    self.speak_male("Invalid Student ID or Password!")
                    return

        for i in result.keys():
            if result[i]['Student ID'] == stud_id:
                if result[i]['Password'] != password:
                    self.speak_male("Invalid Student ID or Password!")
                    return

        for i in result.keys():
            if result[i]['Student ID'] != stud_id:
                if result[i]['Password'] == password:
                    self.speak_male("Invalid Student ID or Password!")
                    return

    def admin_login(self, admin_id, admin_password):
        if not admin_id:
            self.speak_male("Please input your Admin ID!")
            return

        if not admin_password:
            self.speak_male("Please input your Admin Password!")
            return

        firebase_app = firebase.FirebaseApplication('https://test-e079c-default-rtdb.firebaseio.com/', None)
        result = firebase_app.get('aidb-72811-default-rtdb/Admin', '')

        for i in result.keys():
            if result[i]['Admin ID'] == admin_id:
                if result[i]['Admin Password'] == admin_password:
                    self.speak_male("Admin Logged In Successfully!")

                    self.clear_admin_login_fields()
                    self.root.current = 'Adminhome'
                    return

        for i in result.keys():
            if result[i]['Admin ID'] == admin_id:
                if result[i]['Admin Password'] != admin_password:
                    self.speak_male("Invalid Admin ID or Password!")
                    return

        for i in result.keys():
            if result[i]['Admin ID'] != admin_id:
                if result[i]['Admin Password'] != admin_password:
                    self.speak_male("Invalid Admin ID or Password!")
                    return

    def forgot_password(self):
        self.speak_male("Contact admin to retrieve your account")

    # Clearing Inputs-------------------------------------------------------------------------------------------------------
    def clear_admin_fields(self):
        Love = self.root.get_screen('Love_Command-screen')
        Academic = self.root.get_screen('Academic_Command-screen')
        Family = self.root.get_screen('Family_Command-screen')
        Financial = self.root.get_screen('Financial_Command-screen')

        Love.ids.command.text = ""
        Love.ids.new_response.text = ""

        Academic.ids.command.text = ""
        Academic.ids.new_response.text = ""

        Family.ids.command.text = ""
        Family.ids.new_response.text = ""

        Financial.ids.command.text = ""
        Financial.ids.new_response.text = ""

    def clear_registration_fields(self):
        screen = self.root.get_screen('Register')
        screen.ids.name.text = ""
        screen.ids.stud_id.text = ""
        screen.ids.yr_course.text = ""
        screen.ids.section.text = ""
        screen.ids.password.text = ""

    def clear_admin_login_fields(self):
        screen = self.root.get_screen('Admin_login')
        screen.ids.admin_id.text = ""
        screen.ids.admin_password.text = ""

    def clear_user_login_fields(self, ):
        screen = self.root.get_screen('Login')
        screen.ids.stud_id.text = ""
        screen.ids.password.text = ""

    # Admin & User Logout---------------------------------------------------------------------------------------------------

    def user_logout(self):
        Snackbar(text="Logged out successful!",
                 snackbar_animation_dir="Top",
                 font_size='12sp',
                 snackbar_x=.1,
                 size_hint_x=.999,
                 size_hint_y=.07,
                 bg_color=(1, 0, 0, 1)
                 ).open()

        self.root.current = 'Login'

    def admin_logout(self):
        Snackbar(text="Logged out successful!",
                 snackbar_animation_dir="Top",
                 font_size='12sp',
                 snackbar_x=.1,
                 size_hint_x=.999,
                 size_hint_y=.07,
                 bg_color=(1, 0, 0, 1)
                 ).open()
        self.root.current = 'Admin_login'

    # Display Users profile & Admin Homescreen users---------------------------------------------------------------------------------------------------------------
    def display_users_profile(self):
        firebase_app = firebase.FirebaseApplication('https://test-e079c-default-rtdb.firebaseio.com/', None)
        result = firebase_app.get('aidb-72811-default-rtdb/User', '')
    def display_all_user(self):
        firebase_app = firebase.FirebaseApplication('https://test-e079c-default-rtdb.firebaseio.com/', None)
        result = firebase_app.get('aidb-72811-default-rtdb/User', '')

        for i in result.keys():
            screen.get_screen('Adminhome').user_list.add_widget(
                User_data(text="Name:               " + result[i]['Name'], font_name="fonts/OpenSans-Bold.ttf",
                          pos_hint={"center_x": .6, "center_y": .5}, font_size=14))
            screen.get_screen('Adminhome').user_list.add_widget(
                User_data(text="Student ID:            " + result[i]['Student ID'],
                          font_name="fonts/OpenSans-Semibold.ttf",
                          pos_hint={"center_x": .6, "center_y": .5}))

            screen.get_screen('Adminhome').user_list.add_widget(
                User_data(text="Yr & Course:          " + result[i]['Year & Course'],
                          font_name="fonts/OpenSans-Semibold.ttf",
                          pos_hint={"center_x": .6, "center_y": .5}))
            screen.get_screen('Adminhome').user_list.add_widget(
                User_data(text="Section:                   " + result[i]['Section'],
                          font_name="fonts/OpenSans-Semibold.ttf",
                          pos_hint={"center_x": .6, "center_y": .5}))

            screen.get_screen('Adminhome').user_list.add_widget(
                User_data(text="-------------------------------------------------------", opacity=.5))

    # other functions---------------------------------------------------------------------------------------------------

    def on_touch(self, instance):
        pass

    def on_start(self):
        Clock.schedule_once(self.start, 3)

    def carousel_autonext(self):
        screen = self.root.get_screen('Welcome-screen')
        carousel = screen.ids.carousel
        carousel.loop = True
        Clock.schedule_interval(carousel.load_next, 0)

        screen = self.root.get_screen('Home-screen')
        carousel_1 = screen.ids.carousel_1
        carousel_1.loop = True
        Clock.schedule_interval(carousel_1.load_next, 3)

    def start(self, *args):
        self.root.current = "Profile-screen"
        self.carousel_autonext()
        self.display_all_user()

    # not yet use functions---------------------------------------------------------------------------------------------
    def wish(self):

        firebase_app = firebase.FirebaseApplication('https://test-e079c-default-rtdb.firebaseio.com/', None)
        result = firebase_app.get('aidb-72811-default-rtdb/User', '')

        hour = int(datetime.datetime.now().hour)

        for i in result.keys():

            if 0 <= hour < 12:
                self.speak_male(f"Good Morning!, Welcome to T C U Artificial Intelligence{(result[i]['Name'])}")
            elif 12 <= hour < 18:
                self.speak_male(f"Good Afternoon!, Welcome to T C U Artificial Intelligence{(result[i]['Name'])}")
            else:
                self.speak_male(f"Good Evening!, Welcome to T C U Artificial Intelligence{(result[i]['Name'])}")

    def exit(self):
        MDApp.get_running_app().stop()
        Window.close()


if __name__ == "__main__":
    TCUAdvisor().run()
