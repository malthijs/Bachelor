// GLOBALE VARIABELEN
const options = {
    "T": [0, 1, 2, 4, 7],
    "H": [0, 2, 3, 4, 5, 6, 8],
    "Y": [0, 2, 4, 7],
    "L": [0, 3, 6, 7, 8],
    "A": [1, 3, 4, 5, 6, 8],
    "K": [0, 2, 3, 4, 6, 8],
    "O": [0, 1, 2, 3, 5, 6, 7, 8],
    "I": [0, 1, 2, 4, 6, 7, 8],
    "D": [0, 1, 3, 5, 6, 7]
}
let code_answers = []
let index = -1
let letters = ""
let letter = letters[index]
let clicked = []


// FUNCTIES
function code_generator(code) {
    for (const i of code) { // GENERATE CODE
        code_answers.push([i, options[i]])
        letters += i
    }
}

function match() {
    if (index === letters.length - 1) {
        location.href='/phase_2.html'
        return
    }
    index++
    letter = letters[index]
}

function image(id) {
    let button = document.getElementById(id)
    button.innerHTML = "<img src='../static/skins/endgame/player_1.png' alt=''>"
    button.disabled = true
}

function fire(sound_switch) {
    const audio = new Audio()
    audio.src = '../static/sounds/fire.mp3'
    if (sound_switch === 'on') {
        audio.play().then()
    }
}

function check(sound_switch, id) {
    if (options[letter].includes(id)) { // MATCH
        clicked.push(id)
        if (clicked.length === options[letter].length) {
            match()
            ping(sound_switch)
            for (const id of clicked) {
                document.getElementById(id).innerHTML = ""
                document.getElementById(id).disabled = false
            }
            clicked = []
        }
    }
    else {
        location.href='/?conclusion=lose' // NO MATCH
    }
}

function ping(sound_switch) {
    const audio = new Audio()
    audio.src = '../static/sounds/ping.mp3'
    if (sound_switch === 'on') {
        audio.play().then()
    }
}
