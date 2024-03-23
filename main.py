import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGridLayout(GridLayout):
    #  Initialize infinite keywords
    def __init__(self, **kwargs):
        #  Call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)

        #  Set Columns
        self.cols = 1

        #  Create a second gridlayout
        self.top_grid = GridLayout(
            row_force_default=True,
            col_force_default=True,
            row_default_height=50,
            col_default_width=400
        )
        self.top_grid.cols = 2
        self.row_force_default = True
        self.row_default_height = 110
        self.col_force_default = True
        self.col_default_width = 400

        #  Add Widgets
        self.top_grid.add_widget(Label(text="Name: "))
        # Add Input Box
        self.name = TextInput(
            # multiline=False,
            # size_hint_y=None,  # has to be explicitly be stated
            # height=50,
            # size_hint_x=None,
            # width=400
        )
        self.top_grid.add_widget(self.name)

        #  Add Widgets
        self.top_grid.add_widget(Label(text="Pizza: "))
        # Add Input Box
        self.pizza = TextInput(multiline=False)
        self.top_grid.add_widget(self.pizza)

        #  Add new top_grid to new app
        self.add_widget(self.top_grid)

        #  Create a submit button
        self.submit = Button(
            text="Submit",
            size_hint_y=None,  # has to be explicitly be stated
            height=50,
            size_hint_x=None,
            width=200
        )

        #  Bind button for it to work
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, instance):
        name = self.name.text
        pizza = self.pizza.text

        # print(f'Hello {name} you like {pizza} pizza.')
        # Print to screen
        self.add_widget(Label(text=f'Hello {name} you like {pizza} pizza.'))

        # Clear input boxes
        self.name.text = ''
        self.pizza.text = ''


class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    MyApp().run()
