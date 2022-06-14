command = input('Choose a formatter:')
formatters = ('plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'new-line', 'unordered-list', 'ordered-list')
formatted_text = ''
while command != '!done':
    if command == '!help':
        print('''Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line
Special commands: !help !done''')
    elif command not in formatters:
        print('Unknown formatting type or command')
    elif command == 'plain':
        user_text = input('Text:')
        formatted_text += user_text
        print(formatted_text)
    elif command == 'bold':
        user_text = input('Text:')
        formatted_text += f'**{user_text}**'
        print(formatted_text)
    elif command == 'italic':
        user_text = input('Text:')
        formatted_text += f'*{user_text}*'
        print(formatted_text)
    elif command == 'header':
        header_level = int(input('Level:'))
        while not 1 <= header_level <= 6:
            print('The level should be within the range of 1 to 6')
            header_level = int(input('Level:'))
        user_text = input('Text:')
        if len(formatted_text) >= 2:
            if formatted_text[-2:] != '\n':
                formatted_text += f'\n'
        formatted_text += f'{"#" * header_level} {user_text}\n'
        print(formatted_text)
    elif command == 'link':
        user_label = input('Label:')
        user_url = input('URL')
        formatted_text += f'[{user_label}]({user_url})'
        print(formatted_text)
    elif command == 'inline-code':
        user_text = input('Text:')
        formatted_text += f'`{user_text}`'
        print(formatted_text)
    elif command == 'new-line':
        formatted_text += f'\n'
        print(formatted_text)
    elif command == 'unordered-list' or command == 'ordered-list':
        user_rows = int(input('Number of rows:'))
        user_row_input = []
        while user_rows <= 0:
            print('The number of rows should be greater than zero')
            user_rows = int(input('Number of rows:'))
        for i in range(1, user_rows + 1):
            user_row_input.append(input(f'Row #{i}'))
        if len(formatted_text) >= 2:
            if formatted_text[-2:] != '\n':
                formatted_text += f'\n'
        if command == 'ordered-list':
            for n, x in enumerate(user_row_input):
                formatted_text += f'{n + 1}. {x}\n'
        elif command == "unordered-list":
            for x in user_row_input:
                formatted_text += f'* {x}\n'
        print(formatted_text)

    command = input('Choose a formatter:')

with open('output.md', 'w', encoding='utf-8') as file:
    file.write(formatted_text)
