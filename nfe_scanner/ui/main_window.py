import PySimpleGUI as sg


def create_main_window():
    """
    Define o layout da janela principal com as opções de entrada.
    """

    # Tema da interface
    sg.theme("LightBlue3")

    # Layout da janela
    layout = [
        [
            sg.Text(
                "NFe Scanner",
                size=(30, 1),
                font=("Helvetica", 25),
                justification="center",
            )
        ],
        [sg.HSeparator()],
        [
            sg.Text(
                "Escolha o método de entrada da Nota Fiscal Eletrônica (NF-e):",
                font=("Helvetica", 12),
            )
        ],
        [
            sg.Radio(
                "Chave de Acesso (44 dígitos)",
                "RADIO1",
                default=True,
                key="-RADIO_CHAVE-",
                font=("Helvetica", 11),
            )
        ],
        [
            sg.Radio(
                "Leitura de QR Code",
                "RADIO1",
                key="-RADIO_QRCODE-",
                font=("Helvetica", 11),
            )
        ],
        [sg.HSeparator()],
        [
            sg.Button("Iniciar Captura", key="-BUTTON_INICIAR-", size=(15, 1)),
            sg.Button("Sair", key="-BUTTON_SAIR-", size=(15, 1)),
        ],
    ]

    return sg.Window(
        "NFe Scanner - Início", layout, finalize=True, element_justification="center"
    )


def run_main_window():
    """
    Executa o loop principal da janela.
    """
    window = create_main_window()

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == "-BUTTON_SAIR-":
            break

        if event == "-BUTTON_INICIAR-":
            if values["-RADIO_CHAVE-"]:
                sg.popup("Opção Escolhida", "Você escolheu: Chave de Acesso")
                # Futuramente: chamar a tela de entrada de chave
            elif values["-RADIO_QRCODE-"]:
                sg.popup("Opção Escolhida", "Você escolheu: Leitura de QR Code")
                # Futuramente: chamar a tela de leitura de QR Code

    window.close()


if __name__ == "__main__":
    run_main_window()
