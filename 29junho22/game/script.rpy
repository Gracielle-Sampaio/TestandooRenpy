define lf = Character('Larissa Fantina', color="#540b0e")
define sk = Character('Kary', color="#335c67")
image Larissa front = ("images/Larissa_front.png")
image Larissa back = ("images/Larissa_back.png")
image Kary front = ("images/Kary_front.png")
image Kary back = ("images/Kary_back.png")

label start:

    scene bg janela
    "Kary estava na sacada, parecia estar distraida em seus pensamentos"
    show Larissa front

    lf "O que você tanto olha ai?"

   

    scene bg sacada

    show Kary back

    sk "Nada... "
    sk "Só gosto de ver a movimentação da rua"

    show Kary front

   
    "Kary, olha para trás e dá um sorriso convidativo, para Larissa, que não se opõem ao convite"

    scene bg sacada

    show Larissa back
    
    show Kary back

    "As duas ficam ali na sacada por um tempo, observando a paisagem"