# app.py
# Gerador de Senhas
# Direitos autorais © 2024 Richardson Almeida com auxílio do ChatGPT

from flask import Flask, render_template, request, redirect, url_for, make_response
import random
import string

app = Flask(__name__)

# Dicionário de traduções para suportar múltiplos idiomas
translations = {
    'en': {
        'title': 'Password Generator',
        'welcome': 'Welcome to your secure password generator system. Keep your passwords safe and organized.',
        'get_started': 'Get Started',
        'generate_password': 'Generate Password',
        'password_length': 'Password Length',
        'include_special': 'Include Special Characters',
        'include_numbers': 'Include Numbers',
        'password_generated': 'Generated Password:',
        'copy_password': 'Copy Password',
        'change_theme': 'Change Theme',
        'clear': 'Clear',
        'password_copied': 'Password Copied'
    },
    'pt': {
        'title': 'Gerador de Senhas',
        'welcome': 'Bem-vindo ao seu sistema seguro de geração de senhas. Mantenha suas senhas seguras e organizadas.',
        'get_started': 'Começar',
        'generate_password': 'Gerar Senha',
        'password_length': 'Comprimento da Senha',
        'include_special': 'Incluir Caracteres Especiais',
        'include_numbers': 'Incluir Números',
        'password_generated': 'Senha Gerada:',
        'copy_password': 'Copiar Senha',
        'change_theme': 'Mudar Tema',
        'clear': 'Limpar',
        'password_copied': 'Senha Copiada'
    },
    'es': {
        'title': 'Generador de Contraseñas',
        'welcome': 'Bienvenido a su sistema seguro de generación de contraseñas. Mantén tus contraseñas seguras y organizadas.',
        'get_started': 'Empezar',
        'generate_password': 'Generar Contraseña',
        'password_length': 'Longitud de la Contraseña',
        'include_special': 'Incluir Caracteres Especiales',
        'include_numbers': 'Incluir Números',
        'password_generated': 'Contraseña Generada:',
        'copy_password': 'Copiar Contraseña',
        'change_theme': 'Cambiar Tema',
        'clear': 'Limpiar',
        'password_copied': 'Contraseña Copiada'
    }
}

# Função para gerar a senha
def generate_password(length, include_special, include_numbers):
    characters = string.ascii_letters
    if include_special:
        characters += string.punctuation
    if include_numbers:
        characters += string.digits
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Rota principal que exibe a página inicial
@app.route('/', methods=['GET', 'POST'])
@app.route('/<lang>', methods=['GET', 'POST'])
def index(lang='en'):
    if lang not in translations:
        lang = 'en'
    
    theme = request.cookies.get('theme', 'mystery')
    
    password = None
    if request.method == 'POST':
        length = int(request.form['length'])
        include_special = 'include_special' in request.form
        include_numbers = 'include_numbers' in request.form
        password = generate_password(length, include_special, include_numbers)
    
    return render_template('index.html', lang=lang, translations=translations[lang], password=password, theme=theme)

# Rota para mudar o tema da aplicação
@app.route('/change_theme/<theme>')
def change_theme(theme):
    resp = make_response(redirect(url_for('index')))
    resp.set_cookie('theme', theme)
    return resp

if __name__ == '__main__':
    app.run(debug=True)
