# Registrar recargas, compromisos y residuales

## Estado

- Revisión de fuente: revisada en código
- Verificación en entorno: pendiente
- Paridad con la versión desplegada: pendiente

## Objetivo

Agregar una recarga a una orden de carga confirmada cuando el recorrido la
habilite, revisando los compromisos y residuales mostrados por el sistema.

## Acceso condicional

La recarga es condicional y se muestra para una orden confirmada sin descarga.
No equivale a crear otra orden de carga ni autoriza por sí sola una reposición.

## Requisitos y datos

- Una orden de carga cuyo detalle habilite **Recargar orden de carga**.
- Productos para la recarga y, si se solicita, su seguimiento.
- Comprensión de las opciones de reposición de compromisos visibles.

## Punto de partida

Abra el detalle de la orden y seleccione **Recargar orden de carga** solo si la
acción está disponible.

## Pasos

1. Revise el documento, estado, almacén, vehículo y distribuidor de solo lectura.
2. Revise los déficits de compromisos que se muestren.
3. Agregue productos y cantidades para la recarga; use el modo por serie si aplica.
4. Marque una reposición de compromiso solo si identifica el déficit y la cantidad.
5. Registre una sola vez y regrese a la lista para revisar el resultado.

## Campos y validaciones observados

La pantalla conserva documento, estado, origen, vehículo, distribuidor y fecha.
Permite observación, productos, ventas y selección de reposiciones. La cantidad
de reposición se limita al déficit mostrado. Debe existir al menos un producto;
las reglas exactas de seguimiento y cantidades requieren runtime.

## Resultado revisado en fuente

La recarga registra detalles vinculados a la orden y puede incluir reposiciones
de compromisos seleccionadas. La interfaz expone residual comprometido, residual
libre y cantidades de preventa o manuales. Esos datos son mecánica de fuente;
no prueban disponibilidad física, reserva, stock ni un compromiso comercial en
un tenant.

## Advertencias y casos límite

No interprete el residual como una cantidad libre para usar sin revisión. Si el
producto requiere serie o lote, deténgase cuando no pueda asignarlo. No use una
recarga para corregir una descarga o una liquidación.

## Problemas frecuentes y condiciones de detención

- La acción no aparece: revise estado y existencia de descarga.
- Déficit o cantidad no comprendidos: no seleccione la reposición.
- Falta producto o seguimiento: complete el dato o cancele.
- Error de registro: no duplique la recarga; consulte el detalle primero.

## Verificaciones pendientes en runtime

- Elegibilidad de la recarga y cálculo de déficits/residuales.
- Reglas de seguimiento, reservas y reposición de compromisos.
- Consecuencias sobre stock, ventas, caja y liquidación.

## Enlaces relacionados

- [Crear una orden de carga](crear-orden-de-carga.md)
- [Gestionar el ciclo de una orden de carga](gestionar-orden-de-carga.md)
- [Asignar series en movimientos](../inventario/asignar-series-en-movimientos.md)
