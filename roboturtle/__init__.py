try:
    import gpiozero
    from .localturtle import LocalTurtle
except ImportError:
    warnings.warn("Package 'gpiozero' not found (this is for raspberry Pi only).  LocalTurtle will not work")