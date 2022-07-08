define lf = Character('Larissa Fantina', color="#540b0e")
define k = Character('Kary', color="#335c67")
image Larissa front = ("images/Larissa_front.png")
image Larissa back = ("images/Larissa_back.png")
image Kary front = ("images/Kary_front.png")
image Kary back = ("images/Kary_back.png")

   
label start:
    scene bg sacada

    lf "Kary esta parada a um tempo ali"
    "Devo incomoda-lá?"

menu:

    "A gente precisa sair, é bom chamar ela":
        jump chamar

    "Perguntar o que está fazendo":
        jump perguntar

label chamar:

    lf "Kary??"

    jump marry

label perguntar:

    lf "Kary??"

    jump marry

label marry:

    scene bg janela 
    play music "audio/carro.mp3" fadeout 1 loop
 
    "Kary estava na sacada, parecia estar distraida em seus pensamentos"

    show Larissa front
    with Fade(0.5,0.0,0.5,color="#000")

    lf "O que você tanto olha ai?"

    scene bg sacada
    with None
    show Kary back
    with fade
    stop  music
    
    k "Nada... "
    k "Só gosto de ver a movimentação da rua"

    show Kary front
    with dissolve
   
    "Kary, olha para trás e dá um sorriso convidativo, para Larissa, que não se opõem ao convite"

    scene bg sacada
    play music "audio/carro.mp3" fadeout 1 fadeout 1.0
    show Larissa back at right
    
    show Kary back at left

    "As duas ficam ali na sacada por um tempo, observando a paisagem"
label leaving:

    show Kary front

    k "bem, precisamos sair agora"

    hide Kary
    with dissolve
    "..."

    lf "tudo bem eu te acompanho"
    show Larissa front
    with dissolve

    "Antes de sair"
    menu:
        "Pegar a bolsa":
            jump bolsa
        "Não precisa":
            jump esqueceu

default esqueceu = False

label bolsa:

    "Larissa pega a bolsa e sai"

    jump sair

label esqueceu:
    $ esqueceu = True
    "Larissa esquece de pegar a bolsa e sai"

    jump sair

label sair:

if esqueceu:
    lf "Ah, poxa! preciso voltar!"
    lf "Esqueci a Bolsa..."
else:
    k "Ei, você esta com dinheiro?"
    lf "Sim, por que?"
    k "Podemos ir na padaria!"
    return