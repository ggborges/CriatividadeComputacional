label start:
    scene bg_cenario1

    "Bem-vindo a 'O Encanto da Chuva', uma jornada inspirada pelas gotas que caem do céu."
    "Você é um morador do sertão, onde a chuva é escassa e seu povo anseia por sua chegada."

    menu:
        "Esperar pela chuva":
            jump esperar_chuva
        "Pelejar pela chuva":
            jump pelejar_chuva

label esperar_chuva:
    scene bg_cenario2

    "Você decide esperar pacientemente pela chuva, observando o céu com esperança."
    "Ao seu lado, Aderaldo, um morador cego que acredita na força da natureza, compartilha sua esperança."

    menu:
        "Participar das rezas":
            jump participar_rezas
        "Refletir sobre a seca":
            jump refletir_seca

label pelejar_chuva:
    scene bg_cenario3

    "Decidido a fazer sua parte, você se une a Maria, uma mulher forte que mói mandioca, para pelejar pela chuva."
    "Juntos, vocês organizam rituais e cerimônias para invocar a tão esperada chuva."

    menu:
        "Dançar ao som da zabumba":
            jump dançar_zabumba
        "Rezar em conjunto":
            jump rezar_conjunto

label participar_rezas:
    scene bg_cenario4

    "Você participa das rezas coletivas, em busca de uma conexão espiritual com a chuva."
    "Cantos e orações enchem o ar, elevando as esperanças e renovando as energias do povo."

    jump transicao_chuva

label refletir_seca:
    scene bg_cenario5

    "Enquanto reflete sobre a seca, você encontra Aderaldo, que compartilha suas histórias de superação e resiliência."
    "Maria, por sua vez, destaca a importância de manter a fé e a esperança no coração."

    jump transicao_chuva

label dançar_zabumba:
    scene bg_cenario6

    "Ao som contagiante da zabumba, você, Maria e outros moradores dançam com alegria e intensidade."
    "Cada batida ressoa como uma invocação ao céu, buscando atrair a chuva para a terra sedenta."

    jump transicao_chuva

label rezar_conjunto:
    scene bg_cenario7

    "Em um círculo de oração, você, Maria e outros moradores elevam suas vozes e mentes em união."
    "Palavras de fé e esperança são proferidas, enquanto a energia coletiva flui em direção às nuvens."

    jump transicao_chuva

label transicao_chuva:
    scene bg_cenario8

    "Após dias de espera e esforço conjunto, nuvens escuras começam a se formar no céu."
    "A chuva finalmente chega ao sertão, trazendo consigo uma renovação e alegria indescritíveis."

    menu:
        "Celebrar com a comunidade":
            jump celebrar_comunidade
        "Agradecer pela dádiva":
            jump agradecer_dadiva

label celebrar_comunidade:
    scene bg_cenario9

    "Você e outros moradores se juntam à comunidade em uma festa para celebrar a chegada da chuva."
    "A música, a dança e a alegria transbordam por todo o sertão, fortalecendo os laços entre as pessoas."

    jump ajudar_comunidade

label agradecer_dadiva:
    scene bg_cenario10

    "Em gratidão pela dádiva da chuva, você se retira para um local tranquilo e faz suas preces."
    "Enquanto agradece, você se depara com Maria, que também expressa sua gratidão pela chuva."

    jump falar_boiadeiro

label ajudar_comunidade:
    scene bg_cenario11

    "A chuva contínua traz uma renovação à comunidade do sertão."
    "Você e os moradores se unem para reconstruir casas, cultivar novas plantações e fortalecer o espírito comunitário."

    jump falar_boiadeiro

label explorar_paisagem:
    scene bg_cenario12

    "Inspirados pela transformação do sertão, você e Maria decidem explorar a nova paisagem."
    "Juntos, descobrem riachos cristalinos, vegetação exuberante e se encantam com a renovação que a chuva trouxe."

    jump falar_boiadeiro

label falar_boiadeiro:
    scene bg_cenario13

    "Enquanto desfruta da alegria trazida pela chuva, você tem um encontro inesperado."
    "Um boiadeiro, figura misteriosa, surge diante de você e transmite uma mensagem de gratidão pelas preces atendidas."

    menu:
        "Agradecer ao boiadeiro":
            jump agradecer_boiadeiro
        "Perguntar sobre o futuro":
            jump perguntar_futuro

label agradecer_boiadeiro:
    scene bg_cenario14

    "Em gratidão ao boiadeiro, você expressa seus agradecimentos pelas bênçãos recebidas."
    "O boiadeiro sorri e desaparece, deixando você com uma sensação de paz e conexão com a natureza."

    jump final_ajuda_boiadeiro

label perguntar_futuro:
    scene bg_cenario15

    "Curioso sobre o futuro do sertão, você pergunta ao boiadeiro sobre o que está por vir."
    "O boiadeiro responde enigmaticamente, deixando nas entrelinhas que a jornada pela chuva é contínua e cheia de aprendizados."

    jump final_exploracao_boiadeiro

label final_ajuda_boiadeiro:
    scene bg_cenario16

    "Com a ajuda do boiadeiro e a dedicação da comunidade, o sertão floresce em sua plenitude."
    "A gratidão e a fé em cada gota de chuva guiam vocês em um futuro promissor."

    "Fim."

label final_exploracao_boiadeiro:
    scene bg_cenario17

    "Guiado pelas palavras do boiadeiro, você e Maria continuam a explorar as maravilhas do sertão."
    "Cada descoberta é uma nova lição e a chuva é a trilha sonora constante de suas jornadas."

    "Fim."
