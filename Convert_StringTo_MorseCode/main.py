from text_base_programm import TextBase

def main():

    message = input("Enter text: ")
    converter_obj = TextBase()
    morse = converter_obj.to_morse(message)
    print(f"Morse Code: {morse}")
    
if __name__ == '__main__':
    main()