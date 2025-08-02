// GLOBALE VARIABELEN
const options = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
const reversed = ['8', '7', '6', '5', '4', '3', '2', '1', '0']
let grid = [-1, -1, -1, -1, -1, -1, -1, -1, -1]
let count = 0
let turn = 1
let obstructed = false
let previous_obstruct = null


// FUNCTIES
function image(id) {
    let button = document.getElementById(reversed[id])
    if (turn % 2 === 1) {
        button.innerHTML = "<img src='../static/skins/endgame/player_1.png' alt=''>"
        grid[id] = 1
    }
    else {
        button.innerHTML = "<img src='../static/skins/endgame/player_2.png' alt=''>"
        grid[id] = 0
    }
    turn++
    document.getElementById(id).disabled = true
}

function fire(sound_switch) {
    const audio = new Audio()
    audio.src = '../static/sounds/fire.mp3'
    if (sound_switch === 'on') {
        audio.play().then()
    }
}

function check(sound_switch) {
    const combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for (const combo of combinations) {
        if (grid[combo[0]] === 1 && grid[combo[1]] === 1 && grid[combo[2]] === 1) {  // WIN
            ping(sound_switch)
            reset()
            count++
            if (count === 7) {
                location.href='/credits.html'
            }
            return
        }
        if (grid[combo[0]] === 0 && grid[combo[1]] === 0 && grid[combo[2]] === 0) {  // LOSE
            location.href='/?conclusion=lose'
            return
        }
    }
    if (!grid.includes(-1)) {  // DRAW
        reset()
    }
}

function ping(sound_switch) {
    const audio = new Audio()
    audio.src = '../static/sounds/ping.mp3'
    if (sound_switch === 'on') {
        audio.play().then()
    }
}

function reset() {
    for (const id of options) {
        document.getElementById(id).innerHTML = ""
        document.getElementById(id).disabled = false
        grid[id] = -1
    }
}

function andre(sound_switch) {
    obstruct()
    image(random())
    fire(sound_switch)
    check()
}

function obstruct() {
     // REMOVE OBSTACLE IF PRESENT
    if (obstructed) {
        document.getElementById(reversed[previous_obstruct]).innerHTML = "<img src='' alt=''>"
        document.getElementById(previous_obstruct).disabled = false
        grid[previous_obstruct] = -1
        obstructed = false
    }
    // CHOOSE OBSTACLE
    let option, button
    do {
        option = options[Math.floor(Math.random() * options.length)]
        button = document.getElementById(option)
    } while (button.disabled)

    // PLACE OBSTACLE
    document.getElementById(reversed[option]).innerHTML = "<img src='../static/backgrounds/death.png' alt=''>"
    document.getElementById(option).disabled = true
    grid[option] = Infinity
    obstructed = true
    previous_obstruct = option
}

function random() {
    let option, button
    do {
        option = options[Math.floor(Math.random() * options.length)]
        button = document.getElementById(option)
    } while (button.disabled)
    return option
}
