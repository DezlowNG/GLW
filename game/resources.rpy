init offset = -1

## Begin /CHARACTERS/
define girl = Character('Девочка', color="#e5003d")
define guide = Character('Проводник', color="#e5003d")
define bantik = Character('Бантик', color="#e5003d")
define boy = Character('Парень', color="#e5003d")
define feloni = Character('Фэлони', color="#e5003d")
define nocturne = Character('Ноктюрн', color="#e5003d")
## End /CHARACTERS/

## Begin /SPRITES/FELONI/
image feloni 1 = "images/sprites/feloni/1.1.png"
image feloni 2 = "images/sprites/feloni/1.2.png"
image feloni 3 = "images/sprites/feloni/1.3.png"
image feloni 4 = "images/sprites/feloni/1.4.png"
image feloni 5 = "images/sprites/feloni/1.5.png"
image feloni 6 = "images/sprites/feloni/1.6.png"
image feloni 7 = "images/sprites/feloni/1.7.png"
image feloni 8 = "images/sprites/feloni/1.8.png"
image feloni 9 = "images/sprites/feloni/1.9.png"
image feloni 10 = "images/sprites/feloni/1.10.png"
image feloni 11 = "images/sprites/feloni/1.11.png"
image feloni 12 = "images/sprites/feloni/1.12.png"
## End /SPRITES/FELONI/

## Begin /SPRITES/BANTIK/
image bantik 1 = "images/sprites/bantik/2_1.png"
## End /SPRITES/BANTIK/

## Begin /SPRITES/FEL/
image fel 1 = "images/sprites/fel/3.1.png"
image fel 2 = "images/sprites/fel/3.2.png"
image fel 3 = "images/sprites/fel/3.3.png"
image fel 4 = "images/sprites/fel/3.4.png"
## End /SPRITES/FEL/

## Begin /BGS/
image bg 0 = "images/bgs/background0.png"
image bg 1 = "images/bgs/background1.png"
image bg 2 = "images/bgs/background2.png"
image bg 3 = "images/bgs/background3.png"
image bg 4 = "images/bgs/background4.png"
image bg 5 = "images/bgs/background5.png"
image bg 6 = "images/bgs/background6.png"
image bg 7 = "images/bgs/background7.png"
image bg 8 = "images/bgs/background8.png"
image bg 9 = "images/bgs/background9.png"
image bg 10 = "images/bgs/background10.png"
image bg 12 = "images/bgs/background12.png"

image white = "#ffff"
## End /BGS/

## Begin /CGS/
image cg 1 = "images/cgs/CG1.png"
image cg 2 = "images/cgs/CG2.png"
image cg 3 = "images/cgs/CG3.png"
image cg 4 = "images/cgs/CG4.png"
image cg 5 = "images/cgs/CG5.png"
image cg 6 = "images/cgs/CG6.png"
image cg 7 = "images/cgs/CG7.png"
## End /CGS/

## Begin /AUDIO/MUSIC/
define audio.welcome_to_the_hell = "audio/music/welcome_to_the_hell.ogg"
define audio.mioki_jam = "audio/music/mioki_jam.ogg"
define audio.russian_severity = "audio/music/russian_severity.ogg"
define audio.zetsubo = "audio/music/zetsubo.ogg"
define audio.help_me = "audio/music/help_me.ogg"
define audio.quiet_river = "audio/music/quiet_river.ogg"
define audio.ending = "audio/music/ending.mp3"
## End /AUDIO/MUSIC/

## Begin /AUDIO/SFX/
define audio.horror_glitch = "audio/sfx/horror_01_drone_glitch_01.ogg"
## End /AUDIO/SFX/

## Begin /OTHER/TRANSITIONS/
define dspr = Dissolve(0.2)
define flash = Fade(.25, 0, .75, color="#fff")
## Begin /OTHER/TRANSITIONS/

## Begin /OTHER/VARS
define score = 0
define choices = set()
## Begin /OTHER/VARS

## Begin /OTHER/PERSIST
define persistent.disclaimer = True
## End /OTHER/PERSIST