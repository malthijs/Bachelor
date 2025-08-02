// GLOBALE VARIABELEN
let turn = 1
let grid = [-1, -1, -1, -1, -1, -1, -1, -1, -1]


// FUNCTIES
function image(skin, id, modifier) {
    let button = document.getElementById(id)
    if (modifier === 0) { // SAID
        turn++
        return
    }
    if (modifier === 2) { // SUZAN, JACOB en JEROEN
        button.innerHTML = `<img src='../static/skins/${skin}/player_2.png' alt='skin van tegenstander'>`
        grid[id] = 0
        turn += 0.5
        button.disabled = true
        return
    }
    if (turn % 2 === 1) { // SPELER 1
        button.innerHTML = `<img src='../static/skins/${skin}/player_1.png' alt='skin van speler'>`
        grid[id] = 1
    }
    else { // SPELER 2, BOT, BO, JAN en TOM
        button.innerHTML = `<img src='../static/skins/${skin}/player_2.png' alt='skin van tegenstander'>`
        grid[id] = 0
    }
    turn++
    button.disabled = true
}

function audio(sound, sound_switch) {
    const audio = new Audio()
    audio.src = `../static/sounds/${sound}`
    if (sound_switch === 'on') {
        audio.play().then()
    }
}

function check() {
    const combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for (const combo of combinations) {
        if ((grid[combo[0]] === 1) && (grid[combo[1]] === 1) && (grid[combo[2]] === 1)) {  // WIN PLAYER 1
            location.href='/?result=win'
            return
        }
        if ((grid[combo[0]] === 0) && (grid[combo[1]] === 0) && (grid[combo[2]] === 0)) {  // LOSE PLAYER 1
            location.href='/?result=lose'
            return
        }
    }
    if (!grid.includes(-1)) {  // DRAW
        location.href='/?result=draw'
    }
}

function bot(bot, skin, sound, sound_switch) {
    if (bot === 'easy') {
        image(skin, random())
        audio(sound, sound_switch)
        check()

    }
    if (bot === 'hard') {
        image(skin, minimaxMove())
        audio(sound, sound_switch)
        check()
    }
}

function random() {
    const options = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    let option, button

    do {
        option = options[Math.floor(Math.random() * options.length)]
        button = document.getElementById(option)
    } while (button.disabled)
    return option
}

function minimaxEvaluate() {
    const combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for (const combo of combinations) {
        if ((grid[combo[0]] === 1) && (grid[combo[1]] === 1) && (grid[combo[2]] === 1)) {  // LOSE AI
            return -10
        }
        if ((grid[combo[0]] === 0) && (grid[combo[1]] === 0) && (grid[combo[2]] === 0)) {  // WIN AI
            return 10
        }
    }
    if (!grid.includes(-1)) {  // DRAW
        return 0
    }
    return null
}

function minimax(depth, isMaximizing) {
    let score = minimaxEvaluate()
    if (score !== null) {
        return score
    }

    if (isMaximizing) {
        let maxBest = -Infinity
        let maxIndex = 0
        for (let i of grid) {  // AI
            if (i === -1) {
                grid[maxIndex] = 0
                maxBest = Math.max(maxBest, minimax(depth + 1, false)*0.99)
                grid[maxIndex] = -1
            }
            maxIndex++
        }
        return maxBest
    } else {  // PLAYER
        let minBest = Infinity
        let minIndex = 0
        for (let i of grid) {
            if (i === -1) {
                grid[minIndex] = 1
                minBest = Math.min(minBest, minimax(depth + 1, true)*0.99)
                grid[minIndex] = -1
            }
            minIndex++
        }
        return minBest
    }
}

function minimaxMove() {
    let optimalVal = -Infinity
    let optimalIndex = null
    let index = 0
    for (let i of grid) {
        if (i === -1) {
            grid[index] = 0
            let newVal = minimax(0, false)
            grid[index] = -1
            if (newVal > optimalVal) { // MOVE
                optimalVal = newVal
                optimalIndex = index
            }
        }
        index++
    }
    return optimalIndex
}


function said(skin) {
    image(skin, random(), 0)
}

function bo(skin, sound, sound_switch) {
    image(skin, random())
    audio(sound, sound_switch)
    check()

}

function jan(skin, sound, sound_switch) {
    const move = 4
    const button = document.getElementById(move.toString())
    grid[move] = Infinity
    button.disabled = true

    image(skin, random())
    audio(sound, sound_switch)
    check()
}

function tom(skin, sound, sound_switch) {
    const moves = [0, 2, 6, 8]
    for (const move of moves) {
        const button = document.getElementById(move.toString())
        grid[move] = Infinity
        button.disabled = true
    }

    image(skin, random())
    audio(sound, sound_switch)
    check()
}

function suzan(skin, sound, sound_switch) {
    let i = 2
    while (i--) {
        image(skin, random(), 2)
        audio(sound, sound_switch)
        check()
    }
}

function jacob(skin, sound, sound_switch) {
    let i = 2
    while (i--) {
        image(skin, random(), 2)
        audio(sound, sound_switch)
        check()
    }
}

function jeroen(skin, sound, sound_switch) {
    let i = 2
    while (i--) {
        image(skin, random(), 2)
        audio(sound, sound_switch)
        check()
    }
}
