# Gestionar tarifas, relaciones y descuentos

## Estado

- Revisión de fuente: revisada en código.
- Verificación en entorno: pendiente.
- Paridad con la versión desplegada: pendiente.

## Objetivo

Preparar tarifas de estancia y revisar relaciones o descuentos que la fuente
puede considerar al registrar una estancia.

## Acceso condicional

En **Estancias**, abra la opción declarada para tarifas, relaciones o descuentos
según la tarea que necesite realizar. No modifique datos reales durante una
prueba sin una instrucción operativa confirmada.

## Punto de partida

Identifique el caso y la tarifa existente antes de crear o modificar datos.

## Requisitos y datos

- Una tarifa incluye producto relacionado, nombre, duración, unidad y estado.
- Las unidades de duración revisadas son minuto, hora y día.
- La fuente requiere producto, nombre, duración y unidad para guardar una
  tarifa.
- Los descuentos se resuelven con información activa del sujeto y sus relaciones
  y se aplican al registro cuando el caso resulta válido.

## Pasos

1. Revise si ya existe una tarifa activa que cubre el caso antes de crear otra.
2. Al crear o editar, seleccione el producto relacionado, complete nombre,
   duración y unidad.
3. Confirme el estado disponible en el entorno y guarde solo después de revisar
   los datos.
4. Para una relación o descuento, localice primero el sujeto y revise la
   información disponible en el caso.
5. En el registro de estancia, seleccione un descuento únicamente si aparece
   como opción disponible; revise el total resultante antes de guardar.

## Campos y validaciones observados

- Una tarifa requiere sus cuatro datos principales; si falta uno, no continúe.
- El registro de estancia exige una tarifa activa y conserva al menos una tarifa
  cuando se modifican sus ítems.
- La fuente calcula el descuento a partir de datos aplicables y evita pagos por
  encima del total neto.
- Una opción de descuento visible no prueba elegibilidad comercial, resultado
  financiero ni una política universal.

## Resultado revisado en fuente

La fuente permite administrar tarifas y puede recalcular importes de una
estancia con datos aplicables. La disponibilidad de productos, descuentos,
campos y resultados debe verificarse en el entorno.

## Advertencias y casos límite

La disponibilidad de una opción no confirma una regla comercial para todos los casos.

## Problemas frecuentes y condiciones de detención

- No hay producto o tarifa activa: deténgase y confirme la configuración.
- El importe cambia de forma inesperada: revise tarifa, ítems y descuento antes
  de guardar.
- No puede explicar por qué un descuento aparece o no aparece: no lo fuerce ni
  infiera una política; escale la consulta operativa.

## Verificaciones pendientes en runtime

- Nombres, formularios y estados visibles de tarifas.
- Disponibilidad y cálculo mostrado de descuentos.
- Comportamiento de relaciones en cada configuración del entorno.

## Enlaces relacionados

- [Registrar una estancia](registrar-estancia.md)
- [Gestionar sujetos y personas relacionadas](gestionar-personas-de-la-estancia.md)
