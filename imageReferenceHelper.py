import pyperclip

def main():
    
    t = input('Who is the author(Last name, first inital, second inital): ')
    if t != '':
        author = t
    else:
        author = ''
    t = input('Title of the image: ')
    if t != '':
        title = t + ' '
    else:
        title = ''
    descType = input('Type of image (NEEDED): ')
    t = input('Year created: ')
    if t != '':
        year = f'({t}). '
    else:
        year = ''
    theLink = input('Copy and paste website link (NEEDED): ')
    
    if author != '':
        finalOutput = f'{author}. {year}{title}[{descType}]. Retrieved from {theLink}'
    else:
        finalOutput = f'{title}[{descType}]. {year}Retrieved from {theLink}'
    
    print(finalOutput)
    pyperclip.copy(finalOutput)
    redo = input("Output copied, y to make another reference, n to quit: ")
    if redo == 'y':
        main()
    else:
        print("Bye!")
    
main()