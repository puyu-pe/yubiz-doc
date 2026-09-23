# Iniciar sesión y elegir establecimiento

## Estado

- Revisión de fuente: revisada en código
- Verificación en entorno: pendiente
- Paridad con la versión desplegada: pendiente

## Objetivo

Iniciar una sesión de trabajo con el establecimiento que corresponda a la tarea.

## Acceso condicional

El acceso depende de una cuenta activa y de una relación válida con el
establecimiento seleccionado. Las cuentas y establecimientos disponibles deben
confirmarse en runtime.

## Requisitos y datos

- Usuario y credencial de acceso vigentes.
- Establecimiento acordado para la jornada.

## Punto de partida

En la pantalla de inicio de sesión, cuando esté disponible en su entorno.

## Pasos

1. Seleccione el **Establecimiento** que corresponda a su tarea.
2. Complete **Usuario** y **Contraseña**.
3. Seleccione **Iniciar sesión**.
4. Tras el acceso, revise el contexto de establecimiento antes de iniciar una
   operación.

## Campos y validaciones observados

La pantalla revisada contiene establecimiento, usuario y contraseña. La fuente
requiere usuario y contraseña, y comprueba que la cuenta tenga una asociación
activa con el establecimiento elegido.

## Resultado revisado en fuente

Cuando la validación se completa, el sistema prepara el contexto de persona
usuaria, establecimiento y rol para continuar a la primera opción disponible.

## Advertencias y casos límite

No elija un establecimiento por conveniencia si no corresponde a la tarea. No
comparta ni registre credenciales en canales no autorizados.

## Problemas frecuentes y condiciones de detención

- Credenciales rechazadas: revise el dato con el responsable de acceso.
- Establecimiento sin acceso: detenga el intento y confirme la asignación.
- Contexto posterior inesperado: no continúe con operaciones hasta verificarlo.

## Verificaciones pendientes en runtime

- Establecimientos y mensajes visibles para cada cuenta.
- Procedimiento de recuperación o soporte de acceso.
- Comportamiento de la versión desplegada.

## Enlaces relacionados

- [Ubicarse en Yubiz y reconocer el menú disponible](ubicarse-en-yubiz.md)
- [Cambiar de establecimiento durante la sesión](cambiar-establecimiento.md)
