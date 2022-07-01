define lf = Character('Larissa Fantina', color="#540b0e")
define k = Character('Kary', color="#335c67")
image Larissa front = ("images/Larissa_front.png")
image Larissa back = ("images/Larissa_back.png")
image Kary front = ("images/Kary_front.png")
image Kary back = ("images/Kary_back.png")

label start:

    scene bg janela
    with fade
    "Kary estava na sacada, parecia estar distraida em seus pensamentos"
    show Larissa front
    with Fade(0.5,0.0,0.5,color="#000")

    lf "O que você tanto olha ai?"

   

    scene bg sacada
    with None
    show Kary back
    with fade

    k "Nada... "
    k "Só gosto de ver a movimentação da rua"

    show Kary front
    with dissolve
   
    "Kary, olha para trás e dá um sorriso convidativo, para Larissa, que não se opõem ao convite"

    scene bg sacada

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