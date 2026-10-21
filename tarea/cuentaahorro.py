from tarea import cuentabancaria as cb

class CuentaAhorro(cb.Cuentas):
    def __init__(self, titular, CBU, saldo_inicial):
            super().__init__(titular, CBU, saldo_inicial)
            self.tipocuenta="CajaAhorro"

    def extraer(self, monto):
        if self._saldo - monto < 0:
            print(f"El monto a extrer $({monto})supera el saldo disponible.")
        else:
            self._saldo = self._saldo - monto
            #print(f"El nuevo saldo disponible es $({self.saldo}).")

    def aplicar_interes(self): 
        #SUMA AL SALDO UN INTERÉS DEL 0.1% (TASA = 0.001) 

        self._saldo = self._saldo * 1.001

        #print(f"El nuevo saldo disponible es $({self.saldo}).")

