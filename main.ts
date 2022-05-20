input.onButtonPressed(Button.A, function () {
    radio.sendNumber(6)
})
input.onButtonPressed(Button.B, function () {
    radio.sendNumber(8)
})
radio.setGroup(40)
basic.showIcon(IconNames.Yes)
