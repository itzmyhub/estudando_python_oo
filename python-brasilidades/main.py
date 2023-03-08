from acesso_cep import BuscaEndereco

cep = "77006066"
cadastro = BuscaEndereco(cep)


bairro, cidade, uf = cadastro.acessa_via_cep()
print(bairro, cidade, uf)
