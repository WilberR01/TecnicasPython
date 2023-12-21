from contaimposto import ContaImposto

conta_imposto = ContaImposto(12345, "João", 1000.0, 5)


conta_imposto.depositar(500.0)
conta_imposto.sacar(200.0)
conta_imposto.calcularImposto()


print(conta_imposto.mostrar_saldo())