from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton,MDIconButton
from kivy.core.window import Window

screen_helper = """

ScreenManager:
    Inicio:
    Login:
    Registro:
    Principal:
    Agregar:
    Receta:

<Inicio>:
    name: 'inicio'

    MDFloatLayout:
        BoxLayout:
            orientation: 'vertical'
            Image:
                source: 'images/logo.png'
                size_hint_y: None
                height: dp(350)
            MDLabel:
                halign: 'center'

    MDRectangleFlatButton:
        text: '  Iniciar Sesion  '
        pos_hint: {'center_x':0.5, 'center_y':0.28}
        on_press: root.manager.current = 'logeo'
    MDRectangleFlatButton:
        text: '    Registrarse    '
        pos_hint: {'center_x':0.5, 'center_y':0.20}
        on_press: root.manager.current = 'registro'
    
<Login>:
    name: 'logeo'
   
    MDFloatLayout:
       
        BoxLayout:
            orientation: 'vertical'
            Image:
                source: 'images/logo.png'
                size_hint_y: None
                height: dp(300)
            MDLabel:
                halign: 'center'

        MDBoxLayout:
            orientation: 'vertical'
            size_hint: None, None
            pos_hint: {'center_x': 0.32, 'center_y': 0.3}
            spacing: '15dp'
            
            MDTextField:
                id: username_input
                hint_text: "Nombre"
                size_hint_x: None
                width: "200dp"
                
            MDTextField:
                id: password_input
                hint_text: "Contraseña"
                size_hint_x: None
                width: "200dp"
                password: True
   
    MDRectangleFlatButton:
        text: '   Iniciar Sesion   '
        pos_hint: {'center_x':0.5, 'center_y':0.1}                       
        on_press: root.manager.current = 'principal'
    MDIconButton:
        icon:'arrow-left-thick'
        pos_hint: {'center_x':0.1, 'center_y':0.943}
        on_press: root.manager.current = 'inicio'
        
<Registro>:
    name: 'registro'
    
    MDFloatLayout:
        BoxLayout:
            orientation: 'vertical'
            Image:
                source: 'images/logo.png'
                size_hint_y: None
                height: dp(280)
            MDLabel:
                halign: 'center'
    
    MDBoxLayout:
        orientation: 'vertical'
        size_hint: None, None
        pos_hint: {'center_x': 0.38, 'center_y': 0.24}
        spacing: '15dp'
        
        MDTextField:
            id: name_input
            hint_text: "Nombre"
            size_hint_x: None
            width: "150dp"
            
            padding_y: '20dp'  # Agregamos un margen superior

        MDBoxLayout:
            orientation: 'vertical'
            size_hint_y: None  
            height: "136dp"  # Ajustamos la altura para dejar espacio suficiente
            spacing: '15dp'
            pos_hint: {'center_x': 0.5}
            
            MDTextField:
                id: password1_input
                hint_text: "Contraseña"
                size_hint_x: None
                width: "150dp"
                password: True
                
            MDTextField:
                id: password2_input
                hint_text: "Contraseña"
                size_hint_x: None
                width: "150dp"
                password: True
    
    MDRectangleFlatButton:
        text: '   Registrarse   '
        pos_hint: {'center_x':0.5, 'center_y':0.1}
        on_press: root.manager.current = 'principal'
    MDIconButton:
        icon:'arrow-left-thick'
        pos_hint: {'center_x':0.1, 'center_y':0.943}
        on_press: root.manager.current = 'inicio'


<Principal>:
    name: 'principal'                             
    
    MDBoxLayout:
        orientation: "vertical"

        MDTopAppBar:
            title: "SmartiPill"
            left_action_items: [["menu", lambda x: app.navigation_draw()]]
        MDLabel:
            text: ""
                        
    MDIconButton:
        icon:'arrow-left-thick'
        pos_hint: {'center_x':0.1, 'center_y':0.1}
        on_press: root.manager.current = 'inicio'
                  
    MDFloatingActionButton:
        icon:'account-plus'
        pos_hint: {'center_x':0.33, 'center_y':0.75}
        user_font_size: '72sp'
        on_press: root.manager.current = 'agregar'
        size_hint: .15, .085
    MDFloatingActionButton:
        icon:'account-plus'
        pos_hint: {'center_x':0.33, 'center_y':0.35}
        user_font_size: '72sp'
        on_press: root.manager.current = 'agregar'
        size_hint: .15, .085
    MDFloatingActionButton:
        icon:'account-plus'
        pos_hint: {'center_x':0.33, 'center_y':0.55}
        font_size: '48sp'
        on_press: root.manager.current = 'agregar'
        size_hint: .15, .085
    MDFloatingActionButton:
        icon:'account-plus'
        pos_hint: {'center_x':0.67, 'center_y':0.35}
        font_size: '48sp'
        on_press: root.manager.current = 'agregar'
        size_hint: .15, .085
    MDFloatingActionButton:
        icon:'account-plus'
        pos_hint: {'center_x':0.67, 'center_y':0.75}
        font_size: '48sp'
        on_press: root.manager.current = 'agregar'
        size_hint: .15, .085
    MDFloatingActionButton:
        icon:'account-plus'
        pos_hint: {'center_x':0.67, 'center_y':0.55}
        font_size: '48sp'
        on_press: root.manager.current = 'agregar'
        size_hint: .15, .085
    MDFloatingActionButton:
        icon:'plus'
        pos_hint: {'center_x':0.5, 'center_y':0.15}
        on_press: root.manager.current = 'inicio'
        size_hint: .09, .05    


<Agregar>:
    name:'agregar'            
    MDBoxLayout:
        orientation: "vertical"

        MDTopAppBar:
            title: "    Nuevo Paciente"
            left_action_items: [["arrow-left-thick", lambda x: app.navigation_draw()]]
            
        MDLabel:
            text: ""
    MDFloatLayout:
            
        MDBoxLayout:
            orientation: 'vertical'
            size_hint: None, None
            pos_hint: {'center_x': 0.32, 'center_y': 0.3}
            spacing: '15dp'
            
            
            MDTextField:
                id: username_input
                hint_text: "CI"
                size_hint_x: None
                width: "200dp"
                
            MDTextField:
                id: password_input
                hint_text: "Nombre"
                size_hint_x: None
                width: "200dp"
                
            MDTextField:
                id: password_input
                hint_text: "Apellido"
                size_hint_x: None
                width: "200dp"
                
            MDTextField:
                id: password_input
                hint_text: "Edad"
                size_hint_x: None
                width: "200dp"
                
    MDRectangleFlatButton:
        text: '   Siguiente   '
        pos_hint: {'center_x':0.5, 'center_y':0.1}                       
        on_press: root.manager.current = 'receta'

        
<Receta>:
    name: 'receta'        
        
    MDBoxLayout:
        orientation: "vertical"

        MDTopAppBar:
            title: "    Medicamento"
            left_action_items: [["arrow-left-thick", lambda x: app.navigation_draw()]]
            
        MDLabel:
            text: ""
    MDFloatLayout:
            
        MDBoxLayout:
            orientation: 'vertical'
            size_hint: None, None
            pos_hint: {'center_x': 0.32, 'center_y': 0.23}
            spacing: '15dp'
            
            
            MDTextField:
                id: username_input
                hint_text: "Medicamento"
                size_hint_x: None
                width: "200dp"
                
            MDTextField:
                id: password_input
                hint_text: "Dosis"
                size_hint_x: None
                width: "200dp"
                
            MDTextField:
                id: password_input
                hint_text: "Fecha"
                size_hint_x: None
                width: "200dp"
                
            MDTextField:
                id: password_input
                hint_text: "Hora"
                size_hint_x: None
                width: "200dp"
                
            MDTextField:
                id: password_input
                hint_text: "Frecuencia"
                size_hint_x: None
                width: "200dp"
                
    
    MDRectangleFlatButton:
        text: '   Agregar   '
        pos_hint: {'center_x':0.5, 'center_y':0.1}                       
        on_press: root.manager.current = 'principal'    

        
        
"""

class Inicio(Screen):
    pass


class Login(Screen):
    pass


class Registro(Screen):
    pass

class Principal(Screen):
    pass

class Agregar(Screen):
    pass

class Receta(Screen):
    pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(Inicio(name='inicio'))
sm.add_widget(Login(name='logeo'))
sm.add_widget(Registro(name='registro'))
sm.add_widget(Principal(name ='principal'))
sm.add_widget(Agregar(name ='agregar'))
sm.add_widget(Receta(name ='receta'))

class SmartPill(MDApp):
        
    def build(self):
        
        
        self.theme_cls.primary_palette = "Cyan"
        screen = Builder.load_string(screen_helper)
        return screen
        
SmartPill().run()