# Registrar una estancia

## Estado

- Revisión de fuente: revisada en código.
- Verificación en entorno: pendiente.
- Paridad con la versión desplegada: pendiente.

## Objetivo

Registrar una estancia con una persona de contacto, un sujeto, una tarifa y los
datos operativos disponibles en el entorno.

## Acceso condicional

En el menú declarado **Estancias**, abra la opción para registrar una estancia.
Compruebe el establecimiento activo antes de continuar.

## Punto de partida

Use un caso ficticio y confirme que el contexto mostrado corresponde a la tarea.

## Requisitos y datos

- Persona que entrega, sujeto de la estancia y documento o serie de trabajo.
- Una tarifa activa y los ítems adicionales que correspondan.
- Modalidad de tiempo, observación y, cuando estén disponibles, medios de pago.

## Pasos

1. Seleccione la persona que entrega y el sujeto. Para practicar, use datos
   ficticios, por ejemplo, “Caso de prueba” y “Sujeto de ejemplo”.
2. Revise la serie disponible y elija una tarifa activa.
3. Complete la modalidad de tiempo y una observación breve si el caso la
   necesita.
4. Agregue ítems adicionales solo si corresponden al caso; revise cantidad y
   precio antes de guardar.
5. Si registra un pago, confirme que el importe no supera el total mostrado.
6. Guarde la estancia y vuelva a la lista para buscar el registro creado.

## Campos y validaciones observados

- La fuente requiere datos de estancia válidos y al menos una tarifa activa.
- Cada ítem debe tener cantidad y precio mayores que cero.
- La suma de pagos no puede superar el total neto de la estancia.
- Si la tarifa deja de estar activa o falta una serie, no continúe: revise la
  configuración del entorno antes de volver a intentar.

## Resultado revisado en fuente

La fuente registra la estancia, sus ítems y pagos dentro de una transacción. La
numeración, los mensajes y la actualización visible de la lista requieren
verificación en el entorno.

## Advertencias y casos límite

No use datos reales ni confirme un registro cuando el caso no esté completo.

## Problemas frecuentes y condiciones de detención

- No hay tarifa activa: deténgase; no sustituya la tarifa por un importe manual.
- El total no coincide con los ítems o pagos: revise los datos antes de guardar.
- El sujeto no aparece: consulte la guía de sujetos y relaciones antes de crear
  un registro nuevo.

## Verificaciones pendientes en runtime

- Etiquetas, orden de campos y mensajes mostrados por la interfaz.
- Disponibilidad real de series, tarifas y medios de pago.
- Efecto visible del registro en la lista diaria y el detalle.

## Enlaces relacionados

- [Consultar las estancias del día, la lista y el detalle](gestionar-estancias.md)
- [Gestionar tarifas, relaciones y descuentos](gestionar-tarifas-y-descuentos.md)
