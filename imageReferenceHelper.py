import pyperclip

def main():
    descType = input('Description of image: ')
    theLink = input('Copy and paste website link: ')
    
    finalOutput = f'[{descType}]. Retrieved from {theLink}'
    
    print(finalOutput)
    pyperclip.copy(finalOutput)
    print("Output copied!")
main()