<a id="cambiar-de-establecimiento-durante-la-sesión"></a>

# 1.3 Cambiar de establecimiento durante la sesión

<a id="estado"></a>
<a id="verificaciones-pendientes-en-runtime"></a>

## Objetivo

Cambiar el establecimiento de la sesión antes de continuar una tarea que requiere
otro contexto de trabajo.

## Acceso condicional

El selector solo se presenta cuando la sesión dispone de más de un establecimiento
asociado. El cambio también valida la relación de la cuenta con el destino.

## Requisitos y datos

- Sesión iniciada.
- Establecimiento de destino acordado.
- Una tarea pendiente que aún no se haya confirmado en el contexto actual.

## Punto de partida

En el menú de la persona usuaria, cuando el selector de establecimiento esté
visible.

## Pasos

1. Abra el menú de la persona usuaria.
2. Localice el selector de establecimiento, si está disponible.
3. Seleccione el establecimiento de destino.
4. Espere la actualización de la pantalla y confirme el establecimiento mostrado
   antes de continuar.

## Campos y validaciones observados

El selector muestra los establecimientos asociados a la sesión y marca el actual.
Al cambiarlo, confirme la selección y revise la pantalla antes de continuar;
la interfaz valida la asociación de la cuenta antes de sustituir el contexto de
sesión.

<a id="resultado-revisado-en-fuente"></a>

## Resultado esperado

El mecanismo revisado actualiza el establecimiento guardado en la sesión y luego
recarga la página. La persistencia visual y los efectos sobre formularios abiertos
pueden variar según la configuración disponible.

## Advertencias y casos límite

No cambie de establecimiento mientras tenga datos sin confirmar en un formulario.
La recarga observada puede interrumpir el trabajo visible; guarde o abandone la
operación según el procedimiento aplicable antes de cambiar.

## Problemas frecuentes y condiciones de detención

- No aparece el selector: no infiera que existe acceso a otro establecimiento.
- El cambio muestra un error: conserve el contexto actual y confirme la
  asignación antes de reintentar.
- La pantalla recarga con datos inesperados: detenga cualquier operación y revise
  el establecimiento mostrado.

## Enlaces relacionados

- [Iniciar sesión y elegir establecimiento](iniciar-sesion.md)
- [Ubicarse en Yubiz y reconocer el menú disponible](ubicarse-en-yubiz.md)
