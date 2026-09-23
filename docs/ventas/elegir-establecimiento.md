# Elegir establecimiento

## Estado

- Revisión de fuente: revisada en código
- Verificación en entorno: pendiente
- Paridad con la versión desplegada: pendiente

## Objetivo

Confirmar el contexto de establecimiento antes de continuar una tarea de ventas.

## Acceso condicional

La sesión y las opciones disponibles pueden depender de la persona usuaria y de su
rol. La fuente revisada no permite afirmar que exista un selector para todas las
cuentas.

## Requisitos y datos

- Una sesión iniciada.
- El establecimiento acordado para la operación.

## Punto de partida

Después de iniciar sesión y antes de abrir o continuar una venta.

## Pasos

1. Revise el establecimiento que muestra el contexto de su sesión.
2. Si su entorno presenta una opción para cambiarlo, seleccione el establecimiento
   acordado para la operación.
3. Antes de continuar, confirme con su equipo que el contexto corresponde a la
   venta que realizará.

## Campos y validaciones observados

La fuente revisada asocia el contexto de establecimiento con la sesión y el rol.
No se observó un control de selección común que permita describir su etiqueta,
ubicación o reglas para todas las personas usuarias.

## Resultado revisado en fuente

El contexto de establecimiento participa en la información disponible para una
venta. La forma en que se muestra o cambia requiere verificación en runtime.

## Advertencias y casos límite

No continúe si el establecimiento visible no coincide con la operación acordada.
No suponga que otra cuenta verá las mismas opciones.

## Problemas frecuentes y condiciones de detención

- Si no puede identificar el establecimiento activo, detenga la operación y
  confirme el contexto con el equipo responsable.
- Si no aparece una opción de cambio, no infiera que la cuenta tiene o no tiene
  permiso; solicite verificación en el entorno.

## Verificaciones pendientes en runtime

- Etiqueta, ubicación y comportamiento del cambio de establecimiento.
- Establecimientos disponibles por cuenta, rol y configuración.
- Paridad con la versión desplegada.

## Enlaces relacionados

- [Seleccionar cliente](seleccionar-cliente.md)
- [Registrar venta al contado](registrar-venta-al-contado.md)
