let num = 0
function Show (in_num: number) {
    if (in_num == 0) {
        led.plot(2, 2)
    } else if (in_num == 1) {
        led.unplot(2, 2)
        led.plot(0, 0)
        led.plot(4, 4)
    } else if (in_num == 2) {
        led.plot(2, 2)
    } else if (in_num == 3) {
        led.unplot(2, 2)
        led.plot(4, 0)
        led.plot(0, 4)
    } else if (in_num == 4) {
        led.plot(2, 2)
    } else {
        led.unplot(2, 2)
        led.plot(0, 2)
        led.plot(4, 2)
    }
}
input.onGesture(Gesture.Shake, function () {
    num = randint(0, 5)
    basic.showLeds(`
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        `)
    basic.clearScreen()
    for (let index = 0; index <= 5; index++) {
        Show(index)
        basic.pause(100)
        if (index == num) {
            break;
        }
    }
})
