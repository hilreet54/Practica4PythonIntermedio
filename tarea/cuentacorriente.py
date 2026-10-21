from tarea import cuentabancaria as cb

class CuentaCorriente(cb.Cuentas):
    def __init__(self, titular, CBU, saldo_inicial, limite_descubierto =500):
            super().__init__(titular, CBU, saldo_inicial)
            self.limite_descubierto = limite_descubierto
            self.tipocuenta="Cuenta Corriente"

    def extraer(self, monto):
        if (self._saldo + self.limite_descubierto) - monto < 0:
            print(f"El monto a extrer $({monto})supera el saldo disponible tomando en cuenta su descubierto.")
        else:
            self._saldo = self._saldo - monto
            #print(f"El nuevo saldo disponible es $({self.saldo}).")

    