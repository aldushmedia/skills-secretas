# Formato de los registros de aprendizaje

Los registros de aprendizaje viven en `./learning-records/` y van numerados en
orden: `0001-nombre.md`, `0002-nombre.md`, etc. Crea la carpeta solo cuando
escribas el primer registro.

Son el equivalente, en la enseñanza, de los registros de decisiones de
arquitectura: guardan lecciones no obvias, ideas clave y conocimientos previos
que el usuario declaró, y que van a guiar las siguientes sesiones. Se usan para
calcular la zona de desarrollo próximo.

## Plantilla

```md
# {Título corto de lo que se aprendió o se estableció}

{1 a 3 oraciones: qué se aprendió (o qué conocimiento previo quedó establecido) y por qué importa para las siguientes sesiones.}
```

Ese es todo el formato. Un registro puede ser un solo párrafo. El valor está en
dejar constancia de _que_ esto ya se sabe y de _por qué_ cambia lo que hay que
enseñar después, no en llenar secciones.

## Secciones opcionales

Inclúyelas solo cuando aporten de verdad. La mayoría de los registros no las
necesitan.

- **Estado**, en una línea al inicio (`Estado: vigente` o `Estado: reemplazado
  por 0007-nombre.md`): sirve cuando una comprensión anterior resulta estar mal
  y se reemplaza.
- **Evidencia**: cómo demostró el usuario que entiende (una pregunta que
  respondió, un ejercicio que completó, una experiencia previa que citó). Sirve
  cuando la afirmación podría revisarse.
- **Implicaciones**: qué abre o qué descarta esto para las siguientes sesiones.
  Vale la pena anotarlo cuando no es obvio.

## Numeración

Busca en `./learning-records/` el número más alto que ya existe y súmale uno.

## Cuándo escribir un registro

Escribe uno cuando se cumpla cualquiera de estas condiciones:

1. **El usuario demostró que entiende de verdad algo no trivial**: no solo que
   lo vio, sino evidencia de que puede usar el concepto correctamente. Eso
   marca un nuevo piso para lo que hay que enseñar después.
2. **El usuario contó lo que ya sabe**, o lo que no sabe: "Ya sé X", "nunca
   hice X". Anótalo para que las siguientes sesiones no se lo vuelvan a
   enseñar. Anota también qué tan a fondo dice saberlo.
3. **Se corrigió una idea equivocada**: el usuario creía algo incorrecto y ahora
   ve por qué. Valen mucho: anticipan tropiezos futuros en temas relacionados.
4. **La misión cambió por lo aprendido**: el usuario descubrió que le importaba
   algo distinto de lo que creía. Enlaza a `MISSION.md` y actualízalo.

### Lo que _no_ cuenta

- Material que solo se vio. Ver no es aprender. Espera la evidencia.
- Lo que ya está guardado de forma breve en `GLOSSARY.md` como
  definición de un término. No lo dupliques.
- Bitácoras de lo que se hizo en cada sesión. Los registros no son un diario:
  son ideas que sirven para decidir.

## Reemplazo

Cuando un registro nuevo contradiga a uno anterior (la comprensión del usuario
se profundizó o se corrigió), marca el viejo con
`Estado: reemplazado por 0007-nombre.md` (el número y el nombre del registro
nuevo) en lugar de borrarlo. La historia de cómo evolucionó la comprensión
también es una señal útil.
