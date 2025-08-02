"""
Projectnaam: TicTacToe

Auteur: Matthijs de Vries

Einddatum: 01-juli-2024

Versienummer: 2
"""
from flask import (Flask, render_template, request,
                   session, redirect, url_for)
from os import urandom, path

app = Flask(__name__)
app.secret_key = urandom(24)


@app.route('/')
def menu():
    """Functie beschrijving:
    Genereert een code dat nodig is om tegen de baas te spelen. Als
    zeven leraren verslagen zijn, dan wordt er een tekstbestand in
    de TicTacToe directory aangemaakt. In deze tekstbestand zit de
    code verwerkt dat ontcijferd zal moeten worden (_secret.txt).

    :return: HTML-template van Menu
    """
    # VOORDAT EEN GAME GESPEELD IS
    defeated_teachers = session.setdefault('defeated_teachers', [])
    message = 'Is love a tender thing?'.lower()
    secret_message, code = '', ''

    for letter in message:
        if letter in 'thylakoid':
            secret_message += letter.upper()
            code += letter.upper()
        else:
            secret_message += letter.lower()
    session['code'] = code

    # NADAT EEN GAME GESPEELD IS
    mode = session.get('mode')
    result = request.args.get('result')
    boss = session.get('boss')
    if (mode == 'map' and result == 'win'
            and boss not in defeated_teachers):
        defeated_teachers.append(boss)
        session.modified = True

    if len(defeated_teachers) == 7:
        with open(path.join(app.root_path, '_secret.txt'),
                  'w') as file:
            file.write(secret_message)
    return render_template('menu.html')


@app.route('/guide.html')
def guide():
    """Functie beschrijving:
    Standaard wordt de gebruiker veel plezier gewenst. Als zeven
    leraren verslagen zijn, dan verschijnt er tekst dat de gebruiker
    erop attendeert dat een tekstbestand in zijn TicTacToe directory
    aangemaakt is. Als de gebruiker de baas verslagen heeft, dan
    feliciteert de tekst de gebruiker.

    :return: HTML-template van Guide
    """
    player_1 = session.get('player_1', '')
    player_2 = session.get('player_2', '')
    defeated_teachers = len(session['defeated_teachers'])
    return render_template('guide.html',
                           player_1=player_1,
                           player_2=player_2,
                           defeated_teachers=defeated_teachers)


@app.route('/settings.html')
def settings():
    """Functie beschrijving:
    Als de gebruiker het formulier ingediend heeft, dan hoeven de
    namen niet opnieuw ingevuld te worden.

    :return: HTML-template van Settings
    """
    player_1 = session.get('player_1', '')
    player_2 = session.get('player_2', '')
    return render_template('settings.html',
                           player_1=player_1,
                           player_2=player_2)


@app.route('/gamemodes.html')
def gamemodes():
    """Functie beschrijving:
    Toont drie gamemodes: BOT, PVP of MAP.

    :return: HTML-template van Gamemodes
    """
    return render_template('gamemodes.html')


@app.route('/difficulty.html')
def difficulty():
    """Functie beschrijving:
    Toont twee difficulties: EASY en HARD.

    EASY is gebaseerd op een random algoritme dat een willekeurige
    positie kiest.
    HARD is gebaseerd op een minimax algoritme dat ervan uitgaat
    dat de gebruiker optimaal speelt.

    :return: HTML-template van Difficulty
    """
    return render_template('difficulty.html')


@app.route('/map.html')
def map():
    """Functie beschrijving:
    Toont een map met 8 leraren die verslaan moeten worden om het
    spel uit te kunnen spelen.

    :return: HTML-template van Map
    """
    music_switch = session.get('music_switch', 'on')
    return render_template('map.html',
                           music_switch=music_switch)


@app.route('/game.html', methods=['GET', 'POST'])
def game():
    """Functie beschrijving:
    Houdt bij of de gebruiker een formulier wel/niet heeft ingevuld.
    Daarnaast kijkt het welke opties de gebruiker gekozen heeft:
    gamemode, leraar, bot, e.t.c.

    :return: HTML-template van Game
    """
    session['mode'] = request.args.get('mode')
    session['boss'] = request.args.get('boss')
    session['bot'] = request.args.get('bot')

    mode = session.get('mode')
    boss = session.get('boss')
    bot = session.get('bot')

    # SUBMIT
    if request.method == 'POST':
        session['player_1'] = request.form.get('player_1')
        session['player_2'] = request.form.get('player_2')
        session['background'] = request.form.get('background')
        session['skin'] = request.form.get('skin')
        session['music'] = request.form.get('music')
        session['music_switch'] = request.form.get('music_switch')
        session['sound'] = request.form.get('sound')
        session['sound_switch'] = request.form.get('sound_switch')
        return redirect(url_for('menu'))

    # NO SUBMIT
    player_1 = session.get('player_1', '')
    player_2 = session.get('player_2', '')
    background = session.get('background', 'background_1.png')
    skin = session.get('skin', 'skin_1')
    music = session.get('music', 'music_1.mp3')
    music_switch = session.get('music_switch', 'on')
    sound = session.get('sound', 'sound_1.mp3')
    sound_switch = session.get('sound_switch', 'on')
    return render_template('game.html',
                           player_1=player_1,
                           player_2=player_2,
                           background=background,
                           skin=skin,
                           music=music,
                           music_switch=music_switch,
                           sound=sound,
                           sound_switch=sound_switch,
                           mode=mode,
                           boss=boss,
                           bot=bot)


@app.route('/phase_1.html')
def phase_1():
    """Functie beschrijving:
    Hier moet de code ingevoerd worden.

    :return: HTML-template van Phase 1
    """
    code = session.get('code')
    music_switch = session.get('music_switch', 'on')
    sound_switch = session.get('sound_switch', 'on')
    return render_template('phase_1.html',
                           code=code,
                           music_switch=music_switch,
                           sound_switch=sound_switch)


@app.route('/phase_2.html')
def phase_2():
    """Functie beschrijving:
    De gebruiker gaat nu tegen de baas spelen. Helaas heeft de baas
    verschillende trucjes dat de gebruiker in de weg zal gaan
    zitten.

    1. De baas heeft 7 levens.
    2. De baas plaatst na elk spel een obstakel dat daarna
    verplaatst zal gaan worden. Hierdoor zal de gebruiker gehinderd
    worden.
    3. De invoervakken zijn gespiegeld. Hierdoor zal de gebruiker in
    de war raken.

    :return: HTML-template van Phase 2
    """
    music_switch = session.get('music_switch', 'on')
    sound_switch = session.get('sound_switch', 'on')
    return render_template('phase_2.html',
                           music_switch=music_switch,
                           sound_switch=sound_switch)


@app.route('/credits.html')
def credits():
    """Functie beschrijving:
    Hierin staan alle referenties.

    :return: HTML-template van Credits
    """
    # indien het spel uitgespeeld is
    defeated_teachers = session['defeated_teachers']
    if 'André' not in defeated_teachers:
        defeated_teachers.append('André')
        session.modified = True

    music_switch = session.get('music_switch', 'on')
    return render_template('credits.html',
                           music_switch=music_switch)


if __name__ == '__main__':
    app.run()
