"""
corpus.py
---------
20 fragmentos simulados de manuais médicos técnicos.
Gerados com IA e revisados manualmente.
"""

DOCUMENTS = [
    "Cefaleia pulsátil (migrânea) é caracterizada por dor latejante unilateral, acompanhada de náuseas, fotofobia e fonofobia. O diagnóstico é clínico pelos critérios da ICHD-3. O tratamento agudo inclui triptanos e AINEs.",
    "Fotofobia é hipersensibilidade patológica à luz, associada a meningite, enxaqueca e uveíte. A avaliação inclui fundoscopia e, quando indicado, punção lombar para análise do líquor.",
    "Hipertensão intracraniana manifesta-se com cefaleia progressiva, vômitos em jato e papiledema. A TC de crânio sem contraste é o exame inicial. O manejo envolve elevação da cabeceira a 30° e osmoterapia com manitol.",
    "AVC isquêmico: déficit neurológico focal de início súbito. Trombólise com rt-PA é indicada até 4,5 horas do início dos sintomas, após exclusão de hemorragia por neuroimagem.",
    "Meningite bacteriana: tríade de febre, rigidez de nuca e alteração do nível de consciência. Antibioticoterapia empírica com ceftriaxona deve ser iniciada imediatamente.",
    "Síncope vasovagal: perda transitória da consciência por hipoperfusão cerebral. Precipitada por estresse emocional ou ortostatismo prolongado. O tilt-test confirma o diagnóstico.",
    "Diabetes mellitus tipo 2: resistência periférica à insulina. Diagnóstico por glicemia de jejum ≥ 126 mg/dL ou HbA1c ≥ 6,5%. Metformina é a droga de primeira linha.",
    "Infarto agudo do miocárdio com supra de ST: dor torácica em aperto irradiada para o membro superior esquerdo, sudorese fria e dispneia. Angioplastia primária é o tratamento de reperfusão preferencial.",
    "Pneumonia adquirida na comunidade: consolidação lobar ao RX de tórax, febre e tosse produtiva. Amoxicilina-clavulanato oral para casos leves; ceftriaxona IV para casos graves.",
    "Insuficiência renal aguda: aumento da creatinina sérica ≥ 0,3 mg/dL em 48h ou débito urinário < 0,5 mL/kg/h por mais de 6 horas. Classificação KDIGO em estágios 1, 2 e 3.",
    "Sepse: disfunção orgânica por resposta desregulada do hospedeiro à infecção. Critério SOFA ≥ 2 pontos. O bundle de 1 hora inclui hemoculturas, lactato, antibióticos e ressuscitação volêmica.",
    "Epilepsia: predisposição a crises epilépticas não provocadas. EEG e RM de crânio são os exames principais. Valproato e lamotrigina são antiepilépticos de amplo espectro.",
    "Hipotireoidismo primário: TSH elevado com T4 livre reduzido. Sintomas incluem fadiga, ganho de peso, intolerância ao frio e bradicardia. Levotiroxina sódica é o tratamento padrão.",
    "Doença de Parkinson: perda de neurônios dopaminérgicos na substância negra. Tríade: tremor de repouso, rigidez em roda dentada e bradicinesia. Levodopa/carbidopa é o tratamento principal.",
    "Úlcera péptica: erosão da mucosa gástrica por H. pylori ou AINEs. Epigastralgia em queimação melhora com antiácidos. Tratamento com inibidores de bomba de prótons e erradicação do H. pylori.",
    "Artrite reumatoide: doença autoimune inflamatória crônica das articulações sinoviais, simétrica. Fator reumatoide e anti-CCP são os marcadores sorológicos. Metotrexato é o DMARD de primeira linha.",
    "Anafilaxia: reação de hipersensibilidade imediata grave mediada por IgE. Manifestações: urticária, broncoespasmo e hipotensão. Epinefrina intramuscular 0,3 mg na coxa é o tratamento de primeira linha.",
    "Asma brônquica: doença inflamatória crônica das vias aéreas com hiperresponsividade brônquica. Diagnóstico por espirometria com prova broncodilatadora positiva. Corticoide inalatório é o pilar do controle.",
    "Insuficiência cardíaca com fração de ejeção reduzida: FE < 40%. Diagnóstico por ecocardiograma. Tratamento farmacológico: IECA + betabloqueador + antagonista da aldosterona + diurético de alça.",
    "Tromboembolismo pulmonar: obstrução da artéria pulmonar por trombo proveniente de TVP. Angiotomografia pulmonar é o padrão-ouro. Anticoagulação plena com heparina seguida de NOAC.",
    "Derrame pleural: acúmulo de líquido no espaço pleural. Classificado em transudato (ICC, cirrose) ou exsudato pelos critérios de Light. Toracocentese para diagnóstico e tratamento.",
    "Glaucoma de ângulo aberto: neuropatia óptica progressiva com escavação do disco óptico. Pressão intraocular elevada é o principal fator de risco. Colírios betabloqueadores reduzem a PIO.",
]
