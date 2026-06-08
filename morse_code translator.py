morse= {'._':'a',
         '_...':'b',
        '_._.':'c',
        '_..':'d',
        '.':'e',
        '.._.':'f',
        '__.':'g',
        '....':'h',
         '..':'i',
        '.___':'j',
        '_._':'k',
        '._..':'l',
        '__':'m',
        '_.':'n',
        '___':'o',
        '.__.':'p',
        '__._':'q',
        '._.':'r',
        '...':'s',
        '_':'t',
        '.._':'u',
        '..._':'v',
        '.__':'w',
        '_.._':'x',
        '_.__':'y',
        '__..':'z',
        '.____':'1',
        '..___':'2',
        '...__':'3',
        '...._':'4',
        '.....':'5',
        '_....':'6',
        '__...':'7',
        '___..':'8',
        '____.':'9',
        '_____':'0',
        ' ': ' ',
        '._._._': '.',
        '__.__': ',',
        '..__..': '?',
        '...___...' : 'SOS'
    }


def translate_manager():
    print('Welcome again to one of my projects!')
    print('This time i coded a program for morse code translation.')
    print('Input the characters of the letters (dots and underscores). Press the spacebar to start another word and q to quit')
    results=[]
    text=''
    while True:
        char= input('Enter character. -> ')
        if char == 'q':
            break
        translated='null '
        if char in morse:
            translated=morse[char]
        results.append(translated)
    if results :
        for i in results:
            text+=i
        print(f'Your translated morse code: {text}')


translate_manager()

        
        
