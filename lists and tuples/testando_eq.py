from functools import total_ordering


@total_ordering
class ContaSalario:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, other):
        if type(other) != ContaSalario:
            return False

        return self._codigo == other._codigo and self._saldo == other._saldo

    def __lt__(self, other):
        if self._saldo != other._saldo:
            return self._saldo < other._saldo

        return self._codigo < other._codigo

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return "[>>Código {} Saldo {}<<]".format(self._codigo, self._saldo)


conta1 = ContaSalario(37)
conta2 = ContaSalario(38)

print(conta1 <= conta2)