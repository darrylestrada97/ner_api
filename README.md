### Production

```bash
$ docker-compose  up --build -d
```

### Bugs

For some reason the firt time running after loading the models, the brat* folders do not get deleted, if that is the case, go inside the docker and delete them by using
rm -r brat*

### TEST API

POST Request to yourdomain:8003/get_annotations
request: {"INPUTTEXT": "Mujer de 59 años cuyos antecedentes personales incluyen hipertensión arterial, artropatía degenerativa cervical, lumbociática crónica, tuberculosis ganglionar diagnosticada por cuadro de eritema nudoso y migraña. En su tratamiento habitual, destaca el candesartán 32 mg/día.﻿Acudió en marzo de 2020 al servicio de urgencias por sensación distérmica de 5 días de evolución, acompañada de dolor torácico de características opresivas en ausencia de síntomas respiratorios. A su llegada presentaba SatO2 del 96% con gafas nasales a 2 l/min y presión arterial de 75/53 mmHg. En la exploración física destacan signos de hipoperfusión periférica con auscultación respiratoria normal. A pesar de la sobrecarga hídrica y la noradrenalina, persistía hipotensa con signos de hipoperfusión (frialdad cutánea y ácidos lácticos elevados: 3,9 mmol/l). En el electrocardiograma destacaba elevación cóncava del ST y descenso del PR, así como bajos voltajes. En la radiografía de tórax se observaron ligeros signos de redistribución vascular sin infiltrados. La reacción en cadena de la polimerasa (PCR) de virus del frotis nasofaríngeo resultó positiva para SARS-CoV-2 y negativo para adenovirus y virus Influenza A y B, con un ambiente epidemiológico positivo (familiares con fiebre y cuadro respiratorio días previos). Entre los datos del laboratorio, destacaba la elevación de troponinas (TnT, 220-1.100 ng/dl) y NT-proBNP (4.421 ng/l), ligera leucocitosis (14,17 × 109/l), linfocitos (2,59 × 109/l), PCR 10 mg/l y dímero D a las 24 h (23.242 ng/ml). Una ecocardiografía mostró hipertrofia concéntrica moderada, volúmenes intraventriculares disminuidos con fracción de eyección del ventrículo izquierdo conservada sin segmentarismos y derrame pericárdico moderado sin claros signos de deterioro hemodinámico. Debido al cuadro tan indicativo de miocarditis (elevación concaviforme y difusa del ST, fiebre, derrame pericárdico y engrosamiento miocárdico) y la fracción de eyección del ventrículo izquierdo conservada sin segmentarismos, no se realizó coronariografía por baja sospecha clínica de síndrome coronario agudo. En la unidad coronaria, durante el implante de un catéter de Swan-Ganz, se produjo un rápido deterioro hemodinámico hasta llegar a una actividad eléctrica sin pulso que requirió reanimación cardiopulmonar, pericardiocentesis emergente (drenaje de líquido seroso) y altas dosis de vasopresores para la recuperación hemodinámica de la paciente. Se realizó otro ecocardiograma (a las 2 h del ingreso), que mostró disfunción biventricular grave y edema miocárdico difuso, por lo que se decidió implantar un balón de contrapulsación y oxigenador extracorpóreo de membrana (ECMO) venoarterial femoral. Se inició el tratamiento de la miocarditis con inmunoglubulinas (80 mg/día) durante 4 días y metilprenisolona (500 mg/día) en pauta descendente durante 14 días y tratamiento antiviral: IFN B (0,25 mg/48 h) y (ritonavir 400 mg/lopinavir 100 mg/12 h). Al quinto día de ingreso, se constató la normalización de la función biventricular, pero se mantuvo el dispositivo ECMO por la disnea, con hipoxemia refractaria, actualmente pendiente de progreso respirator",
"ner_type":"conjunto"
}
