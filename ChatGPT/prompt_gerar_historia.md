# Promptv.1

    Quero que você crie histórias, como um Visual Novel, onde vão ocorrer pontos de decisões (checkpoints) sendo apresentadas escolhas para o leitor decidir qual caminho quer tomar na história. Forneça até 3 opções para cada ponto de decisão, não ultrapassando 5 pontos de decisão. Forneça também a opção de voltar ao ponto de decisão anterior. As histórias devem ser construídas a partir de uma letra de música que será enviada no próximo prompt.  Essa letra estará no formato de marcações do MarkDown. Cada marcação, após o título "# Letra da Música", refere-se as etapas da letra e suas funções são descritas a seguir. Refrões devem ser usados para o contexto geral da história. Os versos, pontes e prelúdios, na ordem em que aparecem, servem para guiar a evolução da história. Use o nome da música para nomear a história.

## Output
    Entendido! Agora ficou claro o que você deseja. Vou criar uma história interativa no estilo de um Visual Novel com base na letra da música que você vai fornecer. A cada ponto de decisão, apresentarei opções para o leitor escolher o caminho que deseja seguir na história. Não ultrapassarei 5 pontos de decisão e fornecerei a opção de voltar ao ponto de decisão anterior. Farei uso das marcações presentes no formato Markdown da letra da música para guiar a evolução da história, utilizando refrões, versos, pontes e prelúdios. O nome da música será usado para nomear a história. Aguardo a próxima mensagem com a letra da música em formato Markdown para começar a criar a história interativa.

## Prompt
    Arquivo .md de "Another Brick in the Wall"

## Output

# História: Another Brick in the Wall

Você se encontra em uma escola onde a educação é rígida e controladora. O sistema parece sufocar sua individualidade e criatividade. Você está cansado das restrições impostas e deseja encontrar uma maneira de escapar dessa opressão. À medida que a música começa a tocar, você sente uma onda de rebelião percorrer seu corpo. É hora de tomar uma decisão e moldar seu próprio destino.

## Checkpoint 1: Em busca da liberdade

Você está na sala de aula, ouvindo o professor falar sobre o sistema educacional. Suas palavras não fazem sentido para você, e você começa a questionar o propósito de tudo isso. Neste momento, você tem algumas opções:

1. **Desafiar o professor**: Levante a mão e questione as regras impostas pelo professor. (Ir para o Checkpoint 2)
2. **Ficar quieto**: Decida permanecer em silêncio, mas prometa a si mesmo que encontrará uma maneira de se libertar dessa opressão. (Ir para o Checkpoint 3)
3. **Conversar com um colega**: Vire-se para um colega ao seu lado e comece uma conversa sobre a falta de liberdade na escola. (Ir para o Checkpoint 4)

Escolha o número correspondente à opção que deseja seguir e prossiga para o próximo checkpoint.

---

### Checkpoint 2: Desafiando o sistema

Você decide desafiar o professor e expressar sua insatisfação com as regras opressoras da escola. Isso chama a atenção dos outros alunos, que começam a prestar atenção em você. O professor fica surpreso com sua coragem, mas rapidamente o repreende. As consequências podem ser severas, mas você se sente empoderado por ter expressado sua opinião.

Continue a história no próximo checkpoint.

---

### Checkpoint 3: A busca silenciosa

Você decide não confrontar diretamente o professor, mas promete a si mesmo que encontrará uma maneira de se libertar dessa opressão. Durante as aulas, você começa a observar os pontos fracos do sistema e a planejar sua fuga silenciosa. Enquanto todos estão ocupados com as atividades escolares, você aproveita a oportunidade para explorar alternativas fora da sala de aula.

Continue a história no próximo checkpoint.

---

### Checkpoint 4: Compartilhando a insatisfação

Você decide iniciar uma conversa com um colega ao seu lado sobre a falta de liberdade na escola. Para sua surpresa, o colega compartilha da mesma insatisfação. Juntos, vocês começam a trocar ideias sobre como desafiar o sistema e encontrar uma maneira de escapar dessa opressão. Essa parceria fortalece sua determinação e criatividade.

Continue a história no próximo checkpoint.

---

## Checkpoint 5: Rompendo os muros

Independente da escolha que você fez nos checkpoints anteriores, você está disposto a romper os muros que o cercam. Inspirado pela música e pela união com outros alunos, vocês decidem se rebelar em conjunto. Planejam uma manifestação pacífica para chamar a atenção das autoridades e da comunidade, denunciando as injustiças do sistema educacional.

A história continua com a manifestação e suas consequências. O destino dos personagens será determinado por suas ações e escolhas ao longo do caminho.

---

Essa é apenas uma das histórias possíveis que podem ser criadas com base na letra da música "Another Brick in the Wall". As escolhas feitas pelos leitores irão moldar o desenrolar da narrativa e os finais possíveis. Divirta-se explorando diferentes caminhos e descobrindo as consequências de cada decisão.

# Prompt.v2

    Quero que você crie histórias, como um Visual Novel, onde existirão pontos de decisões (checkpoints). Em cada ponto de decisão, serão apresentadas escolhas para o leitor interagir com a história que lhe foi apresentada. O leitor é o personagem protagonista da história. Forneça até 3 opções em cada ponto de decisão, quando o leitor escolher sua opção, gere um caminho para aquela escolha, permanecendo no contexto geral da história gerada. Apenas desenvolver os outros caminhos após a escolha do leitor. Cada escolha leva para um caminho diferente, levando a um final diferente. Não ultrapasse 5 pontos de decisão. Forneça também a opção de voltar ao ponto de decisão anterior. As histórias devem ser construídas a partir de uma letra de música que será enviada no próximo prompt. 

    Essa letra estará no formato de marcações do MarkDown. Cada marcação, após o título "# Letra da Música", refere-se as etapas da letra e suas funções são descritas a seguir. Refrões devem ser usados para o contexto geral da história. Os versos, pontes e prelúdios, na ordem em que aparecem, servem para guiar a evolução da história. Use o nome da música para nomear a história.

# Prompt
## Gerar sugestões de prompt para o PlayGroundAI

    me sugira prompts para geração de imagens no playground para cada label do script .rpy que será enviado no próximo prompt. Cada sugestão de prompt deve estar entitulado com o respectivo label. Quero que os prompts gerem imagens que reflitam o ambiente em que aquele label se passa. Ou seja, quero que gere imagens para que eu possa usar como parâmetro para o 'scene'. Se você achar que dois labels devem possuir a mesma imagem, indique que aquele label tem o mesmo background que outro (nomeie o label). Um label pode ter dois ambientes diferentes, logo duas imagens diferentes, identifique. Pode ser também que a imagem do label anterior se prorrogue para o próximo label. Exemplo: Label x possui a scene com a imagem "bg-lblx", a label y (que é alcançável imediatamente após o label x) começa com a imagem "bg-lblx" e após alguma indicação de mudança de ambiente mude a scene para "bg-lbly".

        Para cada sugestão, de um título para a imagem

# Output

    Certainly! Here are the succinct and assertive prompts in English for each label:

    **Label: start**
    Image Title: "Dry Sertão"
    Description: Generate an image depicting the aridness of the sertão with cracked soil, dry vegetation, and few trees. The sky should be clear without clouds.

    **Label: interagir_boiadeiro**
    Image Title: "Solitary Encounter"
    Description: Generate an image showing a meeting between the main character and the boiadeiro in an open environment with few trees and a bright sun in the sky.

    **Label: esperar_chuva**
    Image Title: "Hope in the Sky"
    Description: Generate an image that portrays the main character gazing hopefully at the sky, eagerly awaiting the arrival of rain. The landscape should reflect the drought of the sertão with dried vegetation surrounding.

    **Label: pelejar_chuva**
    Image Title: "Rain Ritual"
    Description: Generate an image depicting the main character and Maria performing rituals

# Prompt

    voce entendeu errado. A sua resposta será em português, apenas a descrição em inglês (lembre-se de que a descrição é um prompt para geração de imagem no playground AI)  e mantenha sucinta, use a menor quantidade de palavras possível, mas que descreva suficientemente a imagem que reflita o ambiente que o label sugere

# Output

    Desculpe pelo mal entendido. Aqui estão as descrições em inglês, de forma sucinta, para os prompts de geração de imagem:

    **Label: start**
    Image Title: "Dry Sertão"
    Description (Prompt for image generation): Generate an image depicting the arid landscape of the sertão with cracked soil, dry vegetation, and a barren sky.

    **Label: interagir_boiadeiro**
    Image Title: "Solitary Encounter"
    Description (Prompt for image generation): Generate an image showing a solitary meeting between the main character and the boiadeiro in an open, desolate setting.

    **Label: esperar_chuva**
    Image Title: "Hopeful Sky"
    Description (Prompt for image generation): Generate an image that conveys the character's hopeful gaze towards the sky, anticipating the arrival of rain, amidst a dry and barren landscape.

    **Label: pelejar_chuva**
    Image Title: "Rain Ritual"
    Description (Prompt for image generation): Generate an image that portrays the main character and Maria performing rituals and ceremonies to invoke the much-awaited rain in a serene and determined manner.

# Prompt

    faltam mais labels

# Output

    Peço desculpas pela falta de atenção. Aqui estão os prompts em inglês para os restantes dos labels:

**Label: ouvir_historias**
Image Title: "Tales of the Sertão"
Description (Prompt for image generation): Generate an image depicting the main character sitting beside the boiadeiro, listening to his stories of long journeys through the sertão. The scene should evoke a sense of nostalgia and convey the importance of rain in people's lives.

**Label: compartilhar_esperanca**
Image Title: "Words of Hope"
Description (Prompt for image generation): Generate an image that shows the main character sharing their own experiences and words of hope with the boiadeiro, fostering a sense of unity and mutual strength.

**Label: participar_rezas**
Image Title: "Collective Prayers"
Description (Prompt for image generation): Generate an image portraying the main character participating in collective prayers, seeking a spiritual connection with the rain. The scene should convey the power of collective faith and renewal.

**Label: refletir_seca**
Image Title: "Contemplating Drought"
Description (Prompt for image generation): Generate an image showing the main character deep in thought, reflecting on the impact of the drought. The scene should convey a sense of introspection and resilience.

**Label: dançar_zabumba**
Image Title: "Zabumba Dance"
Description (Prompt for image generation): Generate an image capturing the joy and intensity of the main character, Maria, and other residents dancing to the captivating rhythm of the zabumba. The scene should exude energy and a celebratory atmosphere.

**Label: rezar_conjunto**
Image Title: "Unified Prayers"
Description (Prompt for image generation): Generate an image showing the main character, Maria, and other residents gathered in a circle, their voices and minds united in prayer. The scene should convey a sense of collective spiritual energy and devotion.

**Label: transicao_chuva**
Image Title: "Arrival of Rain"
Description (Prompt for image generation): Generate an image that depicts the transition from a dry landscape to the arrival of rain. Dark clouds are forming in the sky, symbolizing the imminent rainfall and bringing a sense of renewal and joy.

**Label: celebrar_comunidade**
Image Title: "Community Celebration"
Description (Prompt for image generation): Generate an image showing the main character and other residents coming together in a festive celebration to honor the arrival of rain. The scene should reflect a sense of community spirit, with music, dance, and jubilation.

**Label: agradecer_dadiva**
Image Title: "Gratitude for Rain's Gift"
Description (Prompt for image generation): Generate an image portraying the main character finding a quiet place to express gratitude for the gift of rain. The scene should evoke a sense of tranquility and deep appreciation.

**Label: ajudar_comunidade**
Image Title: "Community Support"
Description (Prompt for image generation): Generate an image showing the main character and other residents working together to rebuild homes, cultivate new crops, and strengthen community bonds in the wake of the rain. The scene should convey a sense of unity and resilience.

**Label: explorar_paisagem**
Image Title: "Exploring the Transformed Landscape"
Description (Prompt for image generation): Generate an image that portrays the main character and Maria exploring the newly transformed landscape. They encounter crystal-clear streams, lush vegetation, and are captivated by the beauty that the rain has brought.

**Label: falar_boiadeiro**
Image Title: "Mysterious Encounter"
Description (Prompt for image generation): Generate an image capturing the moment when the main character has an unexpected encounter with a mysterious boiadeiro. The scene should convey a sense of intrigue and connection to nature.

**Label: agradecer_boiadeiro**
Image Title: "Gratitude to the Boiadeiro"
Description (Prompt for image generation): Generate an image showing the main character expressing gratitude to the boiadeiro for the blessings received. The scene should evoke a sense of peace and deep connection to nature.

**Label: perguntar_futuro**
Image Title: "Seeking Insight"
Description (Prompt for image generation): Generate an image portraying the main character inquiring about the future of the sertão from the boiadeiro. The scene should convey a sense of curiosity and anticipation, with an enigmatic atmosphere.

**Label: final_ajuda_boiadeiro**
Image Title: "Blossoming Sertão"
Description (Prompt for image generation): Generate an image that depicts the sertão flourishing with the help of the boiadeiro and the community's dedication. The scene should convey gratitude and a promising future.

**Label: final_exploracao_boiadeiro**
Image Title: "Journey Continues"
Description (Prompt for image generation): Generate an image showing the main character and Maria continuing their exploration of the wonders of the sertão based on the guidance of the boiadeiro. Each discovery is a new lesson, and rain serves as the constant soundtrack to their journeys.

Espero que esses prompts sejam úteis para você!