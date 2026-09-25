<a id="elegir-establecimiento"></a>

# 2.1 Elegir establecimiento

<a id="estado"></a>
<a id="verificaciones-pendientes-en-runtime"></a>

## Objetivo

Confirmar el contexto de establecimiento antes de continuar una tarea de ventas.

## Acceso condicional

La sesión y las opciones disponibles pueden depender de la persona usuaria y de su
rol. La interfaz no permite afirmar que exista un selector para todas las
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

La interfaz asocia el contexto de establecimiento con la sesión y el rol.
No se observó un control de selección común que permita describir su etiqueta,
ubicación o reglas para todas las personas usuarias.

<a id="resultado-revisado-en-fuente"></a>

## Resultado esperado

El contexto de establecimiento participa en la información disponible para una
venta. La forma en que se muestra o cambia pueden variar según la configuración disponible.

## Advertencias y casos límite

No continúe si el establecimiento visible no coincide con la operación acordada.
No suponga que otra cuenta verá las mismas opciones.

## Problemas frecuentes y condiciones de detención

- Si no puede identificar el establecimiento activo, detenga la operación y
  confirme el contexto con el equipo responsable.
- Si no aparece una opción de cambio, no infiera que la cuenta tiene o no tiene
  permiso; solicite verificación en el entorno.

## Enlaces relacionados

- [Seleccionar cliente](seleccionar-cliente.md)
- [Registrar venta al contado](registrar-venta-al-contado.md)
