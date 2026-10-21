from abc import ABC, abstractmethod

class Cuentas(ABC):
    def __init__(self, titular, CBU, saldo_inicial):
        self.titular = titular
        self._CBU = CBU
        self._saldo = saldo_inicial
        self.tipocuenta=""
        
    @property
    def CBU(self):
        return self._CBU

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError("EL Saldo debe ser mayor o igual a cero.")
        self._saldo = valor


    def depositar(self, monto):
        if monto < 0:
            raise ValueError("EL monto a depositar debe ser mayor a cero.")
        self._saldo = self._saldo + monto
        print(f"el nuevo saldo de la cuenta {self._CBU} es $ {self._saldo}")

    def __str__(self):
        return f"TIPODECUENTA: {self.tipocuenta} | TITULAR: {self.titular} | CBU: {self._CBU} | SALDO: ${self._saldo}"
        

    @abstractmethod
    def extraer(self, monto):
        """Cada tipo de cuenta implementar sus propia accion."""
        pass