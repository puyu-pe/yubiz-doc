# Registrar una orden de servicio o internado

## Estado

- Revisión de fuente: revisada en código.
- Verificación en entorno: pendiente.
- Paridad con la versión desplegada: pendiente.

## Objetivo

Registrar una orden de servicio con sus datos de cliente, unidad, documento y
detalle de ítems.

## Acceso condicional

El menú declarado incluye **Agregar internado**. La pantalla y sus datos dependen
de la configuración del entorno.

## Requisitos y datos

- Cliente, unidad, documento y serie seleccionables.
- Fecha de registro, fecha estimada, categoría, responsable, prioridad y almacén.
- Al menos un ítem válido con cantidad, descripción, importe y tipo de afectación.

## Punto de partida

En **Internado**, abra **Agregar internado** y confirme que está trabajando en el
establecimiento correcto.

## Pasos

1. Seleccione el cliente y la unidad correspondiente.
2. Elija documento y serie; revise las fechas de registro y salida estimada.
3. Complete categoría, responsable, prioridad y almacén cuando estén disponibles.
4. Agregue los ítems, revise cantidades, descripción e importes.
5. Confirme subtotales, impuesto y total antes de registrar.
6. Guarde y compruebe que la lista reconoce la nueva orden.

## Campos y validaciones observados

La interfaz exige cliente, unidad, documento, serie, fechas, categoría,
responsable, prioridad y detalle. El guardado de fuente valida cliente, documento
y serie, fechas y cada ítem con cantidad, descripción, precio, importe y afectación.

## Resultado revisado en fuente

El guardado válido crea la orden en una transacción, asigna numeración y registra
el detalle. Si falla, la fuente revierte la operación; el resultado visible debe
confirmarse en el entorno.

## Advertencias y casos límite

No registre si faltan datos del detalle o si hay ítems eliminados en la tabla. No
suponga que fechas, series o almacenes tendrán los mismos valores en cada entorno.

## Problemas frecuentes y condiciones de detención

- No hay serie o documento seleccionable: deténgase y confirme la configuración.
- Falta un dato obligatorio: complete el dato o no continúe.
- El total no representa el detalle: revise los ítems antes de guardar.

## Verificaciones pendientes en runtime

- Mensajes, numeración, campos visibles y actualización de la lista.
- Efecto real sobre el detalle, existencias y registros relacionados.

## Enlaces relacionados

- [Gestionar unidades e ítems de servicio](gestionar-unidades-e-items.md)
- [Consultar un internado y agregar procedimientos](gestionar-internado.md)
