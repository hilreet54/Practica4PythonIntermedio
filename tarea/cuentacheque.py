from tarea import cuentabancaria as cb

class CuentaCheque(cb.Cuentas):
    def __init__(self, titular, CBU, saldo_inicial,costo_emision =50):
            super().__init__(titular, CBU, saldo_inicial)
            self.costo_emision = costo_emision
            self.tipocuenta="Cuenta Cheque"

    def extraer(self, monto):
        if self._saldo - self.costo_emision - monto < 0:
            print(f"El monto a extrer $({monto})supera el saldo disponible.")
        else:
            self._saldo = self._saldo - self.costo_emision - monto
            #print(f"El nuevo saldo disponible es $({self.saldo}).")