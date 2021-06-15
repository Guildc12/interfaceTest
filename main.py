import PySimpleGUI as sg


class Geo:
    # construtor e defaults
    def __init__(self):
        self.eventn = list()
        self.arraydeteste = [['Valor1'], ['Valor2'],['Valor3'],['Valor4'],['Valor5'],['Valor6'],['Valor7'],['Valor8']
                             ,['Valor9']]
        sg.theme('reddit')
        # layout
        self.layout = [
            [sg.Button('HID', key='hid'), sg.Listbox(values=[f'a',f'b',f'c'], size=(45, 12), key='listaa', enable_events=True)],
            [sg.Button('SAN', key='san')],
            [sg.Button('ENE', key='ene'), sg.Output(size=(40,20))]
        ]
        # janela
        self.window = sg.Window('Geog').layout(self.layout)
        self.iniciar()

    # front-end
    def iniciar(self):
        while True:
            self.eventos, self.valores = self.window.read()
            if self.eventos in (sg.WIN_CLOSED, 'Exit'):
                break


# !+!+!++!+!+!++!+!+!++!+!+!+!++!+!+!++!!++!+!+!+!+!++!+!+!+!+!++!+!+!+!++!+!+!+!+!+!++!+!+!++!
# !+!+!++!+!+!++!+!+!++!+!+!+!++!+!+!++!!++!+!+!+!+!++!+!+!+!+!++!+!+!+!++!+!+!+!+!+!++!+!+!++!
# Substituir código abaixo por dados tratados em outra funcao dentro da propria classe nossos ifs a seguir
# Isso é só um teste
# !+!+!++!+!+!++!+!+!++!+!+!+!++!+!+!++!!++!+!+!+!+!++!+!+!+!+!++!+!+!+!++!+!+!+!+!+!++!+!+!++!
# !+!+!++!+!+!++!+!+!++!+!+!+!++!+!+!++!!++!+!+!+!+!++!+!+!+!+!++!+!+!+!++!+!+!+!+!+!++!+!+!++!




            self.eventn.append(self.eventos)

            if 'hid' in self.eventn:
                if 'listaa' in self.eventn:
                    if self.valores['listaa'][0] == "a":
                        print(self.arraydeteste[0][0])
                        self.eventn = list()
                    if self.valores['listaa'][0] == "b":
                        print(self.arraydeteste[1][0])
                        self.eventn = list()
                    if self.valores['listaa'][0] == "c":
                        print(self.arraydeteste[2][0])
                        self.eventn = list()

            if 'san' in self.eventn:
                if 'listaa' in self.eventn:
                    if self.valores['listaa'][0] == "a":
                        print(self.arraydeteste[3][0])
                        self.eventn = list()
                    if self.valores['listaa'][0] == "b":
                        print(self.arraydeteste[4][0])
                        self.eventn = list()
                    if self.valores['listaa'][0] == "c":
                        print(self.arraydeteste[5][0])
                        self.eventn = list()

            if 'ene' in self.eventn:
                if 'listaa' in self.eventn:
                    if self.valores['listaa'][0] == "a":
                        print(self.arraydeteste[6][0])
                        self.eventn = list()
                    if self.valores['listaa'][0] == "b":
                        print(self.arraydeteste[7][0])
                        self.eventn = list()
                    if self.valores['listaa'][0] == "c":
                        print(self.arraydeteste[8][0])
                        self.eventn = list()

geografia = Geo()