from pyfiglet import Figlet
figlet = Figlet()
import random

def get_user_font():
    fonts = Figlet().getFonts()
    while True:
        user_input = input(f"Ingrese el nombre de una fuente ({', '.join(fonts)}) o presione Enter para seleccionar una al azar: ")
        if user_input == "":
            return random.choice(fonts)
        elif user_input in fonts:
            return user_input
        else:
            print("Fuente no válida. Intente de nuevo.")

def get_user_text():
    return input("Ingrese el texto que desea convertir: ")

def main():
    font_name = get_user_font()
    figlet = Figlet(font=font_name)
    text = get_user_text()
    rendered_text = figlet.renderText(text)
    print(rendered_text)

if __name__ == "__main__":
    main()