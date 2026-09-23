# Crear una orden de carga

## Estado

- Revisión de fuente: revisada en código
- Verificación en entorno: pendiente
- Paridad con la versión desplegada: pendiente

## Objetivo

Preparar una orden de carga cuando Distribución esté habilitada, con el origen,
vehículo, distribuidor, fecha y productos que correspondan al recorrido.

## Acceso condicional

La opción depende del módulo, la sesión y la configuración disponible. No use
esta guía para una [carga de contenedores](../inventario/gestionar-cargas-de-contenedores.md): son flujos distintos.

## Requisitos y datos

- Serie documental, almacén de origen, vehículo y distribuidor disponibles.
- Fecha de salida y, si corresponde, una observación.
- Al menos un producto, ya sea cargado manualmente o desde ventas disponibles.

## Punto de partida

Abra **Orden de carga > Agregar** si aparece para su sesión.

## Pasos

1. Seleccione la serie y el almacén de origen.
2. Elija el vehículo y el distribuidor; indique la fecha de salida.
3. Agregue productos o use **Cargar ventas** cuando corresponda.
4. Revise cantidades, origen y seguimiento antes de registrar.
5. Registre una sola vez y abra el detalle para comprobar el resultado mostrado.

## Campos y validaciones observados

La pantalla solicita serie, almacén de origen, vehículo, distribuidor y fecha.
Exige al menos un producto; el almacén de origen no puede coincidir con el
vehículo seleccionado. Al cambiar el almacén, los productos ingresados por
serie se retiran de la tabla. La fecha mínima y las opciones disponibles deben
confirmarse en runtime.

## Resultado revisado en fuente

El navegador registra una orden con su detalle y ofrece impresión. También
consulta residuales y compromisos del vehículo antes del registro. Esto no
confirma un despacho, una salida física ni una consecuencia comercial en un
entorno desplegado.

## Advertencias y casos límite

El resumen de residuales puede incorporar cantidades no editables. Si la vista
no termina de consultar ese resumen, no continúe; el formulario detiene el
registro. No duplique productos ni asuma que una venta queda atendida por el
solo hecho de incluirla.

## Problemas frecuentes y condiciones de detención

- Faltan serie, almacén, vehículo, distribuidor o fecha: complete el dato visible.
- No hay productos: agregue al menos uno o cancele la operación.
- No se puede validar el residual: deténgase y actualice el contexto del vehículo.
- El resultado no es claro: no repita el registro; consulte la lista o el detalle.

## Verificaciones pendientes en runtime

- Disponibilidad del módulo, controles, series y datos de la sesión.
- Reglas de cantidades, seguimiento, residuales y productos provenientes de ventas.
- Efectos reales sobre existencias, compromisos, documentos y operaciones posteriores.

## Enlaces relacionados

- [Gestionar el ciclo de una orden de carga](gestionar-orden-de-carga.md)
- [Registrar recargas, compromisos y residuales](recargas-y-compromisos.md)
- [Inventario](../inventario/index.md)
