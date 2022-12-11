def start_template(w):
        t = []
        for l in w:
                t.append('_')
        return t

def get_word(w):
        """
        inpute: w - list with string (words)
        output: for now: first element in list as string
                TODO: random string from list
        """
        return w[0]

def welcome_speech(t):
        print(f'''добро пожаловать ваше состоит из {len(t)} букв {t}''')

def list_to_string_convert(t):
        s = ''
        return s.join(t)

def user_input():
        return input('введите букву: ')

def build_template(t, w, g= ''):
        for i in range(len(w)):
              if w[i] == g:
                        t[t] = g
        return t

def check_win(g):
        for l in g:
                if l == '_':
                        return True
        return False

def check_mistake(w,g):
        for i in w:
                if i == g:
                        return False
        return True

def game():
        progress = True
        word = ['orange']
        lifes = 3

        word_in_game = get_word(word)
        template = start_template(word_in_game)
        welcome_speech(list_to_string_convert(template))

        while progress:
                user_quess = user_input()
                template = build_template(template, word_in_game, user_quess)
                quessed = list_to_string_convert(template)
                print(f'результат: {quessed}')
                progress = check_win(quessed)

                if not check_mistake(word_in_game, user_quess):
                        print(f'Осталось {lifes} попитки')
                        lifes -= 1
                
                if lifes == 0:
                        print('вы проиграли')
                        break

                if not progress:
                        print('вы выиграли')

game()
