<a id="crear-un-pedido-de-preventa"></a>

# 7.1 Crear un pedido de preventa

<a id="estado"></a>
<a id="verificaciones-pendientes-en-runtime"></a>

## Objetivo

Registrar un pedido en el recorrido heredado de preventa cuando sus opciones estén
habilitadas.

## Acceso condicional

Este formulario heredado convive con la lista moderna de preventas. No suponga que
sus campos, conversión o estados equivalen al recorrido moderno de borrador,
confirmación, procesamiento y cancelación.

## Requisitos y datos

- Documento, serie y fecha disponibles.
- Promotor y cliente identificados.
- Línea, productos, cantidades y precios disponibles.
- Detalle u observación cuando correspondan.

## Punto de partida

Abra el registro de pedido de venta dentro de Preventa si aparece para la sesión.

## Pasos

1. Seleccione documento y serie; revise el correlativo mostrado.
2. Indique fecha y promotor disponibles.
3. Busque o registre el cliente mediante su documento cuando el control lo permita.
4. Seleccione la línea disponible y agregue productos a la tabla.
5. Revise cantidad, precio unitario, importe y los totales calculados.
6. Complete detalles u observación si son necesarios y guarde el pedido.

## Campos y validaciones observados

El formulario muestra documento, serie, correlativo de solo lectura, fecha, promotor,
identificador de cliente, línea, productos, cantidad, precio unitario, subtotal, IGV,
total, detalle y observación. Los totales se presentan como campos calculados.

<a id="resultado-revisado-en-fuente"></a>

## Resultado esperado

El recorrido heredado reúne datos de documento, cliente, promotor y detalle de
productos para registrar el pedido. Los efectos comerciales, fiscales, de stock o de
reserva pueden variar según la configuración disponible.

## Advertencias y casos límite

No interprete el correlativo o total calculado como confirmación final. No use este
procedimiento para editar una preventa de la lista moderna; use su ficha específica.

## Problemas frecuentes y condiciones de detención

- Cliente o producto no identificado: confirme el dato de origen antes de guardar.
- Total inesperado: revise cantidades y precios antes de continuar.
- Serie no disponible: no sustituya el control por una serie no observada.

## Enlaces relacionados

- [Consultar y editar preventas](consultar-y-editar.md)
- [Confirmar, anular o convertir una preventa en venta](confirmar-anular-convertir.md)
